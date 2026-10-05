#!/usr/bin/env python3
"""
CHECK DE FONTES FACTUAIS — INFOHAUS RP (scripts/check_fontes_factuais.py)
Valida afirmações factuais da narrativa de cada página de linha contra
content/dados-fonte/linhas.json (+ pontos/, rp-perfil.json, lista-mestre.json).

Aprovação: Leo, 03/10/2026 (regra 1.20 EXECUCAO.md).
Integração à suíte audit_all.py como FATAL bloqueante (wrapper
check_fontes_factuais_suite): Decisão 1 do Leo, 05/10/2026.

Priorização FATAL (Ajuste 3):
  1. INSTITUICAO-INVENTADA  2. PLATAFORMA-ERRADA  3. VIA-ERRADA
  4. HORARIO-ERRADO         5. BAIRRO-ERRADO (Ajuste 1)
Whitelist (Ajuste 2): "50%" NÃO incluído — sem fonte em dados-fonte/
(benefício real é Cartão Nosso Estudante Gratuito, fonte externa).
NÃO corrige nada. Saída em reports/.
"""

import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
FONTES = ROOT / 'content' / 'dados-fonte'
PAGINAS = ROOT / 'content' / 'paginas' / 'linhas'
REPORTS = ROOT / 'reports'

# tokens genéricos: NÃO valem como prova de batida (evitam falso-passar
# tipo "Av. Presidente Médici" bater com parada "Av. Presidente Kennedy")
GENERICOS = {
    'rua', 'ruas', 'avenida', 'avenidas', 'alameda', 'estrada', 'rodovia',
    'travessa', 'praca', 'parque', 'terminal', 'teatro', 'theatro',
    'shopping', 'hospital', 'escola', 'museu', 'igreja', 'catedral',
    'paroquia', 'estacao', 'universidade', 'faculdade', 'mercado',
    'rodoviaria', 'forum', 'creche', 'vila', 'jardim', 'conjunto',
    'residencial', 'campos', 'nucleo', 'bosque', 'santuario', 'palacete',
    'quarteirao', 'biblioteca', 'ceagesp', 'emei', 'eme', 'ubs',
    'general', 'presidente', 'doutor', 'professor', 'prefeito', 'coronel',
    'major', 'brigadeiro', 'padre', 'engenheiro', 'vereador', 'deputado',
    'dep', 'dr', 'municipal', 'estadual', 'federal', 'urbano', 'central',
    'norte', 'sul', 'leste', 'oeste', 'cidade', 'velho', 'novo', 'maior',
}

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')

def strip_tags(html):
    return re.sub(r'<[^>]+>', ' ', html)

def tokens(nome):
    out = set()
    for t in norm(nome).split():
        t = t.strip('.,;:!?()"\'[]{}«»—–-_…')
        if len(t) > 4 and not t.isdigit():
            out.add(t)
    return out

def tokens_especificos(nome):
    """Tokens prováveis de batida, removendo genéricos (ex.: 'presidente')."""
    t = tokens(nome)
    esp = t - GENERICOS
    return esp if esp else t

# ---------- carregamento ----------
# ---------- pontos com coordenada (dados-fonte/pontos/*.json) ----------
PONTOS_COORD = []
for _p in sorted((FONTES / 'pontos').glob('*.json')):
    try:
        with open(_p, encoding='utf-8') as f:
            _d = json.load(f)
        _nome = _d.get('nome')
        if isinstance(_nome, dict):
            _nome = _nome.get('valor')
        if _d.get('lat') is not None and _d.get('lng') is not None and _nome:
            PONTOS_COORD.append((_nome, _d['lat'], _d['lng']))
    except Exception:
        pass

def coord_de_pontos(toks):
    """Procura ponto em dados-fonte/pontos/ com ≥1 token específico em comum."""
    for nome, lat, lng in PONTOS_COORD:
        if tokens_especificos(nome) & toks:
            return (lat, lng)
    return None

def dist_min_parada(paradas, coord):
    from math import radians, sin, cos, asin, sqrt
    melhor = None
    for p in paradas:
        lat, lng = p.get('lat'), p.get('lng')
        if lat is None or lng is None:
            continue
        la1, lo1, la2, lo2 = map(radians, [coord[0], coord[1], lat, lng])
        h = sin((la2-la1)/2)**2 + cos(la1)*cos(la2)*sin((lo2-lo1)/2)**2
        d = 2*6371000*asin(sqrt(h))
        if melhor is None or d < melhor:
            melhor = d
    return melhor

