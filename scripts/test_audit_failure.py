#!/usr/bin/env python3
"""
Testa se audit_all.py falha como FATAL diante de um link proibido href="#"
"""

import sys
import subprocess
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

html_path = Path('dist/teste-exemplo.html')
if not html_path.exists():
    print("[ERRO] dist/teste-exemplo.html não existe.")
    sys.exit(1)

original_content = html_path.read_text(encoding='utf-8')

try:
    # 1. Injeta o link proibido href="#"
    test_content = original_content.replace('<main id="conteudo-principal"', '<main id="conteudo-principal"><a href="#">Link Proibido Teste</a>')
    html_path.write_text(test_content, encoding='utf-8')

    print("[*] Executando audit_all.py sobre página com link '#'...")
    res = subprocess.run([sys.executable, 'scripts/audit_all.py'], capture_output=True, text=True, encoding='utf-8')

    print(f"[*] Código de saída: {res.returncode}")
    print(f"[*] Saída do audit_all.py:\n{res.stdout}")
    if res.stderr:
        print(f"[*] Erro do audit_all.py:\n{res.stderr}")

    if res.returncode != 0 and ("FATAL" in res.stdout or "FALHOU" in res.stdout):
        print("✅ [TESTE APROVADO] A auditoria detectou o link '#' e barrou como FATAL com código de saída != 0.")
    else:
        print("❌ [TESTE FALHOU] A auditoria não barrou o link '#'.")
        sys.exit(1)
finally:
    # Restaura arquivo
    html_path.write_text(original_content, encoding='utf-8')

print("✅ Todos os critérios do Bloco A5 foram rigorosamente comprovados!")
