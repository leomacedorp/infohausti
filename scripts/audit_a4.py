#!/usr/bin/env python3
"""
Auditoria do Bloco A4 - Validação do gerador build.py, HTML e JSON-LD
"""

import sys
import json
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_a4():
    issues = []

    # 1. Checa existência dos arquivos obrigatórios de saída
    required_files = [
        Path('scripts/build.py'),
        Path('templates/base.html'),
        Path('content/config.json'),
        Path('content/correcoes.json'),
        Path('dist/sitemap.xml'),
        Path('dist/search-index.json'),
        Path('dist/teste-exemplo.html')
    ]

    for rf in required_files:
        if not rf.exists():
            issues.append(f"Arquivo de saída obrigatório ausente: {rf}")

    if issues:
        print("[ERRO] AUDITORIA A4 FALHOU:")
        for iss in issues:
            print(f"  - {iss}")
        return False

    # 2. Inspeciona o HTML gerado
    html_content = Path('dist/teste-exemplo.html').read_text(encoding='utf-8')

    if 'https://infohausti.com.br/teste-exemplo.html' not in html_content:
        issues.append("Canonical absoluto incorreto ou ausente em dist/teste-exemplo.html")

    if '<!-- TRILHA DE AUDITORIA:' not in html_content:
        issues.append("Comentário de trilha de auditoria ausente em dist/teste-exemplo.html")

    # 3. Valida sintaxe e conteúdo do JSON-LD
    json_match = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', html_content, re.DOTALL)
    if not json_match:
        issues.append("Bloco JSON-LD não encontrado no HTML gerado.")
    else:
        try:
            data = json.loads(json_match.group(1))
            if data.get('@context') != 'https://schema.org':
                issues.append("JSON-LD: @context não é https://schema.org")
            graph = data.get('@graph', [])
            types = [item.get('@type') for item in graph]
            if 'WebPage' not in types:
                issues.append("JSON-LD: Entidade WebPage ausente no @graph")
            if 'BreadcrumbList' not in types:
                issues.append("JSON-LD: Entidade BreadcrumbList ausente no @graph")
            if 'FAQPage' not in types:
                issues.append("JSON-LD: Entidade FAQPage ausente no @graph")
        except json.JSONDecodeError as e:
            issues.append(f"JSON-LD inválido (erro de parsing JSON): {e}")

    # 4. Valida sitemap e search index
    sitemap = Path('dist/sitemap.xml').read_text(encoding='utf-8')
    if 'https://infohausti.com.br/teste-exemplo.html' not in sitemap:
        issues.append("Sitemap.xml não contém a URL gerada.")

    search_idx = Path('dist/search-index.json').read_text(encoding='utf-8')
    if 'Página de Teste de Compilação' not in search_idx:
        issues.append("search-index.json não indexou a página de teste.")

    if issues:
        print("[ERRO] AUDITORIA A4 FALHOU:")
        for iss in issues:
            print(f"  - {iss}")
        return False

    print("[OK] AUDITORIA A4 APROVADA:")
    print("  - build.py gerou HTML válido com canonical absoluto")
    print("  - JSON-LD parseou perfeitamente com WebPage, BreadcrumbList e FAQPage")
    print("  - Trilha de auditoria presente")
    print("  - sitemap.xml e search-index.json gerados com sucesso")
    return True

if __name__ == '__main__':
    ok = audit_a4()
    sys.exit(0 if ok else 1)
