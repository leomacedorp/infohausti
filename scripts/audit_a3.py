#!/usr/bin/env python3
"""
Auditoria do Bloco A3 - Verificação das Partials
"""

import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_a3():
    partials_dir = Path('partials')
    if not partials_dir.exists():
        print("[ERRO] Diretório partials/ não existe.")
        return False

    required_partials = [
        'cabecalho.html',
        'rodape.html',
        'breadcrumb.html',
        'skip_link.html',
        'lgpd_banner.html',
        'bloco_autoria.html',
        'bloco_fontes.html',
        'anuncio_topo.html',
        'anuncio_meio.html',
        'anuncio_rodape.html'
    ]

    issues = []

    for name in required_partials:
        file_path = partials_dir / name
        if not file_path.exists():
            issues.append(f"Partial obrigatória ausente: {name}")
            continue

        content = file_path.read_text(encoding='utf-8')

        # 1. Deve documentar variáveis no topo
        if "VARIÁVEIS UTILIZADAS" not in content and "PARTIAL:" not in content:
            issues.append(f"{name}: Não documenta as variáveis utilizadas no topo.")

        # 2. Proibido link vazio ou placeholder '#'
        # Procura por href="#" ou href='#'
        if re.search(r'href\s*=\s*["\']#["\']', content):
            issues.append(f"{name}: Contém link proibido href='#'")

    if issues:
        print("[ERRO] AUDITORIA A3 FALHOU:")
        for iss in issues:
            print(f"  - {iss}")
        return False

    print("[OK] AUDITORIA A3 APROVADA:")
    print(f"  - Todas as {len(required_partials)} partials presentes e em conformidade.")
    print("  - Cada partial documenta variáveis no cabeçalho.")
    print("  - Nenhum link vazio '#' encontrado.")
    return True

if __name__ == '__main__':
    ok = audit_a3()
    sys.exit(0 if ok else 1)
