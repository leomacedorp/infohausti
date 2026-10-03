#!/usr/bin/env python3
"""
AUDITORIA: check_pendentes.py
Garante que nenhuma página com status 'pronta' publique dados com status 'pendente' (Regras 4 e 87)
"""

import sys
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / 'content'
PAGINAS_DIR = CONTENT_DIR / 'paginas'
STATUS_FILE = CONTENT_DIR / 'status.json'

def find_pending_fields(obj, current_path=""):
    """Varre recursivamente uma estrutura procurando por 'status': 'pendente'"""
    pendentes = []
    if isinstance(obj, dict):
        if obj.get('status') == 'pendente':
            pendentes.append(current_path or 'campo_raiz')
        for k, v in obj.items():
            sub_path = f"{current_path}.{k}" if current_path else k
            pendentes.extend(find_pending_fields(v, sub_path))
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            sub_path = f"{current_path}[{idx}]"
            pendentes.extend(find_pending_fields(item, sub_path))
    return pendentes

def check_pendentes():
    fatals = []
    avisos = []

    status_map = {}
    if STATUS_FILE.exists():
        try:
            with open(STATUS_FILE, 'r', encoding='utf-8') as f:
                status_map = json.load(f)
        except Exception:
            pass

    if not PAGINAS_DIR.exists():
        return [], ["[INFO] Nenhuma página JSON encontrada em content/paginas/."]

    for json_file in PAGINAS_DIR.glob('**/*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                page_data = json.load(f)
        except Exception as e:
            fatals.append(f"{json_file.name}: Erro ao ler JSON: {e}")
            continue

        slug = page_data.get('slug', '')
        st = page_data.get('status') or status_map.get(slug, 'rascunho')

        # Se página está marcada como pronta, não pode conter nenhum dado pendente!
        if st == 'pronta':
            pending_items = find_pending_fields(page_data)
            if pending_items:
                fatals.append(
                    f"{json_file.name}: Página marcada como 'pronta' contém {len(pending_items)} dado(s) pendente(s): {', '.join(pending_items)}"
                )

    return fatals, avisos

def main():
    fatals, avisos = check_pendentes()
    for a in avisos:
        print(f"[AVISO] {a}")
    for f in fatals:
        print(f"[FATAL] {f}")

    if fatals:
        print(f"\n[ERRO] check_pendentes falhou com {len(fatals)} erro(s) fatal(is).")
        sys.exit(1)
    else:
        print(f"[OK] check_pendentes aprovado.")
        sys.exit(0)

if __name__ == '__main__':
    main()
