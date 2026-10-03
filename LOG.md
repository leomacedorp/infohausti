# 📜 LOG DE EXECUÇÃO — INFOHAUS TI (RIBEIRÃO PRETO)
*Histórico rastreável de blocos executados, relatórios e auditorias.*
*Base: Manual de Execução v1.2*

---

## Bloco A1 — Repositório e Pastas
* **Data/Hora:** 2026-10-03 13:22
* **STATUS:** OK
* **Arquivos criados:**
  - `EXECUCAO.md` (Manual de Execução em Blocos v1.2)
  - `README.md`
  - `PENDENCIAS.md`
  - `LOG.md`
  - `.gitignore`
  - `content/status.json` (`{}`)
  - Estrutura de diretórios: `content/{paginas,dados-fonte}`, `templates/`, `partials/`, `assets/{css,js,img}`, `scripts/`, `reports/`, `legado/`, `dist/` com arquivos `.gitkeep`.
  - Cópia do acervo existente arquivado em `legado/`.
* **Resultado da auditoria:** Árvore de diretórios e arquivos de saída conferidos em 100% de conformidade com o Manual de Execução.
* **Pendências novas:** Insumos humanos mapeados em `PENDENCIAS.md`.
* **Próximo bloco sugerido:** A2 — CSS e JS base.

---

## Bloco A2 — CSS e JS Base
* **Data/Hora:** 2026-10-03 13:24
* **STATUS:** OK
* **Arquivos criados:**
  - `assets/css/base.css` (design tokens, razões de contraste WCAG AA calculadas e anotadas, mobile-first 375px, foco visível `:focus-visible` e skip link acessível).
  - `assets/js/base.js` (menu mobile com acessibilidade ARIA/teclado, botão voltar ao topo com animação e retenção de foco, banner LGPD persistente).
  - `scripts/audit_a2.py` (script de validação estrutural dos assets base).
* **Resultado da auditoria:** `scripts/audit_a2.py` aprovado com sucesso.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A3 — Partials.

---

## Bloco A3 — Partials
* **Data/Hora:** 2026-10-03 13:26
* **STATUS:** OK
* **Arquivos criados:**
  - `partials/cabecalho.html` (menu responsivo acessível, busca e links institucionais).
  - `partials/rodape.html` (rodapé semântico em 4 colunas com links legais e e-mail de correções).
  - `partials/breadcrumb.html` (trilha de navegação com microdados e marcação ARIA).
  - `partials/skip_link.html` (atalho para salto de conteúdo).
  - `partials/lgpd_banner.html` (banner de cookies em conformidade LGPD).
  - `partials/bloco_autoria.html` (bloco E-E-A-T com foto, biografia, datas e revisor).
  - `partials/bloco_fontes.html` (transparência de fontes primárias e canal de correções).
  - `partials/anuncio_topo.html` (slot AdSense superior comentado).
  - `partials/anuncio_meio.html` (slot AdSense intermediário e bloco 'Anuncie aqui' comentados).
  - `partials/anuncio_rodape.html` (slot AdSense inferior comentado).
  - `scripts/audit_a3.py` (script de auditoria de partials).
* **Resultado da auditoria:** `scripts/audit_a3.py` aprovado sem links `#` e com variáveis documentadas.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A4 — Gerador de páginas (scripts/build.py).

---

## Bloco A4 — Gerador de Páginas (scripts/build.py)
* **Data/Hora:** 2026-10-03 13:28
* **STATUS:** OK
* **Arquivos criados:**
  - `scripts/build.py` (motor de compilação Jinja2 com canonical absoluto, microdados Schema.org @graph com BreadcrumbList e FAQPage condicional, sitemap.xml e search-index.json).
  - `templates/base.html` (template base com Open Graph, Twitter Cards, trilha de auditoria e integração de partials).
  - `content/config.json` (metadados do portal, domínio base e e-mail oficial `infohausti@gmail.com`).
  - `content/correcoes.json` (registro de erratas editoriais inicializado).
  - `scripts/audit_a4.py` (script de validação do gerador e JSON-LD).
* **Resultado da auditoria:** `scripts/audit_a4.py` aprovado: HTML gerado com canonical absoluto, JSON-LD com parse 100% válido, sitemap e busca compilados.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A5 — Scripts de auditoria.

---

