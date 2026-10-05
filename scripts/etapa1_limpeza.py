#!/usr/bin/env python3
"""
ETAPA 1 — LIMPEZA DO RELATÓRIO DE FONTES FACTUAIS (Infohaus RP)
Classifica os fatais do check_fontes_factuais.py em:
  A — ERRO REAL (via de outra linha em seção de trajeto; horário fora da grade;
      item contextual a >500m da linha)
  B — NÃO CONFIRMADA EM FONTE (instituição/via plausível, ausente nas 4 fontes;
      precisa investigação — Etapa 2)
  C — RUÍDO DE PARSER (capturas truncadas, genéricas, fragmentos)
  C-CONTEXTO — menção contextual legítima: item com coordenada a ≤500m de
      alguma parada da linha citada (regra 500m) → rebaixado a AVISO.

Vocabulário (Ajuste 1):
  VIA AUSENTE NAS PARADAS DA LINHA | INSTITUIÇÃO NÃO CONFIRMADA EM FONTE |
  BAIRRO AUSENTE NAS PARADAS DA LINHA

NÃO corrige conteúdo. Saída: reports/check_fontes_factuais_limpo.txt
Autorização: Leo, Etapa 1 apenas (Fase 2).
"""

import json
import re
import sys
from datetime import datetime
from math import radians, sin, cos, asin, sqrt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_fontes_factuais as ck

ROOT = Path(__file__).resolve().parent.parent
PAGINAS = ROOT / 'content' / 'paginas' / 'linhas'
REPORTS = ROOT / 'reports'

SECOES_TRAJETO = {'itinerario_texto', 'paradas_destaque'}
FUNCIONAIS = {'e', 'de', 'da', 'do', 'das', 'dos', 'o', 'a', 'na', 'no',
              'em', 'que', 'dentre', 'entre', 'essa', 'esse', 'ao', 'os'}
RUIDO_UNICO = {'atende', 'usuarios', 'fiscalizada', 'regulada',
               'supervisionada', 'entre', 'dentre', 'usuários'}

def haversine_m(a, b):
    la1, lo1, la2, lo2 = map(radians, [a[0], a[1], b[0], b[1]])
    h = sin((la2 - la1) / 2) ** 2 + cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371000 * asin(sqrt(h))

# ---------- coordenadas globais (paradas de todas as linhas, GTFS) ----------
GLOBAL_STOPS = []
for ln, fonte in ck.LINHAS_FONTE.items():
    for p in (fonte.get('paradas', {}) or {}).get('valor', []) or []:
        lat, lng = p.get('lat'), p.get('lng')
        if lat is None or lng is None:
            continue
        toks = ck.tokens(p['nome'])
        GLOBAL_STOPS.append((ln, p['nome'], lat, lng, toks))

def coord_do_item(toks_cit):
    """Parada global (de qualquer linha) que case com os tokens do item citado."""
    toks_cit = {t for t in toks_cit if len(t) > 4}
    if not toks_cit:
        return None
    for ln, nome, lat, lng, toks in GLOBAL_STOPS:
        inter = toks & toks_cit
        if len(inter) >= 2:
            return (ln, nome, lat, lng)
        if len(inter) == 1 and len(next(iter(inter))) > 7:
            return (ln, nome, lat, lng)
    return None

def dist_minima_linha(linha_fonte, coord):
    melhor = None
    for p in (linha_fonte.get('paradas', {}) or {}).get('valor', []) or []:
        lat, lng = p.get('lat'), p.get('lng')
        if lat is None or lng is None:
            continue
        d = haversine_m((lat, lng), coord)
        if melhor is None or d < melhor:
            melhor = d
    return melhor

# ---------- classificação de captura ----------
def limpa_captura(cap):
    """Remove sufixo truncado após ponto final; devolve (nome_limpo, truncado)."""
    m = re.match(r'^(.*?)\.\s', cap + '. ')
    if m and m.group(1):
        return m.group(1).strip(), True
    return cap.strip(), False

def eh_ruido(nome_limpo):
    toks_esp = ck.tokens_especificos(nome_limpo) - FUNCIONAIS
    if not toks_esp:
        return True
    if toks_esp <= RUIDO_UNICO:
        return True
    palavras = [t for t in ck.norm(nome_limpo).split() if len(t) > 3]
    if len(palavras) == 0:
        return True
    return False

