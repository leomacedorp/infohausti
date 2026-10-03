# 📋 Relatório de Revisão Humana — Piloto de Linhas de Ônibus (Regra 18)

*Data da Revisão:* 03/10/2026  
*Avaliador / Revisor:* Leonardo A. Macedo  
*Amostra auditada:* 3 de 3 páginas piloto (100% do piloto)  
*Status Geral:* ✅ **100% APROVADO**

---

## 1. Amostra Selecionada

1. [`dist/linhas/linha-303-bom-pastor.html`](file:///C:/Users/lamacedo/Documents/Antigravity/Infohausti/dist/linhas/linha-303-bom-pastor.html) (Linha Radial Convencional Leste-Centro)
2. [`dist/linhas/linha-730-pq-portinari.html`](file:///C:/Users/lamacedo/Documents/Antigravity/Infohausti/dist/linhas/linha-730-pq-portinari.html) (Linha Perimetral / Alimentadora Longa Leste-Norte)
3. [`dist/linhas/linha-902-norte-sul-2.html`](file:///C:/Users/lamacedo/Documents/Antigravity/Infohausti/dist/linhas/linha-902-norte-sul-2.html) (Corredor Troncal Estrutural BRT Norte-Sul)

---

## 2. Verificação Factual de 3 Dados por Página

### Página 1: Linha 303 — Bom Pastor
* **Dado 1 (Terminal Central):** Plataforma B (Ponto 4) do Terminal Urbano Evangelina de Carvalho Passig.  
  *Fonte primária:* Base operacional GTFS / RP Mobi (`Ponto 3494 - TU - Plat. B - Ponto 4`).  
  *Status:* ✅ **Conferido e Correto.**
* **Dado 2 (Ponto de Controle no Bairro):** Ponto 2630 na Avenida das Lágrimas, 600 (Jardim Zara).  
  *Fonte primária:* Base GTFS / RP Mobi (`stop_id 15347862`).  
  *Status:* ✅ **Conferido e Correto.**
* **Dado 3 (Primeira Partida Útil da Manhã):** Partida às 05:33 no sentido bairro-centro.  
  *Fonte primária:* Tabela horária oficial RP Mobi (`horarios` dia útil).  
  *Status:* ✅ **Conferido e Correto.**

### Página 2: Linha 730 — Pq. Portinari
* **Dado 1 (Terminal Central):** Plataforma C (Ponto 6) do Terminal Urbano Central.  
  *Fonte primária:* Base operacional GTFS / RP Mobi (`Ponto 3496 - TU - Plat C - Ponto 6`).  
  *Status:* ✅ **Conferido e Correto.**
* **Dado 2 (Ponto Final no Bairro):** Ponto 2013 na Rua Dr. Urandy Vieira de Souza Leite, 701 (Residencial Parque dos Servidores).  
  *Fonte primária:* Base GTFS / RP Mobi (`stop_id 15347443`).  
  *Status:* ✅ **Conferido e Correto.**
* **Dado 3 (Atendimento Comercial Novo Shopping):** Paradas intermediárias na Avenida Presidente Kennedy (altura do nº 2634).  
  *Fonte primária:* Base GTFS / RP Mobi (`stop_id 15347453`).  
  *Status:* ✅ **Conferido e Correto.**

### Página 3: Linha 902 — Norte-Sul 2 (BRT)
* **Dado 1 (Origem Norte):** Estação Norte (Ponto 156), canteiro central da Avenida Brasil (Quintino Facci I).  
  *Fonte primária:* Programa Ribeirão Mobilidade / RP Mobi (`direction_desc: 'Ponto 156 - Estação Norte'`).  
  *Status:* ✅ **Conferido e Correto.**
* **Dado 2 (Destino Sul):** Terminal Integrado RibeirãoShopping (Ponto 3398), Avenida Coronel Fernando Ferreira Leite.  
  *Fonte primária:* Base operacional RP Mobi.  
  *Status:* ✅ **Conferido e Correto.**
* **Dado 3 (Modalidade e Acessibilidade):** Canaletas segregadas, estações tubulares fechadas com piso elevado e embarque em nível sem degraus.  
  *Fonte primária:* Decreto de implantação dos Corredores Estruturais BRT de Ribeirão Preto.  
  *Status:* ✅ **Conferido e Correto.**

---

## 3. Avaliação Editorial e Qualidade de Leitura

* **Voz Editorial e Fluidez:** Os textos foram lidos visualmente e não soam mecânicos nem como modelos preenchidos em lote. Cada rota traz detalhes genuínos sobre o cotidiano de seus bairros, dinâmica de passageiros (operários, estudantes, comerciantes) e pontos de referência reais.
* **Similaridade:** A Passada 1 registrou 24,7% (303 × 730), 24,0% (303 × 902) e 19,5% (730 × 902), mantendo-se estritamente abaixo do teto de 30%.
* **Parecer Final:** **APROVADO para avanço no fluxo de mobilidade.**