def carrega_fontes():
    with open(FONTES / 'linhas.json', encoding='utf-8') as f:
        linhas = json.load(f)
    pontos_cidade = []
    for p in sorted((FONTES / 'pontos').glob('*.json')):
        with open(p, encoding='utf-8') as f:
            d = json.load(f)
        nome = d.get('nome')
        if isinstance(nome, dict):
            nome = nome.get('valor')
        if not nome:
            nome = d.get('titulo') or p.stem
        pontos_cidade.append(nome)
    with open(FONTES / 'rp-perfil.json', encoding='utf-8') as f:
        perfil = json.load(f)
    with open(ROOT / 'content' / 'lista-mestre.json', encoding='utf-8') as f:
        mestre = json.load(f)
    return linhas, pontos_cidade, perfil, mestre

LINHAS_FONTE, PONTOS_CIDADE, PERFIL, MESTRE = carrega_fontes()
TOKS_CIDADE = set()
for n in PONTOS_CIDADE:
    TOKS_CIDADE |= tokens_especificos(n)
TOKS_PERFIL = tokens_especificos(json.dumps(PERFIL, ensure_ascii=False))
TOKS_MESTRE = tokens_especificos(json.dumps(MESTRE, ensure_ascii=False))
BAIRROS_TODOS = set()
for l in LINHAS_FONTE.values():
    for b in (l.get('bairros', {}) or {}).get('valor', []) or []:
        if b:
            BAIRROS_TODOS.add(norm(b))

# ---------- extração ----------
RUA_RE = re.compile(
    r'(?:[Rr]uas?|[Aa]venidas?|[Aa][vV]\.?|[Rr]\.|[Ee]stradas?|'
    r'[Rr]odovias?|[Tt]ravessas?|[Aa]lamedas?)\s+'
    r'(?:[Dd][aeo]s?\s+)?'
    r'([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ\'’-]*(?:\s+(?:[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ\'’-]*|de|da|do|das|dos|e))*)')
INST_RE = re.compile(
    r'\b(Escola|Hospital|UBS|Shopping|Teatro|Theatro|Parque|Praça|Catedral|'
    r'Paróquia|Igreja|Terminal|Estação|Museu|Mercado|Ceagesp|Universidade|'
    r'Faculdade|EMEI|Creche|Fórum|Rodoviária|Biblioteca|Santuário)\b'
    r'((?:\s+(?:[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ\'’.-]*|de|da|do|das|dos|e|—|-))*)')
HORA_H_RE = re.compile(r'\b(\d{1,2})h(\d{2})\b')
HORA_2P_RE = re.compile(r'\b(\d{1,2}):(\d{2})\b')
PLAT_RE = re.compile(r'[Pp]lataforma\s+([A-H]\b|\d+)')
NUM_RE = re.compile(r'\b(\d+(?:[.,]\d+)?)\b')
BAIRRO_CIT_RE = re.compile(
    r'\b(Jardim|Parque|Vila|Conjunto|Residencial|Campos|Núcleo|Quintino|'
    r'Avelino|Independência|Bonfim|Sumarezinho|Sumaré|Recanto|Jóquei)\b'
    r'((?:\s+(?:[A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ\'’.-]*|de|da|do|das|dos|I|II))*)')

def extrai_horarios(texto):
    out = set()
    for m in HORA_H_RE.finditer(texto):
        out.add(f'{int(m.group(1)):02d}:{m.group(2)}')
    for m in HORA_2P_RE.finditer(texto):
        out.add(f'{int(m.group(1)):02d}:{m.group(2)}')
    return out