# ---------- main ----------
def main():
    lista_A, lista_B, lista_C, lista_ctx = [], [], [], []
    rel = ['RELATÓRIO LIMPO — CHECK FONTES FACTUAIS (ETAPA 1)',
           f'Data/Hora: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
           'Vocabulário: VIA AUSENTE NAS PARADAS DA LINHA / '
           'INSTITUIÇÃO NÃO CONFIRMADA EM FONTE / BAIRRO AUSENTE NAS PARADAS DA LINHA',
           'Regra de contexto: item citado a <=500m de alguma parada da linha = menção '
           'contextual legítima (AVISO), exceto em seções de trajeto (itinerario_texto, '
           'paradas_destaque), onde afirmar trajeto sem parada = erro real.',
           '=' * 70, '']

    erros_a_por_linha = {}
    arquivos = sorted(PAGINAS.glob('linha-*.json'))
    SEM_FONTE = []

    for arq in arquivos:
        try:
            pag = json.load(open(arq, encoding='utf-8'))
        except Exception:
            continue
        num_pag = pag.get('linha_numero') or arq.stem.split('-')[1]
        chave = None
        for cand in (num_pag, str(int(num_pag)), num_pag.zfill(3)):
            if cand in ck.LINHAS_FONTE:
                chave = cand
                break
        if chave is None:
            SEM_FONTE.append(arq.name)
            continue
        fonte = ck.LINHAS_FONTE[chave]
        paradas = (fonte.get('paradas', {}) or {}).get('valor', []) or []
        toks_paradas = set()
        for p in paradas:
            for campo in ('nome', 'rua', 'bairro'):
                toks_paradas |= ck.tokens(p.get(campo) or '')
            if re.search(r'\bTU\b', p.get('nome', '')):
                toks_paradas |= {'terminal', 'urbano'}
        grade = set()
        hor = (fonte.get('horarios', {}) or {}).get('valor', {}) or {}
        for dia in ('dias_uteis', 'sabado', 'domingo'):
            grade |= set(hor.get(dia, []) or [])

        secoes = {k: v for k, v in (pag.get('secoes') or {}).items() if isinstance(v, str)}
        for nome_sec, html in secoes.items():
            texto = ck.strip_tags(html)
            eh_trajeto = nome_sec in SECOES_TRAJETO

            # --- VIAS ---
            for m in ck.RUA_RE.finditer(texto):
                via = (m.group(1) or '').strip()
                via, _ = limpa_captura(via)
                vt = ck.tokens_especificos(via)
                if not vt:
                    continue
                if vt & toks_paradas:
                    continue
                if (vt & ck.TOKS_PERFIL) or (vt & ck.TOKS_MESTRE) or (vt & ck.TOKS_CIDADE):
                    lista_ctx.append((chave, 'AVISO-VIA-CONTEXTO-URBANO', via, nome_sec, ''))
                    continue
                if eh_ruido(via):
                    lista_C.append((chave, 'RUÍDO:VIA', via, nome_sec, 'captura truncada/genérica'))
                    continue
                # existe em outra linha?
                outras = set()
                for ln, nome, lat, lng, toks in GLOBAL_STOPS:
                    if vt & toks:
                        outras.add(ln)
                if outras:
                    if eh_trajeto:
                        lista_A.append((chave, 'ERRO REAL:VIA AUSENTE NAS PARADAS DA LINHA (seção de trajeto)',
                                        via, nome_sec, f'via presente na(s) linha(s): {", ".join(sorted(outras))}'))
                    else:
                        coord = coord_do_item(vt)
                        d = dist_minima_linha(fonte, (coord[2], coord[3])) if coord else None
                        if d is not None and d <= 500:
                            lista_ctx.append((chave, 'AVISO-CONTEXTO ≤500m', via, nome_sec, f'{d:.0f}m da parada mais próxima'))
                        else:
                            lista_A.append((chave, 'ERRO REAL:VIA AUSENTE NAS PARADAS DA LINHA (contexto distante)',
                                            via, nome_sec, f'via das linhas {", ".join(sorted(outras))}; dist mín {f"{d:.0f}m" if d else "sem coord"}'))
                    continue
                # não está em nenhuma linha do sistema
                lista_B.append((chave, 'VIA NÃO CONFIRMADA EM FONTE', via, nome_sec,
                                'ausente em todas as 113 linhas — verificar existência'))

            # --- INSTITUIÇÕES ---
            for m in ck.INST_RE.finditer(texto):
                inst = (m.group(0) or '').strip()
                inst, trunc = limpa_captura(inst)
                it = ck.tokens_especificos(m.group(2) or '') or ck.tokens_especificos(inst)
                if not it:
                    continue
                if it & toks_paradas:
                    continue
                if (it & ck.TOKS_CIDADE) or (it & ck.TOKS_MESTRE) or (it & ck.TOKS_PERFIL):
                    continue
                if eh_ruido(inst):
                    lista_C.append((chave, 'RUÍDO:INSTITUIÇÃO', inst, nome_sec, 'captura truncada/genérica'))
                    continue
                coord = coord_do_item(it)
                d = dist_minima_linha(fonte, (coord[2], coord[3])) if coord else None
                if d is not None and d <= 500:
                    lista_ctx.append((chave, 'AVISO-CONTEXTO ≤500m', inst, nome_sec, f'{d:.0f}m (coord da parada "{coord[1]}", linha {coord[0]})'))
                    continue
                nota = ''
                if coord and d is not None:
                    nota = f'item real mapeado a {d:.0f}m da linha (parada "{coord[1]}", linha {coord[0]}) — além de 500m'
                elif d is None:
                    nota = 'sem coordenada em nenhuma parada do sistema — investigar existência (Etapa 2)'
                rotulo = ('ERRO REAL:INSTITUIÇÃO FORA DE POSIÇÃO' if nota.startswith('item real')
                          else 'INSTITUIÇÃO NÃO CONFIRMADA EM FONTE')
                alvo = lista_A if rotulo.startswith('ERRO REAL') else lista_B
                alvo.append((chave, rotulo, inst, nome_sec, nota))

            # --- HORÁRIOS ---
            for h in sorted(ck.extrai_horarios(texto)):
                if h not in grade:
                    lista_A.append((chave, 'ERRO REAL:HORÁRIO FORA DA GRADE', h, nome_sec, 'verificável contra dados-fonte'))

            # --- BAIRROS ---
            for m in ck.BAIRRO_CIT_RE.finditer(texto):
                frag = (m.group(0) or '').strip()
                ft = ck.tokens_especificos(frag)
                if not ft or eh_ruido(frag):
                    if ft:
                        lista_C.append((chave, 'RUÍDO:BAIRRO', frag, nome_sec, 'captura truncada'))
                    continue
                frag_n = ck.norm(frag)
                if any(bt and bt in frag_n for bt in ck.BAIRROS_TODOS):
                    continue
                if (ft & toks_paradas) or (ft & ck.TOKS_MESTRE):
                    continue
                lista_B.append((chave, 'BAIRRO AUSENTE NAS PARADAS DA LINHA', frag, nome_sec,
                                'não casa com bairros[].valor nem lista-mestre — investigar'))

    # ---------- recontagem com erros REAIS (lista A) ----------
    for linha, *_ in lista_A:
        erros_a_por_linha[linha] = erros_a_por_linha.get(linha, 0) + 1
    n0 = [l for l in sorted({k for a in (lista_A,)} for k in [])]  # placeholder
    todas = set()
    for arq in arquivos:
        try:
            pag = json.load(open(arq, encoding='utf-8'))
            todas.add(pag.get('linha_numero') or arq.stem.split('-')[1])
        except Exception:
            pass
    zero = sorted(t for t in todas if erros_a_por_linha.get(t, 0) == 0)
    um_dois = sorted(t for t in todas if 1 <= erros_a_por_linha.get(t, 0) <= 2)
    tres_mais = sorted(t for t in todas if erros_a_por_linha.get(t, 0) >= 3)

    # ---------- relatório ----------
    def bloco(titulo, itens):
        rel.append('')
        rel.append(titulo)
        por_linha = {}
        for it in itens:
            por_linha.setdefault(it[0], []).append(it)
        for ln in sorted(por_linha):
            rel.append(f'  [{ln}]')
            for _, rotulo, nome, sec, nota in por_linha[ln]:
                rel.append(f'    - ({sec}) {rotulo}: "{nome}"' + (f' — {nota}' if nota else ''))

    rel.append(f'RECONCILIAÇÃO: {len(lista_A)} erros reais (A) + '
               f'{len(lista_B)} não confirmados (B) + {len(lista_C)} ruídos (C) + '
               f'{len(lista_ctx)} contextos legítimos rebaixados a AVISO = '
               f'{len(lista_A) + len(lista_B) + len(lista_C) + len(lista_ctx)} itens classificados '
               f'(base anterior: 120 fatais brutos)')
    bloco('LISTA A — ERROS REAIS (corrigir na Fase 2, Etapa 3):', lista_A)
    bloco('LISTA B — NÃO CONFIRMADOS EM FONTE (investigar na Etapa 2):', lista_B)
    bloco('LISTA C — RUÍDO DE PARSER (descartar; não é erro):', lista_C)
    bloco('REBAIXADOS A AVISO — CONTEXTO LEGÍTIMO (regra 500m):', lista_ctx)
    rel.append('')
    rel.append('=' * 70)
    rel.append('RECONTAGEM COM ERROS REAIS (só lista A):')
    rel.append(f'  Linhas com 0 erros reais:  {len(zero)}')
    rel.append(f'  Linhas com 1-2:            {len(um_dois)}  ({", ".join(um_dois)})')
    rel.append(f'  Linhas com 3+:             {len(tres_mais)}  ({", ".join(tres_mais)})')
    rel.append('STATUS: ' + ('OK' if not lista_A else 'FALHOU (erros reais presentes)'))

    out = REPORTS / 'check_fontes_factuais_limpo.txt'
    out.write_text('\n'.join(rel), encoding='utf-8')
    print('\n'.join(rel[:60]))
    print(f'\n[...] Relatório completo: {out}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
