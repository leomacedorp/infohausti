#!/usr/bin/env python3
"""
VALIDADOR OFICIAL: scripts/valida_linhas.py
Valida o schema, campos obrigatórios e conformidade de content/dados-fonte/linhas.json (Bloco C0)
Regra de Schema: Todo dado segue o formato da Seção 4:
{ "valor": ..., "status": "verificado|pendente", "fonte_url": "...", "verificado_em": "..." }
"""

import sys
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
LINHAS_JSON_PATH = ROOT_DIR / 'content' / 'dados-fonte' / 'linhas.json'

CAMPOS_OBRIGATORIOS = [
    'numero',
    'nome',
    'itinerario',
    'paradas',
    'horarios',
    'bairros',
    'integracoes',
    'fonte'
]

def validar_campo_schema(campo_nome, campo_obj, linha_id):
    erros = []
    if not isinstance(campo_obj, dict):
        return [f"Linha {linha_id}: Campo '{campo_nome}' deve ser um objeto/dict."]
    
    for key in ['valor', 'status', 'fonte_url', 'verificado_em']:
        if key not in campo_obj:
            erros.append(f"Linha {linha_id}: Campo '{campo_nome}' não possui a propriedade '{key}'.")
            
    status = campo_obj.get('status')
    if status not in ('verificado', 'pendente'):
        erros.append(f"Linha {linha_id}: Campo '{campo_nome}' possui status inválido: '{status}'. Permitidos: 'verificado', 'pendente'.")
        
    if status == 'verificado':
        if campo_obj.get('valor') is None:
            erros.append(f"Linha {linha_id}: Campo '{campo_nome}' com status 'verificado' não pode ter valor nulo.")
        if not campo_obj.get('fonte_url'):
            erros.append(f"Linha {linha_id}: Campo '{campo_nome}' com status 'verificado' deve conter 'fonte_url'.")
            
    return erros

def validar_linhas():
    if not LINHAS_JSON_PATH.exists():
        print(f"[FATAL] Arquivo não encontrado: {LINHAS_JSON_PATH}")
        return False

    with open(LINHAS_JSON_PATH, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"[FATAL] Erro ao decodificar JSON: {e}")
            return False

    if not isinstance(data, (dict, list)):
        print(f"[FATAL] Formato raiz inválido em linhas.json (esperado dict ou list).")
        return False

    linhas_items = data.items() if isinstance(data, dict) else [(item.get('numero', {}).get('valor', idx), item) for idx, item in enumerate(data)]

    total_linhas = len(linhas_items)
    total_verificadas_completas = 0
    linhas_com_pendencia = []
    erros_schema = []

    for linha_id, linha in linhas_items:
        linha_erros = []
        linha_tem_pendencia = False
        
        # 1. Verifica campos obrigatórios
        for campo in CAMPOS_OBRIGATORIOS:
            if campo not in linha:
                linha_erros.append(f"Linha {linha_id}: Campo obrigatório ausente: '{campo}'.")
            else:
                campo_erros = validar_campo_schema(campo, linha[campo], linha_id)
                linha_erros.extend(campo_erros)
                if linha[campo].get('status') == 'pendente':
                    linha_tem_pendencia = True
                    
        if linha_erros:
            erros_schema.extend(linha_erros)
        elif linha_tem_pendencia:
            linhas_com_pendencia.append(linha_id)
        else:
            total_verificadas_completas += 1

    print("==================================================")
    print("      VALIDAÇÃO DE LINHAS (scripts/valida_linhas.py)     ")
    print("==================================================")
    print(f"Total de linhas analisadas: {total_linhas}")
    print(f"Linhas 100% verificadas:    {total_verificadas_completas}")
    print(f"Linhas com dados pendentes: {len(linhas_com_pendencia)}")
    if linhas_com_pendencia:
        print(f"  -> Linhas pendentes identificadas: {', '.join(linhas_com_pendencia)}")

    if erros_schema:
        print(f"\n[ERRO] Foram encontrados {len(erros_schema)} erro(s) de schema estrutural:")
        for err in erros_schema[:20]:
            print(f"  [X] {err}")
        if len(erros_schema) > 20:
            print(f"  ... e mais {len(erros_schema) - 20} erro(s).")
        return False
    else:
        print("\n[OK] Schema estrutural de todas as linhas está 100% válido e conforme a Seção 4!")
        return True

if __name__ == '__main__':
    sucesso = validar_linhas()
    sys.exit(0 if sucesso else 1)