# ---------- verificação ----------
def verifica_linha(num, fonte, secoes):
    fatais, avisos = [], []
    paradas = fonte.get('paradas', {}).get('valor', []) or []
    toks_paradas = set()
    nums_paradas = set()
    for p in paradas:
        for campo in ('nome', 'rua', 'bairro'):
            v = p.get(campo) or ''
            toks_paradas |= tokens(v)
            # abreviações oficiais do GTFS (tolerância aprovada na espec.):
            # TU = Terminal Urbano; Plat = Plataforma
            if re.search(r'\bTU\b', v):
                toks_paradas |= {'terminal', 'urbano'}
            if re.search(r'\bPlat\b', v):
                toks_paradas |= {'plataforma'}
            nums_paradas |= set(re.findall(r'\d+', v))
    horarios = fonte.get('horarios', {}).get('valor', {}) or {}
    grade = set()
    for dia in ('dias_uteis', 'sabado', 'domingo'):
        grade |= set(horarios.get(dia, []) or [])
    bairros_linha = {norm(b) for b in (fonte.get('bairros', {}) or {}).get('valor', []) or []}
    n_paradas_fonte = {i.get('num_paradas') for i in (fonte.get('itinerario', {}) or {}).get('valor', []) or []}

    texto = ' '.join(secoes.values())          # ← conteúdo, não chaves
    texto_plano = strip_tags(texto)

    # 3. PLATAFORMAS (FATAL)
    plats_fonte = set()
    for p in paradas[:6] + paradas[-6:]:
        m = re.search(r'[Pp]lat\w*\s*([A-H]\b|\d+)', p.get('nome', ''))
        if m:
            plats_fonte.add(m.group(1).upper())
    for m in PLAT_RE.finditer(texto_plano):
        pl = m.group(1).upper()
        if plats_fonte and pl not in plats_fonte:
            fatais.append(f'PLATAFORMA-ERRADA: "Plataforma {pl}" citada; '
                          f'fonte indica {sorted(plats_fonte)} na linha {num}.')

    # 1. VIAS (FATAL se ausente na própria linha; AVISO se contexto urbano)
    for m in RUA_RE.finditer(texto_plano):
        via = (m.group(1) or '').strip()
        vt = tokens_especificos(via)
        if not vt:
            continue
        if vt & toks_paradas:
            continue
        if (vt & TOKS_PERFIL) or (vt & TOKS_MESTRE) or (vt & TOKS_CIDADE):
            avisos.append(f'AVISO-VIA-CONTEXTO: "{via}" ausente nas paradas '
                           f'da {num}, mas consta em rp-perfil/lista-mestre/pontos (contexto urbano).')
            continue
        fatais.append(f'VIA-ERRADA: "{via}" citada mas ausente nas paradas da linha {num}.')

    # 2. INSTITUIÇÕES (FATAL se sem batida em qualquer fonte)
    for m in INST_RE.finditer(texto_plano):
        inst = (m.group(0) or '').strip()
        it = tokens_especificos(m.group(2) or '') or tokens_especificos(inst)
        if not it:
            continue
        if it & toks_paradas:
            continue
        if (it & TOKS_CIDADE) or (it & TOKS_MESTRE) or (it & TOKS_PERFIL):
            continue
        # Ajuste 4 (Leo, 04/10/2026): instituição REAL mas ausente das 4 fontes
        # → se houver coordenada e distância ≤500m de alguma parada da linha,
        #   é menção contextual legítima: AVISO, não FATAL.
        coord = coord_de_pontos(it)  # procura em dados-fonte/pontos/*.json
        if coord is not None:
            d = dist_min_parada(paradas, coord)
            if d is not None and d <= 500:
                avisos.append(f'AVISO-INSTITUICAO-PROXIMA: "{inst}" real e a {d:.0f}m '
                               f'de parada da linha {num} (contexto legítimo — não é parada).')
                continue
            if d is not None:
                avisos.append(f'AVISO-INSTITUICAO-DISTANTE: "{inst}" real mas a {d:.0f}m '
                               f'da linha {num} (>500m) — revisar menção.')
                continue
        # captura truncada (só token genérico sobreviveu): ruído do parser,
        # não dá para afirmar invenção → AVISO para revisão humana
        especificos = tokens(inst) - GENERICOS
        if len(especificos) == 0:
            avisos.append(f'AVISO-INSTITUICAO-TRUNCADA: "{inst}" — captura '
                           f'incompleta no texto (linha {num}); verificar manualmente.')
            continue
        fatais.append(f'INSTITUICAO-INVENTADA: "{inst}" sem batida em paradas, '
                      f'pontos/, lista-mestre ou rp-perfil.')

    # 4. HORÁRIOS (FATAL se fora da grade)
    for h in sorted(extrai_horarios(texto_plano)):
        if h not in grade:
            fatais.append(f'HORARIO-ERRADO: "{h}" citado mas ausente na grade da linha {num}.')

    # 5. BAIRROS (Ajuste 1 — AVISO isolado; FATAL se houver outro fatal)
    for m in BAIRRO_CIT_RE.finditer(texto_plano):
        frag = (m.group(0) or '').strip()
        ft = tokens_especificos(frag)
        if not ft:
            continue
        frag_n = norm(frag)
        if any(bt and bt in frag_n for bt in BAIRROS_TODOS):
            continue
        if (ft & toks_paradas) or (ft & bairros_linha) or (ft & TOKS_MESTRE):
            continue
        avisos.append(f'AVISO-BAIRRO-SUSPEITO: "{frag}" não casa com bairros[].valor '
                      f'da linha {num} nem com lista-mestre.')

    # 6. NÚMEROS (whitelist; "50%" sem fonte = AVISO — Ajuste 2)
    wl_num = {'5,00', '5.00', '120', '113'}
    wl_num |= {str(n) for n in n_paradas_fonte if n}
    wl_num |= nums_paradas
    for k in LINHAS_FONTE:
        wl_num |= {k, str(int(k))}
    if num:
        wl_num |= {str(int(num)), num.zfill(3), num}
    anos = {str(a) for a in range(2020, 2031)}
    texto_num = re.sub(r'\b\d{1,2}[:h]\d{2}\b', ' ', texto_plano)
    for m in NUM_RE.finditer(texto_num):
        v = m.group(1)
        vn = v.replace(',', '.')
        if v in wl_num or vn in anos or re.match(r'^\d{5}-?\d{3}$', v):
            continue
        ini = m.start()
        ctx = texto_num[max(0, ini - 60):ini]
        if re.search(r'(?:rua|avenida|alameda|r\.|av\.)\s*[\wÀ-ÿ\s]+,\s*$', ctx, re.I):
            continue
        seg = texto_num[m.end():m.end() + 3]
        if seg.strip().startswith('%'):
            avisos.append(f'AVISO-NUMERO: "{v}%" citado — política de desconto sem '
                           f'fonte em dados-fonte/ (Ajuste 2: validar antes de manter).')
            continue
        avisos.append(f'AVISO-NUMERO: "{v}" citado sem fonte em dados-fonte/ (linha {num}).')

    # Ajuste 1: bairro suspeito vira FATAL se houver qualquer outro fatal na linha
    if fatais:
        for i, a in enumerate(avisos):
            if a.startswith('AVISO-BAIRRO-SUSPEITO'):
                avisos[i] = a.replace('AVISO-BAIRRO-SUSPEITO', 'FATAL-BAIRRO-ERRADO')
    for i in range(len(avisos)):
        if avisos[i].startswith('FATAL-BAIRRO-ERRADO'):
            fatais.append(avisos.pop(i))
            break
    return fatais, avisos

