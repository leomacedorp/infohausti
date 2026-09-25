# 🏛️ START HERE AI — Guia de Onboarding (Blueprint Soberano)
*Este arquivo é a porta de entrada única para qualquer IA que for trabalhar neste repositório.*

---

## 🛡️ Os Pilares Fundamentais deste Projeto

1. **PILAR 1 — PRODUTO & VOZ DO PROJETO:**
   * Toda linha de código existe para servir a uma proposta de valor real para pessoas reais.
   * Zero código morto e zero dependências desnecessárias (Filosofia Ponytail).
   * Proibido o "Substituto Plausível": proibição de dados mockados ou operações fakes em produção.

2. **PILAR 2 — ENGENHARIA DE SEGURANÇA & QUALITY GATE:**
   * Nenhuma entrega é aceita sem a validação do terminal:
     ```bash
     node scripts/gate.js
     ```
   * O Quality Gate verifica:
     1. Proibição de segredos hardcoded (`sk_live_`, `sk_test_`, senhas, tokens).
     2. Proteção de rotas API contra bots e requisições anônimas sem assinatura.
     3. TypeScript estrito sem nenhum erro (`tsc --noEmit`).
     4. Testes unitários automatizados.
     5. Registro da entrega atualizado em `STATUS.md`.

3. **PILAR 3 — O ESTADO VIVO:**
   * Consulte sempre o topo de [`STATUS.md`](STATUS.md) para saber o que acabou de ser feito e qual o próximo passo.

---

## ⚖️ Hierarquia de Confiança Absoluta
`Código Atual no Disco` ➔ `STATUS.md` ➔ `AGENTS.md` ➔ Documentação histórica.
