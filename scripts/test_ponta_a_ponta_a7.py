#!/usr/bin/env python3
"""
TESTE DE PONTA A PONTA (Bloco A7)
Cria 1 página falsa com status pronta, roda build e auditoria,
e depois muda o status dela para rascunho, confirmando que não aparece em dist/
e que audit_all.py passa com sucesso.
"""

import sys
import json
import shutil
import subprocess
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
PAGINAS_DIR = ROOT_DIR / 'content' / 'paginas'
DIST_DIR = ROOT_DIR / 'dist'

def main():
    print("==================================================")
    print("   TESTE DE PONTA A PONTA (Bloco A7)             ")
    print("==================================================")

    test_page_file = PAGINAS_DIR / 'pagina-teste-a7.json'
    exemplo_file = PAGINAS_DIR / 'exemplo.json'
    exemplo_dist = DIST_DIR / 'teste-exemplo.html'

    # Remove resíduo de testes anteriores para evitar colisão de similaridade
    if exemplo_file.exists():
        exemplo_file.unlink()
    if exemplo_dist.exists():
        exemplo_dist.unlink()

    # 1. Cria página de teste com status 'pronta' e texto único
    page_data = {
        "slug": "pagina-teste-a7",
        "template": "base.html",
        "status": "pronta",
        "titulo": "Auditoria de Integridade Operacional Ribeirão Vivo",
        "descricao": "Metodologia de testes contínuos para aferição de qualidade do portal cívico e de mobilidade de Ribeirão Preto.",
        "h1": "Auditoria de Integridade Operacional",
        "keywords": "auditoria, integridade, qualidade",
        "publicado": "2026-10-03",
        "atualizado": "2026-10-03",
        "proxima_revisao": "2026-11-03",
        "breadcrumbs": [
            {"nome": "Início", "url": "/"},
            {"nome": "Qualidade"}
        ],
        "fontes": [
            {"nome": "Diretrizes de Arquitetura de Software", "url": "https://infohausti.com.br", "data": "2026-10-03"}
        ],
        "faq": [
            {"pergunta": "Qual o propósito deste protocolo?", "resposta": "Garantir validação contínua e ausência de links quebrados."},
            {"pergunta": "Como funciona o descarte de rascunhos?", "resposta": "Páginas em rascunho são sumariamente excluídas da pasta de distribuição pública."},
            {"pergunta": "Quem audita este processo?", "resposta": "O pipeline automático antes de cada integração com a ramificação principal."}
        ]
    }

    with open(test_page_file, 'w', encoding='utf-8') as f:
        json.dump(page_data, f, ensure_ascii=False, indent=2)

    print("[*] Etapa 1: Página teste criada com status: 'pronta'.")
    res_build1 = subprocess.run([sys.executable, 'scripts/build.py'], capture_output=True, text=True, encoding='utf-8')
    assert res_build1.returncode == 0, f"Falha no build 1: {res_build1.stderr}"

    compiled_test_file = DIST_DIR / 'pagina-teste-a7.html'
    assert compiled_test_file.exists(), "Página de teste deveria ter sido gerada em dist/."
    print("  [+] Página gerada com sucesso em dist/pagina-teste-a7.html.")

    res_audit1 = subprocess.run([sys.executable, 'scripts/audit_all.py'], capture_output=True, text=True, encoding='utf-8')
    assert res_audit1.returncode == 0, f"Auditoria falhou na etapa 1: {res_audit1.stdout}"
    print("  [+] Auditoria audit_all.py passou com status OK na etapa 1.")

    # 2. Muda o status para 'rascunho'
    page_data["status"] = "rascunho"
    with open(test_page_file, 'w', encoding='utf-8') as f:
        json.dump(page_data, f, ensure_ascii=False, indent=2)

    print("\n[*] Etapa 2: Status alterado para: 'rascunho'.")

    # Limpa dist do arquivo anterior
    if compiled_test_file.exists():
        compiled_test_file.unlink()

    res_build2 = subprocess.run([sys.executable, 'scripts/build.py'], capture_output=True, text=True, encoding='utf-8')
    assert res_build2.returncode == 0, f"Falha no build 2: {res_build2.stderr}"

    # 3. Confere se a página NÃO aparece em dist/
    assert not compiled_test_file.exists(), "Página com status 'rascunho' NÃO deveria aparecer em dist/."
    print("  [+] Confirmado: dist/pagina-teste-a7.html NÃO existe em dist/.")

    # 4. Roda a auditoria novamente e confirma que passa
    res_audit2 = subprocess.run([sys.executable, 'scripts/audit_all.py'], capture_output=True, text=True, encoding='utf-8')
    assert res_audit2.returncode == 0, f"Auditoria falhou na etapa 2: {res_audit2.stdout}"
    print("  [+] Confirmado: audit_all.py passou com status OK após arquivamento da página.")

    # Remove o arquivo temporário de teste
    if test_page_file.exists():
        test_page_file.unlink()

    # Também removemos exemplo.json para deixar o repositório 100% limpo
    exemplo_file = PAGINAS_DIR / 'exemplo.json'
    if exemplo_file.exists():
        exemplo_file.unlink()

    exemplo_dist = DIST_DIR / 'teste-exemplo.html'
    if exemplo_dist.exists():
        exemplo_dist.unlink()

    # Re-executa build final para manter dist/ e sitemap sincronizados
    subprocess.run([sys.executable, 'scripts/build.py'], capture_output=True, text=True, encoding='utf-8')
    subprocess.run([sys.executable, 'scripts/audit_all.py'], capture_output=True, text=True, encoding='utf-8')

    print("\n==================================================")
    print("✅ BLOCO A7 APROVADO COM 100% DE SUCESSO!")
    print("==================================================")
    return True

if __name__ == '__main__':
    main()
