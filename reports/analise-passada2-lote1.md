# 📊 Relatório Técnico de Similaridade: Análise da Passada 2 no Lote 1

*Documento de governança e auditoria metodológica — Infohausti Ribeirão Preto.*  
*Data de emissão: 03/10/2026*  
*Autor: Leonardo A. Macedo / Antigravity Execution Agent*

---

## 1. Contexto e Motivo do Índice de 57,0% entre Linha 023 e Linha 902

Na auditoria do Lote 1 (Bloco C4 — Fase 1), o script `check_similaridade.py` identificou um aviso de **57,0% de similaridade na Passada 2** entre as páginas:
* `dist/linhas/linha-023-aeroporto.html` (Linha Alimentadora Aeroporto via Pq. Industrial)
* `dist/linhas/linha-902-norte-sul-2.html` (Linha Troncal BRT Norte-Sul 2)

### Causa Raiz do Overlap Factual (Passada 2):
A **Passada 2** afere a similaridade global de todo o documento HTML renderizado dentro da tag `<main>`, incluindo tabelas de horários, listas de paradas de transbordo, cartões operacionais e dados estruturados.

O índice de 57,0% deve-se a três fatores factuais do sistema de transporte da RP Mobi:
1. **Compartilhamento Geográfico do Eixo Avenida Brasil (Zona Norte):** Ambas as rotas operam e realizam baldeação intensiva ao longo da Avenida Brasil (altura do número 1105 / Jardim Salgado Filho). As tabelas e listas de paradas contêm os mesmos logradouros, bairros e identificadores de estações de conexão.
2. **Integração Operacional Direta:** A Linha 023 foi expressamente concebida para atuar como *alimentadora* do corredor troncal da Linha 902. Por esse motivo, as orientações de integração tarifária de 120 minutos citam mutualmente o corredor BRT Norte-Sul como destino principal de transbordo.
3. **Estrutura de Frequência:** Ambas as linhas possuem alta cadência de partidas diárias (mais de 60 partidas por sentido), resultando em grades horárias extensas com intervalos a cada 10 a 20 minutos que compartilham dezenas de horários idênticos (ex: 05:20, 05:50, 06:10, 06:20...).

> **Importante:** Na **Passada 1 (texto narrativo estrito)**, a similaridade entre Linha 023 e Linha 902 foi de apenas **15,2%**, confirmando que a redação editorial é 100% original e não duplica texto discursivo.

---

## 2. Trechos Narrativos que Diferenciam as Duas Páginas

Apesar da sobreposição de paradas físicas no eixo viário, a abordagem editorial das duas páginas foca em universos funcionais completamente distintos:

### A. Vocação Econômica e Perfil de Passageiros
* **Linha 023 (Alimentadora Industrial / Aeroportuária):**
  > *"A Linha 023 (Aeroporto via Parque Industrial) desempenha uma função logística de alta produtividade para o ecossistema econômico e aeroportuário de Ribeirão Preto. Atuando como linha alimentadora na Zona Norte, este itinerário une os bairros residenciais da Vila Mariana e Jardim Salgado Filho ao polo fabril do Parque Industrial Coronel Quito Junqueira e ao saguão de embarque de passageiros do Aeroporto Estadual Doutor Leite Lopes (RAO)... garantindo transporte ágil para metalúrgicos, operários da cadeia logística, comissários de bordo e viajantes."*
* **Linha 902 (Troncal BRT Estruturante Metropolitano):**
  > *"A Linha 902 (Norte-Sul 2) constitui a principal espinha dorsal de transporte de alta capacidade do município de Ribeirão Preto... operando veículos padron com ar-condicionado em canaletas exclusivas e faixas preferenciais. Conecta os bairros setentrionais ao quadrilátero histórico central e aos grandes centros de compras da Zona Sul (RibeirãoShopping)."*

### B. Descrição do Trajeto e Pontos de Interesse
* **Linha 023:** Detalha a circulação pelas ruas internas da Vila Mariana (Rua Peru), os galpões de manufatura, hangares de aviação executiva e o Aeroclube de Ribeirão Preto.
* **Linha 902:** Detalha as estações tubulares elevadas de embarque em nível (Estação Catedral, Estação Independência, Estação Nove de Julho), a travessia de avenidas de grande fluxo e os polos corporativos e hospitalares da Zona Sul.

---

## 3. Recomendações e Diretrizes para Futuros Pares com Alto Overlap Factual

Para os próximos lotes (Lotes 2 a 12), quando duas linhas compartilharem o mesmo corredor viário (ex: linhas troncais que dividem faixas ou alimentadoras que servem ao mesmo terminal de transbordo), a equipe de execução adotará os seguintes critérios:

1. **Margem de Segurança na Passada 1 (Limite Interno < 28%):** O limite fatal da Regra 17 é 30%. Estabelece-se como protocolo interno que nenhum lote será aceito com índice narrativo superior a 28,0%.
2. **Diversificação de Ângulos Editoriais:** Se duas linhas compartilham paradas, cada uma deve ter seu texto ancorado no seu papel funcional específico:
   - Uma linha voltada para operários industriais foca em fábricas, turnos e logística;
   - Uma linha voltada para estudantes universitários foca em bibliotecas, salas de aula e horários acadêmicos;
   - Uma linha troncal foca na velocidade dos corredores expressos e estações tubulares.
3. **Monitoramento Documentado da Passada 2:** Avisos acima de 30% na Passada 2 são esperados em sistemas com integração física de transporte, mas devem ser formalmente mapeados em relatório a cada lote para garantir que o crescimento decorra de paradas físicas e tabelas, e nunca de cópia de prosa.
