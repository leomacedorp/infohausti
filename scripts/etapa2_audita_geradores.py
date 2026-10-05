#!/usr/bin/env python3
"""
ETAPA 2 — (A) Auditoria estrutural dos gera_lote*.py e (B) extração de
unidades-saude.json a partir do Obsidian Hermes.

A: classifica como cada gerador constrói a narrativa (hardcoded vs dados-fonte),
   quantas paradas reais do GTFS aparecem no código-fonte, e a taxa de erros
   fatais reais por lote (lista A do relatório limpo da Etapa 1).
B: extrai as 69 unidades de saúde da SMS Ribeirão Preto (fonte: Portal
   Municipal + CNES/DataSUS, Mar/2026 — consolidado no Obsidian Hermes
   Unidades_Saude_Classificadas.md). Extração autorizada pelo Leo (04/10/2026).
NÃO altera conteúdo de páginas. NÃO commite.
"""
import json
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
DADOS = ROOT / "content" / "dados-fonte"
REPORTS = ROOT / "reports"
OBS = Path(r"C:/Users/lamacedo/Documents/Hermes/Obsidian/Hermes/Unidades_Saude_Classificadas.md")

# ---------------- A: AUDITORIA DOS GERADORES ----------------
linhas = json.load(open(DADOS / "linhas.json", encoding="utf-8"))
all_stops = set()
for d in linhas.values():
    for p in (d.get("paradas", {}) or {}).get("valor", []) or []:
        if p.get("nome"):
            all_stops.add(p["nome"])

mestre = json.load(open(ROOT / "content" / "lista-mestre.json", encoding="utf-8"))
lote_lines = {i: [e["codigo"] for e in mestre.get(f"linhas_lote{i}", [])] for i in range(1, 8)}

limpo = (REPORTS / "check_fontes_factuais_limpo.txt").read_text(encoding="utf-8")
fatais_por_linha = {}
mA = re.search(r"LISTA A — .*?\n(.*?)(?=\nLISTA B — )", limpo, re.S)
if mA:
    for ln in mA.group(1).splitlines():
        m = re.match(r"\s*\[(\w+)\]", ln)
        if m:
            fatais_por_linha[m.group(1)] = fatais_por_linha.get(m.group(1), 0) + 1

