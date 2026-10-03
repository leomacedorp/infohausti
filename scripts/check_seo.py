#!/usr/bin/env python3
"""
AUDITORIA: check_seo.py
Verifica title, meta description, canonical absoluto e tags sociais em dist/
"""

import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / 'dist'

def check_seo():
    fatals = []
    avisos = []

    if not DIST_DIR.exists():
        return ["[FATAL] Diretório dist/ não existe."], []

    html_files = list(DIST_DIR.glob('**/*.html'))
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')
        rel_path = html_file.relative_to(ROOT_DIR)

        # 1. <title>
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if not title_match or not title_match.group(1).strip():
            fatals.append(f"{rel_path}: Tag <title> ausente ou vazia.")

        # 2. Meta description
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        if not desc_match or not desc_match.group(1).strip():
            fatals.append(f"{rel_path}: Meta description ausente ou vazia.")

        # 3. Canonical absoluto (Regra 86: Canonical relativo = Fatal)
        can_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
        if not can_match:
            fatals.append(f"{rel_path}: Link canonical ausente.")
        else:
            can_url = can_match.group(1).strip()
            if not can_url.startswith(('http://', 'https://')):
                fatals.append(f"{rel_path}: Canonical relativo proibido: '{can_url}' (deve ser absoluto).")

        # 4. OpenGraph e Twitter Cards (Aviso)
        if 'og:title' not in content or 'og:description' not in content:
            avisos.append(f"{rel_path}: Tags Open Graph incompletas.")

    return fatals, avisos

def main():
    fatals, avisos = check_seo()
    for a in avisos:
        print(f"[AVISO] {a}")
    for f in fatals:
        print(f"[FATAL] {f}")

    if fatals:
        print(f"\n[ERRO] check_seo falhou com {len(fatals)} erro(s) fatal(is).")
        sys.exit(1)
    else:
        print(f"[OK] check_seo aprovado.")
        sys.exit(0)

if __name__ == '__main__':
    main()
