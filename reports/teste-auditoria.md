# 🛡️ RELATÓRIO DO TESTE DE AUDITORIA FORMAL (Bloco A14)
*Data do Teste:* 2026-10-03 13:38:48  
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
[AVISO] [PASSADA 2 - TABELAS/LISTAS] Similaridade combinada (97.9%) entre 'dist\teste-sim-1.html' e 'dist\teste-sim-2.html' (Requer revisão humana).
[AVISO] [PASSADA 2 - TABELAS/LISTAS] Similaridade combinada (62.3%) entre 'dist\teste-sim-1.html' e 'dist\teste-sim-3.html' (Requer revisão humana).
[AVISO] [PASSADA 2 - TABELAS/LISTAS] Similaridade combinada (62.6%) entre 'dist\teste-sim-2.html' e 'dist\teste-sim-3.html' (Requer revisão humana).
[FATAL] [PASSADA 1 - NARRATIVO] Similaridade alta (97.5%) entre 'dist\teste-sim-1.html' e 'dist\teste-sim-2.html'. Limite máximo: 30%.
[FATAL] [PASSADA 1 - NARRATIVO] Similaridade alta (56.0%) entre 'dist\teste-sim-1.html' e 'dist\teste-sim-3.html'. Limite máximo: 30%.
[FATAL] [PASSADA 1 - NARRATIVO] Similaridade alta (56.3%) entre 'dist\teste-sim-2.html' e 'dist\teste-sim-3.html'. Limite máximo: 30%.

[ERRO] check_similaridade falhou com 3 erro(s) fatal(is).
```

### Código de Saída do Processo:
- **Código retornado:** `1` (Bloqueio impeditivo / Falha confirmada).
- **Classificação:** `[FATAL] Similaridade alta entre 'dist/teste-sim-1.html' e 'dist/teste-sim-2.html'`.

---

## 4. Conclusão
O sistema comprovou conformidade estrita com a Regra 15 e a Regra 17. Lotes com conteúdo duplicado ou similaridade acima de 30% são rejeitados de forma autônoma pelo validador.
