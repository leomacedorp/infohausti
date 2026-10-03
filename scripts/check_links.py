#!/usr/bin/env python3
"""
AUDITORIA: check_links.py
Verifica integridade de links internos, links vazios e proibição de href="#"
"""

import sys
import re
from pathlib import Path
from urllib.parse import urlparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / 'dist'

def check_links():
    fatals = []
    avisos = []

    if not DIST_DIR.exists():
        return ["[FATAL] Diretório dist/ não existe para verificação de links."], []

    html_files = list(DIST_DIR.glob('**/*.html'))
    if not html_files:
        return ["[FATAL] Nenhum arquivo HTML encontrado em dist/."], []

    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')
        rel_path = html_file.relative_to(ROOT_DIR)

        # Procura todos os hrefs
        links = re.findall(r'href\s*=\s*["\'](.*?)["\']', content)

        for link in links:
            # 1. Proibição de link '#' vazio (Fatal)
            if link.strip() == '#' or link.strip() == '':
                fatals.append(f"{rel_path}: Link vazio proibido encontrado: href='{link}'")
                continue

            # Links externos (http/https), mailto, tel e âncoras locais ignoram checagem local
            if link.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                continue

            # 2. Links internos relativos ou absolutos locais
            parsed = urlparse(link)
            clean_path = parsed.path

            if clean_path.startswith('/'):
                target = DIST_DIR / clean_path.lstrip('/')
            else:
                target = (html_file.parent / clean_path).resolve()

            # Se for diretório, checa se tem index.html
            if target.is_dir():
                target = target / 'index.html'

            # Se não tiver extensão e nem for barra, tenta .html
            if not target.exists() and not target.suffix:
                target = target.with_suffix('.html')

            if not target.exists():
                fatals.append(f"{rel_path}: Link interno quebrado para '{link}' (alvo não existe em dist/)")

    return fatals, avisos

def main():
    fatals, avisos = check_links()
    for a in avisos:
        print(f"[AVISO] {a}")
    for f in fatals:
        print(f"[FATAL] {f}")

    if fatals:
        print(f"\n[ERRO] check_links falhou com {len(fatals)} erro(s) fatal(is).")
        sys.exit(1)
    else:
        print(f"[OK] check_links aprovado.")
        sys.exit(0)

if __name__ == '__main__':
    main()