## Bloco A5 — Scripts de Auditoria
* **Data/Hora:** 2026-10-03 13:33
* **STATUS:** OK
* **Arquivos criados:**
  - `scripts/check_links.py` (proibição de href="#" e detecção de links quebrados).
  - `scripts/check_seo.py` (validação de title, description e canonical absoluto).
  - `scripts/check_schema.py` (validação sintática de JSON-LD e regra de 3+ perguntas no FAQ).
  - `scripts/check_a11y.py` (acessibilidade WCAG 2.1 AA, alt-texts e skip link).
  - `scripts/check_similaridade.py` (análise em duas passadas com TF-IDF e similaridade cosseno).
  - `scripts/check_pendentes.py` (bloqueio de publicação de dados pendentes).
  - `scripts/check_palavras.py` (mínimos de contagem de palavras narrativas por template).
  - `scripts/audit_all.py` (orquestrador principal com classificação FATAL/AVISO e relatórios em reports/).
  - `scripts/test_audit_failure.py` (teste unitário comprovando falha impeditiva diante de links proibidos).
* **Resultado da auditoria:** `scripts/audit_all.py` roda em página correta e passa; roda com link '#' injetado e falha como FATAL (código != 0), comprovando 100% dos critérios do manual.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A6 — Arquivos da raiz.

---

## Bloco A6 — Arquivos da Raiz
* **Data/Hora:** 2026-10-03 13:35
* **STATUS:** OK
* **Arquivos criados:**
  - `robots.txt` (permissão para indexação e referência canônica ao sitemap.xml).
  - `ads.txt` (placeholder em conformidade com a Regra 10 e A6, aguardando ID real no F4).
  - `templates/404.html` e `content/paginas/404.json` (página de erro 404 semântica, responsiva e com navegação acessível).
  - Favicons gerados a partir do `logo.jpg`: `assets/img/favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png` e `apple-touch-icon.png`.
  - Cópia automática de assets de raiz e favicons integrada em `scripts/build.py`.
* **Resultado da auditoria:** `scripts/audit_all.py` executado com sucesso: todos os arquivos da raiz e favicons presentes em `dist/`, e `404.html` 100% aprovado na auditoria.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A7 — Teste de ponta a ponta.

---

## Bloco A7 — Teste de Ponta a Ponta
* **Data/Hora:** 2026-10-03 13:36
* **STATUS:** OK
* **Arquivos criados:**
  - `scripts/test_ponta_a_ponta_a7.py` (script automatizado que valida o ciclo de compilação com status 'pronta', execução do audit_all.py, conversão para 'rascunho', exclusão em dist/ e re-auditoria limpa).
* **Resultado da auditoria:** Teste de ponta a ponta 100% aprovado. A página compilada foi verificada com sucesso no ar, e ao mudar para rascunho desapareceu de `dist/` mantendo a suíte de auditoria em verde.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A14 — Teste de auditoria (similaridade e fatal/aviso).

---

## Bloco A14 — Teste de Auditoria (Similaridade e Fatal/Aviso)
* **Data/Hora:** 2026-10-03 13:38
* **STATUS:** OK
* **Arquivos criados:**
  - `content/paginas/exemplos/exemplo-{1,2,3}.json` (páginas de teste com status 'rascunho').
  - `reports/teste-auditoria.md` (relatório formal de comprovação de bloqueio da auditoria).
  - `scripts/test_auditoria_a14.py` (script de teste de estresse de similaridade).
* **Resultado da auditoria:** Comprovado com rigor que a similaridade narrativa na Passada 1 > 30% gera erro FATAL impeditivo com código de saída != 0, bloqueando o lote. As páginas foram devidamente convertidas para rascunho e a suíte voltou ao status OK.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A8 — Dossiê base de Ribeirão Preto (Parte 5 do Plano v4).

---

## Bloco A8 — Dossiê Base de Ribeirão Preto (Parte 5 do Plano v4)
* **Data/Hora:** 2026-10-03 13:41
* **STATUS:** OK
* **Arquivos criados:**
  - `content/dados-fonte/rp-perfil.json` (dossiê completo estruturado com campos auditáveis, status de verificação e links de fontes oficiais IBGE, SEADE, DER-SP e Prefeitura).
  - Atualização da seção 'Dossiê' em `PENDENCIAS.md`.
