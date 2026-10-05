# 📋 PENDÊNCIAS — INFOHAUS TI (RIBEIRÃO PRETO)
*Registro de itens em aberto, insumos humanos e dados sob verificação.*
*Base: Manual de Execução v1.2 / Plano Mestre v4*

---

## 👤 Insumos Humanos (Aguardando Leonardo)

- [ ] **Expansão Turística (05/10/2026) — 4 pendências aceitas por Leo:**
  - [ ] **Telefone do Sesc RP:** sem fonte oficial (páginas da unidade não publicam); página corretamente NÃO publica telefone — contato via formulário sescsp.org.br/fale-conosco.
  - [ ] **História do IFF:** página institucional inacessível (timeout de extração); campo pendente no dossiê — história não publicada sem fonte.
  - [ ] **Endereço postal das Estações (Barracão e Mogiana):** fontes oficiais só dão referência viária (junção Dom Pedro I × Capitão Salomão; alinhamento da Av. Mogiana) — páginas usam a referência.
  - [ ] **Visitação do Palácio Rio Branco:** obras de restauro desde 06/2024; visitação marcada como "não confirmada" até obra concluída.
- [x] **`content/autor.json` (A9):** Preenchido com dados biográficos reais do editor/autor Leonardo A. Macedo (analista de TI, servidor público municipal, orquestrador de sistemas inteligentes).
- [x] **`content/lista-mestre.json` (G1, B2, H0):** 6 serviços públicos, 12 pontos turísticos e 5 roteiros temáticos definidos e auditados. Pendente apenas D1 (10 bairros) e J1 (5 pilares da história).
- [x] **Padronização de Slug — Theatro Pedro II (Decisão Leo 03/10/2026):** O arquivo de dados fonte/dossiê se chama `theatro-pedro-ii.json` (nome oficial tombado). A URL pública em `dist/` é mantida como `teatro-dom-pedro.html` (por herança do legado + comportamento de busca real do usuário no Google: "teatro dom pedro"). Decisão intencional e documentada.
- [ ] **Foto Oficial do Autor (A9):** Arquivo de foto real para `assets/img/autor.jpg` (atualmente exibindo avatar estilizado com iniciais LM).
- [ ] **Logo e Favicon (A6):** Arquivos oficiais em alta resolução para geração dos favicons e assets de marca.

---

## 🔍 Seção Dossiê (Concluído no Bloco A8)

- [x] **Fundador e Silvio Santos:** Tratado em `rp-perfil.json` — removida afirmação de nascimento em RP (nascido no Rio de Janeiro/RJ).
- [x] **Região Metropolitana:** Confirmado ano 2016 e Lei Complementar Estadual nº 1.290/2016 (34 municípios).
- [x] **Hospitais:** Resolvida duplicidade, padronizado como `HC-FMRP-USP` (Unidade Campus e Unidade Emergência).
- [x] **BRT:** Definido oficialmente como corredores estruturais em implantação progressiva do programa Ribeirão Mobilidade.
- [x] **Tarifa e Bilhete:** Tarifa vigente R$ 5,00 (Decreto Municipal) com integração de 120 minutos do sistema RP Mobi.
- [x] **Rodovias:** Retificado DER-SP: SP-330 (Anhanguera), SP-322 (Attílio Balbo/Duarte Nogueira), SP-328 (Alexandre Balbo), SP-333 (Carlos Tonani). Removida confusão com SP-348 Bandeirantes.
- [x] **Distâncias Rodoviárias:** Confirmadas via DER-SP (São Paulo: 315 km, Campinas: 225 km, Brasília: 710 km).
- [ ] **Indicadores Socioeconômicos Pendentes:** MEIs ativos (aguardando atualização Portal do Empreendedor 2025/2026), estoque Caged e contagem de leitos SUS no CNES mantidos como `status: pendente` em `rp-perfil.json` até validação pontual.

---

## 📝 Notas Técnicas e Deliberações Editoriais

- [x] **Padrão de Contagem de Palavras Narrativas (Lote 1: 800+, Lotes 2–4: 460+):**
  * **Intencionalidade:** Sim, decisão editorial deliberada e intencional.
  * **Motivo:** O requisito mínimo regulamentar da Regra 16 do `EXECUCAO.md` para páginas de linhas de ônibus é de **250 palavras narrativas**. No Lote 1, que abrangeu as linhas Noturnas (001 a 008) e rotas radiais pioneiras (015 e 023), a extensão foi ampliada para 800+ palavras devido à necessidade de contextualizar a dinâmica urbana da madrugada ribeirão-pretana, polos de lazer e segurança. Para as linhas alimentadoras (Lotes 2 e 3) e convencionais (Lote 4 em diante), o padrão de 460+ palavras garante concisão, rigor factual e riqueza descritiva (quase o dobro do mínimo exigido de 250 palavras), evitando redundâncias e 'padding' textual, o que protege a integridade da similaridade cruzada da Passada 1 (mantendo-a confortavelmente abaixo de 26% em toda a malha).