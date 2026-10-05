#!/usr/bin/env python3
"""Consolida pesquisas das 4 frentes em dossiês oficiais (18 pontos reais).
Expansão turística — Leo/Hermes, 05/10/2026."""
import json
import re
from pathlib import Path

B = Path(r"C:\Users\lamacedo\AppData\Local\hermes\cache\delegation")
ROOT = Path(__file__).resolve().parent.parent
DOSSIES = ROOT / 'content' / 'dados-fonte' / 'pontos'
HOJE = '2026-10-05'


def parse(f):
    raw = open(f, encoding='utf-8').read().strip()
    raw = re.sub(r'^```(json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)
    return json.loads(raw)


igrejas = parse(B / 'subagent-summary-0-20261005_115509_819662.txt')['pontos']
museus = parse(B / 'subagent-summary-2-20261005_115509_819662.txt')['pontos']
predios = parse(B / 'subagent-summary-3-20261005_115509_819662.txt')['pontos']
ws = json.load(open(ROOT / 'workspace_expansao_turistica.json', encoding='utf-8'))

SLUGS_IGREJAS = [
    ('Igreja Santo Antônio de Pádua', 'basilica-santo-antonio-de-padua'),
    ('Igreja Nossa Senhora do Rosário', 'santuario-nossa-senhora-do-rosario'),
    ('Igreja Santa Rita de Cássia', 'paroquia-santa-rita-de-cassia'),
    ('Paróquia Santa Teresinha Doutora', 'paroquia-santa-teresinha-doutora'),
    ('Igreja São Benedito', 'igreja-sao-benedito'),
    ('Igreja Matriz de Bonfim Paulista', 'paroquia-senhor-bom-jesus-do-bonfim'),
]
SLUGS_MUSEUS = [
    ('MIS-RP', 'mis-rp'),
    ('Museu Histórico e de Ordem Geral', 'museu-historico-plinio-travassos'),
    ('Casa da Memória Italiana', 'casa-da-memoria-italiana'),
]
SLUGS_PREDIOS = [
    ('Palácio Rio Branco', 'palacio-rio-branco'),
    ('Mercado Municipal', 'mercado-municipal'),
    ('Estação Barracão', 'estacao-barracao'),
    ('Estação Mogiana', 'estacao-mogiana'),
]

CAMPO_MAP = {'nome_oficial': 'nome', 'endereco': 'endereco',
             'horarios': 'horario_visita', 'telefone': 'telefone',
             'status_atual': 'status_atual', 'historia_breve': 'historia',
             'capacidade': 'capacidade', 'programacao': 'programacao',
             'entrada': 'entrada'}
PEND_MAP = {'nome': 'nome', 'nome_oficial': 'nome',
            'horarios': 'horario_visita', 'horario': 'horario_visita',
            'telefone': 'telefone', 'endereco': 'endereco',
            'historia_breve': 'historia', 'historia': 'historia',
            'capacidade': 'capacidade', 'entrada': 'entrada',
            'programacao': 'programacao', 'status_atual': 'status_atual'}


def by_name(lst, prefix):
    for p in lst:
        if p['nome_consulta'].startswith(prefix):
            return p
    return None


def dossie_de(p):
    d = {}
    fts = p.get('fontes') or {}
    doc = f"{p.get('nome_consulta')}. Dossiê da expansão turística 05/10/2026 (fonte obrigatória por campo)."
    if p.get('observacoes'):
        doc += ' OBS: ' + str(p['observacoes'])
    d['_doc'] = doc
    for sk, dk in CAMPO_MAP.items():
        v = p.get(sk)
        if v:
            d[dk] = {'valor': v, 'status': 'verificado',
                     'fonte_url': fts.get(sk), 'verificado_em': HOJE}
    if p.get('nome_popular'):
        d['nome_popular'] = p['nome_popular']
    if p.get('tipo'):
        d['tipo'] = p['tipo']
    for pend in (p.get('pendencias') or []):
        pk = pend.split(':')[0].split(' (')[0].strip().lower()
        dk = PEND_MAP.get(pk)
        if dk and dk not in d:
            d[dk] = {'valor': None, 'status': 'pendente',
                     'motivo': pend[:220], 'verificado_em': HOJE}
    return d


WS_PARES = [('nome_oficial', 'nome', 'fonte'),
            ('endereco', 'endereco', 'fonte_endereco'),
            ('horario', 'horario_visita', 'fonte_horario'),
            ('entrada', 'entrada', 'fonte_entrada'),
            ('telefone', 'telefone', 'fonte_telefone'),
            ('capacidade', 'capacidade', None),
            ('programacao', 'programacao', 'fonte_programacao'),
            ('status_atual', 'status_atual', None),
            ('historia_breve', 'historia', None),
            ('observacoes', None, None)]


def dossie_workspace(w):
    d = {}
    doc = f"{w.get('nome_oficial')}. Dossiê da expansão turística 05/10/2026 (fonte obrigatória por campo)."
    if w.get('observacoes'):
        doc += ' OBS: ' + str(w['observacoes'])
    d['_doc'] = doc
    if w.get('pendencia_telefone'):
        d['telefone'] = {'valor': None, 'status': 'pendente',
                         'motivo': w['pendencia_telefone'], 'verificado_em': HOJE}
    for sk, dk, fk in WS_PARES:
        v = w.get(sk)
        if v is None or dk is None:
            continue
        url = w.get(fk) if fk else None
        d[dk] = {'valor': v, 'status': 'verificado',
                 'fonte_url': url, 'verificado_em': HOJE}
    for k in ('nome_popular', 'tipo'):
        if w.get(k):
            d[k] = w[k]
    return d


novo, pulados = [], []
for prefix, slug in SLUGS_IGREJAS + SLUGS_MUSEUS + SLUGS_PREDIOS:
    origem = (igrejas if (prefix, slug) in SLUGS_IGREJAS
              else museus if (prefix, slug) in SLUGS_MUSEUS
              else predios)
    p = by_name(origem, prefix)
    if not p:
        pulados.append(f'{prefix}: NAO ENCONTRADO NA PESQUISA')
        continue
    if not p.get('existe', True):
        pulados.append(f"{prefix}: INEXISTENTE — {str(p.get('observacoes'))[:150]}")
        continue
    dos = dossie_de(p)
    with open(DOSSIES / f'{slug}.json', 'w', encoding='utf-8') as f:
        json.dump(dos, f, ensure_ascii=False, indent=1)
    novo.append(slug)

for slug in ('teatro-municipal', 'teatro-de-arena', 'centro-cultural-palace',
             'sesc-ribeirao-preto', 'instituto-figueiredo-ferraz'):
    dos = dossie_workspace(ws[slug])
    with open(DOSSIES / f'{slug}.json', 'w', encoding='utf-8') as f:
        json.dump(dos, f, ensure_ascii=False, indent=1)
    novo.append(slug)

print(f'DOSSIES ESCRITOS ({len(novo)}):')
for s in novo:
    d = json.load(open(DOSSIES / f'{s}.json', encoding='utf-8'))
    ver = [k for k, v in d.items() if isinstance(v, dict) and v.get('status') == 'verificado']
    pen = [k for k, v in d.items() if isinstance(v, dict) and v.get('status') == 'pendente']
    print(f'  {s}: verif={ver}')
    if pen:
        print(f'        pend={pen}')
print()
print('PULADOS (documentados, sem pagina):')
for s in pulados:
    print(' ', s)

print()
print('=== OBS MUSEU HISTORICO (integra) ===')
print(by_name(museus, 'Museu Histórico').get('observacoes'))
print()
print('=== OBS ESTACAO MOGIANA ===')
print(by_name(predios, 'Estação Mogiana').get('observacoes'))
print()
print('=== HISTORIA ESTACAO MOGIANA ===')
print(by_name(predios, 'Estação Mogiana').get('historia_breve'))
print()
print('=== NOME OFICIAL EST MOGIANA:', by_name(predios, 'Estação Mogiana').get('nome_oficial'))
