#!/usr/bin/env python3
"""Diagnóstico dos 22 fatais — Passo 1 (Leo GO, 05/10/2026)."""
import json

rep = open('reports/audit_20261005_131423.txt', encoding='utf-8').read()
print('=== SIMILARIDADE FATAIS (completos) ===')
for l in rep.splitlines():
    if 'Similaridade estrutural' in l:
        print(l.strip())

src = open('scripts/check_similaridade.py', encoding='utf-8').read()
print('\n=== TRECHOS-CHAVE check_similaridade.py ===')
for i, l in enumerate(src.splitlines()):
    if any(k in l for k in ['mestre', 'limite', '0.30', '0.40', '0.50',
                            '80', 'compartilhadas', 'overlap', 'mask']):
        print(f'{i+1}: {l.rstrip()[:150]}')

lf = json.load(open('content/dados-fonte/linhas.json', encoding='utf-8'))


def paradas(num):
    for k in lf:
        if k == num or k == str(int(num)) or k == num.zfill(3):
            return [(p.get('nome') or '').strip()
                    for p in (lf[k].get('paradas', {}).get('valor', []) or [])]
    return []


p301, p311 = paradas('301'), paradas('311')
s301, s311 = set(p301), set(p311)
inter = s301 & s311
uni = s301 | s311
print('\n=== 301 x 311 ===')
print(f'301: {len(s301)} paradas | 311: {len(s311)} | interseção: {len(inter)}')
if s311:
    print(f'311 contida em 301: {len(inter)/len(s311)*100:.1f}%')
if uni:
    print(f'jaccard: {len(inter)/len(uni)*100:.1f}%')

D = 'content/dados-fonte/pontos/'
for slug in ['museu-historico-plinio-travassos', 'palacio-rio-branco',
             'mis-rp', 'casa-da-memoria-italiana', 'mercado-municipal',
             'estacao-barracao', 'estacao-mogiana']:
    d = json.load(open(D + slug + '.json', encoding='utf-8'))
    v = d.get('historia', {})
    print(f'\n=== {slug}.historia ===')
    print(str(v.get('valor'))[:900])
