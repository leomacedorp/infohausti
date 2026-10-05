# Ângulos Editoriais — Templates de Narração por Modalidade
*Documento de referência do gerador novo (Etapa 3). Aprovado na essência pelo Leo (Guardrail 1, Ajuste 1).*

O gerador escolhe o ângulo pela **modalidade da linha** em `dados-fonte/linhas.json` — nunca por heurística livre. Cada ângulo define voz, público, ênfase e proibições. Todo texto passa pelo `check_fontes_factuais.py` antes de gravar.

---

## 1. Radial-Paradora (linhas convencionais: bairro ↔ Centro)

- **Modalidade-alvo:** `Convencional` com itinerário "Até Centro" + "Até Bairro" (ida e volta distintas) e grade diária extensa (primeira partida ≤05:30, última ≥22:00).
- **Público:** morador do bairro no cotidiano — trabalho, mercado, escola, posto de saúde, repartições.
- **Voz:**companheira e prática. Segunda pessoa implícita ("desça na parada...", "embarque na R. X"). Frases médias, vocabulário direto.
- **Ênfase:** o bairro em si (de ONDE o usuário sai), os pontos de conexão no Centro, a grade completa (a linha como relógio do dia: madrugada → noite), e a cobertura porta a porta.
- **Estrutura:** (1) visão geral — a linha como cotidiano do bairro; (2) itinerário — narrado por ordem real das paradas de dados-fonte; (3) paradas destaque — 2-3 paradas reais com âncora geográfica da própria linha; (4) integração — tarifa R$ 5,00 + 120 min + onde baldear; (5) bairros — lista real de dados-fonte; (6) atrações — só as que têm parada da própria linha ou ≤500m com fonte.
- **Evita:** termos técnicos operacionais (telemetria, "jornada pendular"), linguagem fabril em bairro residencial, superlativos, e qualquer via/instituição que não esteja nas paradas da própria linha.

## 2. Expresso-Semidireto (expressos, semidiretos, linhas de hora marcada)

- **Modalidade-alvo:** nome contendo "Expresso" ou grade curta concentrada em poucos horários fixos (ex.: 311 com 3 partidas).
- **Público:** quem precisa programar o dia em torno do horário fixo — volta do trabalho/estudo ao bairro.
- **Voz:** objetiva e operacional, como um quadro de horários bem explicado. Terceira pessoa, frases curtas e densas em fato.
- **Ênfase:** a grade enxuta (horários exatos, dias SEM serviço), o itinerário único e direto (nº de paradas), o que a linha NÃO faz (não circula dentro de todos os bairros), e o embarque de retorno (de onde partir).
- **Estrutura:** (1) visão geral — o desenho operacional (nº de partidas, janela de horários, silêncio aos fins de semana); (2) itinerário — eixo principal com vias reais; (3) paradas destaque — o ponto de origem e o ponto final com coordenada; (4) integração — mesmo padrão; (5) bairros — os reais; (6) atrações — mínimas, só as na rota.
- **Evita:** inventar velocidade ("alta velocidade"), ganhos de tempo numéricos sem fonte, "faixa exclusiva" sem parada correspondente, e menções a bairros que a linha não toca.

## 3. Circular (linha circular horário/anti-horário)

- **Modalidade-alvo:** nome contendo "Circular" (199, 299, 399, 499).
- **Público:** quem precisa cruzar a cidade sem passar pelo Terminal Central, e quem faz vão-e-volta no mesmo eixo.
- **Voz:** narrativa de itinerário — descreve o LAÇO, o que se repete e o que distingue cada sentido.
- **Ênfase:** o sentido como ESCOLHA DO PASSAGEIRO (pegar 199 vs 299 pelo lado da cidade onde está), os pontos de partida em comum, e as conexões ao longo do anel.
- **Estrutura:** (1) visão geral — a função do laço no sistema; (2) itinerário — narrado por sentido, com vias reais; (3) paradas destaque — paradas compartilhadas e paradas exclusivas de cada sentido; (4) integração — padrão; (5) bairros; (6) atrações — só as com parada na rota.
- **Evita:** repetir a mesma frase entre os dois sentidos, espelhar a página irmã (similaridade 199×299 ≤40%: família, ângulo distinto obrigatório), e descrever o laço com vias genéricas do centro.

---

## Regra Transversal — Parada vs. Referência Próxima (Ajuste 2)

- **Parada (na whitelist da linha):** "desça **na parada** [nome GTFS]" — linguagem de embarque/desembarque.
- **Referência próxima (≤500m, com fonte em dados-fonte/, mas SEM parada da linha):** "a [X] metros **fica o/a** [instituição]" — linguagem de proximidade. NUNCA "desça no/no Terminal [nome]" para referência.
- Instituição sem fonte em dados-fonte/ e sem parada → não entra, sem exceção.

## Regra Transversal — Fonte de Todo Dado

- Vias/bairros/paradas/horários: só de `dados-fonte/linhas.json` da própria linha.
- Instituições: só de `dados-fonte/pontos/`, `dados-fonte/unidades-saude.json`, ou parada GTFS.
- Tarifa R$ 5,00 / 120 min / nº de linhas 113: whitelist fixa (documentada em rp-perfil.json).
- Nenhum outro número entra sem campo `fonte_url` no JSON de fonte.
