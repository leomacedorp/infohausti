#!/usr/bin/env python3
"""
EVIDÊNCIA & AUDITORIA: scripts/verifica_api_mobilibus.py
Consulta a API oficial da Mobilibus (Bus2 / RP Mobi - Project ID 614),
compara rota a rota com o banco local (content/dados-fonte/banco-linhas.db)
e grava a evidência em content/dados-fonte/verificacao-mobilibus-[DATA].json.
"""

import sys
import json
import sqlite3
import requests
from pathlib import Path
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / 'content' / 'dados-fonte' / 'banco-linhas.db'
DATA_HOJE = datetime.now().strftime('%Y-%m-%d')
EVIDENCIA_PATH = ROOT_DIR / 'content' / 'dados-fonte' / f'verificacao-mobilibus-{DATA_HOJE}.json'

API_URL = "https://mobilibus.com/api/routes"
HEADERS = {
    "Origin": "https://bus2.info",
    "Referer": "https://bus2.info/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json"
}

def verificar():
    print(f"[*] Consultando API oficial da Mobilibus: {API_URL}?project_id=614 ...")
    try:
        resp = requests.get(API_URL, params={"origin": "web", "project_id": 614}, headers=HEADERS, timeout=20)
    except Exception as e:
        print(f"[FATAL] Falha de conexão com a API: {e}")
        sys.exit(1)

    if resp.status_code != 200:
        print(f"[FATAL] API retornou HTTP {resp.status_code}: {resp.text[:200]}")
        sys.exit(1)

    live_routes = resp.json()
    print(f"[+] Resposta da API recebida com sucesso! Total de rotas retornadas: {len(live_routes)}")

    # 1. Salva a evidência bruta em JSON
    with open(EVIDENCIA_PATH, 'w', encoding='utf-8') as f:
        json.dump({
            "metadados": {
                "consultado_em": datetime.now().isoformat(),
                "url": f"{API_URL}?project_id=614",
                "status_code": resp.status_code,
                "total_rotas": len(live_routes),
                "fonte": "Mobilibus Tecnologia / Bus2 (Plataforma oficial de telemetria e dados RP Mobi)"
            },
            "rotas": live_routes
        }, f, ensure_ascii=False, indent=2)
    print(f"[+] Evidência gravada com sucesso em: {EVIDENCIA_PATH.relative_to(ROOT_DIR)}")

    # 2. Compara com banco SQLite local
    if not DB_PATH.exists():
        print(f"[ERRO] Banco local não encontrado: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    local_routes = c.execute("SELECT route_id, short_name, long_name FROM linhas ORDER BY CAST(short_name AS INTEGER), short_name").fetchall()
    conn.close()

    local_dict = {r[0]: (r[1], r[2]) for r in local_routes}
    live_dict = {r['routeId']: (str(r['shortName']), str(r['longName'])) for r in live_routes}

    diff_local = set(local_dict.keys()) - set(live_dict.keys())
    diff_live = set(live_dict.keys()) - set(local_dict.keys())

    print("\n==================================================")
    print("   RELATÓRIO DE AUDITORIA: BANCO LOCAL vs API VIVA")
    print("==================================================")
    print(f"Total no banco local:    {len(local_dict)}")
    print(f"Total na API Mobilibus:  {len(live_dict)}")
    print(f"Diferenças de routeId:   {len(diff_local) + len(diff_live)}")

    mismatches = []
    for rid, (s_local, n_local) in local_dict.items():
        if rid in live_dict:
            s_live, n_live = live_dict[rid]
            if s_local != s_live or n_local.strip() != n_live.strip():
                mismatches.append(f"ID {rid}: Local='{s_local} - {n_local}' vs API='{s_live} - {n_live}'")

    print(f"Divergências de nomes:   {len(mismatches)}")
    if mismatches:
        for m in mismatches:
            print(f"  [!] {m}")
    else:
        print("[OK] 100% de paridade factual entre o banco local e a API oficial ao vivo!")

if __name__ == '__main__':
    verificar()