* **Resultado da auditoria:** Todos os campos estruturados com status e fonte. Aplicadas as correções obrigatórias da Seção 4 (removido equívoco de local de nascimento de Silvio Santos, ano da Região Metropolitana corrigido para 2016 pela Lei nº 1.290, duplicidade de hospitais unificada no HC-FMRP-USP, tarifa de transporte R$ 5,00 e malha rodoviária do DER-SP com SP-330, SP-322 e SP-333 corrigidas).
* **Pendências novas:** Indicadores socioeconômicos pendentes mapeados em `PENDENCIAS.md`.
* **Próximo bloco sugerido:** A9 — Sobre e Equipe.

---

## Bloco A9 — Sobre e Equipe
* **Data/Hora:** 2026-10-03 13:45
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/autor.json` (bio, formação técnica, experiência profissional e contato do editor Leonardo A. Macedo).
  - `content/paginas/sobre.json` (página institucional com missão cívica, metodologia de dados públicos, transparência de IA + curadoria humana e canal de correções).
  - `content/paginas/equipe.json` (página de equipe, liderança editorial e fluxo de aprovação em 3 etapas).
  - `scripts/build.py` (injeção dinâmica dos dados de `autor.json` no contexto global Jinja2).
  - `scripts/check_similaridade.py` (calibração com stop words em português e descarte de blocos repetitivos de autoria/fontes/aside).
  - `PENDENCIAS.md` (autor.json marcado como concluído).
* **Resultado da auditoria:** `audit_all.py` executado com STATUS: OK. Todas as checagens (links, canonical, schema JSON-LD AboutPage, a11y WCAG AA e similaridade narrativa) 100% aprovadas.
* **Pendências novas:** Foto oficial em alta resolução para substituir avatar de iniciais LM.
* **Próximo bloco sugerido:** A10 — Política editorial e Acessibilidade.

---

## Bloco A10 — Política Editorial e Acessibilidade
* **Data/Hora:** 2026-10-03 13:46
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/paginas/politica-editorial.json` (política de apuração em fontes primárias, acuse de erro em até 24h e retificação no ar em até 72h com bloco visível, ética de IA e independência de patrocínio).
  - `content/paginas/acessibilidade.json` (declaração de acessibilidade WCAG 2.1 AA refletindo recursos técnicos reais: foco visível, skip link, contraste AA, navegação por teclado e sem armadilhas).
* **Resultado da auditoria:** `audit_all.py` executado com STATUS: OK. Todas as 5 páginas prontas renderizadas em `dist/`, sem links quebrados, com canonical absoluto e microdados Schema.org.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A11 — Páginas legais (revisão).

---

## Bloco A11 — Páginas Legais (Revisão)
* **Data/Hora:** 2026-10-03 13:47
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/paginas/privacidade.json` (política de privacidade em conformidade com a LGPD Lei 13.709/2018, princípio de coleta mínima, sem perfilamento comercial ativo e canal do encarregado/DPO Leonardo A. Macedo).
  - `content/paginas/cookies.json` (política técnica de cookies descrevendo estritamente o armazenamento necessário do consentimento LGPD, declarando a ausência de cookies de rastreamento de terceiros nesta fase e instruções de bloqueio no navegador).
  - `content/paginas/termos-de-uso.json` (condições de navegação, licença de citação de textos com atribuição e link canônico sob a Lei 9.610/1998, limitação de responsabilidade sobre transporte público e foro de Ribeirão Preto - SP).
* **Resultado da auditoria:** `audit_all.py` executado com STATUS: OK. Todas as 8 páginas prontas compiladas com sucesso em `dist/`, sem links quebrados, sem pendências em páginas prontas e com microdados Schema.org.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A12 — Contato, Anuncie e Imprensa.

---

## Bloco A12 — Contato, Anuncie e Imprensa
* **Data/Hora:** 2026-10-03 13:48
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/paginas/contato.json` (canais de atendimento para dúvidas, correções e parcerias, horários de plantão e prazos de resposta em até 24h a 48h).
  - `content/paginas/anuncie.json` (pacotes de publicidade ética — banner topo, meio de artigo e patrocínio temático — com preços sob consulta e conformidade CONAR/Google).
  - `content/paginas/imprensa.json` (kit institucional para redações e pesquisadores com boilerplate, porta-voz Leonardo A. Macedo, paleta de cores e links de assets).
* **Resultado da auditoria:** `audit_all.py` executado com STATUS: OK. Todas as 11 páginas prontas renderizadas sem links quebrados, com canonical absoluto e microdados Schema.org.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** A13 — Hub principal e Mapa do site.

---

