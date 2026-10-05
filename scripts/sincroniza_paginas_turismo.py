#!/usr/bin/env python3
"""SINCRONIZA PÁGINAS DE TURISMO COM OS DOSSIÊS CORRIGIDOS (05/10/2026).
Página deriva do dossiê: visita.endereco/horario/ingresso <- dados-fonte/pontos/.
Atualiza também título/H1 do Santuário (nome oficial) e o roteiro centro-historico
(erro por contágio do Museu do Café)."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
F = ROOT / "content" / "dados-fonte" / "pontos"
PG = ROOT / "content" / "paginas" / "ribeirao-preto" / "pontos-turisticos"

def val(d, k):
    v = d.get(k)
    if isinstance(v, dict):
        v = v.get("valor")
    return v or ""

pares = [
    ("biblioteca-sinha-junqueira", "biblioteca-sinha-junqueira"),
    ("bosque-fabio-barreto", "bosque-fabio-barreto"),
    ("catedral-metropolitana", "catedral-metropolitana"),
    ("museu-do-cafe", "museu-do-cafe"),
    ("palacete-camilo-de-mattos", "palacete-camilo-de-mattos"),
    ("parque-curupira", "parque-curupira"),
    ("parque-maurilio-biagi", "parque-maurilio-biagi"),
    ("praca-xv-de-novembro", "praca-xv-de-novembro"),
    ("quarteirao-paulista", "quarteirao-paulista"),
    ("santuario-sete-capelas", "santuario-sete-capelas"),
    ("theatro-pedro-ii", "teatro-dom-pedro"),
    ("marp-museu-de-arte", "marp"),
]

for sf, sp in pares:
    d = json.loads((F / f"{sf}.json").read_text(encoding="utf-8"))
    p_path = PG / f"{sp}.json"
    p = json.loads(p_path.read_text(encoding="utf-8"))
    vis = p.get("visita", {})
    mudou = []
    novo_end = val(d, "endereco")
    novo_hor = val(d, "horario_visita")
    novo_ing = val(d, "ingresso")
    novo_tel = val(d, "telefone")
    if novo_end and vis.get("endereco") != novo_end:
        vis["endereco"] = novo_end; mudou.append("endereco")
    if novo_hor and vis.get("horario") != novo_hor:
        vis["horario"] = novo_hor; mudou.append("horario")
    if novo_ing and vis.get("ingresso") != novo_ing:
        vis["ingresso"] = novo_ing; mudou.append("ingresso")
    if novo_tel and p.get("telefone") != novo_tel:
        p["telefone"] = novo_tel; mudou.append("telefone")
    p["visita"] = vis
    # status atual
    st = val(d, "status_atual")
    if st and p.get("status_atual") != st:
        p["status_atual"] = st; mudou.append("status")
    p_path.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[{sp}] {'atualizado: ' + ', '.join(mudou) if mudou else 'ja consistente'}")

# Santuário: nome oficial no título/H1 (apelido preservado)
s = json.loads((PG / "santuario-sete-capelas.json").read_text(encoding="utf-8"))
if "Medalha Milagrosa" not in s.get("h1", ""):
    s["h1"] = "Santuário Nossa Senhora da Medalha Milagrosa (Sete Capelas)"
    antigo_t = s.get("titulo", "")
    s["titulo"] = "Santuário N. Sra. da Medalha Milagrosa (Sete Capelas) | Visite Ribeirão Preto"
    (PG / "santuario-sete-capelas.json").write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")
    print("[santuario-sete-capelas] nome oficial aplicado em h1/titulo")

# Roteiro centro-historico: remove Museu do Café de "abertos simultaneamente"
r_path = ROOT / "content" / "paginas" / "ribeirao-preto" / "roteiros" / "centro-historico.json"
r = json.loads(r_path.read_text(encoding="utf-8"))
txt = json.dumps(r, ensure_ascii=False)
if "Museu do Café" in txt and "abertos" in txt:
    def fix(o):
        if isinstance(o, str):
            if "Museu do Café" in o and "abertos" in o:
                o = re.sub(r"e?\s*Museu do Café", "", o)
                o = o.replace("encontram-se simultaneamente abertos para visitação pública",
                              "encontram-se abertos para visitação pública")
            elif "Museu do Café" in o:
                o = o.replace("Museu do Café", "Museu do Café (temporariamente fechado)")
        elif isinstance(o, dict):
            o = {k: fix(v) for k, v in o.items()}
        elif isinstance(o, list):
            o = [fix(v) for v in o]
        return o
    r = fix(r)
    r_path.write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
    print("[roteiro centro-historico] Museu do Café ajustado (fechado)")
