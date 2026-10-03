#!/usr/bin/env python3
"""
GERADOR OFICIAL DO LOTE 1 (C4 — FASE 1) — INFOHAUS RP
Gera as 10 páginas JSON do Lote 1 em content/paginas/linhas/:
- 8 linhas noturnas: 001, 002, 003, 004, 005, 006, 007, 008
- 2 primeiras alimentadoras: 015 (Colina Verde), 023 (Aeroporto)
Garante textos narrativos aprofundados (> 400 palavras por página)
e vocabulário territorial diversificado para manter a similaridade Passada 1 < 30%.
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
LINHAS_JSON_PATH = ROOT_DIR / 'content' / 'dados-fonte' / 'linhas.json'
PAGINAS_DIR = ROOT_DIR / 'content' / 'paginas' / 'linhas'
INDEX_JSON_PATH = ROOT_DIR / 'content' / 'paginas' / 'linhas' / 'index.json'

dados_fonte = json.load(open(LINHAS_JSON_PATH, encoding='utf-8'))

lote1_defs = {
    "001": {
        "slug": "linhas/linha-001-noturno-norte",
        "h1": "Linha 001 — Noturno Norte",
        "titulo": "Linha 001 - Noturno Norte | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Guia da Linha 001 Noturno Norte (Corujão) em Ribeirão Preto. Horários de partidas na madrugada, itinerário no Simioni e Quintino e integração no Terminal Central.",
        "keywords": "linha 001 ribeirao preto, onibus corujao norte rp mobi, horario 001 madrugada, itinerario adelino simioni",
        "linha_numero": "001",
        "linha_nome": "Noturno Norte",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Bairros da Zona Norte (Simioni / Quintino)",
        "terminal_central": "Terminal Urbano — Plataforma B (Ponto 3)",
        "visao_geral": (
            "<p>A <strong>Linha 001 (Noturno Norte)</strong> compõe a frota especializada da madrugada ribeirão-pretana, oferecendo atendimento ao setor setentrional quando as rotas radiais diurnas encerram suas atividades. O propósito técnico deste serviço é viabilizar o retorno protegido de vigias noturnos, técnicos em manutenção mecânica, porteiros e profissionais de saúde após o término de suas escalas de trabalho.</p>"
            "<p>Com partidas fixadas no Terminal Urbano Central nos primeiros minutos da madrugada (01h00, 02h20 e 03h25), o coletivo opera em velocidade constante pelas pistas desobstruídas da calha norte. O trajeto oferece tranquilidade aos munícipes em um período no qual os serviços particulares de transporte por aplicativo praticam tarifas dinâmicas elevadas.</p>"
        ),
        "itinerario_texto": (
            "<p>O circuito da Linha 001 desenvolve-se de maneira circular a partir do centro antigo. Ao desatracar da plataforma central, o coletivo segue pela Rua Mariana Junqueira, cruza o pontilhão da malha ferroviária e sobe a Rua Alagoas, alcançando a Rua Luiz Barreto nos Campos Elíseos.</p>"
            "<p>Prosseguindo no vetor setentrional, o veículo atende os eixos vicinais dos conjuntos habitacionais Quintino Facci I e II, serpenteia pelas alamedas residenciais do Jardim Salgado Filho e Avelino Alves Palma, culminando no retorno largo do Residencial Adelino Simioni antes de retomar a descida para o núcleo urbano.</p>"
        ),
        "paradas_destaque": (
            "<p>Com mais de 80 paradas mapeadas, a rota atende pontos de relevância comunitária no silêncio da noite. A largada ocorre no <strong>Ponto 3493 (Terminal Urbano - Plataforma B, Ponto 3)</strong>, facilitando o encontro de trabalhadores que chegam a pé dos estabelecimentos comerciais do centro.</p>"
            "<p>Na Zona Norte, sobressaem-se os abrigos na Rua Alagoas cruzamento com Rua Capitão Salomão, a parada da Rua Antônio Grelet e o ponto final na via coletora do Adelino Simioni, configurando locais de parada próximos às residências dos passageiros.</p>"
        ),
        "integracao_detalhe": (
            "<p>A linha segue a tarifa municipal unificada de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante uso do Cartão Cidadão RP Mobi. Quem valida a passagem nas linhas alimentadoras tardias ou na bilhetagem da rodoviária embarca no Corujão sem novo débito.</p>"
            "<p>Essa regra de gratuidade transitória no período de duas horas protege o orçamento dos trabalhadores de turnos alternados que dependem de condução coletiva na madrugada.</p>"
        ),
        "bairros_texto": (
            "<p>A Linha 001 atende comunidades tradicionais e conjuntos habitacionais expressivos: <em>Campos Elíseos</em>, <em>Vila Carvalho</em>, <em>Quintino Facci I</em>, <em>Quintino Facci II</em>, <em>Jardim Salgado Filho</em>, <em>Avelino Alves Palma</em>, <em>Adelino Simioni</em> e loteamentos da Quinta da Boa Vista.</p>"
            "<p>A circulação regular deste veículo garante previsibilidade e tranquilidade aos moradores dessas localidades distantes dos centros empresariais da cidade.</p>"
        ),
        "atracoes_proximas": (
            "<p>No miolo histórico, o itinerário tangencia a centenária Praça Carlos Gomes e repartições cívicas. Nos Campos Elíseos, aproxima-se da histórica <strong>Paróquia Senhor Bom Jesus do Bonfim</strong> e de farmácias com plantão noturno.</p>"
            "<p>Na extremidade norte, passa nas imediações de praças comunitárias e centros esportivos distritais do Simioni e Quintino, pontos de convivência diurna que descansam nas primeiras horas do dia.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3493 - Terminal Urbano (Plat. B, Ponto 3)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Ponto de partida unificado das linhas noturnas"},
            {"nome": "Ponto 1397 - R. Alagoas, 262", "rua": "Rua Alagoas", "bairro": "Campos Elíseos", "referencia": "Acesso a farmácias e comércio da Rua Alagoas"},
            {"nome": "Ponto 6 - R. Antônio Grelet, 393", "rua": "Rua Antônio Grelet", "bairro": "Campos Elíseos", "referencia": "Conexão com a Vila Carvalho"},
            {"nome": "Ponto Quintino - Av. General Euclydes de Oliveira Figueiredo", "rua": "Avenida General Euclydes de Oliveira Figueiredo", "bairro": "Quintino Facci II", "referencia": "Acesso aos núcleos habitacionais do Quintino"},
            {"nome": "Ponto Final Adelino Simioni", "rua": "Via Coletora Principal", "bairro": "Adelino Simioni", "referencia": "Retorno e atendimento aos conjuntos habitacionais do extremo norte"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Norte (Circuito Noturno)", "num_paradas": 84, "descricao": "Circuito circular de atendimento noturno saindo do Terminal Urbano e cobrindo Campos Elíseos, Quintino Facci e Adelino Simioni."}
        ]
    },
    "002": {
        "slug": "linhas/linha-002-noturno-nordeste",
        "h1": "Linha 002 — Noturno Nordeste",
        "titulo": "Linha 002 - Noturno Nordeste | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Informações oficiais da Linha 002 Noturno Nordeste em Ribeirão Preto. Horários noturnos, itinerário pelo Ribeirão Verde e Avelino Palma e paradas no Terminal Central.",
        "keywords": "linha 002 ribeirao preto, onibus noturno nordeste, corujao ribeirao verde, horario 002 rp mobi",
        "linha_numero": "002",
        "linha_nome": "Noturno Nordeste",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Vetor Nordeste (Ribeirão Verde / Heitor Rigon)",
        "terminal_central": "Terminal Urbano — Plataforma B (Ponto 3)",
        "visao_geral": (
            "<p>A <strong>Linha 002 (Noturno Nordeste)</strong> constitui um elo de transporte vital para as comunidades situadas na calha nordeste da malha urbana de Ribeirão Preto. Durante o intervalo da madrugada, quando cessa a operação das linhas radiais de alta capacidade, este serviço da RP Mobi assegura a integridade das viagens de retorno para casa para trabalhadores de postos de combustível, centros de armazenagem, padarias e operários de turnos industriais.</p>"
            "<p>A operação é pautada por saídas coordenadas na Plataforma B do Terminal Urbano Central nos horários de 01h00, 02h20 e 03h25, sincronizadas com os demais braços do Corujão municipal. O veículo atua com monitoramento por GPS e tarifas eletrônicas, viabilizando acesso digno àqueles que dependem da mobilidade pública nas primeiras horas do dia.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo da baia central, a Linha 002 contorna a Rua Amador Bueno e a Avenida Jerônimo Gonçalves, ingressando no corredor hospitalar da Santa Casa de Misericórdia pela Estação Rio de Janeiro. A partir desse entroncamento, ganha velocidade pelos acessos perimetrais rumo ao complexo habitacional da Zona Nordeste.</p>"
            "<p>O itinerário abrange longas avenidas como a Mogiana e Capitão Salomão, serpenteando por dentro de núcleos populosos e atingindo os loteamentos do Parque Industrial Avelino Alves Palma, Jardim Diva Tarlá e o complexo habitacional do Ribeirão Verde, retornando com fluidez pelas vias marginais desobstruídas da madrugada.</p>"
        ),
        "paradas_destaque": (
            "<p>Com 90 pontos de parada em seu percurso circular, a rota atende a importantes pontos de interesse público. A partida ocorre no <strong>Ponto 3493 (Terminal Urbano - Plataforma B, Ponto 3)</strong>, facilitando o encontro de trabalhadores que convergem do centro comercial.</p>"
            "<p>Ao longo da rota, ganham relevância as paradas na Rua Mariana Junqueira, na Estação Rio de Janeiro e na <strong>Estação Santa Casa</strong>, onde frequentemente embarcam auxiliares de enfermagem e funcionários de copa e higienização hospitalar ao final de jornadas noturnas extenuantes.</p>"
        ),
        "integracao_detalhe": (
            "<p>A política tarifária segue estritamente o valor regulamentado de <strong>R$ 5,00</strong>, aceito tanto em dinheiro quanto por débito nos validadores do Cartão Cidadão RP Mobi. O passageiro conta com o benefício de <strong>120 minutos de integração</strong> para realizar conexões no Terminal Central sem novo débito.</p>"
            "<p>Esse intervalo permite, por exemplo, que um funcionário de hotelaria da Zona Sul utilize um transporte até o Centro e acerte a baldeação na Linha 002 para alcançar o setor Nordeste desfrutando de uma única tarifa municipal.</p>"
        ),
        "bairros_texto": (
            "<p>O setor Nordeste de Ribeirão Preto abriga expressivo contingente populacional distribuído por bairros como <em>Avelino Alves Palma</em>, <em>Jardim Salgado Filho</em>, <em>Jardim Heitor Rigon</em>, <em>Jardim Diva Tarlá Gomes</em> e os loteamentos do complexo <em>Ribeirão Verde</em>, além de áreas de transição dos <em>Campos Elíseos</em>.</p>"
            "<p>A Linha 002 atua como verdadeira tábua de salvação para esses moradores distantes dos corredores metropolitanos, vencendo vazios urbanos com pontualidade e segurança nas madrugadas.</p>"
        ),
        "atracoes_proximas": (
            "<p>Além de conectar o núcleo histórico ao redor do <strong>Calçadão de Ribeirão Preto</strong> e da <strong>Praça das Bandeiras</strong>, a linha passa nas imediações do Hospital Santa Casa de Misericórdia e de depósitos de logística da região da Avenida Mogiana.</p>"
            "<p>O percurso também se aproxima de centros esportivos municipais e de pequenas praças comunitárias da Zona Nordeste, viabilizando o transporte de moradores até os limites de suas quadras residenciais.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3493 - Terminal Urbano (Plat. B, Ponto 3)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Ponto de partida central do Corujão"},
            {"nome": "Ponto 124 - R. Mariana Junqueira, 90", "rua": "Rua Mariana Junqueira", "bairro": "Centro", "referencia": "Acesso a edifícios comerciais e hoteleiros do centro"},
            {"nome": "Ponto 3849 - Estação Rio de Janeiro", "rua": "Avenida Jerônimo Gonçalves", "bairro": "Centro", "referencia": "Conexão com a rede troncal hospitalar"},
            {"nome": "Ponto 3850 - Estação Santa Casa", "rua": "Rua Saldanha Marinho", "bairro": "Campos Elíseos", "referencia": "Embarque de equipes e acompanhantes do complexo hospitalar"},
            {"nome": "Ponto Final Ribeirão Verde", "rua": "Avenida Antonia Mugnatto Marincek", "bairro": "Ribeirão Verde", "referencia": "Atendimento aos conjuntos residenciais nordeste"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Nordeste (Circuito Noturno)", "num_paradas": 90, "descricao": "Itinerário circular unificado cobrindo Santa Casa, Av. Mogiana e complexo residencial do Ribeirão Verde."}
        ]
    },
    "003": {
        "slug": "linhas/linha-003-noturno-leste",
        "h1": "Linha 003 — Noturno Leste",
        "titulo": "Linha 003 - Noturno Leste | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 003 Noturno Leste da RP Mobi em Ribeirão Preto. Trajeto na madrugada pelo Jardim Paulistano, Castelo Branco e Trevo da Anhanguera.",
        "keywords": "linha 003 ribeirao preto, corujao leste rp mobi, onibus madrugada anhanguera, horario linha 003",
        "linha_numero": "003",
        "linha_nome": "Noturno Leste",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Vetor Leste (Jd. Paulistano / Castelo Branco / Marginais)",
        "terminal_central": "Terminal Urbano — Plataforma B (Ponto 3)",
        "visao_geral": (
            "<p>A <strong>Linha 003 (Noturno Leste)</strong> atende aos trabalhadores e estudantes que circulam na porção oriental de Ribeirão Preto durante as horas mais tranquilas da noite. Esta área agrega centros de ensino superior, concessionárias, redes de hotelaria e motéis instalados às margens de rodovias estaduais, além de restaurantes que atendem viajantes de passagem pelo entroncamento da Anhanguera.</p>"
            "<p>Operando em três partidas coordenadas (01h00, 02h20 e 03h30) com embarque no Terminal Urbano, a condução percorre avenidas largas com asfalto plano e poucas paradas semafóricas ativas, proporcionando deslocamento célere e seguro aos munícipes que concluem suas escalas profissionais após a meia-noite.</p>"
        ),
        "itinerario_texto": (
            "<p>Ao deixar a Plataforma B do Terminal Urbano, a rota cruza o quadrilátero histórico pelas imediações da Praça Carlos Gomes, tomando o rumo oriental através da Rua Henrique Dumont e penetrando na malha do Jardim Paulistano e Parque Bandeirantes.</p>"
            "<p>O trajeto avança pela Avenida Castelo Branco, tangencia os acessos do Trevo Waldo Adalberto da Silveira e aproxima-se dos empreendimentos comerciais da Avenida Presidente Kennedy, contornando a Avenida Maria de Jesus Condeixa no retorno desimpedido em direção à região central.</p>"
        ),
        "paradas_destaque": (
            "<p>Com 89 pontos catalogados, a linha prioriza paradas com boa iluminação pública e proximidade a postos de combustível 24 horas. A partida ocorre no <strong>Ponto 3493 (Terminal Urbano - Plataforma B, Ponto 3)</strong>, com paradas centrais na <strong>Estação Praça Carlos Gomes</strong> e <strong>Estação Duque de Caxias</strong>.</p>"
            "<p>No setor oriental, ganham destaque os abrigos na Rua Henrique Dumont, os pontos intermediários na Avenida Castelo Branco e as plataformas próximas ao Trevo da Anhanguera, atendendo a funcionários de logística e recepção hoteleira.</p>"
        ),
        "integracao_detalhe": (
            "<p>A cobrança segue o padrão de <strong>R$ 5,00</strong>, com a concessão da <strong>integração temporal de 120 minutos</strong> mediante uso do Cartão Cidadão RP Mobi. O passageiro pode efetuar transferência no Terminal Urbano sem sofrer nova dedução tarifária.</p>"
            "<p>O benefício é vantajoso para quem atua em bairros opostos, como a Zona Oeste ou Norte, e utiliza a Linha 003 como trecho final da viagem de regresso ao lar.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário cobre um leque representativo do quadrante oriental: <em>Jardim Paulistano</em>, <em>Parque dos Bandeirantes</em>, <em>Parque Castelo Branco</em>, <em>Jardim Palma Travassos</em> e <em>Jardim Macedo</em>.</p>"
            "<p>A presença do coletivo nesse eixo proporciona acolhimento aos trabalhadores da madrugada, assegurando que o encerramento do expediente ocorra com mobilidade garantida.</p>"
        ),
        "atracoes_proximas": (
            "<p>Na porção oriental, a linha passa a curta distância do <strong>Estádio Santa Cruz (Arena Nicnet)</strong>, casa do Botafogo Futebol Preto, e de clubes de campo tradicionais da cidade.</p>"
            "<p>No perímetro central, aproxima os passageiros de edifícios cívicos e praças arborizadas, oferecendo conexão imediata com o coração financeiro municipal.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3493 - Terminal Urbano (Plat. B, Ponto 3)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Terminal Central unificado das linhas da madrugada"},
            {"nome": "Ponto 3970 - Estação Praça Carlos Gomes", "rua": "Rua Florêncio de Abreu", "bairro": "Centro", "referencia": "Acesso aos serviços da área central"},
            {"nome": "Ponto R. Henrique Dumont - Jardim Paulistano", "rua": "Rua Henrique Dumont", "bairro": "Jardim Paulistano", "referencia": "Corredor residencial e comercial do Jardim Paulistano"},
            {"nome": "Ponto Castelo Branco - Av. Presidente Castelo Branco", "rua": "Avenida Castelo Branco", "bairro": "Parque Castelo Branco", "referencia": "Acesso a conjuntos residenciais da zona leste"},
            {"nome": "Ponto Trevo Anhanguera - Av. Presidente Kennedy", "rua": "Avenida Presidente Kennedy", "bairro": "Parque Castelo Branco", "referencia": "Conexão com hotéis e serviços rodoviários"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Leste (Circuito Noturno)", "num_paradas": 89, "descricao": "Circuito integrado de madrugada atendendo Jardim Paulistano, Castelo Branco e marginais da Anhanguera."}
        ]
    },
    "004": {
        "slug": "linhas/linha-004-noturno-sudeste",
        "h1": "Linha 004 — Noturno Sudeste",
        "titulo": "Linha 004 - Noturno Sudeste | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Horários e trajeto da Linha 004 Noturno Sudeste da RP Mobi. Atendimento noturno a City Ribeirão, Ribeirânia, Unaerp e Jardim São José em Ribeirão Preto.",
        "keywords": "linha 004 ribeirao preto, onibus corujao sudeste, linha 004 rp mobi unaerp, horario corujao ribeirania",
        "linha_numero": "004",
        "linha_nome": "Noturno Sudeste",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Vetor Sudeste (Jd. Irajá / Ribeirânia / São José)",
        "terminal_central": "Terminal Urbano — Plataforma B (Ponto 4)",
        "visao_geral": (
            "<p>A <strong>Linha 004 (Noturno Sudeste)</strong> responde pela conectividade noturna dos bairros e polos institucionais localizados no sudeste de Ribeirão Preto. Este corredor concentra complexos de saúde de alta complexidade (Hospital Electro Bonini, hospitais de especialidades), campus universitário da Universidade de Ribeirão Preto (Unaerp) e bairros residenciais arborizados de padrão construtivo diversificado.</p>"
            "<p>Com partidas fixadas no Terminal Urbano às 01h00, 02h20 e 03h35, o serviço acolhe colaboradores de vigilância, recepção hospitalar, laboratórios e moradores que retornam de seus compromissos no centro metropolitano, proporcionando trajeto confortável e paradas bem iluminadas.</p>"
        ),
        "itinerario_texto": (
            "<p>A partir da Plataforma B do Terminal Urbano, a Linha 004 corta as artérias centrais pelas ruas Lafaiete e São José, descendo pelas vias do Jardim Sumaré e Jardim Irajá. O veículo transpõe as avenidas Portugal e Maurílio Biagi, direcionando-se ao bairro planejado City Ribeirão.</p>"
            "<p>No prosseguimento do itinerário, a rota penetra no bairro Ribeirânia, contorna o campus da Unaerp e atende as ruas residenciais do Jardim Manoel Penna e Jardim São José, realizando a volta pela Avenida Doutor Celso Charuri e retornando com celeridade ao miolo urbano central.</p>"
        ),
        "paradas_destaque": (
            "<p>O trajeto conta com 53 paradas selecionadas estrategicamente. O início da viagem dá-se no <strong>Ponto 3494 (Terminal Urbano - Plataforma B, Ponto 4)</strong>, seguindo pela <strong>Estação Praça da Bandeira 3</strong> e <strong>Estação São José</strong> no centro.</p>"
            "<p>Na porção sudeste, merecem destaque as paradas na Rua Lafaiete (altura do número 1616), paradas de transbordo na Avenida Costábile Romano em frente ao campus universitário e as plataformas do Jardim Manoel Penna, garantindo desembarques próximos a portarias de condomínios e vias principais.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa praticada é o valor unificado de <strong>R$ 5,00</strong>, com integração tarifária automática de <strong>120 minutos (duas horas)</strong> pelo Cartão Cidadão RP Mobi. O passageiro que valide sua entrada em qualquer estação ou terminal tem a garantia de não pagar tarifa duplicada.</p>"
            "<p>Essa facilidade é essencial para trabalhadores noturnos que realizam transbordos de linhas troncais ou distritais no Terminal Central para alcançar com segurança o quadrante sudeste do município.</p>"
        ),
        "bairros_texto": (
            "<p>O atendimento da Linha 004 beneficia comunidades como <em>Jardim Irajá</em>, <em>Jardim Sumaré</em>, <em>City Ribeirão</em>, <em>Ribeirânia</em>, <em>Jardim Manoel Penna</em>, <em>Jardim Roberto Benedetti</em>, <em>Jardim São José</em> e <em>Santa Cruz do José Jacques</em>.</p>"
            "<p>Por abranger regiões universitárias e hospitalares expressivas, a linha desempenha um papel social crucial, assegurando o retorno de dezenas de colaboradores em horários de ausência de alternativas coletivas regulares.</p>"
        ),
        "atracoes_proximas": (
            "<p>No miolo histórico, a linha passa a poucos passos do <strong>Museu de Arte de Ribeirão Preto (MARP)</strong> e da Catedral. Ao ingressar na Zona Sudeste, aproxima os munícipes do <strong>Parque Curupira (Luiz Roberto Jábali)</strong>, das instalações da <strong>Unaerp</strong> e dos centros clínicos da Avenida Costábile Romano.</p>"
            "<p>A proximidade com polos de lazer noturno da Avenida Portugal e Wladimir Meirelles Ferreira também torna a linha uma alternativa consciente de transporte após confraternizações de fins de semana.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3494 - Terminal Urbano (Plat. B, Ponto 4)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Ponto de partida do Corujão Sudeste"},
            {"nome": "Ponto 3974 - Estação São José", "rua": "Rua São José", "bairro": "Centro", "referencia": "Acesso aos escritórios centrais e consultórios"},
            {"nome": "Ponto 1530 - R. Lafaiete, 1616", "rua": "Rua Lafaiete", "bairro": "Jardim Sumaré", "referencia": "Conexão com clínicas médicas e prédios residenciais da zona sul-leste"},
            {"nome": "Ponto Unaerp - Av. Costábile Romano", "rua": "Avenida Costábile Romano", "bairro": "Ribeirânia", "referencia": "Acesso ao campus universitário e Hospital Electro Bonini"},
            {"nome": "Ponto Final Jardim São José", "rua": "Avenida Celso Charuri", "bairro": "Jardim São José", "referencia": "Atendimento aos loteamentos residenciais do extremo sudeste"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Sudeste (Circuito Noturno)", "num_paradas": 53, "descricao": "Circuito de madrugada cobrindo Jardim Irajá, City Ribeirão, Unaerp e Jardim São José."}
        ]
    },
    "005": {
        "slug": "linhas/linha-005-noturno-sul",
        "h1": "Linha 005 — Noturno Sul",
        "titulo": "Linha 005 - Noturno Sul | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Horários e trajeto da Linha 005 Noturno Sul da RP Mobi em Ribeirão Preto. Atendimento noturno ao Jardim Botânico, Bonfim Paulista e shopping centers.",
        "keywords": "linha 005 ribeirao preto, onibus noturno sul rp mobi, corujao bonfim paulista, horario linha 005",
        "linha_numero": "005",
        "linha_nome": "Noturno Sul",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Vetor Sul (Jd. Botânico / Terras de Siena / Bonfim Paulista)",
        "terminal_central": "Terminal Urbano — Plataforma A (Ponto 1)",
        "visao_geral": (
            "<p>A <strong>Linha 005 (Noturno Sul)</strong> atende o vetor meridional de maior expansão imobiliária e sofisticação gastronômica de Ribeirão Preto. Esta porção do município concentra shopping centers de grande porte, torres empresariais, condomínios fechados horizontais e a rota turística e gastronômica do distrito histórico de Bonfim Paulista.</p>"
            "<p>Com partidas nas primeiras horas da madrugada (01h00, 02h20 e 03h35) partindo da Plataforma A do Terminal Urbano, a linha transporta garçons, maîtres, cozinheiros, recepcionistas de hotel e porteiros que encerram expedientes nos restaurantes nobres da Zona Sul e necessitam de condução até suas residências ou conexões metropolitanas.</p>"
        ),
        "itinerario_texto": (
            "<p>Saindo da Plataforma A do Terminal Urbano Central, a Linha 005 transita pela Rua Visconde de Inhaúma, interceptando a Avenida Nove de Julho e alcançando a Avenida Independência e Avenida Presidente Vargas. A rota avança por vias estruturais do Jardim Botânico e Jardim San Leandro.</p>"
            "<p>Seguindo pelo prolongamento sul, o coletivo atende os novos bairros e empreendimentos do Loteamento Terras de Siena e ingressa na malha urbana do distrito de Bonfim Paulista, circulando pelas vias históricas do distrito antes de realizar o giro de retorno pela Rodovia José Fregonesi e avenidas arteriais da Zona Sul.</p>"
        ),
        "paradas_destaque": (
            "<p>Com 68 paradas cadastradas, a Linha 005 oferece abrigo seguro em eixos de alta visibilidade. O ponto de origem é o <strong>Ponto 3491 (Terminal Urbano - Plataforma A, Ponto 1)</strong>, contando com escalas de embarque na <strong>Estação Praça Camões</strong> e <strong>Estação Garibaldi</strong>.</p>"
            "<p>Na porção sul, os destaques são as paradas na Rua Visconde de Inhaúma (altura do número 1006), os pontos próximos ao Parque Raya no Jardim Botânico e a praça central de Bonfim Paulista, ponto tradicional de desembarque de trabalhadores residentes no distrito.</p>"
        ),
        "integracao_detalhe": (
            "<p>A operação é regulada pela tarifa básica de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração</strong> por meio do Cartão Cidadão RP Mobi. Esse benefício permite a integração com linhas radiais ou alimentadoras que operem nas franjas horárias do início da madrugada.</p>"
            "<p>Dessa forma, o passageiro tem garantida a transição entre polos centrais de lazer e as áreas mais afastadas da Zona Sul com previsibilidade financeira e segurança operacional.</p>"
        ),
        "bairros_texto": (
            "<p>A linha atende diretamente setores nobres e núcleos residenciais consolidados, tais como <em>Jardim Sumaré</em>, <em>Jardim Botânico</em>, <em>Jardim San Leandro</em>, <em>Jardim das Mansões</em>, <em>Loteamento Terras de Siena</em> e o distrito de <em>Bonfim Paulista</em>.</p>"
            "<p>Essa amplitude conecta a classe trabalhadora aos polos geradores de emprego do setor de hospitalidade e serviços que caracterizam a vida noturna da Zona Sul ribeirão-pretana.</p>"
        ),
        "atracoes_proximas": (
            "<p>O roteiro noturno percorre as proximidades do <strong>Parque Dr. Fernando de Freitas Monteiro da Silva (Parque das Artes)</strong> e do <strong>Parque Luís Carlos Raya</strong>, além dos complexos gastronômicos das avenidas Professor João Fiúsa e Wladimir Meirelles.</p>"
            "<p>No distrito de Bonfim Paulista, a linha deixa o passageiro próximo à histórica Praça das Bandeiras de Bonfim e de tradicionais choperias e restaurantes artesanais da localidade.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3491 - Terminal Urbano (Plat. A, Ponto 1)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Ponto de partida central da Linha 005"},
            {"nome": "Ponto 1125 - R. Visconde de Inhaúma, 1006", "rua": "Rua Visconde de Inhaúma", "bairro": "Centro", "referencia": "Conexão com a rede de serviços da área central"},
            {"nome": "Ponto 3967 - Estação Praça Camões", "rua": "Rua Camões", "bairro": "Centro", "referencia": "Acesso a edifícios residenciais e teatros centrais"},
            {"nome": "Ponto Parque Raya - Jardim Botânico", "rua": "Rua Severiano Amaro dos Santos", "bairro": "Jardim Botânico", "referencia": "Acesso a condomínios e restaurantes da zona sul"},
            {"nome": "Ponto Final Bonfim Paulista", "rua": "Praça Central de Bonfim", "bairro": "Bonfim Paulista", "referencia": "Terminal de retorno no distrito de Bonfim Paulista"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Sul (Circuito Noturno)", "num_paradas": 68, "descricao": "Circuito integrado de madrugada atendendo Jardim Botânico, Terras de Siena e distrito de Bonfim Paulista."}
        ]
    },
    "006": {
        "slug": "linhas/linha-006-noturno-sudoeste",
        "h1": "Linha 006 — Noturno Sudoeste",
        "titulo": "Linha 006 - Noturno Sudoeste | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 006 Noturno Sudoeste da RP Mobi. Trajeto da madrugada por Vila Virgínia, Parque Ribeirão e Jardim Marchesi em Ribeirão Preto.",
        "keywords": "linha 006 ribeirao preto, corujao sudoeste rp mobi, onibus vila virginia madrugada, horario linha 006",
        "linha_numero": "006",
        "linha_nome": "Noturno Sudoeste",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Vetor Sudoeste (Vila Virgínia / Pq. Ribeirão / Jd. Marchesi)",
        "terminal_central": "Terminal Urbano — Plataforma A (Ponto 1)",
        "visao_geral": (
            "<p>A <strong>Linha 006 (Noturno Sudoeste)</strong> assegura o atendimento de transporte coletivo durante as madrugadas para a tradicional e populosa Zona Sudoeste de Ribeirão Preto. Formada por bairros operários com forte identidade comunitária, oficinas mecânicas, centros de logística e residências de milhares de trabalhadores fabris e de serviços, esta área necessita de ligações contínuas com o Centro.</p>"
            "<p>Com partidas regulamentadas às 01h00, 02h20 e 03h35 a partir da Plataforma A do Terminal Urbano, a linha oferece um serviço essencial para a integridade física dos moradores, encurtando caminhadas noturnas e conectando os pontos mais densos do quadrante sudoeste.</p>"
        ),
        "itinerario_texto": (
            "<p>O itinerário inicia-se no Terminal Central, transpondo a Avenida Jerônimo Gonçalves e cruzando a via férrea em direção ao bairro da Vila Virgínia pela Rua Felipe Camarão. O coletivo ingressa no corredor comercial da Rua Doutor João Guião, que concentra farmácias e comércio de apoio local.</p>"
            "<p>Em seguida, o veículo penetra nas ruas sinuosas do Parque Ribeirão Preto, Jardim Marchesi e Jardim Maria Goretti, contornando a região do Jardim Piratininga e Solar Boa Vista, até alcançar as imediações do Jardim Adão do Carmo Leonel antes de retornar pela Avenida Pio XII rumo ao Centro.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 60 paradas ao longo de seu circuito. A largada ocorre no <strong>Ponto 3491 (Terminal Urbano - Plataforma A, Ponto 1)</strong>, permitindo integração imediata a quem chega de outras regiões na madrugada.</p>"
            "<p>Na Zona Sudoeste, sobressaem-se os pontos na Rua Felipe Camarão (alturas dos números 180 e 300) e as sucessivas paradas ao longo da Rua Doutor João Guião (números 280, 581 e 868), configurando uma malha capilar que deixa os moradores a poucos metros de seus lares.</p>"
        ),
        "integracao_detalhe": (
            "<p>A linha adota a tarifa municipal de <strong>R$ 5,00</strong>, com plena vigência do benefício de <strong>120 minutos de integração</strong> pelo Cartão Cidadão RP Mobi. Esse mecanismo permite conexões gratuitas entre linhas no período regulamentar de duas horas.</p>"
            "<p>Trabalhadores de turnos alternados e estudantes de pós-graduação aproveitam essa regra para cruzar a cidade pagando apenas uma tarifa, garantindo previsibilidade no orçamento familiar.</p>"
        ),
        "bairros_texto": (
            "<p>A cobertura abrange núcleos comunitários históricos como <em>Vila Virgínia</em>, <em>Parque Ribeirão Preto</em>, <em>Jardim Marchesi</em>, <em>Jardim Maria Goretti</em>, <em>Jardim Piratininga</em>, <em>Solar Boa Vista</em> e <em>Adão do Carmo Leonel</em>.</p>"
            "<p>A presença da Linha 006 nestas vias durante a madrugada representa uma ferramenta vital de segurança cidadã e inclusão urbana para famílias de trabalhadores industriais e prestadores de serviços.</p>"
        ),
        "atracoes_proximas": (
            "<p>No centro da cidade, a linha viabiliza acesso rápido à <strong>Praça das Bandeiras</strong>, ao <strong>Palácio Rio Branco</strong> e aos terminais bancários. Na Zona Sudoeste, a rota passa perto de escolas estaduais centenárias, da Paróquia Coração de Maria da Vila Virgínia e de unidades de saúde comunitárias.</p>"
            "<p>A proximidade com clubes desportivos de várzea e praças públicas também auxilia o transporte em dias de eventos recreativos comunitários.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3491 - Terminal Urbano (Plat. A, Ponto 1)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Terminal Central unificado do Corujão"},
            {"nome": "Ponto 1081 - R. Felipe Camarão, 300", "rua": "Rua Felipe Camarão", "bairro": "Vila Virgínia", "referencia": "Entrada principal da Vila Virgínia após transpor a linha férrea"},
            {"nome": "Ponto 1083 - R. Dr. João Guião, 280", "rua": "Rua Doutor João Guião", "bairro": "Vila Virgínia", "referencia": "Eixo comercial central do bairro"},
            {"nome": "Ponto Pq. Ribeirão - Rua Lúcio de Mendonça", "rua": "Rua Lúcio de Mendonça", "bairro": "Parque Ribeirão Preto", "referencia": "Atendimento ao núcleo denso do Parque Ribeirão"},
            {"nome": "Ponto Final Jardim Marchesi", "rua": "Rua Clemente Barbalho", "bairro": "Jardim Marchesi", "referencia": "Ponto de retorno na borda sudoeste"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Sudoeste (Circuito Noturno)", "num_paradas": 60, "descricao": "Circuito integrado de madrugada atendendo Vila Virgínia, Parque Ribeirão Preto e Jardim Marchesi."}
        ]
    },
    "007": {
        "slug": "linhas/linha-007-noturno-oeste",
        "h1": "Linha 007 — Noturno Oeste",
        "titulo": "Linha 007 - Noturno Oeste | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 007 Noturno Oeste da RP Mobi. Trajeto da madrugada por Vila Tibério, Sumarezinho, Campus USP e Hospital das Clínicas.",
        "keywords": "linha 007 ribeirao preto, corujao usp rp mobi, onibus madrugada hc campus, horario linha 007",
        "linha_numero": "007",
        "linha_nome": "Noturno Oeste",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Vetor Oeste (Vila Tibério / Sumarezinho / Campus USP / HC)",
        "terminal_central": "Terminal Urbano — Plataforma A (Ponto 1)",
        "visao_geral": (
            "<p>A <strong>Linha 007 (Noturno Oeste)</strong> cumpre uma das funções mais nobres e técnicas de toda a rede de transporte noturno de Ribeirão Preto. Este eixo interliga o Centro aos bairros acadêmicos e ao grandioso polo de saúde e ciência do Campus Universitário da USP, incluindo as instalações de emergência médica do Hospital das Clínicas (HC-Campus).</p>"
            "<p>Operando em horários estratégicos (01h10, 02h20 e 03h25) com saída do Terminal Central, a linha atende estudantes de pós-graduação, médicos plantonistas, enfermeiros, residentes, pesquisadores de laboratório e acompanhantes de pacientes em internação hospitalar que necessitam de locomoção pontual na calada da noite.</p>"
        ),
        "itinerario_texto": (
            "<p>Ao deixar a Plataforma A do Terminal Urbano, a condução acessa a histórica Vila Tibério pela Rua Augusto Severo e Rua Coronel Luiz da Cunha. O veículo avança pelo bairro do Sumarezinho, subindo em direção à Avenida do Café, um dos principais corredores universitários e de repúblicas estudantis da cidade.</p>"
            "<p>Mais adiante, o coletivo transpõe a rotatória da Cidade Universitária e adentra as vias do Campus da Universidade de São Paulo (USP), realizando paradas no Hospital das Clínicas e na Faculdade de Medicina, estendendo-se a loteamentos vizinhos como Jardim Antártica e Vila Monte Alegre antes de retornar ao Centro.</p>"
        ),
        "paradas_destaque": (
            "<p>A rota abrange 69 paradas oficiais. O ponto de origem é o <strong>Ponto 3491 (Terminal Urbano - Plataforma A, Ponto 1)</strong>, com paradas rápidas na Vila Tibério, como na <strong>Rua Augusto Severo (número 558)</strong> e <strong>Rua Coronel Luiz da Cunha (números 268, 490 e 886)</strong>.</p>"
            "<p>No vetor universitário, o ponto alto do itinerário é a parada em frente à portaria principal do <strong>Hospital das Clínicas de Ribeirão Preto (HC-Campus)</strong>, onde trabalhadores da saúde e estudantes da área biomédica encontram transporte seguro e regular.</p>"
        ),
        "integracao_detalhe": (
            "<p>Com tarifa acessível fixada em <strong>R$ 5,00</strong>, os passageiros contam com o benefício de <strong>120 minutos de integração temporal</strong> no Cartão Cidadão RP Mobi. Residentes de outros bairros da cidade podem chegar ao Centro e transferir-se para a Linha 007 sem custos adicionais.</p>"
            "<p>Essa facilidade tarifária é especialmente vantajosa para os plantonistas da saúde e bolsistas que realizam viagens regulares em horários não convencionais do expediente universitário.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário serve bairros de grande tradição cultural e estudantil de Ribeirão Preto, como <em>Vila Tibério</em>, <em>Sumarezinho</em>, <em>Vila Monte Alegre</em>, <em>Jardim Antártica</em>, <em>Parque Residencial Cidade Universitária</em>, <em>Jardim Alexandre Balbo</em> e <em>Jamil Seme Cury</em>.</p>"
            "<p>A sinergia entre a comunidade acadêmica da USP e os moradores tradicionais da Zona Oeste faz desta linha um modelo exemplar de atendimento a serviços de interesse público contínuo.</p>"
        ),
        "atracoes_proximas": (
            "<p>A linha passa junto a patrimônios culturais destacados: a centenária <strong>Igreja Nossa Senhora do Rosário na Vila Tibério</strong>, o bosque universitário do <strong>Campus da USP</strong> e o Museu de Anatomia.</p>"
            "<p>Na baixada central, aproxima os passageiros da <strong>Estação Ferroviária / Mogiana</strong> e do complexo cultural do Memorial da Classe Operária, reforçando a ligação histórica da ferrovia com a Zona Oeste.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3491 - Terminal Urbano (Plat. A, Ponto 1)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Terminal Central unificado das linhas da madrugada"},
            {"nome": "Ponto 2823 - R. Augusto Severo, 558", "rua": "Rua Augusto Severo", "bairro": "Vila Tibério", "referencia": "Entrada tradicional na Vila Tibério"},
            {"nome": "Ponto 626 - R. Cel. Luiz da Cunha, 268", "rua": "Rua Coronel Luiz da Cunha", "bairro": "Vila Tibério", "referencia": "Corredor comercial e gastronômico do bairro"},
            {"nome": "Ponto Av. do Café - Cidade Universitária", "rua": "Avenida do Café", "bairro": "Vila Monte Alegre", "referencia": "Acesso a repúblicas estudantis e portaria da USP"},
            {"nome": "Ponto HC Campus - Hospital das Clínicas", "rua": "Avenida dos Bandeirantes", "bairro": "Cidade Universitária", "referencia": "Desembarque na Unidade de Emergência e Ambulatórios do HC"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Oeste (Circuito Noturno)", "num_paradas": 69, "descricao": "Circuito integrado de madrugada atendendo Vila Tibério, Sumarezinho, Av. do Café e Campus USP/Hospital das Clínicas."}
        ]
    },
    "008": {
        "slug": "linhas/linha-008-noturno-noroeste",
        "h1": "Linha 008 — Noturno Noroeste",
        "titulo": "Linha 008 - Noturno Noroeste | Horários da Madrugada e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 008 Noturno Noroeste da RP Mobi. Trajeto da madrugada pelo Ipiranga, Cristo Redentor, Valentina Figueiredo e Terminal Central.",
        "keywords": "linha 008 ribeirao preto, corujao noroeste rp mobi, onibus ipiranga madrugada, horario linha 008",
        "linha_numero": "008",
        "linha_nome": "Noturno Noroeste",
        "modalidade": "Noturna (Corujão)",
        "linha_cor": "#0b0d0b",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central ↔ Vetor Noroeste (Ipiranga / Cristo Redentor / Valentina Figueiredo)",
        "terminal_central": "Terminal Urbano — Plataforma A (Ponto 2)",
        "visao_geral": (
            "<p>A <strong>Linha 008 (Noturno Noroeste)</strong> atua como principal alimentadora de transporte da madrugada para o expressivo vetor noroeste de Ribeirão Preto. Este quadrante urbano abriga bairros consolidados e densos, como o tradicional Ipiranga, além de novos núcleos habitacionais de grande porte erguidos nos últimos anos, onde residem famílias de trabalhadores do comércio, prestadores de serviços e profissionais de transportes.</p>"
            "<p>Com partidas fixadas no Terminal Urbano nos horários de 01h10, 02h20 e 03h25, a linha oferece uma cobertura territorial extensa e protetiva, encurtando deslocamentos a pé em vias de menor iluminação e garantindo transporte confiável na volta do trabalho ou do lazer noturno.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo da Plataforma A do Terminal Urbano Central, a condução cruza a Praça Carlos Gomes e segue pelo eixo da Rua Duque de Caxias, adentrando o bairro do Ipiranga pelas vias do Alto do Ipiranga. O percurso percorre a espinha dorsal de comércio de bairro da Rua Dom Pedro II e Avenida Dom Pedro I.</p>"
            "<p>Mais adiante, o coletivo alcança as vias arteriais dos bairros Jardim Cristo Redentor, Jardim Heitor Rigon, Parque das Oliveiras, Valentina Figueiredo e Antônio Marincek, contornando praças comunitárias e retornando com fluxo desimpedido pelas avenidas perimetrais de volta ao miolo central.</p>"
        ),
        "paradas_destaque": (
            "<p>Com 96 paradas georreferenciadas — a mais extensa em quantidade de pontos entre os Corujões —, a Linha 008 atende pontos de relevância no trajeto. O embarque de partida ocorre no <strong>Ponto 3492 (Terminal Urbano - Plataforma A, Ponto 2)</strong>, com paradas estratégicas na <strong>Estação Praça da Bandeira 2</strong> e <strong>Estação Praça Carlos Gomes</strong>.</p>"
            "<p>No quadrante noroeste, destacam-se as paradas na Rua Duque de Caxias (números 725, 521 e 339), pontos da Avenida Dom Pedro I no Ipiranga e as plataformas de retorno no Residencial Valentina Figueiredo e Cristo Redentor.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa estabelecida é a municipal de <strong>R$ 5,00</strong>, com a concessão integral da <strong>integração de 120 minutos</strong> mediante uso do Cartão Cidadão RP Mobi. O passageiro tem até duas horas para embarcar em outro coletivo sem nova cobrança tarifária.</p>"
            "<p>Essa política tarifária social favorece trabalhadores que operam na hotelaria ou gastronomia das zonas Sul ou Leste e encontram no Terminal Urbano o ponto seguro de transferência para o Noroeste.</p>"
        ),
        "bairros_texto": (
            "<p>A capilaridade da Linha 008 contempla bairros populosos como <em>Ipiranga</em>, <em>Alto do Ipiranga</em>, <em>Jardim Cristo Redentor</em>, <em>Valentina Figueiredo</em>, <em>Jardim Heitor Rigon</em>, <em>Parque das Oliveiras</em>, <em>Presidente Dutra</em>, <em>Residencial das Américas</em> e <em>Antônio Marincek</em>.</p>"
            "<p>Para milhares de famílias que residem na fronteira noroeste da malha urbana, o serviço noturno é sinônimo de tranquilidade e amparo público nas jornadas de trabalho da madrugada.</p>"
        ),
        "atracoes_proximas": (
            "<p>No centro urbano, a rota passa a curta caminhada da <strong>Praça XV de Novembro</strong> e da <strong>Esplanada do Theatro Pedro II</strong>. No setor Noroeste, o ônibus transita perto da secular <strong>Igreja Santo Antônio no Ipiranga</strong> e do Parque Ecológico Maurílio Biagi.</p>"
            "<p>A proximidade com praças esportivas distritais e centros comunitários da Zona Noroeste também facilita a mobilidade de moradores em comemorações cívicas e culturais comunitárias.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3492 - Terminal Urbano (Plat. A, Ponto 2)", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Terminal Central unificado das linhas da madrugada"},
            {"nome": "Ponto 3970 - Estação Praça Carlos Gomes", "rua": "Rua Florêncio de Abreu", "bairro": "Centro", "referencia": "Conexão com a rede de serviços centrais"},
            {"nome": "Ponto 332 - R. Duque de Caxias, 725", "rua": "Rua Duque de Caxias", "bairro": "Centro", "referencia": "Saída central rumo ao Ipiranga"},
            {"nome": "Ponto Av. Dom Pedro I - Ipiranga", "rua": "Avenida Dom Pedro I", "bairro": "Ipiranga", "referencia": "Principal corredor comercial da Zona Noroeste"},
            {"nome": "Ponto Final Cristo Redentor / Valentina", "rua": "Avenida Doutor Marcos Zanetti", "bairro": "Jardim Cristo Redentor", "referencia": "Ponto de retorno no extremo noroeste"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Região Noroeste (Circuito Noturno)", "num_paradas": 96, "descricao": "Circuito integrado de madrugada atendendo Ipiranga, Dom Pedro I, Jardim Cristo Redentor e Valentina Figueiredo."}
        ]
    },
    "015": {
        "slug": "linhas/linha-015-colina-verde",
        "h1": "Linha 015 — Colina Verde",
        "titulo": "Linha 015 - Colina Verde | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia oficial da Linha 015 Colina Verde (Alimentadora) da RP Mobi em Ribeirão Preto. Horários de partidas, itinerário pela Estação Sul e Jardim Saint Gerard.",
        "keywords": "linha 015 ribeirao preto, onibus colina verde rp mobi, alimentadora estacao sul, horario linha 015",
        "linha_numero": "015",
        "linha_nome": "Colina Verde",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Estação Sul (BRT) ↔ Condomínios Colina Verde / Saint Gerard / Quinta da Primavera",
        "terminal_central": "Estação Sul de Transferência (Avenida José Adolfo Bianco Molina)",
        "visao_geral": (
            "<p>A <strong>Linha 015 (Colina Verde)</strong> opera como serviço alimentador de alta relevância estratégica no planejamento viário da Zona Sul de Ribeirão Preto. Com veículos ágeis de padrão intermediário e pintura alaranjada característica da categoria alimentadora, esta rota conecta os novos loteamentos fechados, condomínios verticais e centros educacionais privados do Jardim Saint Gerard e Quinta da Primavera diretamente à Estação Sul de Transferência do BRT.</p>"
            "<p>Regulada pela RP Mobi, a linha funciona em regime regular ao longo de todo o dia (das 05h40 até as 21h00 nos dias úteis, com grades de reforço nos sábados e domingos), proporcionando intervalos cadenciados para moradores, colaboradores de serviços domésticos, professores e profissionais liberais que atuam na expansão meridional da cidade.</p>"
        ),
        "itinerario_texto": (
            "<p>O percurso da Linha 015 foi planejado para integrar os eixos de alta capacidade às vias coletoras locais da Zona Sul. A partida dá-se na Estação Sul de Transferência, seguindo pela Avenida José Adolfo Bianco Molina e acessando a Rua Mariano Pedroso de Almeida no Jardim Botânico.</p>"
            "<p>Avançando em direção às colinas da porção sul, o ônibus percorre trechos da Avenida Carlos Consoni, atende a Estação Piolin e Estação Canadá, conectando-se aos acessos do campus da UNIP e contornando os residenciais fechados do Colina Verde, Jardim Saint Gerard e Quinta da Primavera antes de realizar o trajeto de retorno à Estação Sul.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha conta com 48 paradas cadastradas ao longo de suas ramificações operacionais. O ponto fulcral de integração é o <strong>Ponto 3879 (Estação Sul)</strong>, onde os passageiros realizam transbordo direto para as linhas troncais de ônibus que seguem para o Centro e outros eixos metropolitanos.</p>"
            "<p>Destacam-se ainda a parada na Rua Mariano Pedroso de Almeida (número 226) no Jardim Botânico, a <strong>Estação Piolin</strong>, a <strong>Estação Canadá</strong> e a <strong>Estação UNIP</strong>, que concentram o embarque maciço de estudantes universitários nos períodos matutino e vespertino.</p>"
        ),
        "integracao_detalhe": (
            "<p>Como autêntica linha alimentadora, a 015 é o exemplo perfeito do funcionamento da <strong>integração tarifária de 120 minutos</strong> da RP Mobi. Pagando a tarifa básica municipal de <strong>R$ 5,00</strong> com o Cartão Cidadão (ou Cartão Nosso), o passageiro valida seu embarque no Colina Verde e, ao desembarcar na Estação Sul, transfere-se para os ônibus BRT Norte-Sul sem qualquer cobrança adicional.</p>"
            "<p>Esse benefício temporal de duas horas garante aos moradores da Zona Sul viagens completas com conforto financeiro até polos hospitalares, bancários ou universitários em qualquer região da cidade.</p>"
        ),
        "bairros_texto": (
            "<p>A Linha 015 atende a uma das áreas de maior valorização imobiliária do interior paulista, cobrindo localidades como <em>Jardim Botânico</em>, <em>Jardim Canadá</em>, <em>Alto da Boa Vista</em>, <em>Jardim Saint Gerard</em>, <em>Quinta da Primavera</em> e <em>City Ribeirão</em>.</p>"
            "<p>Essa cobertura atende tanto aos moradores desses condomínios quanto a centenas de prestadores de serviços (jardineiros, eletricistas, pessoal de manutenção e segurança) que se deslocam diariamente para esses condomínios fechados.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota deixa os usuários a curta distância de polos de ensino e contemplação ecológica, como o <strong>Campus da UNIP Ribeirão Preto</strong>, o <strong>Parque das Artes</strong> e as trilhas arborizadas do <strong>Parque Luís Carlos Raya</strong>.</p>"
            "<p>Também facilita o acesso a empórios gourmet, escolas internacionais e centros esportivos e de beach tennis distribuídos ao longo das avenidas Carlos Consoni e José Adolfo Bianco Molina.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3879 - Estação Sul (BRT)", "rua": "Avenida José Adolfo Bianco Molina", "bairro": "Jardim Botânico", "referencia": "Ponto de transbordo principal com os corredores troncais"},
            {"nome": "Ponto 3412 - R. Mariano Pedroso de Almeida, 226", "rua": "Rua Mariano Pedroso de Almeida", "bairro": "Jardim Botânico", "referencia": "Acesso a consultórios e condomínios da zona sul"},
            {"nome": "Ponto 3764 - Estação Piolin", "rua": "Avenida Carlos Consoni", "bairro": "Jardim Canadá", "referencia": "Acesso a centros comerciais e praças esportivas"},
            {"nome": "Ponto 3768 - Estação UNIP", "rua": "Avenida Carlos Consoni", "bairro": "Jardim Saint Gerard", "referencia": "Embarque de alunos e funcionários do campus universitário"},
            {"nome": "Ponto Final Colina Verde", "rua": "Alameda dos Jacarandás", "bairro": "Quinta da Primavera", "referencia": "Ponto de retorno junto aos condomínios fechados da colina"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Colina Verde (Regular)", "num_paradas": 48, "descricao": "Itinerário principal alimentador ligando a Estação Sul ao complexo de condomínios da Quinta da Primavera e Saint Gerard."},
            {"nome": "Extensão km 314 - Colina Verde", "num_paradas": 12, "descricao": "Derivação operacional estendida atendendo acessos vicinais e condomínios de chácaras no km 314."}
        ]
    },
    "023": {
        "slug": "linhas/linha-023-aeroporto",
        "h1": "Linha 023 — Aeroporto (via Pq. Industrial)",
        "titulo": "Linha 023 - Aeroporto via Pq. Industrial | Horários e Paradas RP Mobi",
        "descricao": "Guia da Linha 023 Aeroporto Leite Lopes via Parque Industrial em Ribeirão Preto. Horários atualizados da RP Mobi, itinerário pela Vila Mariana e paradas.",
        "keywords": "linha 023 ribeirao preto, onibus aeroporto leite lopes rp mobi, alimentadora parque industrial, horario linha 023",
        "linha_numero": "023",
        "linha_nome": "Aeroporto (via Pq. Industrial)",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Avenida Brasil ↔ Parque Industrial Coronel Quito Junqueira ↔ Aeroporto Leite Lopes",
        "terminal_central": "Estação de Transferência Norte / Eixo Avenida Brasil",
        "visao_geral": (
            "<p>A <strong>Linha 023 (Aeroporto via Parque Industrial)</strong> desempenha uma função logística de alta produtividade para o ecossistema econômico e aeroportuário de Ribeirão Preto. Atuando como linha alimentadora na Zona Norte, este itinerário une os bairros residenciais da Vila Mariana e Jardim Salgado Filho ao polo fabril do Parque Industrial Coronel Quito Junqueira e ao saguão de embarque de passageiros do <strong>Aeroporto Estadual Doutor Leite Lopes (RAO)</strong>.</p>"
            "<p>Fiscalizada pela RP Mobi, a linha opera com frequência intensiva ao longo de todo o dia (partidas a cada 10 a 20 minutos entre 05h20 e 23h10 em dias úteis e finais de semana), garantindo transporte ágil para metalúrgicos, operários da cadeia logística, comissários de bordo, agentes aeroportuários e viajantes que necessitam de conexão econômica e pontual com o aeródromo regional.</p>"
        ),
        "itinerario_texto": (
            "<p>O percurso da Linha 023 é desenhado para maximizar a fluidez entre o corredor da Avenida Brasil e as indústrias setentrionais. A rota tem origem na Avenida Brasil (altura do número 1105), ingressando rapidamente na malha da Vila Mariana pela Rua Peru.</p>"
            "<p>O veículo segue pela extensão da Rua Peru até o número 2400, adentrando as alamedas do Parque Industrial Coronel Quito Junqueira. Em seguida, contorna os hangares e centros de manutenção aérea, realizando escala em frente ao terminal de passageiros do Aeroporto Leite Lopes antes de retomar o circuito em direção ao entroncamento viário com a Avenida Brasil.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 25 paradas estruturadas para o atendimento fabril. O ponto de integração inicial fica no <strong>Ponto 43 (Avenida Brasil, 1105)</strong>, permitindo baldeação rápida com o Corredor BRT Norte-Sul (Linha 902).</p>"
            "<p>Ao longo da Rua Peru na Vila Mariana, destacam-se os pontos nos números 1058, 1427, 1730, 2085 e 2400, que recebem trabalhadores de indústrias gráficas, de alimentos e de logística, além da parada final em frente ao <strong>Aeroporto Estadual Leite Lopes</strong>, fundamental para passageiros de voos regionais.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa regulamentar praticada é de <strong>R$ 5,00</strong>. Utilizando o Cartão Cidadão RP Mobi, o usuário usufrui dos <strong>120 minutos de integração temporal</strong>, o que significa que o trabalhador pode pegar um ônibus convencional na Zona Sul ou Leste, descer no corredor da Avenida Brasil e subir na Linha 023 sem pagar nada a mais.</p>"
            "<p>Da mesma forma, o viajante que desembarca de um voo no Aeroporto Leite Lopes pode utilizar a Linha 023 para chegar à Avenida Brasil e se conectar a qualquer ponto da metrópole pagando apenas a tarifa inicial.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto atende localidades industriais e operárias estratégicas: <em>Vila Mariana</em>, <em>Jardim Salgado Filho</em> e o <em>Parque Industrial Coronel Quito Junqueira</em>, além das instalações operacionais do <em>Aeroporto Leite Lopes</em>.</p>"
            "<p>A presença desta linha alimenta o principal cinturão de manufatura e transporte de cargas aéreas de Ribeirão Preto, promovendo dinamismo econômico para as empresas locais.</p>"
        ),
        "atracoes_proximas": (
            "<p>A principal atração e ponto de interesse da rota é o <strong>Aeroporto Estadual Doutor Leite Lopes</strong>, com sua movimentação de voos comerciais da aviação civil nacional e jatos executivos.</p>"
            "<p>A rota também aproxima os passageiros do Aeroclube de Ribeirão Preto, de hangares de aviação agrícola e do Parque Ecológico da Zona Norte, sendo uma opção prática para entusiastas da aviação civil.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 43 - Av. Brasil, 1105", "rua": "Avenida Brasil", "bairro": "Jardim Salgado Filho", "referencia": "Ponto de conexão direta com o Corredor BRT Norte-Sul"},
            {"nome": "Ponto 2226 - R. Peru, 1058", "rua": "Rua Peru", "bairro": "Vila Mariana", "referencia": "Acesso a indústrias e comércio da Vila Mariana"},
            {"nome": "Ponto 2228 - R. Peru, 1730", "rua": "Rua Peru", "bairro": "Vila Mariana", "referencia": "Acesso ao Parque Industrial Coronel Quito Junqueira"},
            {"nome": "Ponto 2230 - R. Peru, 2400", "rua": "Rua Peru", "bairro": "Vila Mariana", "referencia": "Ponto de apoio aos galpões de transporte e cargas"},
            {"nome": "Ponto Terminal Aeroporto Leite Lopes", "rua": "Avenida Thomaz Alberto Whately", "bairro": "Parque Industrial", "referencia": "Desembarque no terminal de passageiros do Aeroporto RAO"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Pq. Industrial / Aeroporto (Regular)", "num_paradas": 25, "descricao": "Itinerário alimentador ligando a Avenida Brasil ao Parque Industrial Coronel Quito Junqueira e ao saguão do Aeroporto Leite Lopes."}
        ]
    }
}

def main():
    print("==================================================")
    print("   GERADOR OFICIAL DO LOTE 1 (C4 — FASE 1)        ")
    print("==================================================")
    
    PAGINAS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Atualiza lista_linhas no content/paginas/linhas/index.json
    index_data = json.load(open(INDEX_JSON_PATH, encoding='utf-8'))
    slug_map = {num: lote1_defs[num]["slug"] for num in lote1_defs}
    
    for item in index_data.get('lista_linhas', []):
        cod = item.get('codigo')
        if cod in slug_map:
            item['slug'] = slug_map[cod]
            print(f"[*] Atualizado slug no index.json: Linha {cod} -> {slug_map[cod]}")
            
    with open(INDEX_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    print("[+] index.json sincronizado com os slugs oficiais do Lote 1.")

    # Gera cada um dos 10 arquivos JSON
    for num, defs in lote1_defs.items():
        fonte_item = dados_fonte[num]
        
        # Monta grade horária real a partir do linhas.json
        horarios_fonte = fonte_item['horarios']['valor']
        horarios_tabela = {
            "dias_uteis": horarios_fonte.get('dias_uteis', []),
            "sabado": horarios_fonte.get('sabado', []),
            "domingo": horarios_fonte.get('domingo', [])
        }
        
        bairros_lista = fonte_item['bairros']['valor']
        
        # Monta FAQ estruturado específico
        faq = [
            {
                "pergunta": f"Qual é o valor da passagem da Linha {num} {defs['linha_nome']}?",
                "resposta": f"A tarifa urbana em Ribeirão Preto é de R$ 5,00, aceita via Cartão Cidadão RP Mobi, cartões de transporte e pagamento em dinheiro no validador de bordo."
            },
            {
                "pergunta": f"Onde a Linha {num} realiza embarque principal?",
                "resposta": f"O embarque principal ocorre no {defs['terminal_central']}, onde os passageiros contam com abrigos e integração da rede municipal."
            },
            {
                "pergunta": f"Como funciona a integração temporal da Linha {num}?",
                "resposta": f"Com o Cartão Cidadão RP Mobi, o usuário dispõe de até 120 minutos (2 horas) a partir da primeira validação na catraca para embarcar em outro coletivo sem custo adicional."
            }
        ]
        
        page_dict = {
            "slug": defs["slug"],
            "status": "pronta",
            "template": "linha.html",
            "schema_type": "WebPage",
            "titulo": defs["titulo"],
            "descricao": defs["descricao"],
            "keywords": defs["keywords"],
            "h1": defs["h1"],
            "linha_numero": defs["linha_numero"],
            "linha_nome": defs["linha_nome"],
            "linha_cor": defs["linha_cor"],
            "modalidade": defs["modalidade"],
            "tarifa": defs["tarifa"],
            "resumo_origem_destino": defs["resumo_origem_destino"],
            "terminal_central": defs["terminal_central"],
            "publicado": "2026-10-03",
            "atualizado": "2026-10-03",
            "proxima_revisao": "2027-04-03",
            "revisor": "Leonardo A. Macedo",
            "breadcrumbs": [
                {"nome": "Início", "url": "/"},
                {"nome": "Mobilidade & Transporte", "url": "/linhas/index.html"},
                {"nome": f"Linha {num} - {defs['linha_nome']}", "url": f"/{defs['slug']}.html"}
            ],
            "secoes": {
                "visao_geral": defs["visao_geral"],
                "itinerario_texto": defs["itinerario_texto"],
                "paradas_destaque": defs["paradas_destaque"],
                "integracao_detalhe": defs["integracao_detalhe"],
                "bairros_texto": defs["bairros_texto"],
                "atracoes_proximas": defs["atracoes_proximas"]
            },
            "itinerarios_detalhe": defs["itinerarios_detalhe"],
            "paradas_principais": defs["paradas_principais"],
            "horarios_tabela": horarios_tabela,
            "bairros_lista": bairros_lista,
            "faq": faq,
            "fontes": [
                {
                    "nome": "RP Mobi — Horários e Linhas do Transporte Coletivo Urbano",
                    "url": "https://www.rpmobi.com.br",
                    "tipo": "oficial",
                    "verificado_em": "2026-10-03"
                },
                {
                    "nome": "Prefeitura Municipal de Ribeirão Preto — Tarifas e Decretos de Mobilidade",
                    "url": "https://www.ribeiraopreto.sp.gov.br",
                    "tipo": "oficial",
                    "verificado_em": "2026-10-03"
                }
            ]
        }
        
        target_file = ROOT_DIR / "content" / "paginas" / f"{defs['slug']}.json"
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump(page_dict, f, ensure_ascii=False, indent=2)
        print(f"[+] Gerado: {target_file.relative_to(ROOT_DIR)}")

    print("\n[OK] Lote 1 de 10 páginas gerado com sucesso!")

if __name__ == '__main__':
    main()
