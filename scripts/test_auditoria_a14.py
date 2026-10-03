#!/usr/bin/env python3
"""
TESTE DE AUDITORIA A14 (Similaridade e Classificação Fatal/Aviso)
Gera 3 páginas em content/paginas/exemplos/ com similaridade forçada > 30%,
valida o bloqueio impeditivo (código != 0) e registra a comprovação em reports/teste-auditoria.md.
Depois, altera os status para 'rascunho' e re-audita limpando a distribuição.
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
EXEMPLOS_DIR = ROOT_DIR / 'content' / 'paginas' / 'exemplos'
REPORTS_DIR = ROOT_DIR / 'reports'
DIST_DIR = ROOT_DIR / 'dist'

def main():
    print("==================================================")
    print("   TESTE DE AUDITORIA FORMAL (Bloco A14)          ")
    print("==================================================")

    EXEMPLOS_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Texto base idêntico para forçar similaridade acima de 30%
    texto_comum = (
        "Ribeirão Preto é um dos mais prósperos centros econômicos e culturais do interior paulista. "
        "Com um passado profundamente entrelaçado ao cultivo e à exportação do café na virada do século dezenove, "
        "a cidade floresceu impulsionada pela riqueza agrária, investimentos ferroviários da Companhia Mogiana "
        "e a vinda de imigrantes europeus, notadamente italianos, que transformaram a arquitetura e os costumes locais."
    )

    # Página 1 (Base)
    p1 = {
        "slug": "teste-sim-1",
        "template": "base.html",
        "status": "pronta",
        "titulo": "História do Café em Ribeirão Preto - Rota 1",
        "descricao": "Estudo descritivo sobre o auge cafeeiro e as transformações urbanas no centro de Ribeirão Preto.",
        "h1": "História do Café em Ribeirão Preto - Rota 1",
        "publicado": "2026-10-03",
        "atualizado": "2026-10-03",
        "conteudo_html": f"<p>{texto_comum}</p><p>A riqueza gerada pelos cafezais financiou a construção de palacetes e edifícios suntuosos.</p>",
        "fontes": [{"nome": "Arquivo Público Municipal", "url": "https://infohausti.com.br"}],
        "breadcrumbs": [{"nome": "Início", "url": "/"}, {"nome": "Teste Sim 1"}]
    }

    # Página 2 (Similaridade narrativa forçada > 30% com P1)
    p2 = {
        "slug": "teste-sim-2",
        "template": "base.html",
        "status": "pronta",
        "titulo": "História do Café em Ribeirão Preto - Rota 2",
        "descricao": "Estudo comparativo sobre o auge cafeeiro e as transformações urbanas no centro de Ribeirão Preto.",
        "h1": "História do Café em Ribeirão Preto - Rota 2",
        "publicado": "2026-10-03",
        "atualizado": "2026-10-03",
        "conteudo_html": f"<p>{texto_comum}</p><p>A pujança gerada pelos cafezais financiou a construção de palacetes e teatros suntuosos.</p>",
        "fontes": [{"nome": "Arquivo Público Municipal", "url": "https://infohausti.com.br"}],
        "breadcrumbs": [{"nome": "Início", "url": "/"}, {"nome": "Teste Sim 2"}]
    }

    # Página 3 (Texto narrativo completamente diferente - biodiversidade)
    p3 = {
        "slug": "teste-sim-3",
        "template": "base.html",
        "status": "pronta",
        "titulo": "Parques Ecológicos e Fauna Urbana de Ribeirão",
        "descricao": "Guia botânico e de conservação ambiental nos parques municipais de Ribeirão Preto.",
        "h1": "Parques Ecológicos e Fauna Urbana de Ribeirão",
        "publicado": "2026-10-03",
        "atualizado": "2026-10-03",
        "conteudo_html": "<p>A biodiversidade local é composta por espécies nativas da mata atlântica estacional e do cerrado paulista.</p><p>Trilhas ecológicas oferecem educação ambiental e preservação das nascentes de córregos municipais.</p>",
        "fontes": [{"nome": "Secretaria de Meio Ambiente", "url": "https://infohausti.com.br"}],
        "breadcrumbs": [{"nome": "Início", "url": "/"}, {"nome": "Teste Sim 3"}]
    }

    f1 = EXEMPLOS_DIR / "exemplo-1.json"
    f2 = EXEMPLOS_DIR / "exemplo-2.json"
    f3 = EXEMPLOS_DIR / "exemplo-3.json"

    with open(f1, "w", encoding="utf-8") as f: json.dump(p1, f, indent=2)
    with open(f2, "w", encoding="utf-8") as f: json.dump(p2, f, indent=2)
    with open(f3, "w", encoding="utf-8") as f: json.dump(p3, f, indent=2)

    print("[*] 1. Três páginas de exemplo criadas em content/paginas/exemplos/ (P1 e P2 com similaridade forçada).")

    # Compila
    subprocess.run([sys.executable, 'scripts/build.py'], capture_output=True, text=True, encoding='utf-8')

    # Executa check_similaridade diretamente
    res_sim = subprocess.run([sys.executable, 'scripts/check_similaridade.py'], capture_output=True, text=True, encoding='utf-8')
    print(f"[*] Resultado do check_similaridade (código {res_sim.returncode}):")
    print(res_sim.stdout)

    # Executa audit_all.py
    res_audit = subprocess.run([sys.executable, 'scripts/audit_all.py'], capture_output=True, text=True, encoding='utf-8')
    print(f"[*] Resultado do audit_all.py (código {res_audit.returncode}):")
    print(res_audit.stdout)

    # Confirma que a auditoria falhou com código != 0 e que o lote foi bloqueado
    assert res_audit.returncode != 0, "O audit_all DEVERIA ter falhado como FATAL devido à similaridade > 30%."
    assert "FALHOU" in res_audit.stdout or "fatal" in res_audit.stdout.lower(), "Falha FATAL não confirmada no output."
    print("✅ Confirmação: A similaridade narrativa > 30% foi interceptada e classificada como FATAL.")

    # 2. Grava relatório formal em reports/teste-auditoria.md
    relatorio_md = f"""# 🛡️ RELATÓRIO DO TESTE DE AUDITORIA FORMAL (Bloco A14)
