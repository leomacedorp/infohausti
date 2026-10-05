Infohausti RP — Manual de Execução em Blocos



Base: Plano Mestre v4 · Versão 1.2 · 2026-10-03



Para a IA executora: leia a seção 1 inteira e depois SOMENTE o bloco

pedido. Não leia nem execute outros blocos.

Para o Leo: veja a seção 0.



---



0. Como usar (humano)



1. Salve este arquivo na raiz do repositório como EXECUCAO.md.

2. Faça os insumos da seção 3. Os blocos A8, A9, B2, C0, G1, H0 e J1

dependem deles.

3. Para cada bloco, cole o prompt da seção 2 trocando [ID].

4. Só avance quando o relatório vier com STATUS: OK e você tiver olhado as

pendências.

5. Blocos marcados 👤 são seus. A IA só prepara o material.

6. Nos CHECKPOINTS, pare e decida antes de continuar.



Princípios deste manual:



· Nada de dado inventado. Dado só entra com status verificado e fonte.

· A página é gerada por script a partir de JSON. A IA preenche conteúdo;

SEO, schema e canonical saem do gerador.

· FAQPage só entra com 3 ou mais perguntas reais.

· Leo é o aprovador final. A auditoria automática roda antes de cada commit.

· Similaridade é medida só no texto narrativo (sem cabeçalho, rodapé,

tabelas e listas de paradas).

· Checkpoint antes das 120 linhas, para publicar o site e pedir o AdSense

cedo.

· Metas, preços e monetização ficam fora deste manual.



---



1. Regras globais (valem para todo bloco)



1. Faça somente o bloco pedido. Terminou, pare. Não adiante o próximo.

2. Só crie ou edite os arquivos da linha "Saída". Nunca apague nem renomeie

arquivo existente. Qualquer outra necessidade vai para PENDENCIAS.md.

3. Nunca invente dado: número, data, nome, URL, horário, endereço, preço,

slug. Dado só vem de content/dados-fonte/ com status verificado. Faltou

dado, registre em PENDENCIAS.md e siga. A IA também não sugere listas

(pontos, bairros, serviços, roteiros, pilares): quem decide é o Leo.

4. Dado pendente não aparece na página. A página que depende dele fica

"status": "bloqueada" em content/status.json.

5. Texto original, escrito a partir dos dados. Nada copiado de outro site.

Proibido: "lorem", "em breve" visível, links #, botão sem destino.

6. Links internos são resolvidos por slug no gerador. Alvo ainda não

construído é omitido, nunca vira link quebrado. O mínimo de 5 links por

página é cobrado no F2, depois da passada de linkagem do F1.

7. SEO, canonical absoluto, Open Graph, schema, trilha de auditoria e

data-fonte-verificacao saem do build.py. Não escreva isso à mão nas páginas.

8. Imagens: só arquivos de assets/img/ listados em content/imagens.json

(com autor e licença). Nunca baixe imagem de terceiros. Sem imagem, marque

pendente e siga.

9. Mobile-first (375px), sem framework de CSS ou JS. Dependências

permitidas: python3, jinja2, scikit-learn. Mais nada sem perguntar.

10. Nunca coloque IDs reais de AdSense ou GA4. Só placeholders comentados.

11. Antes de terminar, rode python scripts/audit_all.py. Só declare STATUS:

OK se passar. Cole a saída no relatório.

12. Git: antes do bloco, git status limpo e git push para o remoto privado.

Ao final, git commit -m "[ID] descrição curta" seguido de git push. Backup

off-site não é opcional.

13. Dúvida, ambiguidade ou conflito de regras: pare e pergunte. Não

adivinhe.

14. Relatório final, no máximo 15 linhas:

    · STATUS: OK ou STATUS: FALHOU

    · arquivos criados e alterados

    · resultado da auditoria

    · pendências novas

    · próximo bloco sugerido

1.20 — Mudanças estruturais (novos arquivos de política, alteração de
thresholds, mudança de escopo) exigem aprovação explícita do Leo antes de
serem codadas. O executor pode PROPOR, não aplicar.

Regras de auditoria (aplicadas pelo audit_all.py):



15. Classificação de cada checagem:



Checagem Classificação

Link quebrado ou # Fatal

Schema ausente ou inválido Fatal

Canonical relativo Fatal

Dado pendente em página pronta Fatal

Abaixo do mínimo de palavras do template Fatal

Similaridade > 30% no texto narrativo Fatal

Similaridade > 30% em tabelas/listas de paradas Aviso (revisão humana)

Alt-text curto (menos de 5 palavras) Aviso

Fonte próxima do vencimento de revisão Aviso



16. Mínimos de palavras por template:



Template Mínimo

Linha de ônibus 250

Serviço 400

Bairro 400

Ponto turístico 800

Roteiro 500

História 1.500

Evento 300

Dados 500 + tabela

Comparativo 800



A contagem considera só o texto dentro de <main>, excluindo cabeçalho,

rodapé, breadcrumb, blocos de fonte e autoria, tabelas e listas de dados.



17. O check_similaridade.py roda em duas passadas:

    · Primeira: só o texto narrativo (parágrafos e headings editoriais).

Similaridade > 30% = fatal, lote bloqueado.

    · Segunda: inclui tabelas e listas de paradas. Similaridade > 30% =

aviso para revisão humana, sem bloquear.

18. Antes de cada CHECKPOINT, o Leo revisa manualmente 10% das páginas do

lote (mínimo 3 páginas), conferindo 3 dados factuais por página contra a

fonte citada. Resultado em reports/revisao-humana-[lote].md. Sem isso, o

checkpoint não fecha.

19. Política de correção de erros:

    · Canal: o e-mail de correção (definido pelo Leo na seção 3).

    · Prazo: acuse de recebimento em até 24h; correção publicada em até 72h.

    · Quando um erro é corrigido, a página ganha um bloco visível:

"Corrigido em [data]. Versão anterior continha [descrição breve do erro]."

    · O build.py gera esse bloco automaticamente a partir de

content/correcoes.json.



---



2. Prompt de abertura (copiar e colar)



```

Você é a IA executora do projeto Infohausti RP.

Leia EXECUCAO.md: seção 1 (regras globais) e o bloco [ID].

Faça SOMENTE o bloco [ID]. Não avance para outro bloco.

Se faltar algum insumo ou dado, pare e me diga o que falta.

Ao terminar, rode a auditoria, faça o commit + push e responda com o

relatório da regra 14.

```



---



3. Insumos humanos 👤 (antes de começar)



Insumo Arquivo Usado em

Nome, bio real, formação e experiência do autor/editor, foto

content/autor.json A9 e todas as páginas

Domínio base e e-mail de contato content/config.json A4, A11

Endereço de e-mail para correção de erros (ex.: erros@dominio), criado por

você content/config.json A9, A10, todas as páginas

Logo e favicon assets/img/ A6

Dossiês dos 6 pontos já levantados content/dados-fonte/pontos-brutos/ B1

Páginas prontas: Theatro Pedro II e Palacete legado/ B4

Banco das 120 linhas (exportado) content/dados-fonte/banco-linhas.* C0

Malha viária extraída content/dados-fonte/malha/ C3

Fotos próprias ou licenciadas, com autor e licença assets/img/ +

content/imagens.json todos os blocos de página

Listas de 12 pontos, 10 bairros, 6 serviços, 5 roteiros e 5 pilares de

história content/lista-mestre.json G1, B2, H0, D1, J1

Repositório git remoto privado (GitHub, GitLab, Codeberg) — regra 12



Nenhuma lista de slugs entra no repositório sem confirmação do Leo. O

content/lista-mestre.json é preenchido manualmente pelo Leo, não gerado

pela IA.



Slugs oficiais: o slug de cada página é definido a partir do nome oficial

do bem ou instituição, por decisão do Leo. A IA não assume slug existente

nem nome consagrado.



---



4. Formato de dado e correções obrigatórias