# ---------- priorização (Ajuste 3) ----------
ORDEM = ['INSTITUICAO-INVENTADA', 'PLATAFORMA-ERRADA', 'VIA-ERRADA',
         'HORARIO-ERRADO', 'BAIRRO-ERRADO']
def tipo_de(msg):
    for t in ORDEM:
        if msg.startswith(t):
            return t
    return 'OUTROS'

def check_fontes_factuais_suite():
    """Wrapper Decisão 1 (Leo, 05/10/2026): integra este check à suíte
    audit_all.py como FATAL bloqueante, retornando (fatals, avisos) no
    padrão da suíte. Relatório detalhado segue via execução standalone
    (main), que grava reports/check_fontes_factuais_<ts>.txt."""
    fatals, avisos = [], []
    arquivos = sorted(PAGINAS.glob('linha-*.json'))
    for arq in arquivos:
        try:
            with open(arq, encoding='utf-8') as f:
                pag = json.load(f)
        except Exception as e:
            fatals.append(f'FATUAIS-FONTES: {arq.name}: JSON inválido — {e}')
            continue
        num_pag = pag.get('linha_numero') or arq.stem.split('-')[1]
        chave = None
        for cand in (num_pag, str(int(num_pag)), num_pag.zfill(3)):
            if cand in LINHAS_FONTE:
                chave = cand
                break
        if chave is None:
            # mesma régua do main(): página sem fonte em dados-fonte é
            # reportada no relatório standalone, não fatal da suíte
            continue
        secoes = {k: v for k, v in (pag.get('secoes') or {}).items() if isinstance(v, str)}
        f_l, a_l = verifica_linha(chave, LINHAS_FONTE[chave], secoes)
        fatals.extend(f'[{chave}] {m}' for m in f_l)
        avisos.extend(f'[{chave}] {m}' for m in a_l)
    print(f'[check_fontes_factuais_suite] {len(arquivos)} páginas de linha, '
          f'{len(fatals)} fatal(is), {len(avisos)} aviso(s)')
    return fatals, avisos