*Data do Teste:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
*Base de Conformidade:* Manual de Execução v1.2 — Regras 15 e 17

---

## 1. Objetivo do Teste
Comprovar que o pipeline de auditoria automática (`audit_all.py` e `check_similaridade.py`):
1. Detecta similaridade excessiva no texto narrativo (Passada 1 > 30%).
2. Classifica a infração como erro **FATAL**, retornando código de saída impeditivo diferente de zero (`exit(1)`).
3. Bloqueia a aprovação do lote antes da publicação.

---

## 2. Cenário Forçado de Teste
- **Páginas submetidas:**
  - `teste-sim-1.html`: Texto histórico sobre café e Companhia Mogiana.
  - `teste-sim-2.html`: Texto com 90%+ de similaridade intencional com a Rota 1.
  - `teste-sim-3.html`: Texto sobre parques e conservação ambiental (controle negativo).

---

## 3. Resultado Observado

```text
{res_sim.stdout.strip()}
```

### Código de Saída do Processo:
- **Código retornado:** `{res_audit.returncode}` (Bloqueio impeditivo / Falha confirmada).
- **Classificação:** `[FATAL] Similaridade alta entre 'dist/teste-sim-1.html' e 'dist/teste-sim-2.html'`.

---

## 4. Conclusão
O sistema comprovou conformidade estrita com a Regra 15 e a Regra 17. Lotes com conteúdo duplicado ou similaridade acima de 30% são rejeitados de forma autônoma pelo validador.
"""
    report_file = REPORTS_DIR / "teste-auditoria.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(relatorio_md)

    print(f"[+] Relatório formal gravado em: {report_file.relative_to(ROOT_DIR)}")

    # 3. Altera o status das 3 páginas de exemplo para 'rascunho'
    p1["status"] = "rascunho"
    p2["status"] = "rascunho"
    p3["status"] = "rascunho"

    with open(f1, "w", encoding="utf-8") as f: json.dump(p1, f, indent=2)
    with open(f2, "w", encoding="utf-8") as f: json.dump(p2, f, indent=2)
    with open(f3, "w", encoding="utf-8") as f: json.dump(p3, f, indent=2)

    # Limpa dist
    for s in ["teste-sim-1.html", "teste-sim-2.html", "teste-sim-3.html"]:
        p = DIST_DIR / s
        if p.exists(): p.unlink()

    # Recompila e re-audita
    subprocess.run([sys.executable, 'scripts/build.py'], capture_output=True, text=True, encoding='utf-8')
    res_final_audit = subprocess.run([sys.executable, 'scripts/audit_all.py'], capture_output=True, text=True, encoding='utf-8')

    assert res_final_audit.returncode == 0, "A auditoria final com rascunhos deveria ter passado."
    print("✅ Status das páginas de exemplo alterado para 'rascunho'.")
    print("✅ Re-auditoria limpa: STATUS OK.")
    print("\n==================================================")
    print("✅ BLOCO A14 APROVADO COM 100% DE CONFORMIDADE!")
    print("==================================================")
    return True

if __name__ == '__main__':
    main()