rel = ["# ETAPA 2 — AUDITORIA DOS GERADORES (gera_lote1..7.py)", "",
       f"Gerado: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]

# Heurísticas de construção
PADRAO_HARDCODE = re.compile(r'"(visao_geral|itinerario_texto|paradas_destaque|'
                             r'bairros_texto|atracoes_proximas)":\s*"<p>')
PADRAO_LEITURA_FONTE = re.compile(r"linhas\.json|dados-fonte|json\.load|open\(")
PADRAO_PARADA_GTFS = re.compile(r'"Ponto (\d+) -')

for i in range(1, 8):
    f = ROOT / "scripts" / f"gera_lote{i}.py"
    src = f.read_text(encoding="utf-8")
    n_hard = len(PADRAO_HARDCODE.findall(src))
    le_fonte = bool(PADRAO_LEITURA_FONTE.search(src))
    n_paradas_codigo = len(set(PADRAO_PARADA_GTFS.findall(src)))
    # quantas dessas paradas existem no GTFS oficial?
    paradas_no_codigo = [m.group(0) for m in PADRAO_PARADA_GTFS.finditer(src)]
    batem = sum(1 for p in paradas_no_codigo if p in all_stops)
    codigos = lote_lines.get(i, [])
    fatais = {c: fatais_por_linha.get(c, 0) for c in codigos}
    total_fatais = sum(fatais.values())
    com_fatal = [c for c, n in fatais.items() if n > 0]
    rel += [
        f"## gera_lote{i}.py — linhas {codigos}",
        f"- Textos narrativos hardcoded (secoes:\u00a0<p>...): **{n_hard} blocos**",
        f"- Lê dados-fonte/linhas.json? **{'SIM' if le_fonte else 'NÃO'}**",
        f"- Paradas 'Ponto NNNN' citadas no código: {n_paradas_codigo} únicas | "
        f"presentes no GTFS oficial: {batem}",
        f"- Erros fatais REAIS (lista A) nas linhas deste lote: **{total_fatais}**"
        + (f" (linhas afetadas: {', '.join(com_fatal)})" if com_fatal else ""),
        "",
    ]

padrao_resumo = all(len(PADRAO_HARDCODE.findall((ROOT / "scripts" / f"gera_lote{i}.py").read_text(encoding="utf-8"))) > 0 for i in range(1, 8))
rel += [
    "## DIAGNÓSTICO DO PADRÃO",
    f"- Estrutura: **{'NARRATIVA HARDCODED POR LINHA' if padrao_resumo else 'MISTA'}** "
    "(textos escritos à mão dentro de cada gera_loteN.py, sem extração de dados-fonte)",
    "- Consequência: o texto cita vias/instituições por memória do gerador, não pelas "
    "paradas reais da linha → origem dos 76 erros reais (lista A) e das invenções (lista B)",
    "- A correção (Ajuste 4 do Leo) proposta para a Etapa 3: narrar SOMENTE a partir de "
    "dados-fonte/linhas.json da própria linha (vias reais, bairros reais, grade real),",
    "  com instituições permitidas apenas quando presentes em dados-fonte/pontos/.",
    "",
    "*Sem proposta de correção codificada — aguardando aprovação (regra 1.20).*",
]

out = REPORTS / "etapa2_gerador_auditado.md"
out.write_text("\n".join(rel), encoding="utf-8")
print("\n".join(rel))
print(f"\n[Gravado: {out}]")

# ---------------- B: EXTRAÇÃO UNIDADES-SAUDE.JSON ----------------
txt = OBS.read_text(encoding="utf-8")
rows = []
sec = None
for ln in txt.splitlines():
    if ln.startswith("###"):
        sec = ln
        continue
    m = re.match(r"\|\s*([^|]+)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*(.+?)\s*\|?\s*$", ln)
    if not m or set(m.group(1).strip()) <= {"-", " "}:
        continue
    g = [x.strip() for x in m.groups()]
    if g[0] in ("Unidade", "Distrito") or g[0].startswith("---"):
        continue
    # básica: |Unidade|Tipo|CNES|Distrito|Endereço|Classificação|
    if g[1] and g[2].isdigit():
        rows.append({"nome": g[0], "tipo": g[1], "cnes": g[2], "distrito": g[3],
                     "endereco": g[4], "classificacao": g[5].replace("**", "")})
    # especialidade: |Unidade|Tipo|CNES|Distrito|Endereço|Observação|
    elif g[1] and (g[2].isdigit() or g[2] == "—"):
        rows.append({"nome": g[0], "tipo": g[1], "cnes": g[2] if g[2] != "—" else None,
                     "distrito": g[3], "endereco": g[4], "observacao": g[5].replace("**", "")})

unidades = []
for r in rows:
    e = {"nome": r["nome"], "tipo": r["tipo"], "cnes": r.get("cnes"),
         "distrito": r["distrito"] or None,
         "endereco": (r["endereco"] if r["endereco"] and r["endereco"] != "—" else None),
         "classificacao": r.get("classificacao") or r.get("observacao")}
    unidades.append(e)

doc = {
    "_doc": ("Unidades de saúde da SMS Ribeirão Preto — 69 unidades. Fonte: Portal "
             "Municipal + CNES/DataSUS (Mar/2026), consolidado em base interna Hermes "
             "(Obsidian). Extração autorizada pelo Leo em 04/10/2026. Endereços ausentes "
             "na fonte original ficam null (não inventar)."),
    "_fonte": ["https://cnes2.datasus.gov.br", "Portal Municipal de Ribeirão Preto"],
    "_verificado_em": "2026-03",
    "unidades": unidades,
}
dest = DADOS / "unidades-saude.json"
dest.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\n[unidades-saude.json] {len(unidades)} unidades gravadas em {dest}")
sem_end = sum(1 for u in unidades if not u["endereco"])
print(f"  - com endereço: {len(unidades) - sem_end} | sem endereço na fonte: {sem_end} (null, sem invenção)")
