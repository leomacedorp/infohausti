# 🛡️ Relatório de Procedência e Verificação de Dados — Malha RP Mobi

*Documento técnico de auditoria factual para o projeto Infohausti Ribeirão Preto.*  
*Data de emissão: 03/10/2026*

---

## 1. Procedência e Data Exata de Extração do Banco (`bus_info.db`)

* **Data e Hora Exata da Extração Bruta:** **27 de agosto de 2026 às 11:54:09 (BRT)** (`dados_onibus_completo.json`).
* **Data e Hora Exata da Compilação SQLite:** **27 de agosto de 2026 às 12:00:29 (BRT)** (`bus_info.db`).
* **Origem Física:** Arquivos gerados a partir do scraper batch na infraestrutura de telemetria operacional de Ribeirão Preto.

---

## 2. Natureza da Fonte: Mobilibus Tecnologia (Bus2 / RP Mobi)

* **Classificação:** **Fonte Primária Operacional Homologada** (Não é agregador terceiro não oficial).
* **Entidade Responsável:** A *Mobilibus Tecnologia Ltda* é a fornecedora e desenvolvedora da plataforma tecnológica de despacho, monitoramento de frota por GPS e bilhetagem do transporte coletivo contratada pela concessionária do transporte municipal de Ribeirão Preto (Consórcio PróUrbano) e supervisionada pela **RP Mobi** (Empresa de Mobilidade Urbana de Ribeirão Preto S.A.).
* **Código de Projeto Oficial:** `project_id: 614` (identificador exclusivo do município de Ribeirão Preto na rede Mobilibus).
* **Aplicações que Utilizam a Mesma API:** O site da RP Mobi, o aplicativo oficial para passageiros (*Bus2*) e o sistema de telemetria em tempo real das garagens consomem diretamente essa mesma base de dados.
* **Tempo de Propagação:** Mudanças de itinerário ou criação/extinção de linhas decretadas pela Prefeitura são cadastradas na base operacional da Mobilibus antes ou no próprio dia da entrada em vigor da escala.

---

## 3. Auditoria de Paridade em Tempo Real (03/10/2026)

Em **03/10/2026 às 15:48:53**, foi executada consulta ao vivo contra a API de produção:
* **URL:** `https://mobilibus.com/api/routes?project_id=614`
* **Script de Auditoria:** `scripts/verifica_api_mobilibus.py`
* **Arquivo de Evidência Bruta:** `content/dados-fonte/verificacao-mobilibus-2026-10-03.json`

### Resultado da Checagem Comparativa:
| Métrica | Banco Local (`bus_info.db`) | API Mobilibus (Ao Vivo) | Status |
|---|---|---|---|
| Total de Rotas Cadastradas | 113 | 113 | ✅ Idêntico (100%) |
| Divergência de `routeId` | 0 | 0 | ✅ Idêntico (100%) |
| Divergência de Nomes Oficiais | 0 | 0 | ✅ Idêntico (100%) |

### Situação das Linhas Históricas e Reformuladas:
1. **045 – Vila do Golfe (ID 988632):** Já cadastrada com o novo nome oficial (antiga Vila do Ipê).
2. **055 – San Marco (ID 576903):** Já cadastrada com o novo nome oficial (antiga Royal Park).
3. **105 – Sul Inter Shopping (ID 1008678):** Já cadastrada com o novo nome oficial.
4. **256 – Parque / Shopping Iguatemi (ID 1008677):** Já presente no banco e ativa na API.
5. **043 – Portal dos Ipês, 063 – Pq. das Gaivotas e 073 – Reserva Real:** Todas presentes e ativas.
6. **Linhas 19, 33, 501 e D 402/D 420:** **Totalmente ausentes** do banco e da API (já haviam sido descontinuadas antes da extração de agosto/2026).
7. **Linha 407 – Jd. Paulo Gomes (ID 576911):** Ativa na cidade com grade horária oficial, porém mantida com status `pendente` no projeto até que a concessionária disponibilize as coordenadas geográficas de traçado em seu endpoint.

---

## 4. Política de Atualização Cadastral

* **Frequência de Revisão do Catálogo:** Trimestral (ou sob demanda caso a RP Mobi publique decreto de novas alterações viárias no Diário Oficial do Município).
* **Validação Pré-Deploy:** Qualquer alteração no arquivo `content/dados-fonte/linhas.json` exige a aprovação do script `scripts/valida_linhas.py` e conferência com `scripts/verifica_api_mobilibus.py`.
