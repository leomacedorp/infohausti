# BRIEF HERMES — Reescrita editorial dos 14 pares fatais (Camada 1)

Você é o EXECUTOR. O Antigravity é o arquiteto/validador. Diretório de trabalho:
`C:\Users\lamacedo\Documents\Antigravity\Infohausti`

## Objetivo
Zerar os 14 pares FATAIS da Camada 1 (similaridade editorial mascarada > 30%) do
`scripts/check_similaridade.py`. Meta: todos os pares < 25% (idealmente), obrigatoriamente < 30%.

## Arquivos (content/paginas/linhas/)
Pares fatais e ângulo editorial obrigatório de cada página:

| Par | Ângulo da 1ª | Ângulo da 2ª |
|---|---|---|
| 045 x 256 | 045: condomínios fechados/vilas residenciais | 256: trabalhadores do shopping/varejo |
| 136 x 236 | 136: polo industrial Castelo Branco | 236: travessia diametral da cidade |
| 301 x 311 | 301: comércio de bairro e idosos | 311: telemetria, velocidade, horários de pico |
| 199 x 299 | 199: sentido horário (clínicas/escritórios Zona Sul) | 299: sentido anti-horário (Ipiranga → Campos Elíseos) |
| 210 x 211 | 210: paradas locais, capilaridade de bairro | 211: expresso, deslocamento pendular |
| 201 x 310 | 201: corredor industrial Whately | 310: conexão interbairros Quintino–Avelino |
| 110 x 201 | 110: núcleo residencial histórico | 201: operários fabris e turnos |
| 211 x 311 | 211: pendular casa-trabalho | 311: telemetria/pico (corredor distinto) |
| 130 x 203 | 130: polo forense e judiciário | 203: campus Unaerp e Hospital Santa Lydia |
| 101 x 301 | 101: polo industrial e logística | 301: áreas residenciais e escolas municipais |
| 178 x 217 | 178: rota curta local do Dom Mielle | 217: macro-anel transversal (135 paradas) |
| 101 x 311 | 101: tráfego industrial pesado | 311: trânsito expresso de passageiros |
| 201 x 217 | 201: rota fabril | 217: rota macro-transversal hospitalar |
| 007 x 207 | 007: madrugada, ruas calmas, plantonistas | 207: rotina diurna universitária/acadêmica |

## O que PODE editar (somente texto editorial)
- `descricao` (NÃO começar com "Guia de horários da Linha..." — cada uma deve ter abertura própria)
- `titulo`, `keywords`
- `secoes.*` (visao_geral, itinerario_texto, paradas_destaque, integracao_detalhe, bairros_texto, atracoes_proximas)
- `itinerarios_detalhe[].descricao`, `paradas_principais[].referencia`
- `faq[].pergunta` / `faq[].resposta` (variar a formulação; manter fatos: tarifa R$ 5,00, 120 min de integração)

## PROIBIDO (regras duras)
1. NÃO inventar nomes, sinônimos ou apelidos de lugares. Proibido: "bairro ferroviário ocidental",
   "Alameda da Mogiana", "complexo ambulatorial", "condução" e similares. Use SEMPRE nomes oficiais reais
   que já estão no JSON (bairros, ruas, números de ponto, instituições).
2. NÃO alterar: slug, numero, nome, cor, tarifa, horarios_tabela, bairros_lista, num_paradas,
   nomes/ruas/bairros de paradas_principais, fontes, datas, revisor.
3. NÃO inventar fatos (horários, quantidades, equipamentos inexistentes). Só reorganize/reenquadre o que existe.
4. Evitar frases-molde repetidas entre páginas: "da RP Mobi em", "Guia de horários da", "cumpre uma das funções",
   "Com tarifa acessível fixada em", "O itinerário serve bairros de". Varie estrutura de parágrafo e ordem das seções narrativas.
5. Manter HTML válido (`<p>`, `<strong>`, `<em>`) e JSON válido UTF-8. Manter tamanho semelhante (não encurtar a página).

## Ciclo de trabalho (repita até verde)
```
python scripts/build.py
python scripts/check_similaridade.py
```
Leia os "Par fatal" restantes, reescreva, rode de novo. Quando zerar os fatais, rode:
```
python scripts/audit_all.py
```

## Entrega
Ao final, escreva `reports/hermes-14-pares-resultado.md` com: arquivos alterados, % Camada 1 antes/depois
de cada par, resultado do audit_all (STATUS) e qualquer dúvida. NÃO faça git commit (o arquiteto valida e comita).

---

## ⚠️ CORREÇÃO DO ARQUITETO (após rodada 1 — LEIA ANTES DE TUDO)

A rodada 1 PIOROU a métrica: de 14 para **20 pares fatais** (ex.: 211 x 311 subiu para 45,8%).
Causa: os textos de `secoes` foram ENCURTADOS ~30% (ex.: 007 de 3309 → 2170 caracteres). Com menos texto
próprio, o template fixo do `build.py` passa a dominar a página e a similaridade SOBE.
Além disso, foi criado um molde novo repetido em várias páginas: `<strong>Rótulo:</strong> <p>frase curta</p>`
(HTML inválido e idêntico entre páginas).

Regras adicionais OBRIGATÓRIAS:
1. **Soma de caracteres de `secoes` de cada página ≥ 3000** (mais texto próprio = menos similaridade). Nunca encurtar.
2. Cada seção com **2 a 3 parágrafos `<p>` completos**, prosa corrida, sem o molde `<strong>Rótulo:</strong>`.
   `<strong>` só DENTRO de `<p>`.
3. Cada página deve ter vocabulário e estrutura de frase PRÓPRIOS do seu ângulo. Não reutilize a mesma frase de
   abertura/fechamento em duas páginas. Escreva cada página como se fosse outro jornalista.
4. A meta é **0 pares fatais NO TOTAL** do relatório (incluindo pares novos como 156 x 256, 203 x 207, 211 x 310,
   101 x 310, 217 x 310, 301 x 310). Se precisar, reescreva também a 156.
5. Trabalhe UMA página por vez: reescreve → build → check → próxima. Leia sempre a saída completa de "Par fatal".
6. Os arquivos atuais (versão encurtada da rodada 1) estão backupeados em `reports/backup_hermes_v1_1908/`.
   Para referência factual de nomes reais use `git show HEAD:content/paginas/linhas/<arquivo>.json` (quando existir).