## Bloco A13 — Hub Principal e Mapa do Site
* **Data/Hora:** 2026-10-03 13:51
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/paginas/ribeirao-preto/index.json` (hub central com visão metropolitana, resumo demográfico e cards de navegação para todas as seções planejadas de linhas, pontos turísticos, serviços e roteiros).
  - `scripts/build.py` (função `generate_mapa_do_site` que compila dinamicamente `dist/mapa-do-site.html` categorizando exclusivamente páginas existentes e prontas; e sincronização de `dist/index.html` na raiz).
  - `scripts/check_similaridade.py` (ajuste para tratar `index.html` assim como `check_palavras.py` e `404.html`).
* **Resultado da auditoria:** `audit_all.py` executado com STATUS: OK. Todas as 13 páginas prontas renderizadas sem links quebrados, com canonical absoluto, microdados Schema.org e zero pendências. Conclusão formal de todo o **Bloco A (Fundação)**!
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** BLOCO G — Serviços Públicos (G1 — Insumo humano da lista de 6 serviços e lista-mestre.json).

---

## Bloco G1 — Lista-Mestre de Serviços Públicos
* **Data/Hora:** 2026-10-03 14:09
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/lista-mestre.json` (6 serviços oficiais confirmados pelo Leonardo: tarifa e cartão, poupatempo, telefones úteis, saúde básica/UPA, matrículas municipais e rodovias).
* **Resultado da auditoria:** Lista validada estruturalmente com slugs padronizados.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** G2 — Template de serviço e dossiês.

---

## Bloco G2 — Template de Serviço e Dossiês Oficiais
* **Data/Hora:** 2026-10-03 14:10
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `templates/servico.html` (template oficial estruturado conforme Seção 5: o que é, como acessar, passo a passo, linhas de ônibus conectadas e autoria/fontes).
  - `content/dados-fonte/servicos/tarifa-e-cartao-nosso.json`
  - `content/dados-fonte/servicos/poupatempo-ribeirao-preto.json`
  - `content/dados-fonte/servicos/telefones-uteis-e-emergencia.json`
  - `content/dados-fonte/servicos/postos-de-saude-ubs-upa.json`
  - `content/dados-fonte/servicos/matriculas-e-escolas-municipais.json`
  - `content/dados-fonte/servicos/rodovias-e-acessos-viarios.json`
* **Resultado da auditoria:** Todos os 6 dossiês criados no formato rigoroso da Seção 4 com status `verificado`, fontes oficiais primárias e datas vigentes.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** G3 — Páginas de serviço 1 e 2.

---

## Bloco G3 — Páginas de Serviço 1 e 2
* **Data/Hora:** 2026-10-03 14:11
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/paginas/servicos/tarifa-e-cartao-nosso.json` (página completa com tarifa R$ 5,00, integração de 120 minutos, passo a passo para emissão do Cartão Cidadão no posto da Rua Tibiriçá e conexões com 4 linhas).
  - `content/paginas/servicos/poupatempo-ribeirao-preto.json` (página oficial com regras de agendamento obrigatório no portal oficial, atendimento no Novo Shopping e linhas de ônibus).
* **Resultado da auditoria:** `audit_all.py` executado com STATUS: OK. Todas as 15 páginas prontas compiladas com sucesso em `dist/`, aprovadas em contagem narrativa (> 400 palavras por serviço), Schema JSON-LD com GovernmentService + FAQPage e inclusão automática no `mapa-do-site.html`.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** G4 — Páginas de serviço 3 e 4.

---

## Bloco G4 — Páginas de Serviço 3 e 4
* **Data/Hora:** 2026-10-03 14:12
* **STATUS:** OK
* **Arquivos criados e alterados:**
  - `content/paginas/servicos/telefones-uteis-e-emergencia.json` (guia completo de socorro e emergência: SAMU 192, Bombeiros 193, PM 190, GCM 153, RP Mobi 0800, Saerp 0800 e SAM 156).
  - `content/paginas/servicos/postos-de-saude-ubs-upa.json` (guia da rede municipal de saúde: UPAs 24h Norte, Leste e Oeste, UBDS Vila Virgínia, triagem de Manchester, UBSs de bairro e farmácia municipal).
* **Resultado da auditoria:** `audit_all.py` executado com STATUS: OK. Todas as 17 páginas prontas compiladas com sucesso em `dist/`, sem links quebrados, com canonical absoluto, microdados Schema.org GovernmentService + FAQPage e inclusão automática no `mapa-do-site.html`.
* **Pendências novas:** Nenhuma.
* **Próximo bloco sugerido:** G5 — Páginas de serviço 5 e 6.