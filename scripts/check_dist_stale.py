#!/usr/bin/env python3
"""
CHECK DE DIST STALE — scripts/check_dist_stale.py
Bloqueia commit/publicação se dist/ estiver mais antigo que content/ —
evita o problema do commit 6a91119 (dist stale no ar com dado errado).

Lógica: para cada página .json em content/ com status 'pronta', o .html
correspondente em dist/ deve existir E ser mais recente (mtime) que o .json.
Qualquer página pronta sem .html, ou com .html mais antigo = FATAL.
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content' / 'paginas'
DIST = ROOT / 'dist'

def check_dist_stale():
    import json
    fatals, avisos = [], []
    n_ok = n_stale = n_missing = 0
    for jf in CONTENT.rglob('*.json'):
        if jf.name == 'index.json':
            continue
        try:
            d = json.loads(jf.read_text(encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(d, dict) or d.get('status') != 'pronta' or not d.get('slug'):
            continue
        html = DIST / (d['slug'] + '.html')
        if not html.exists():
            n_missing += 1
            fatals.append(f"DIST-STALE (faltando): '{d['slug']}' está pronta em content/ mas não existe em dist/ — rode build.py antes de commitar")
            continue
        if html.stat().st_mtime < jf.stat().st_mtime:
            n_stale += 1
            fatals.append(f"DIST-STALE (desatualizado): dist/{d['slug']}.html é mais antigo que content/ — rode build.py antes de commitar")
        else:
            n_ok += 1
    resumo = f"[check_dist_stale] {n_ok} em dia, {n_stale} desatualizadas, {n_missing} faltando"
    print(resumo)
    if n_ok and not fatals:
        avisos.append(resumo)
    return fatals, avisos

if __name__ == '__main__':
    f, a = check_dist_stale()
    if f:
        print(f"FATAL: {len(f)} página(s) com dist stale")
        sys.exit(1)
    print("OK: dist em dia com content")
