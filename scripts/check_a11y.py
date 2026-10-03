#!/usr/bin/env python3
"""
AUDITORIA: check_a11y.py
Valida acessibilidade WCAG 2.1 AA (alt-text, skip-link, lang)
"""

import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / 'dist'

def check_a11y():
    fatals = []
    avisos = []

    if not DIST_DIR.exists():
        return ["[FATAL] Diretório dist/ não existe."], []

    html_files = list(DIST_DIR.glob('**/*.html'))
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')
        rel_path = html_file.relative_to(ROOT_DIR)

        # 1. <html lang="...">
        if not re.search(r'<html\s+[^>]*lang=["\']pt-BR["\']', content, re.IGNORECASE):
            fatals.append(f"{rel_path}: Tag <html lang='pt-BR'> ausente ou incorreta.")

        # 2. Skip link acessível
        if 'skip-link' not in content:
            fatals.append(f"{rel_path}: Skip link de acessibilidade ausente.")

        # 3. Tags <img>
        img_tags = re.findall(r'<img\s+([^>]*?)>', content, re.IGNORECASE)
        for img in img_tags:
            alt_match = re.search(r'alt=["\'](.*?)["\']', img, re.IGNORECASE)
            if not alt_match:
                fatals.append(f"{rel_path}: Imagem sem atributo 'alt': <img {img[:50]}...>")
            else:
                alt_text = alt_match.group(1).strip()
                words = alt_text.split()
                # Regra 91: Alt-text com menos de 5 palavras é Aviso
                if len(words) < 5 and len(alt_text) > 0:
                    avisos.append(f"{rel_path}: Alt-text curto ({len(words)} palavras): '{alt_text}'")

    return fatals, avisos

def main():
    fatals, avisos = check_a11y()
    for a in avisos:
        print(f"[AVISO] {a}")
    for f in fatals:
        print(f"[FATAL] {f}")

    if fatals:
        print(f"\n[ERRO] check_a11y falhou com {len(fatals)} erro(s) fatal(is).")
        sys.exit(1)
    else:
        print(f"[OK] check_a11y aprovado.")
        sys.exit(0)

if __name__ == '__main__':
    main()