Todo dado em content/dados-fonte/*.json segue este formato:



```json

"campo": { "valor": "...", "status": "verificado|pendente", "fonte_url":

"https://...", "verificado_em": "AAAA-MM-DD" }

```



Itens do dossiê da Parte 5 do Plano v4 que NÃO podem entrar como

verificados até a checagem no A8:



Item Problema

Silvio Santos Participações, "fundador nascido em RP" Silvio Santos nasceu

no Rio de Janeiro. Remover essa afirmação.

Região Metropolitana "criada em 2018" Provável erro. Confirmar ano e lei

estadual exata.

"Hospital das Clínicas" na lista de hospitais Duplicado com o HC-FMRP-USP.

BRT "parcialmente implantado" Duvidoso. Confirmar com a RP Mobi ou a

Prefeitura.

Tarifa R$ 5,20 e nome "Cartão Nosso" Confirmar valor e nome vigentes.

Rodovias citadas SP-333 foi listada como Bandeirantes (a Bandeirantes é

SP-348), e "Attílio Balbo" aparece associado a SP-322. Confirmar todas no

DER-SP.

Distâncias rodoviárias Conferir todas.

PIB, MEIs, empregos formais, leitos SUS, UBS/UPA, cobertura de saúde da

família, alunos de cursos técnicos Conferir ano e fonte oficial.

Oktoberfest RP, Agrishow, Optibus, Turismo em Foco Já marcados como

"verificar" no plano.

Lista de 12 pontos turísticos Só 6 têm dossiê pronto. Os 6 restantes

precisam ser confirmados pelo Leo antes do Bloco B.



---



5. Estruturas de template



Ordem de precedência:



1. Se existir docs/templates-detalhados.md, ele prevalece. A IA constrói os

templates a partir dele, nunca do zero.

2. Se não existir, a IA usa a tabela abaixo como reserva e registra em

PENDENCIAS.md que o arquivo detalhado está ausente.



Template Seções (em ordem) Schema principal

Linha resumo (origem/destino) · itinerário em ordem · paradas principais ·

horários (dia útil/sábado/domingo) · tarifa e integrações · atrações e

serviços próximos · bairros atendidos · mapa (Leaflet só se houver

geometria) · fontes · autoria WebPage

Ponto turístico resumo · visita (endereço, horário, ingresso) · história e

contexto · como chegar (3–5 linhas) · atrações próximas · roteiros que

incluem · fontes · autoria TouristAttraction

Roteiro perfil e duração · paradas em ordem (links) · deslocamento · melhor

época · fontes · autoria TouristTrip + ItemList

Bairro perfil e zona · como chegar (linhas) · pontos e serviços · história

breve · fontes · autoria Place

Serviço o que é · como acessar (endereço, telefone, horário) · passo a

passo · linhas que chegam · fontes · autoria GovernmentService

História texto-pilar longo · linha do tempo · locais relacionados · fontes

primárias e secundárias · autoria Article

Evento só com edição confirmada em fonte oficial · data · local · como

chegar · fonte Event

Gastronomia / Hotel categorias · só estabelecimentos com dado verificado ·

link de afiliado com rel="sponsored" · patrocinado identificado ItemList /

LocalBusiness

Dados resumo executivo · gráficos (Chart.js) · tabela + CSV · comparativo

com anos anteriores · fontes Dataset

Comparativo tabela comparativa · análise por categoria · prós e contras ·

fontes Article + Dataset



Em todos: breadcrumb (BreadcrumbList) e FAQPage só com 3 ou mais perguntas

reais.



---



6. Blocos



BLOCO A — Fundação



A1 — Repositório e pastas



· Faça: iniciar o git e criar a estrutura content/{paginas,dados-fonte},

templates/, partials/, assets/{css,js,img}, scripts/, reports/. dist/ é

gerado e nunca editado à mão.

· Saída: README.md, PENDENCIAS.md, LOG.md, .gitignore, content/status.json

({}), .gitkeep nas pastas.

· Pronto quando: existe 1 commit e a árvore bate com a descrição acima.



A2 — CSS e JS base



· Faça: base.css com tokens de cor e tipografia, mobile-first 375px,

contraste AA (anotar as razões nos comentários), foco visível, skip link,

font-display: swap. base.js com menu, voltar ao topo e banner LGPD.

· Saída: assets/css/base.css, assets/js/base.js.

· Pronto quando: uma página de teste renderiza bem em 375px e em 1280px,

sem erros no console.



A3 — Partials



· Faça: cabeçalho (menu e busca), rodapé completo, breadcrumb, skip link,

banner LGPD, bloco Autoria, bloco Fontes e verificações, "Anuncie aqui"

comentado, 3 slots AdSense comentados (topo, meio, rodapé).

· Saída: partials/*.html.

· Pronto quando: cada partial documenta no topo as variáveis que usa e não

tem nenhum link #.



A4 — Gerador de páginas (scripts/build.py)



· Entrada: content/paginas/**/*.json com os campos slug, template, titulo,

descricao, h1, autor, publicado, atualizado, proxima_revisao, fontes[],

secoes, faq[], imagens[], links_planejados[], status.

· Faça: title e meta únicos, canonical absoluto (base em config.json), Open

Graph e Twitter, article:published_time e modified_time, JSON-LD (tipo do

template + BreadcrumbList, FAQPage só com 3 ou mais perguntas),

data-fonte-verificacao, comentário de trilha de auditoria (autor, revisor,

publicado, próxima revisão, fonte, versão), resolução de links por slug

(omite alvo inexistente), sitemap.xml, search-index.json para a busca,

bloco de correção a partir de content/correcoes.json. Só vão para dist/ as

páginas com status pronta.

· Saída: scripts/build.py, templates/base.html, content/config.json,

content/correcoes.json (vazio).

· Pronto quando: uma página de exemplo gera HTML válido e o JSON-LD faz

parse sem erro.



A5 — Scripts de auditoria



· Faça: check_links.py, check_seo.py, check_schema.py, check_a11y.py,

