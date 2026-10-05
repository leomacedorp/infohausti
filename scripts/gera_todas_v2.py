#!/usr/bin/env python3
"""
ORQUESTRADOR DO LOTE ÚNICO — 113 linhas (scripts/gera_todas_v2.py)
GO do Leo (04/10/2026), 2 guardrails:
- Leva 1: 61 linhas commitadas (Lotes 1-6) | Leva 2: 52 restantes
- Validação embutida: check_fontes_factuais por linha ANTES de gravar
  (linha com fatal não é gravada — reportada)
- Após gravar tudo: build.py + 3 checks globais + relatório para o Leo
- NADA é commitado (Guardrail 2)
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_fontes_factuais as ck

ROOT = Path(__file__).resolve().parent.parent
PAG = ROOT / "content" / "paginas" / "linhas"

# leva 1 = linhas com página commitada; leva 2 = demais
import subprocess as sp
commitadas = set()
out = sp.run(["git", "ls-files", "content/paginas/linhas/"], cwd=ROOT,
             capture_output=True, text=True).stdout
for ln in out.splitlines():
    m = re.match(r".*linha-(\d+)-.*\.json", ln) if (re := __import__("re")) else None
    if m:
        commitadas.add(m.group(1))

paginas = sorted(PAG.glob("linha-*.json"))
todas = []
for p in paginas:
    m = __import__("re").match(r"linha-(\d+)-", p.name)
    if m:
        todas.append((m.group(1), p))

leva1 = [(n, p) for n, p in todas if n in commitadas]
leva2 = [(n, p) for n, p in todas if n not in commitadas]
print(f"Universo: {len(todas)} páginas | Leva 1 (commitadas): {len(leva1)} | Leva 2: {len(leva2)}")

falhas = []
ok = []
for leva, itens in (("LEVA 1", leva1), ("LEVA 2", leva2)):
    print(f"\n===== {leva} ({len(itens)} linhas) =====")
    for num, alvo in itens:
        # 1. gera secoes (dry)
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "gera_linha_v2.py"), num],
                           capture_output=True, text=True)
        if r.returncode != 0:
            falhas.append((num, "gerador-erro", r.stderr[:150]))
            continue
        secoes = json.loads(r.stdout)["secoes"]
        # 2. valida ANTES de gravar
        chave = num.zfill(3) if num.zfill(3) in ck.LINHAS_FONTE else num
        fonte = ck.LINHAS_FONTE.get(chave) or next(
            (ck.LINHAS_FONTE[k] for k in ck.LINHAS_FONTE if k.lstrip("0") == num.lstrip("0")), None)
        if not fonte:
            falhas.append((num, "sem-fonte", ""))
            continue
        fatais, _ = ck.verifica_linha(chave, fonte, secoes)
        if fatais:
            falhas.append((num, f"{len(fatais)} fatais", fatais[0][:100]))
            continue
        # 3. grava
        pag = json.load(open(alvo, encoding="utf-8"))
        pag["secoes"].update(secoes)
        alvo.write_text(json.dumps(pag, ensure_ascii=False, indent=2), encoding="utf-8")
        ok.append(num)

print(f"\n===== RESULTADO DA GERACAO =====")
print(f"Gravadas com 0 fatais: {len(ok)}/{len(todas)}")
print(f"Nao gravadas: {len(falhas)}")
for num, motivo, det in falhas:
    print(f"  [{num}] {motivo} | {det}")
