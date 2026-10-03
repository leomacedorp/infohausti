#!/usr/bin/env python3
"""
AUDITORIA: check_palavras.py
Valida mínimos de contagem de palavras narrativas por template (Regras 16 e 88 do Manual v1.2)
A contagem considera apenas o texto narrativo dentro de <main>,
excluindo cabeçalho, rodapé, breadcrumb, blocos de fonte/autoria, tabelas e listas de dados.
"""

import sys
import re
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / 'dist'
CONTENT_DIR = ROOT_DIR / 'content'
PAGINAS_DIR = CONTENT_DIR / 'paginas'

MINIMOS_POR_TEMPLATE = {
    'linha': 250,
    'linha.html': 250,
    'servico': 400,
    'servico.html': 400,
    'bairro': 400,
    'bairro.html': 400,
    'ponto': 800,
    'ponto.html': 800,
    'roteiro': 500,
    'roteiro.html': 500,
    'historia': 1500,
    'historia.html': 1500,
    'evento': 300,
    'evento.html': 300,
    'dados': 500,
    'dados.html': 500,
    'comparativo': 800,
    'comparativo.html': 800
}

def extract_countable_words(html_content):
    """Extrai texto contável conforme regra 16"""
    # Isola o <main>
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL | re.IGNORECASE)
    content = main_match.group(1) if main_match else html_content

    # Remove tabelas, listas, blocos de autoria e fontes
    content = re.sub(r'<table[^>]*>.*?</table>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ul[^>]*>.*?</ul>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ol[^>]*>.*?</ol>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<aside[^>]*>.*?</aside>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<section[^>]*aria-label=["\']Fontes.*?>.*?</section>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', ' ', content, flags=re.DOTALL | re.IGNORECASE)

    # Limpa tags HTML restantes
    clean_text = re.sub(r'<[^>]+>', ' ', content)
    words = clean_text.split()
    return len(words)

def check_palavras():
    fatals = []
    avisos = []

    if not DIST_DIR.exists():
        return ["[FATAL] Diretório dist/ não existe."], []

    # Mapeia template de cada slug através dos arquivos JSON de origem
    slug_template_map = {}
    if PAGINAS_DIR.exists():
        for jf in PAGINAS_DIR.glob('**/*.json'):
            try:
                with open(jf, 'r', encoding='utf-8') as f:
                    pdata = json.load(f)
                    slug_template_map[pdata.get('slug')] = pdata.get('template', 'base.html')
            except Exception:
                pass

    for html_file in DIST_DIR.glob('**/*.html'):
        if html_file.name in ('404.html', 'index.html'):
            continue

        slug = html_file.stem
        template = slug_template_map.get(slug, 'base.html')
        minimo = MINIMOS_POR_TEMPLATE.get(template)

        # Se for um template com mínimo estrito cadastrado
        if minimo:
            html = html_file.read_text(encoding='utf-8')
            qtd_palavras = extract_countable_words(html)

            if qtd_palavras < minimo:
                fatals.append(
                    f"{html_file.relative_to(ROOT_DIR)}: Contém {qtd_palavras} palavras narrativas. Mínimo exigido para template '{template}': {minimo} palavras."
                )

    return fatals, avisos

def main():
    fatals, avisos = check_palavras()
    for a in avisos:
        print(f"[AVISO] {a}")
    for f in fatals:
        print(f"[FATAL] {f}")

    if fatals:
        print(f"\n[ERRO] check_palavras falhou com {len(fatals)} erro(s) fatal(is).")
        sys.exit(1)
    else:
        print(f"[OK] check_palavras aprovado.")
        sys.exit(0)

if __name__ == '__main__':
    main()