check_similaridade.py (duas passadas, regra 17), check_pendentes.py,

check_palavras.py (mínimos da regra 16), audit_all.py (roda tudo,

classifica fatal/aviso conforme a regra 15, sai com código diferente de

zero se houver fatal, grava em reports/).

· Saída: scripts/*.py.

· Pronto quando: roda em página correta e passa; roda numa página de teste

com link # e falha como fatal.



A6 — Arquivos da raiz



· Saída: robots.txt, 404.html, ads.txt (só comentário, o ID real entra no

F4), favicon e variantes a partir do logo do insumo.

· Pronto quando: os arquivos aparecem em dist/ e o 404.html passa na

auditoria.



A7 — Teste de ponta a ponta



· Faça: criar 1 página falsa com status pronta, rodar build e auditoria, e

depois mudar o status dela para rascunho.

· Pronto quando: audit_all.py passa e a página de teste não aparece em

dist/.



A14 — Teste de auditoria (similaridade e fatal/aviso) — executar logo

depois do A7, antes do A8



· Faça: rodar check_similaridade.py e audit_all.py sobre 3 páginas de

exemplo criadas em content/paginas/exemplos/, com similaridade forçada

acima de 30% em duas delas. Confirmar que fatal e aviso funcionam conforme

a regra 15, que o lote é bloqueado e que a auditoria sai com código

diferente de zero. Depois, mudar o status das páginas de exemplo para

rascunho.

· Saída: reports/teste-auditoria.md.

· Pronto quando: o teste demonstra o comportamento correto e o Leo aprova.



A8 — Dossiê base de Ribeirão Preto (Parte 5 do Plano v4)



· Faça: converter a Parte 5 em content/dados-fonte/rp-perfil.json no

formato da seção 4, tudo começando como pendente. Verificar nas fontes

oficiais (IBGE, SEADE, DER-SP, ANAC, etc.) e aplicar as correções da seção

4. O que não conseguir confirmar fica pendente.

· Saída: rp-perfil.json, seção "Dossiê" em PENDENCIAS.md.

· Pronto quando: todo campo tem status e fonte, e os itens suspeitos da

seção 4 estão tratados.



A9 — Sobre e Equipe



· Entrada: content/autor.json e o e-mail de correção em

content/config.json. Se faltar, pare e peça. Nunca invente bio nem crie

e-mail.

· Faça: a página exibe quem escreve, quem revisa, quem aprova, como o

conteúdo é produzido (com menção explícita ao uso de IA + revisão humana) e

o canal de correção de erros.

· Saída: sobre, equipe.



A10 — Política editorial e Acessibilidade



· Faça: descrever o processo editorial real (fonte primária, revisão e a

política de correção da regra 19: acuse em 24h, correção em até 72h, bloco

visível na página). Declarar o uso de IA na redação com aprovação humana,

conforme o processo real. A página de acessibilidade deve refletir só o que

o site realmente cumpre.

· Saída: páginas politica-editorial e acessibilidade. (O arquivo

content/correcoes.json já foi criado no A4; aqui não é criado de novo.)



A11 — Páginas legais 👤 (revisão)



· Faça: privacidade (LGPD), cookies e termos de uso. Descrever somente o

que está ativo hoje. O texto sobre AdSense e GA4 entra no F4, quando forem

ativados. O canal de correção usa o e-mail definido na seção 3; a IA não

cria endereço de e-mail.

· Saída: privacidade, cookies, termos-de-uso.

· Observação: você deve revisar o texto jurídico (ou um advogado).



A12 — Contato, Anuncie e Imprensa



· Faça: "Anuncie" com pacotes e preço "sob consulta" até o Leo confirmar

valores. Imprensa com kit básico (logo, descrição, contato).

· Saída: contato, anuncie, imprensa.



A13 — Hub principal e Mapa do site



· Saída: ribeirao-preto/index, mapa-do-site (gerado pelo build).

· Pronto quando: o hub linka as seções planejadas e o mapa-do-site lista só

as páginas existentes.



---



BLOCO G — Serviços públicos



ID Faça Saída

G1 👤 Confirmar os 6 serviços e escrever content/lista-mestre.json (campo

servicos). A IA não sugere lista; só valida o formato. lista-mestre.json

G2 Template de serviço + dossiês (formato da seção 4) dos 6 serviços

templates/servico.html, dados-fonte/servicos/*.json

G3 Páginas de serviço 1 e 2 2 páginas

G4 Páginas de serviço 3 e 4 2 páginas

G5 Páginas de serviço 5 e 6 2 páginas

G6 servicos/index 1 página



---



BLOCO B — Turismo



ID Faça Saída

B1 Consolidar os dossiês dos 6 pontos já levantados no formato da seção 4

dados-fonte/pontos/*.json

B2 Levantar e verificar dossiês dos 6 pontos novos. Só prossegue com a

lista confirmada pelo Leo em content/lista-mestre.json. A IA não assume

nomes. dados-fonte/pontos/*.json

B3 Template de ponto turístico templates/ponto.html

B4 Migrar Theatro Pedro II e Palacete (de legado/) para o novo template.

Slug definido pelo Leo. 2 páginas

B5 2 pontos com dossiê 2 páginas

B6 2 pontos com dossiê 2 páginas

B7 2 pontos novos 2 páginas

B8 2 pontos novos 2 páginas

B9 2 pontos novos 2 páginas

B10 pontos-turisticos/index 1 página



---



BLOCO H — Roteiros



ID Faça Saída

H0 👤 Definir os 5 roteiros e escrever content/lista-mestre.json (campo

roteiros). Os roteiros só podem usar pontos já confirmados no Bloco B. A IA

não sugere lista. lista-mestre.json

H1 Template de roteiro templates/roteiro.html

H2 Roteiros 1 e 2 2 páginas

H3 Roteiros 3 e 4 2 páginas

H4 Roteiro 5 + roteiros/index 2 páginas



---



⛔ CHECKPOINT 1 👤 (pare aqui)



1. Rode audit_all.py e confirme que nenhum fatal disparou.

2. Execute a revisão humana de 10% das páginas do lote (regra 18). Registre

em reports/revisao-humana-lote1.md.

3. Confirme que nenhuma página pronta tem dado pendente.

4. Publique o site (hospedagem estática gratuita) e confira no celular.

5. Peça o AdSense com hub, serviços, pontos, roteiros e páginas legais.

6. Registre no Search Console e envie o sitemap.

7. Só então siga para o Bloco C.



---



BLOCO C — Linhas de ônibus



ID Faça Saída

C0 Converter o banco em linhas.json com schema e validação. Cada linha:

número, nome, itinerário, paradas, horários, bairros, integrações, fonte.

Dado ausente fica pendente. dados-fonte/linhas.json,

scripts/valida_linhas.py

C1 Template de linha. A IA gera o texto a partir dos dados de cada linha.

Mínimo de 250 palavras próprias por página. Linha sem dados suficientes é

agrupada ou bloqueada. templates/linha.html

C2 Piloto de 3 linhas. Rodar a similaridade em duas passadas. Se algum par

do piloto passar de 30% no texto narrativo, o piloto é refeito antes de

gerar lote. 3 páginas, relatório 👤 revisar

C3 linhas/index, linhas/mapa (Leaflet só aqui), linhas/alteracoes 3 páginas

C4–C15 Lotes 1 a 12, de 10 linhas cada. Similaridade acima de 30% no texto

narrativo bloqueia o lote. Lote bloqueado vai para PENDENCIAS.md com as

linhas afetadas e o motivo. Só refaz após decisão do Leo (reescrever,

agrupar ou dividir). 10 páginas por lote



Observação: tempo-real.html NÃO é criado agora. O data-line-id fica no

template e a seção de tempo real fica comentada.



---



⛔ CHECKPOINT 2 👤



1. Veja o Search Console (indexação, impressões) e o status do AdSense.

2. Rode a revisão humana de 10% das páginas do Bloco C.

3. Decida se segue para o Bloco D (bairros) ou se aprofunda as linhas antes.



---



BLOCO D — Bairros



ID Faça Saída

D1 Template de bairro + dossiês dos 10 bairros (a partir da lista

confirmada pelo Leo em content/lista-mestre.json). templates/bairro.html,

dados-fonte/bairros/*.json

D2 Bairros 1 a 5 5 páginas

D3 Bairros 6 a 10 5 páginas

D4 bairros/index 1 página



---



BLOCO K — Dados e comparativos



(executado antes do Bloco J)



ID Faça Saída

K1 Template de dados (Chart.js, tabela, CSV) + dados/index

templates/dados.html, 1 página

K2 perfil-socioeconomico e demografia 2 páginas + CSV

K3 economia e educacao 2 páginas + CSV

K4 saude e mobilidade 2 páginas + CSV

K5 seguranca-publica e meio-ambiente (fontes oficiais estaduais) 2 páginas

+ CSV

K6 Dossiê de Campinas + comparativo dossiê + 1 página

K7 Dossiê de São José do Rio Preto + comparativo dossiê + 1 página

K8 Dossiê de Sorocaba + comparativo dossiê + 1 página



---



BLOCO J — História



ID Faça Saída

J1 👤 Definir os 5 pilares e escrever content/lista-mestre.json (campo

pilares_historia). A IA não sugere lista. lista-mestre.json

J2 Template de história + dossiês com fontes secundárias

templates/historia.html, dados-fonte/historia/*.json

J3 Pilares 1 e 2 2 páginas

J4 Pilares 3 e 4 2 páginas

J5 Pilar 5 + historia/index 2 páginas



---



BLOCO P — Agenda, Gastronomia, Onde ficar



ID Faça Saída

P1 agenda/index e eventos-anuais. Só entra evento com edição confirmada em

fonte oficial. 2 páginas

P2 gastronomia/index + template. Só estabelecimentos com dado verificado.

1–2 páginas

P3 onde-ficar/index + template. Links de afiliado ficam comentados até o

F4. 1–2 páginas



---



BLOCO M — PWA e offline



ID Faça Saída

M1 manifest.json e ícones manifest.json, assets/img/icons/

M2 service-worker.js com cache só das páginas de linhas e dos assets base.

Versionamento forte: cache identificado por hash do conteúdo

(v2026-10-03-a3f2). Ao subir novo lote, o cache anterior é invalidado

automaticamente. Nunca servir horário de ônibus de versão antiga.

service-worker.js

M3 offline.html 1 página

M4 👤 Testar no Android Chrome e no iOS Safari checklist



---



BLOCO N — Parcerias 👤



ID Faça Saída

N1 A IA prepara um kit para cada interlocutor (Convention Bureau,

Prefeitura, Sebrae-SP, USP, hotéis e restaurantes): resumo de uma página e

modelo de e-mail. O Leo faz o contato. content/parcerias/*.md



---



BLOCO E — Tempo real (preparação)



ID Faça Saída

E1 Documentar a integração futura (campos por data-line-id, fonte dos

dados). Não criar página pública. docs/tempo-real.md



---



BLOCO F — Publicação final



ID Faça Saída

F1 Passada de linkagem: revisar linkagem interna de todas as páginas,

garantir hubs conectados, criar links faltantes conforme

links_planejados[]. arquivos atualizados

F2 Auditoria completa com o mínimo de 5 links internos por página,

relatório de similaridade, relatório de links origem→destino e relatório de

pendências. Antes da auditoria final, revisão humana ampliada: 20% das

páginas revisadas manualmente, com foco em páginas de maior tráfego (linhas

centrais, pontos turísticos). Resultado em

reports/final/revisao-humana-ampliada.md. reports/final/

F3 Sitemaps finais, robots.txt final arquivos finais

F4 👤 Colocar o ID real no ads.txt, ativar GA4 e AdSense, atualizar

privacidade e cookies, ativar links de afiliado, configurar DNS —

F5 👤 PageSpeed (meta 90 ou mais), teste com leitor de tela, WCAG AA, teste

em 3G simulado checklist

F6 Marcar a versão v1.0 no git tag



---



7. Ordem de execução



A1 → A2 → A3 → A4 → A5 → A6 → A7 → A14 → A8 → A9 → A10 → A11 → A12 → A13 →

G → B → H → ⛔ CHECKPOINT 1 → C → ⛔ CHECKPOINT 2 → D → K → J → P → M → N → E

→ F



Notas:



· A14 (teste de auditoria) entra antes de qualquer conteúdo real.

· Bloco K antes de J (comparativos rendem mais backlink que história pura).

· Blocos L (API) e O (idiomas) fora do escopo da v1.0. Só entram após a

v1.0 estar no ar há pelo menos 3 meses, se fizer sentido.

· Bloco N é 👤 e depende do Leo fazer o contato.



---



8. Checklist do Leo antes de rodar A1



☐ Escrever content/lista-mestre.json manualmente com nomes e slugs oficiais

dos 12 pontos, 10 bairros, 6 serviços, 5 roteiros e 5 pilares de história.

☐ Consolidar templates 4.1–4.13 em docs/templates-detalhados.md (opcional —

se não existir, a IA usa a seção 5).

☐ Confirmar ano e lei da Região Metropolitana.

☐ Confirmar no DER-SP qual rodovia é SP-333 e qual é SP-322.

☐ Confirmar quais são os 6 pontos turísticos restantes (além dos 6 com

dossiê pronto).

☐ Criar repositório git remoto privado.

☐ Preencher content/autor.json (bio, foto, formação, experiência).

☐ Criar o e-mail de correção de erros e registrá-lo em content/config.json.

☐ Preencher content/config.json (domínio base, e-mail de contato, e-mail de

correção).

☐ Adicionar logo e favicon em assets/img/.



---



9. Encerramento



Este manual é o contrato entre o Leo e a IA executora. Alterações só por

nova versão numerada.



Versão atual: 1.2

Próxima revisão: após Checkpoint 1.



📦 O Que Teremos ao Final da Execução — Estado v1.0



1. O Repositório (o que existe fisicamente)



```

infohausti-rp/

├── EXECUCAO.md                    ← este manual

├── README.md

├── PENDENCIAS.md                  ← tudo que ficou em aberto

├── LOG.md                         ← histórico de blocos executados

├── content/

│   ├── config.json                ← domínio, e-mails, autor

│   ├── autor.json

│   ├── lista-mestre.json          ← 12 pontos, 10 bairros, 6 serviços, 5

roteiros, 5 pilares

│   ├── status.json                ← estado de cada página

│   ├── correcoes.json             ← erros corrigidos

│   ├── imagens.json               ← licenças de imagem

│   ├── parcerias/                 ← kits do Bloco N

│   ├── dados-fonte/

│   │   ├── rp-perfil.json

│   │   ├── linhas.json            ← 120 linhas com status por campo

│   │   ├── pontos/*.json

│   │   ├── bairros/*.json

│   │   ├── servicos/*.json

│   │   └── historia/*.json

│   └── paginas/                   ← cada página como JSON

├── templates/                     ← base, linha, ponto, roteiro, bairro,

serviço, história, dados, comparativo

├── partials/                      ← cabeçalho, rodapé, breadcrumb,

autoria, fontes, anúncio

├── assets/

│   ├── css/base.css

│   ├── js/base.js

│   └── img/

├── scripts/

│   ├── build.py                   ← gerador

│   ├── valida_linhas.py

│   ├── check_links.py

│   ├── check_seo.py

│   ├── check_schema.py

│   ├── check_a11y.py

│   ├── check_similaridade.py

│   ├── check_pendentes.py

│   ├── check_palavras.py

│   └── audit_all.py

├── reports/                       ← auditorias, revisões humanas

├── docs/tempo-real.md

├── legado/                        ← Theatro e Palacete originais

└── dist/                          ← site publicado (gerado)

```



Tudo versionado em Git. Cada bloco tem commit próprio. Backup off-site em

repositório remoto privado.



---



2. O Site Publicado (~200 páginas)



Páginas por bloco



Bloco Páginas Exemplos

A — Fundação ~15 sobre, equipe, política editorial, privacidade, cookies,

termos, contato, anuncie, imprensa, hub principal, mapa do site, 404

G — Serviços 7 tarifa e cartão, atendimento, telefones úteis, saúde,

escolas, rodovias + hub

B — Turismo 13 Theatro, Palacete, Catedral, Biblioteca, MARP, Curupira,

Bosque, Museu do Café, Praça XV, Quarteirão Paulista + outros + hub

H — Roteiros 6 centro histórico, café, crianças, noturno, 3 dias + hub

C — Linhas de ônibus 123 120 linhas individuais + hub + mapa + alterações

D — Bairros 11 Centro, Higienópolis, Ribeirânia, Alto da Boa Vista + outros

+ hub

K — Dados 12 perfil socioeconômico, demografia, economia, educação, saúde,

mobilidade, segurança, meio-ambiente + 3 comparativos + hub

J — História 6 origem, ciclo do café, imigração, personalidades + 1 + hub

P — Agenda / Gastronomia / Onde Ficar 4–6 agenda mensal, eventos anuais,

gastronomia, hospedagem

M — PWA 1 offline fallback

Raiz 3 robots, ads.txt, sitemap



Total: ~200 páginas.



---



3. O Que o Site Faz (capacidades)



Para o usuário



· Consulta qualquer uma das 120 linhas de ônibus com itinerário, horários e

pontos de interesse no trajeto

· Descobre o que fazer em Ribeirão Preto com história, visitação, como

chegar

· Encontra roteiros temáticos prontos (a pé, de ônibus, para crianças)

· Consulta dados socioeconômicos da cidade com gráficos e CSV para download

· Compara Ribeirão com Campinas, Rio Preto e Sorocaba

· Navega por bairros com perfil, linhas e serviços

· Consulta a agenda cultural atualizada

· Funciona offline parcialmente em páginas de linhas (PWA)



Para o Leo



· Build em Python — gera 200 páginas a partir de JSON em segundos

· Auditoria automática — roda antes de cada commit, classifica fatal/aviso

· Trilha editorial — cada página tem autor, data, fontes, próxima revisão

· Política de correção — erros reportados por e-mail, corrigidos em 72h,

com registro visível

· Versionamento completo — qualquer versão anterior recuperável



Para o Google



· Schema.org em 100% das páginas (TouristAttraction, Article, Dataset,

Place, Event, BusTrip, etc.)

· Sitemap completo e canonical absoluto

· E-E-A-T — autor, fontes, data, política editorial, página de equipe

· Core Web Vitals no verde (LCP < 2,5s, CLS < 0,1, INP < 200ms)

· WCAG 2.1 AA — acessibilidade plena



Para anunciantes



· ~200 páginas com 3 slots AdSense cada (placeholders prontos até o F4)

· Bloco "Anuncie aqui" em todas as páginas

· Media kit em /anuncie.html e /imprensa.html

· Estrutura pronta para venda direta (slots para patrocínio local)

· Schema LocalBusiness nas páginas comerciais



---



4. O Que Está Pronto Para Ativar (F4 — feito por você)



Item Estado até F3 Estado depois de F4

AdSense Placeholder comentado ID real + anúncios ativos

GA4 Placeholder comentado ID real + rastreamento ativo

Links de afiliado Comentados Ativos com rel="sponsored"

Privacidade / Cookies Sem menção a AdSense Atualizadas com AdSense e GA4

ads.txt Só comentário ID real publicado

DNS Preview em infohaus Domínio próprio

Search Console — Verificado + sitemap enviado



---



5. O Que NÃO Está Incluído na v1.0



Por decisão explícita do manual:



· API pública (Bloco L) — adiado para pós-v1.0

· Versões em inglês e espanhol (Bloco O) — adiadas para pós-v1.0

· Ônibus em tempo real (Bloco E) — só documentação, sem página pública

· App na Play Store (Bloco M5) — não fazer agora

· Newsletter e redes sociais — fora do escopo



Esses entram depois, se fizer sentido, quando a v1.0 estiver no ar há pelo

menos 3 meses.



---



6. Os Relatórios Que Ficam no Repositório



Relatório O que contém

reports/teste-auditoria.md Prova que a auditoria funciona (A14)

reports/revisao-humana-lote1.md 10% das páginas do Bloco A/B/G conferidas

por você

reports/revisao-humana-lote2.md 10% das linhas do Bloco C conferidas por

você

reports/final/revisao-humana-ampliada.md 20% de todas as páginas conferidas

por você

reports/final/links-origem-destino.md Teia completa de links internos

reports/final/similaridade.md Nenhuma página acima de 30% no texto narrativo

reports/final/pendencias.md Tudo que ficou em aberto, com motivo



---



7. O Valor Concreto do Que Foi Construído



Como infraestrutura



· Uma base de dados estruturada sobre Ribeirão Preto — 120 linhas, 12

pontos, 10 bairros, 6 serviços, dados socioeconômicos

· Um sistema de build que gera páginas em segundos e mantém padrão em 200

páginas

· Uma auditoria automática que impede publicação de página com link

quebrado, schema ausente ou similaridade alta

· Um repositório versionado que pode ser retomado em qualquer ponto



Como ativo comercial



· Tráfego orgânico previsto: 5.000 sessões/mês aos 3 meses, 30.000 aos 6

meses, 100.000 aos 12

· Base para AdSense: ~200 páginas qualificadas, com aprovação em Checkpoint

1

· Base para venda direta: cada linha, ponto ou bairro é um argumento

comercial para um lojista local

· Base para parcerias: Convenção, Prefeitura, Sebrae, USP — o portal tem

dados e alcance para conversar



Como ativo editorial



· E-E-A-T completo — autor real, política editorial, correções rastreadas

· Conteúdo verificável — cada dado tem fonte oficial citada

· Cobertura completa — mobilidade, patrimônio, território, comércio,

história, dados



---



8. O Que o Portal Será (em uma frase)



Ao final da v1.0, o Infohausti RP será a infraestrutura de informação de

Ribeirão Preto — o portal onde moradores consultam ônibus, turistas

planejam visitas, jornalistas buscam dados, investidores comparam cidades,

e anunciantes procuram espaço. Tudo isso com 200 páginas geradas por

sistema, auditadas automaticamente, e mantidas por um processo editorial

claro.



---



Se quiser, posso agora:



· (a) Escrever um README.md que resume esse estado final (para você colar

no repo e ter visão clara do destino)

· (b) Gerar um diagrama da árvore de arquivos em formato visual (Mermaid)

para colar no README

· (c) Fazer uma projeção de tráfego e receita em 3 cenários (conservador /

realista / otimista) com base nos 200 pages e nas metas

· (d) Escrever o discurso de venda do portal para o momento de pedir

AdSense, parcerias ou anunciantes



Qual te ajuda mais agora?











*INFOHAUS - TI*

*Informática, Impressos e Serviços em Geral*

Leonardo A. Macedo

(16)99157-1314

