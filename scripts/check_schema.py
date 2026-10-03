#!/usr/bin/env python3
"""
AUDITORIA: check_schema.py
Valida sintaxe e integridade de microdados Schema.org JSON-LD em dist/
"""

import sys
import json
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / 'dist'

def check_schema():
    fatals = []
    avisos = []

    if not DIST_DIR.exists():
        return ["[FATAL] Diretório dist/ não existe."], []

    html_files = list(DIST_DIR.glob('**/*.html'))
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')
        rel_path = html_file.relative_to(ROOT_DIR)

        # Procura scripts JSON-LD
        blocks = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', content, re.DOTALL)
        if not blocks:
            fatals.append(f"{rel_path}: Bloco Schema.org JSON-LD ausente.")
            continue

        for block in blocks:
            raw_json = block.strip()
            if not raw_json:
                fatals.append(f"{rel_path}: Bloco JSON-LD vazio.")
                continue

            try:
                data = json.loads(raw_json)
            except json.JSONDecodeError as e:
                fatals.append(f"{rel_path}: JSON-LD com sintaxe inválida: {e}")
                continue

            # Valida @context
            if data.get('@context') != 'https://schema.org':
                fatals.append(f"{rel_path}: JSON-LD @context inválido: deve ser 'https://schema.org'.")

            # Valida entidades dentro de @graph ou objeto direto
            entities = data.get('@graph') if isinstance(data.get('@graph'), list) else [data]

            for entity in entities:
                ent_type = entity.get('@type')
                if not ent_type:
                    fatals.append(f"{rel_path}: Entidade sem @type no Schema.org.")
                    continue

                # Regra 31: FAQPage só entra com 3 ou mais perguntas reais
                if ent_type == 'FAQPage' or (isinstance(ent_type, list) and 'FAQPage' in ent_type):
                    main_entity = entity.get('mainEntity', [])
                    if not isinstance(main_entity, list) or len(main_entity) < 3:
                        fatals.append(f"{rel_path}: FAQPage contém apenas {len(main_entity)} pergunta(s). Mínimo exigido: 3.")

    return fatals, avisos

def main():
    fatals, avisos = check_schema()
    for a in avisos:
        print(f"[AVISO] {a}")
    for f in fatals:
        print(f"[FATAL] {f}")

    if fatals:
        print(f"\n[ERRO] check_schema falhou com {len(fatals)} erro(s) fatal(is).")
        sys.exit(1)
    else:
        print(f"[OK] check_schema aprovado.")
        sys.exit(0)

if __name__ == '__main__':
    main()
