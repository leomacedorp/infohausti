#!/usr/bin/env python3
"""
ETAPA 2 — FILTRO B1/B2 (Infohaus RP)
Recebe a lista B do relatório limpo e separa:
  B1 — capturas truncadas/genéricas -> reclassificadas (RUÍDO ou CONTEXTO legítimo)
  B2 — itens genuínos com nome próprio -> vão para web search (Ajuste 2)
Saída: reports/etapa2_b_filtrada.txt (B2 inicialmente sem verificação web;
       a verificação é registrada em seguida pelo Hermes e compilada no mesmo arquivo).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'reports' / 'check_fontes_factuais_limpo.txt'
OUT = ROOT / 'reports' / 'etapa2_b_filtrada.txt'

# ---------- B1: padrões de truncamento/genéricos ----------
TERMINA_PREPOSICAO = re.compile(r'\b(da|do|de|e|em|na|no|dentre|entre)$', re.I)
GENERICAS_EXATAS = {
    # terminais centrais: infraestrutura óbvia do sistema (todas as linhas
    # partem/chegam ao Terminal Urbano Central) — menção legítima;
    # a PLATAFORMA específica é o único dado a validar vs dados-fonte
    'terminal urbano central', 'terminal central', 'terminal urbano',
    'praça da', 'praça', 'parque da', 'parque do', 'paróquia do', 'fórum',
    'museu de arte', 'hospital da',
}
# terminal com plataforma explícita: legítimo como menção ao hub;
# anota para validar a letra da plataforma contra os dados da linha
TERMINAL_PLAT = re.compile(r'^terminal urbano\s*-\s*plataforma\s*([a-h0-9])', re.I)

def eh_b1(nome):
    n = nome.strip().rstrip('.').strip()
    if TERMINA_PREPOSICAO.search(n):
        return 'RUÍDO (preposição pendurada — captura truncada)'
    if n.lower() in GENERICAS_EXATAS:
        return 'RUÍDO (genérica sem nome próprio)'
    if TERMINAL_PLAT.search(n):
        m = TERMINAL_PLAT.search(n)
        return f'CONTEXTO-LEGÍTIMO (Terminal Urbano Central é hub real do sistema; validar Plataforma {m.group(1).upper()} vs dados-fonte da linha)'
    return None

def main():
    txt = SRC.read_text(encoding='utf-8')
    # extrai bloco LISTA B
    m = re.search(r'LISTA B — .*?\n(.*?)(?=\nLISTA C — )', txt, re.S)
    if not m:
        raise SystemExit('Bloco LISTA B não encontrado')
    bloco = m.group(1)

    itens = []  # (linha, tipo, nome, secao, nota)
    linha_atual = None
    for ln in bloco.splitlines():
        ml = re.match(r'\s*\[(\w+)\]', ln)
        if ml:
            linha_atual = ml.group(1)
            continue
        mi = re.match(r'\s*-\s*\(([^)]+)\)\s*([^:]+):\s*"([^"]+)"\s*(?:—\s*(.*))?$', ln)
        if mi:
            secao, tipo, nome, nota = mi.groups()
            itens.append((linha_atual, tipo.strip(), nome, secao, (nota or '').strip()))

    b1, b2 = [], []
    for it in itens:
        motivo = eh_b1(it[2])
        if motivo:
            b1.append((*it, motivo))
        else:
            b2.append(it)

    rel = ['ETAPA 2 — LISTA B FILTRADA (B1/B2)',
           '',
           f'Total de itens na lista B: {len(itens)}',
           f'B1 (truncadas/genéricas — reclassificadas): {len(b1)}',
           f'B2 (genuínas — alvo de web search): {len(b2)}',
           '=' * 70, '']

    rel.append('B1 — RECLASSIFICADAS:')
    for linha, tipo, nome, secao, nota, motivo in b1:
        rel.append(f'  [{linha}] ({secao}) "{nome}" -> {motivo}')

    rel.append('')
    rel.append('=' * 70)
    rel.append('B2 — ITENS GENUÍNOS (verificar por web search):')
    por_linha = {}
    for linha, tipo, nome, secao, nota in b2:
        por_linha.setdefault(linha, []).append((tipo, nome, secao, nota))
    for linha in sorted(por_linha):
        rel.append(f'  [{linha}]')
        for tipo, nome, secao, nota in por_linha[linha]:
            rel.append(f'    - ({secao}) {tipo}: "{nome}"' + (f' — {nota}' if nota else ''))

    rel.append('')
    rel.append('=' * 70)
    unicos = sorted({nome.strip().rstrip('.') for _, _, nome, _, _ in b2})
    rel.append(f'B2 ÚNICOS PARA WEB SEARCH ({len(unicos)}):')
    for u in unicos:
        rel.append(f'  - {u}')

    OUT.write_text('\n'.join(rel), encoding='utf-8')
    print('\n'.join(rel))
    print(f'\n[Gravado: {OUT}]')

if __name__ == '__main__':
    main()