def main():
    arquivos = sorted(PAGINAS.glob('linha-*.json'))
    linhas_rel = []
    fatais_por_tipo = {t: [] for t in ORDEM}
    fatais_por_tipo['OUTROS'] = []
    avisos_por_linha = {}
    n_zero = n_12 = n_3m = 0
    lista_12, lista_3m = [], []

    for arq in arquivos:
        try:
            with open(arq, encoding='utf-8') as f:
                pag = json.load(f)
        except Exception as e:
            linhas_rel.append(f'[ERRO] {arq.name}: JSON inválido — {e}')
            n_3m += 1
            lista_3m.append(arq.name)
            continue
        num_pag = pag.get('linha_numero') or arq.stem.split('-')[1]
        chave = None
        for cand in (num_pag, str(int(num_pag)), num_pag.zfill(3)):
            if cand in LINHAS_FONTE:
                chave = cand
                break
        if chave is None:
            linhas_rel.append(f'[SEM-FONTE] {arq.name}: linha {num_pag} ausente em dados-fonte/linhas.json')
            continue
        secoes = {k: v for k, v in (pag.get('secoes') or {}).items() if isinstance(v, str)}
        fatais, avisos = verifica_linha(chave, LINHAS_FONTE[chave], secoes)
        if avisos:
            avisos_por_linha[chave] = avisos
        for msg in fatais:
            fatais_por_tipo[tipo_de(msg)].append((chave, msg))
        nf = len(fatais)
        linhas_rel.append(f'[{chave}] {arq.name}: '
                          + (f'{nf} FATAL(is)' if nf else '0 fatais')
                          + (f' | {len(avisos)} aviso(s)' if avisos else ''))
        if nf == 0:
            n_zero += 1
        elif nf <= 2:
            n_12 += 1
            lista_12.append(chave)
        else:
            n_3m += 1
            lista_3m.append(chave)

    rel = ['RELATÓRIO CHECK FONTES FACTUAIS — INFOHAUS RP',
           f'Data/Hora: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
           f'Universo: {len(arquivos)} páginas de linha',
           '=' * 64,
           '', '🔴 FATAIS AGRUPADOS POR TIPO (Ajuste 3 — gravidade decrescente):', '']
    total_fatais = 0
    for t in ORDEM + ['OUTROS']:
        occ = fatais_por_tipo[t]
        if not occ:
            continue
        total_fatais += len(occ)
        rel.append(f'--- {t} ({len(occ)} ocorrência[s]) ---')
        for num, msg in sorted(occ):
            rel.append(f'  [{num}] {msg}')
        rel.append('')
    rel.append('=' * 64)
    rel.append('DETALHE POR LINHA:')
    rel.extend('  ' + l for l in linhas_rel)
    rel.append('=' * 64)
    rel.append('AVISOS (revisão humana; não bloqueiam):')
    for num in sorted(avisos_por_linha):
        rel.append(f'  [{num}]')
        for a in avisos_por_linha[num]:
            rel.append(f'    - {a}')
    rel.append('=' * 64)
    rel.append('RESUMO:')
    rel.append(f'  Linhas com 0 fatais:  {n_zero}')
    rel.append(f'  Linhas com 1-2:      {n_12}  ({", ".join(lista_12)})')
    rel.append(f'  Linhas com 3+:        {n_3m}  ({", ".join(lista_3m)})')
    rel.append(f'  Total de fatais: {total_fatais}')
    rel.append('  Padrão por tipo:')
    for t in ORDEM + ['OUTROS']:
        if fatais_por_tipo[t]:
            rel.append(f'    {t}: {len(fatais_por_tipo[t])}')
    rel.append('STATUS: ' + ('OK' if total_fatais == 0 else 'FALHOU'))

    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    out = REPORTS / f'check_fontes_factuais_{ts}.txt'
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(rel))
    print('\n'.join(rel[:120]))
    print(f'\n[...] Relatório completo gravado em {out}]')
    return 0 if total_fatais == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
