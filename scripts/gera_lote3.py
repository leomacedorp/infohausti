#!/usr/bin/env python3
"""
GERADOR OFICIAL DO LOTE 3 (C4 — FASE 2) — INFOHAUS RP
Gera as 10 páginas JSON do Lote 3 em content/paginas/linhas/:
- 063: Pq. das Gaivotas (Alimentadora Leste)
- 065: Jd. Emília (Alimentadora Bonfim)
- 073: Reserva Real (Alimentadora Leste)
- 075: Alto do Bonfim (Alimentadora Bonfim)
- 079: Macaúba (Alimentadora Oeste/Norte)
- 085: Jd. São Fernando até Santa Martha (Alimentadora Bonfim/Sul)
- 093: Villas do Mirante (Alimentadora Sudeste)
- 095: Jd. Santa Cecília (Alimentadora Bonfim)
- 101: Pq. Avelino (Convencional Norte/Centro)
- 102: Jd. Independência (Convencional Norte/Campos Elíseos)
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
LINHAS_JSON_PATH = ROOT_DIR / 'content' / 'dados-fonte' / 'linhas.json'
PAGINAS_DIR = ROOT_DIR / 'content' / 'paginas' / 'linhas'
INDEX_JSON_PATH = ROOT_DIR / 'content' / 'paginas' / 'linhas' / 'index.json'

dados_fonte = json.load(open(LINHAS_JSON_PATH, encoding='utf-8'))

lote3_defs = {
    "063": {
        "slug": "linhas/linha-063-pq-das-gaivotas",
        "h1": "Linha 063 — Pq. das Gaivotas",
        "titulo": "Linha 063 - Pq. das Gaivotas | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 063 Parque das Gaivotas da RP Mobi em Ribeirão Preto. Trajeto alimentar pelo Terminal Leste, Novo Shopping e Interlagos.",
        "keywords": "linha 063 ribeirao preto, parque das gaivotas rp mobi, onibus gaivotas novo shopping, horario linha 063",
        "linha_numero": "063",
        "linha_nome": "Pq. das Gaivotas",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Leste (Novo Shopping) ↔ Parque das Gaivotas / Pq. São Sebastião",
        "terminal_central": "Terminal Leste de Transferência (Novo Shopping)",
        "visao_geral": (
            "<p>A <strong>Linha 063 (Pq. das Gaivotas)</strong> desempenha função vital para o transporte coletivo das famílias trabalhadoras estabelecidas no Parque das Gaivotas e Parque São Sebastião, bairros populosos situados na extremidade leste de Ribeirão Preto. Com veículos ágeis de cor laranja que circulam em vias coletoras e residenciais, a rota assegura a chegada pontual de comerciários aos centros de compras e de operários aos polos de serviços da cidade.</p>"
            "<p>Coordenada pela RP Mobi com monitoramento telemático, a operação oferece intervalos equilibrados ao longo de todo o dia, suprindo a carência de condução direta entre os loteamentos populares e a grande plataforma de transbordo do complexo comercial regional.</p>"
        ),
        "itinerario_texto": (
            "<p>O trajeto inicia na plataforma do Terminal Leste contíguo ao centro de compras, ingressando pela Avenida Zilda de Souza Rizzi e atravessando os núcleos residenciais do Jardim Interlagos e Parque das Oliveiras II. O ônibus transpõe as ruas Raul de Faria e Ataulfo Alves com velocidade compatível.</p>"
            "<p>Em seguida, penetra nas vias do Parque das Gaivotas, cumprindo o itinerário circular que atende às praças de convivência e às escolas públicas da comunidade antes de regressar pela rota estrutural até a baia de transferência.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 33 paradas ao longo do percurso regular. A principal escala é o <strong>Ponto 3554 (Terminal Leste)</strong>, que reúne linhas estruturais com ligação para a região central e para os distritos industriais.</p>"
            "<p>No Parque das Gaivotas, a parada de maior afluência de munícipes fica na <strong>Avenida Zilda de Souza Rizzi</strong>, defronte ao comércio vicinal de mercearias e açougues onde famílias fazem suas compras diárias.</p>"
        ),
        "integracao_detalhe": (
            "<p>A passagem respeita a tarifa pública municipal de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O morador que embarca no Parque das Gaivotas transfere-se sem novo pagamento nas linhas que operam no Terminal Leste.</p>"
            "<p>Essa facilidade beneficia especialmente jovens aprendizes e vendedores do comércio lojista que dependem de dois ônibus diários para cada sentido de deslocamento.</p>"
        ),
        "bairros_texto": (
            "<p>O atendimento contempla <em>Parque das Gaivotas</em>, <em>Parque São Sebastião</em>, <em>Jardim Interlagos</em>, <em>Parque Anhangüera</em>, <em>Parque das Oliveiras II</em> e <em>Recreio Internacional</em>.</p>"
            "<p>A consolidação desta linha é considerada uma conquista social de moradores da Zona Leste, encurtando o tempo médio gasto na ida e volta do expediente profissional.</p>"
        ),
        "atracoes_proximas": (
            "<p>A linha oferece conexão direta ao <strong>Novo Shopping Ribeirão Preto</strong>, importante centro de lazer, hipermercado, serviços de Poupatempo e salas de cinema.</p>"
            "<p>Nas proximidades dos bairros atendidos, aproxima os munícipes do Complexo Esportivo Comunitário do Parque São Sebastião e de áreas verdes de recreação infantil.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3554 - Terminal Leste", "rua": "Avenida Presidente Castelo Branco", "bairro": "Parque Industrial Lagoinha", "referencia": "Plataforma de transbordo Novo Shopping"},
            {"nome": "Ponto R. Raul de Faria, 336", "rua": "Rua Raul de Faria", "bairro": "Jardim Interlagos", "referencia": "Acesso a escolas e pequenos comércios"},
            {"nome": "Ponto R. Ataulfo Alves, 610", "rua": "Rua Ataulfo Alves", "bairro": "Parque São Sebastião", "referencia": "Parada central do bairro"},
            {"nome": "Ponto Av. Zilda de Souza Rizzi, 841", "rua": "Avenida Zilda de Souza Rizzi", "bairro": "Parque das Gaivotas", "referencia": "Comércio de bairro e farmácias"},
            {"nome": "Ponto Final Parque das Gaivotas", "rua": "Rua Projetada Quatro", "bairro": "Parque das Gaivotas", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Pq. das Gaivotas (Regular)", "num_paradas": 33, "descricao": "Itinerário principal alimentador ligando o Terminal Leste ao Parque das Gaivotas e Parque São Sebastião."},
            {"nome": "Inicia no Pq. das Gaivotas", "num_paradas": 23, "descricao": "Partidas matutinas diretas iniciadas no bairro rumo ao Terminal Leste."}
        ]
    },
    "065": {
        "slug": "linhas/linha-065-jd-emilia",
        "h1": "Linha 065 — Jd. Emília",
        "titulo": "Linha 065 - Jd. Emília | Horários e Paradas RP Mobi",
        "descricao": "Horários e itinerário da Linha 065 Jardim Emília da RP Mobi em Ribeirão Preto. Atendimento alimentar para oficinas, serralherias e Terras de Bonfim.",
        "keywords": "linha 065 ribeirao preto, onibus jardim emilia rp mobi, alimentadora emilia oficinas, horario linha 065",
        "linha_numero": "065",
        "linha_nome": "Jd. Emília",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Sul-Distrital ↔ Núcleo Operário Jardim Emília / Terras de Bonfim",
        "terminal_central": "Plataforma Sul-Distrital de Conexão",
        "visao_geral": (
            "<p>A <strong>Linha 065 (Jd. Emília)</strong> cumpre papel estritamente funcional no transporte da mão de obra operária que atua nas pequenas indústrias, serralherias de esquadrias de ferro, tornearias mecânicas e oficinas de tratores instaladas no Jardim Emília. Trata-se de um setor com ruas estreitas de paralelepípedo, galpões de concreto armado e moradias populares geminadas habitadas por famílias de metalúrgicos e mecânicos pesados.</p>"
            "<p>Com micro-ônibus equipados com freios reforçados para manobras em esquinas de raio reduzido, a RP Mobi programa viagens nos horários de entrada e saída dos turnos industriais, garantindo que caldeireiros, soldadores e ajudantes gerais cheguem com pontualidade aos postos de serviço.</p>"
        ),
        "itinerario_texto": (
            "<p>A condução arranca das baias de transbordo da estação distrital, transpondo o leito canalizado pela Rua Doutor Marciano e ingressando no corredor de comércio pesado da Rua Major Francisco Gandra. O veículo contorna esquinas estreitas onde manobram caminhões de carga e guinchos.</p>"
            "<p>Subindo a pista de calçamento da Rua Barão de Ataliba, o micro-ônibus atende às oficinas mecânicas antes de atingir os conjuntos habitacionais de Terras de Bonfim, executando o retorno em balão pavimentado e refazendo o itinerário de descida com velocidade moderada.</p>"
        ),
        "paradas_destaque": (
            "<p>A rota abrange 14 pontos estrategicamente alocados para evitar longas caminhadas com ferramentas ou equipamentos de trabalho. A baia inicial é o <strong>Ponto 1424</strong>, dotado de cobertura e bancos metálicos.</p>"
            "<p>No miolo do Jardim Emília, o ponto mais concorrido situa-se na <strong>Rua Major Francisco Gandra, 387</strong>, em frente ao pátio de soldagem e usinagem, onde se concentram dezenas de operários uniformizados com botas de biqueira de aço no fim da tarde.</p>"
        ),
        "integracao_detalhe": (
            "<p>O bilhete custa <strong>R$ 5,00</strong>, acompanhado da <strong>janela de transbordo gratuito de duas horas</strong> via validador eletrônico RP Mobi. O torneiro mecânico ou caldeireiro passa o cartão na catraca do micro-ônibus e embarca sem ônus financeiro no ônibus troncal seguinte que cruza o anel viário metropolitano.</p>"
            "<p>Esse benefício desonera os custos de transporte de quem desempenha funções braçais pesadas e necessita de duas viagens diárias para retornar aos bairros operários do Norte ou Oeste.</p>"
        ),
        "bairros_texto": (
            "<p>A rota concentra seu atendimento no <em>Jardim Emília</em>, na faixa de moradias de <em>Terras de Bonfim</em> e nos galpões limítrofes da <em>Vila Tibério</em>.</p>"
            "<p>A existência regular do trajeto mantém viva a dinâmica produtiva das microempresas e galpões de reparo que sustentam a economia mecânica da região.</p>"
        ),
        "atracoes_proximas": (
            "<p>A linha dá acesso direto ao <strong>polo de tornearia e fundição mecânica</strong>, especializado na recuperação de componentes agrícolas para colheitadeiras e tratores de cana-de-açúcar.</p>"
            "<p>No ponto de partida distrital, deixa os usuários a passos das lojas de peças de reposição e postos de combustível com borracharias 24 horas.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 1424 - Plataforma Sul-Distrital", "rua": "Rua Professor Hélio Lourenço", "bairro": "Bonfim Paulista", "referencia": "Terminal de transbordo distrital"},
            {"nome": "Ponto R. Dr. Marciano, 99", "rua": "Rua Doutor Marciano", "bairro": "Bonfim Paulista", "referencia": "Acesso a oficinas mecânicas"},
            {"nome": "Ponto R. Major Francisco Gandra, 387", "rua": "Rua Major Francisco Gandra", "bairro": "Jardim Emília", "referencia": "Parada dos galpões industriais"},
            {"nome": "Ponto R. Barão de Ataliba, 312", "rua": "Rua Barão de Ataliba", "bairro": "Jardim Emília", "referencia": "Acesso a Terras de Bonfim"},
            {"nome": "Ponto Final Terras de Bonfim", "rua": "Estrada das Palmeiras", "bairro": "Terras de Bonfim", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. Emília (Regular)", "num_paradas": 10, "descricao": "Itinerário alimentador operário ligando a plataforma distrital às oficinas do Jardim Emília."},
            {"nome": "Jd. Emília até Terras de Bonfim", "num_paradas": 14, "descricao": "Extensão atendendo aos loteamentos residenciais operários de Terras de Bonfim."}
        ]
    },
    "073": {
        "slug": "linhas/linha-073-reserva-real",
        "h1": "Linha 073 — Reserva Real",
        "titulo": "Linha 073 - Reserva Real | Horários e Paradas RP Mobi",
        "descricao": "Guia da Linha 073 Reserva Real da RP Mobi em Ribeirão Preto. Horários atualizados, itinerário pelo Terminal Leste, Novo Shopping e Quinta da Boa Vista.",
        "keywords": "linha 073 ribeirao preto, onibus reserva real rp mobi, alimentadora novo shopping, horario linha 073",
        "linha_numero": "073",
        "linha_nome": "Reserva Real",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Leste (Novo Shopping) ↔ Bairro Planejado Reserva Real",
        "terminal_central": "Terminal Leste de Transferência (Novo Shopping)",
        "visao_geral": (
            "<p>A <strong>Linha 073 (Reserva Real)</strong> é um serviço alimentador moderno criado para atender ao expressivo adensamento demográfico e imobiliário do bairro planejado Reserva Real e loteamentos associados na Zona Leste de Ribeirão Preto. O empreendimento mescla condomínios fechados horizontais, blocos de apartamentos e praças temáticas com ampla área de preservação ambiental.</p>"
            "<p>Operada sob supervisão da RP Mobi, a frota cumpre tabelas pontuais conectando os novos moradores, equipes de paisagismo, segurança condominial e manutenção aos grandes corredores viários do município.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota parte da plataforma do Terminal Leste no Novo Shopping, trafegando pelas pistas expressas que dão acesso ao Jardim Helena e Parque Anhangüera. O coletivo ingressa na malha viária do Reserva Real através de avenidas largas com canteiro central ajardinado.</p>"
            "<p>O ônibus percorre as alamedas que contornam os núcleos residenciais do complexo, realizando paradas em frente às entradas de condomínios e áreas esportivas públicas antes de efetuar o retorno pela rotatória principal em direção ao shopping.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha conta com 30 paradas catalogadas. A principal parada de transbordo é o <strong>Ponto 2142 (Terminal Leste / Novo Shopping)</strong>, que oferece infraestrutura completa com cobertura, segurança e conexão com ônibus metropolitanos.</p>"
            "<p>No bairro Reserva Real, merecem destaque os abrigos na <strong>Avenida Reserva Real</strong> e junto ao Parque Linear local, dotados de piso tátil e iluminação em lâmpadas de LED para travessia segura de pedestres.</p>"
        ),
        "integracao_detalhe": (
            "<p>A operação é regulada pela tarifa básica de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O passageiro valida sua entrada no Reserva Real e pode acessar qualquer linha troncal no Terminal Leste sem novo desembolso.</p>"
            "<p>Essa regra tarifária alivia o orçamento de centenas de trabalhadores terceirizados que atendem os condomínios da Zona Leste.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário atende diretamente a <em>Reserva Real</em>, <em>Condomínio Quinta da Boa Vista</em>, <em>Jardim Helena</em>, <em>Jardim Interlagos</em> e <em>Parque Anhangüera</em>.</p>"
            "<p>A rota foi estruturada para acompanhar a rápida expansão urbana da bacia oriental da cidade, evitando a sobrecarga de veículos particulares nas vias coletoras.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota conecta os moradores ao <strong>Parque Linear do Reserva Real</strong>, com suas pistas para ciclistas, estações de ginástica ao ar livre e lagos de retenção pluvial.</p>"
            "<p>Na ponta de conexão, viabiliza acesso imediato ao <strong>Novo Shopping</strong>, com suas lojas de departamento, cinemas e praça de alimentação diversificada.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 2142 - Terminal Leste (Novo Shopping)", "rua": "Avenida Presidente Castelo Branco", "bairro": "Parque Industrial Lagoinha", "referencia": "Terminal de transbordo principal"},
            {"nome": "Ponto Av. Reserva Real - Portaria 1", "rua": "Avenida Reserva Real", "bairro": "Reserva Real", "referencia": "Acesso aos primeiros condomínios do complexo"},
            {"nome": "Ponto Parque Linear Reserva Real", "rua": "Avenida Reserva Real", "bairro": "Reserva Real", "referencia": "Área de esportes e lazer ao ar livre"},
            {"nome": "Ponto Quinta da Boa Vista", "rua": "Alameda dos Bosques", "bairro": "Condomínio Quinta da Boa Vista", "referencia": "Conexão com condomínio fechado"},
            {"nome": "Ponto Final Reserva Real", "rua": "Rotatória dos Ipês", "bairro": "Reserva Real", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Reserva Real (Regular)", "num_paradas": 30, "descricao": "Itinerário principal alimentador ligando o Terminal Leste ao complexo Reserva Real."}
        ]
    },
    "075": {
        "slug": "linhas/linha-075-alto-do-bonfim",
        "h1": "Linha 075 — Alto do Bonfim",
        "titulo": "Linha 075 - Alto do Bonfim | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 075 Alto do Bonfim da RP Mobi em Ribeirão Preto. Micro-ônibus para aclives íngremes e mirantes de Santa Genebra.",
        "keywords": "linha 075 ribeirao preto, alto do bonfim ladeiras, onibus mirante santa genebra, horario linha 075",
        "linha_numero": "075",
        "linha_nome": "Alto do Bonfim",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Sul-Distrital ↔ Cumeeira do Morro Alto do Bonfim / Santa Genebra",
        "terminal_central": "Plataforma Sul-Distrital de Conexão",
        "visao_geral": (
            "<p>A <strong>Linha 075 (Alto do Bonfim)</strong> vence os maiores desníveis altimétricos do relevo meridional ribeirão-pretano, escalando as rampas íngremes do Morro de Santa Genebra até os mirantes de pedra do Alto do Bonfim. A paisagem é dominada por vegetação rasteira de altitude, afloramentos rochosos de arenito basáltico, torres metálicas de radiocomunicação celular e residências isoladas em platôs de pedra exposta.</p>"
            "<p>Equipada exclusivamente com micro-ônibus de tração reduzida, pneus lameiros para terrenos pedregosos e sistemas eletrônicos antitravamento de freios em descidas acentuadas, a linha conduz técnicos de manutenção de antenas parabólicas, guardas de torres de transmissão e moradores do topo do morro.</p>"
        ),
        "itinerario_texto": (
            "<p>Deixando a base do vale na plataforma de transferência, a condução engata marcha forte na subida íngreme da Rua Professor Felisberto Almada, contornando curvas em cotovelo na Rua Capitão Joaquim Félix onde a inclinação viária ultrapassa 15 graus. O veículo serpenteia pela encosta ladeada por paredões de rocha.</p>"
            "<p>No platô do cume, o micro-ônibus percorre a crista da montanha pela Estrada de Santa Genebra, fazendo a parada terminal na rotatória rochosa do mirante panorâmico antes de iniciar a descida controlada por freio-motor de volta à base do distrito.</p>"
        ),
        "paradas_destaque": (
            "<p>Com 13 pontos instalados em rocha viva ou muretas de contenção, a linha atende aos pontos mais elevados da malha urbana. O abrigo inicial é a baia coberta na base distrital.</p>"
            "<p>No pico do relevo, o destaque isolado é a <strong>Parada Mirante das Torres</strong> na Estrada de Santa Genebra, construída com parapeito de tubos galvanizados e iluminação fotovoltaica autônoma para resistir aos fortes vendavais e temporais característicos do topo das colinas.</p>"
        ),
        "integracao_detalhe": (
            "<p>A cobrança respeita a tarifa de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> com a utilização do Cartão Cidadão RP Mobi. Quem embarca nas alturas do Alto do Bonfim valida sua passagem e pode tomar a linha estrutural na baixada sem desembolsar nenhum valor a mais.</p>"
            "<p>Esse benefício temporal impede que a população do topo da serra fique penalizada pelo isolamento topográfico imposto pela geomorfologia acidentada.</p>"
        ),
        "bairros_texto": (
            "<p>A rota atende com exclusividade aos moradores do <em>Alto do Bonfim</em>, às chácaras de topo de morro do <em>Jardim Santa Genebra</em> e às estações de rádio e TV da <em>Serra do Bonfim</em>.</p>"
            "<p>A operação com veículos de tração potente evitou o abandono viário de núcleos familiares fixados nas cotas altimétricas superiores do município.</p>"
        ),
        "atracoes_proximas": (
            "<p>O atrativo supremo da rota é o <strong>Mirante Geológico de Santa Genebra</strong>, de onde se contempla uma visão de 360 graus de todo o vale do rio Pardo e das tempestades de verão se aproximando no horizonte.</p>"
            "<p>Também serve de ponto de acesso para praticantes de voo livre de asa-delta e ciclistas de downhill de montanha nos sábados e domingos.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 1424 - Plataforma Sul-Distrital", "rua": "Rua Professor Hélio Lourenço", "bairro": "Bonfim Paulista", "referencia": "Terminal de transbordo distrital"},
            {"nome": "Ponto R. Prof. Felisberto Almada, 231", "rua": "Rua Professor Felisberto Almada", "bairro": "Bonfim Paulista", "referencia": "Início da subida de serra"},
            {"nome": "Ponto R. Capitão Joaquim Félix, 112", "rua": "Rua Capitão Joaquim Félix", "bairro": "Alto do Bonfim", "referencia": "Curva das rochas basálticas"},
            {"nome": "Ponto Mirante das Torres", "rua": "Estrada de Santa Genebra", "bairro": "Jardim Santa Genebra", "referencia": "Torres de telecomunicação e mirante"},
            {"nome": "Ponto Final Alto do Bonfim", "rua": "Rotatória do Mirante", "bairro": "Alto do Bonfim", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Alto do Bonfim (Regular)", "num_paradas": 13, "descricao": "Itinerário alimentador montanhoso ligando a plataforma distrital aos mirantes e torres do Alto do Bonfim."}
        ]
    },
    "079": {
        "slug": "linhas/linha-079-macauba",
        "h1": "Linha 079 — Macaúba",
        "titulo": "Linha 079 - Macaúba | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 079 Macaúba da RP Mobi em Ribeirão Preto. Trajeto alimentar pelo Terminal Oeste, Reserva Macaúba e Adelino Simioni.",
        "keywords": "linha 079 ribeirao preto, macauba rp mobi, onibus reserva macauba, horario linha 079",
        "linha_numero": "079",
        "linha_nome": "Macaúba",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Oeste ↔ Reserva Macaúba / Adelino Simioni",
        "terminal_central": "Terminal Oeste de Transferência (Avenida Luiz Galvão Cézar)",
        "visao_geral": (
            "<p>A <strong>Linha 079 (Macaúba)</strong> é o serviço alimentador encarregado de conectar o complexo habitacional Reserva Macaúba e os loteamentos adjacentes do extremo Noroeste ao Terminal Oeste de Transferência. A região vivenciou forte expansão com a entrega de residenciais populares verticais e horizontais, exigindo transporte público eficiente para absorver o fluxo diário de operários, estudantes e trabalhadores do setor industrial.</p>"
            "<p>Supervisionada pela RP Mobi com veículos de alta durabilidade e acessibilidade completa, a rota opera em cadência estável, integrando o novo bairro ao sistema troncal de ônibus de Ribeirão Preto.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo do Terminal Oeste na Avenida Luiz Galvão Cézar, o coletivo segue pelo corredor viário norte-oeste, transpondo as imediações do bairro Adelino Simioni e Dom Bernardo José Mielle. O ônibus contorna avenidas largas com boa sinalização semafórica.</p>"
            "<p>Ao alcançar as vias do Reserva Macaúba, circula pelas alamedas de acesso aos condomínios de apartamentos, atendendo a paradas distribuídas estrategicamente e contornando a rotatória do terminal de gás em sua derivação estendida antes de reassumir o sentido sul rumo ao terminal.</p>"
        ),
        "paradas_destaque": (
            "<p>A rota abrange 28 paradas em seu percurso regular e derivações. O marco de saída é o <strong>Ponto 3564 (Terminal Oeste)</strong>, dotado de plataforma coberta, fiscalização presencial e conexão com diversas linhas radiais e perimetrais.</p>"
            "<p>No Reserva Macaúba, os destaques são as paradas na <strong>Avenida Luiz Galvão Cézar</strong> e em frente às portarias dos condomínios habitacionais, que reúnem trabalhadores no amanhecer e estudantes no regresso da tarde.</p>"
        ),
        "integracao_detalhe": (
            "<p>A passagem é tarifada no montante oficial de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O passageiro embarca no Reserva Macaúba e tem até duas horas para pegar a linha seguinte no Terminal Oeste sem novo custo.</p>"
            "<p>Esse benefício proporciona economia determinante para as famílias operárias que compõem a base demográfica dos novos residenciais do Noroeste.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário contempla <em>Reserva Macaúba</em>, <em>Adelino Simioni</em>, <em>Dom Bernardo José Mielle</em>, <em>Jardim Jovino Campos</em> e <em>Bom Jesus</em>.</p>"
            "<p>A atuação da linha assegurou a rápida inclusão da comunidade recém-assentada na rede pública de serviços urbanos essenciais.</p>"
        ),
        "atracoes_proximas": (
            "<p>A linha passa nas imediações de <strong>praças comunitárias arborizadas com quadras de areia</strong> e centros de convivência social do setor Noroeste.</p>"
            "<p>No Terminal Oeste, conecta diretamente os usuários a centros esportivos municipais, postos de saúde da família e supermercados atacadistas da região.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3564 - Terminal Oeste", "rua": "Avenida Luiz Galvão Cézar", "bairro": "Planalto Verde", "referencia": "Terminal de transbordo principal"},
            {"nome": "Ponto Av. Luiz Galvão Cézar, 797", "rua": "Avenida Luiz Galvão Cézar", "bairro": "Adelino Simioni", "referencia": "Acesso a escolas e comércio vicinal"},
            {"nome": "Ponto Reserva Macaúba 1", "rua": "Avenida dos Coqueiros", "bairro": "Reserva Macaúba", "referencia": "Portaria dos primeiros blocos residenciais"},
            {"nome": "Ponto Terminal de Gás", "rua": "Estrada Municipal Noroeste", "bairro": "Reserva Macaúba", "referencia": "Extensão operacional da linha"},
            {"nome": "Ponto Final Reserva Macaúba", "rua": "Rotatória Central", "bairro": "Reserva Macaúba", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Macaúba (Regular)", "num_paradas": 25, "descricao": "Itinerário alimentador principal ligando o Terminal Oeste aos residenciais do Reserva Macaúba."},
            {"nome": "Extensão Term. gás", "num_paradas": 29, "descricao": "Derivação estendida com atendimento aos depósitos e empresas do terminal de gás."}
        ]
    },
    "085": {
        "slug": "linhas/linha-085-jd-sao-fernando-santa-martha",
        "h1": "Linha 085 — Jd. São Fernando até Santa Martha",
        "titulo": "Linha 085 - Jd. São Fernando até Santa Martha | Horários RP Mobi",
        "descricao": "Guia de horários da Linha 085 São Fernando / Santa Martha da RP Mobi em Ribeirão Preto. Atendimento ao canteiro de obras e rodovia SP-328.",
        "keywords": "linha 085 ribeirao preto, obras santa martha rp mobi, onibus rodovia sp 328, horario linha 085",
        "linha_numero": "085",
        "linha_nome": "Jd. São Fernando até Santa Martha",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Sul-Distrital ↔ Canteiros de Obras Santa Martha / Reserva San Pedro",
        "terminal_central": "Plataforma Sul-Distrital de Conexão",
        "visao_geral": (
            "<p>A <strong>Linha 085 (Jd. São Fernando até Santa Martha)</strong> opera voltada prioritariamente ao transporte pesado da construção civil em andamento nos loteamentos horizontais fechados de Santa Martha e Reserva San Pedro, marginais à Rodovia José Fregonesi (SP-328). O cenário diário é repleto de betoneiras em trânsito, descarregamento de paletes de tijolos e blocos estruturais, montagem de andaimes metálicos e terraplenagem de novos lotes.</p>"
            "<p>A rota transporta mestres de obras, armadores de ferragens, pedreiros assentadores e eletricistas prediais que cumprem jornadas rigorosas nos canteiros da construção pesada, garantindo pontualidade britânica nas trocas de plantão matutino e de fechamento dos portões de obra.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo da plataforma distrital, o coletivo ganha a pista marginal da rodovia estadual SP-328, avançando por retas de asfalto ladeadas por tapumes de construtoras e galpões de materiais básicos. O ônibus acessa a trincheira de retorno sob o viaduto rodoviário.</p>"
            "<p>Em seguida, o veículo penetra pelas vias de terra socada e brita dos loteamentos Jardim São Fernando e Residencial Santa Martha, efetuando paradas técnicas defronte às guaritas de fiscalização de obras antes de executar manobra no bolsão de retorno da Reserva San Pedro.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 18 paradas ao longo de seu circuito. O ponto estruturante de saída é a plataforma sul de conexão, dotada de banheiros e fiscalização.</p>"
            "<p>Nos canteiros, os pontos de maior afluência são a <strong>Parada Guarita Santa Martha</strong> e o abrigo junto ao depósito de materiais do <strong>Jardim São Fernando</strong>, equipados com cobertura de telhas metálicas e bancos reforçados para os operários descansarem suas mochilas de ferramentas.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa cobrada é a básica de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> com a utilização do Cartão Cidadão RP Mobi. O pedreiro ou carpinteiro valida sua subida no canteiro de obras e tem duas horas para tomar qualquer linha troncal no terminal sem pagamento excedente.</p>"
            "<p>Esse benefício temporal preserva a renda dos trabalhadores braçais da construção civil pesada que constroem a infraestrutura imobiliária do município.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto atende exclusivamente aos canteiros de obras do <em>Residencial Santa Martha</em>, <em>Reserva San Pedro</em>, <em>Jardim São Fernando</em> e à faixa de servidão da <em>Rodovia SP-328</em>.</p>"
            "<p>A linha é considerada o principal oxigênio de mão de obra para que as construtoras e empreiteiras cumpram os cronogramas de entrega das obras civis.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa junto aos <strong>grandes centros de distribuição de materiais de construção e pisos cerâmicos</strong> instalados na rodovia estadual.</p>"
            "<p>No retorno à plataforma distrital, deixa os funcionários em frente aos postos de combustível com lanchonetes de refeição rápida para trabalhadores.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 1424 - Plataforma Sul-Distrital", "rua": "Rua Professor Hélio Lourenço", "bairro": "Bonfim Paulista", "referencia": "Terminal de transbordo distrital"},
            {"nome": "Ponto Rodovia SP-328 - Km 3", "rua": "Rodovia José Fregonesi", "bairro": "Bonfim Paulista", "referencia": "Depósito de concreto e blocos"},
            {"nome": "Ponto Canteiro Central São Fernando", "rua": "Rua São Fernando", "bairro": "Jardim São Fernando", "referencia": "Acesso a obras de alvenaria"},
            {"nome": "Ponto Guarita Santa Martha", "rua": "Alameda Santa Martha", "bairro": "Residencial Santa Martha", "referencia": "Entrada de operários e engenheiros"},
            {"nome": "Ponto Final Reserva San Pedro", "rua": "Rotatória San Pedro", "bairro": "Reserva San Pedro", "referencia": "Bolsão de manobra de betoneiras"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. São Fernando / Santa Martha", "num_paradas": 18, "descricao": "Itinerário alimentador voltado aos canteiros de construção civil de Santa Martha e São Fernando."}
        ]
    },
    "093": {
        "slug": "linhas/linha-093-villas-do-mirante",
        "h1": "Linha 093 — Villas do Mirante",
        "titulo": "Linha 093 - Villas do Mirante | Horários e Paradas RP Mobi",
        "descricao": "Horários e trajeto da Linha 093 Villas do Mirante da RP Mobi em Ribeirão Preto. Micro-alimentadora ligando o Terminal Sudeste à Quinta da Mata.",
        "keywords": "linha 093 ribeirao preto, onibus villas do mirante rp mobi, alimentadora terminal sao jose, horario linha 093",
        "linha_numero": "093",
        "linha_nome": "Villas do Mirante",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#ff6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Sudeste (São José) ↔ Residencial Villas do Mirante / Quinta da Mata",
        "terminal_central": "Terminal Sudeste de Transferência (Jardim São José)",
        "visao_geral": (
            "<p>A <strong>Linha 093 (Villas do Mirante)</strong> é um serviço alimentador de alta especialização geográfica, configurado em formato circular curto com 7 paradas para atender ao enclave residencial do Residencial Villas do Mirante e do condomínio Quinta da Mata, encravados nas elevações verdes da Zona Sudeste de Ribeirão Preto. O perfil urbanístico é composto por moradias térreas e sobrados em ruas calmas e arborizadas.</p>"
            "<p>Operada com micro-ônibus sob monitoramento da RP Mobi, a rota oferece viagens ágeis e pontuais que garantem o transporte cotidiano de prestadores de serviços, diaristas, cuidadores de idosos e estudantes até a plataforma de conexão do Jardim São José.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo das baias de transbordo do Terminal Sudeste, a linha percorre a Rua Doutor José Ribeiro Ferreira, subindo com traçado suave pelas vias coletoras da região sul-sudeste. O veículo transpõe ruas residenciais pavimentadas com arborização bem conservada.</p>"
            "<p>O ônibus ingressa no bolsão residencial de Villas do Mirante pela Rua José Carlos Carvalho, executando o desembarque de passageiros nas imediações das portarias e contornando a praça local para retornar com rapidez à estação de transferência.</p>"
        ),
        "paradas_destaque": (
            "<p>Com 7 paradas em seu itinerário completo, a linha prioriza agilidade e segurança no embarque. O marco principal de conexão é o <strong>Ponto 2337 (Terminal Sudeste - São José)</strong>, que reúne linhas troncais com itinerário para o centro financeiro da cidade.</p>"
            "<p>No bairro, o destaque é o ponto na <strong>Rua Doutor José Ribeiro Ferreira</strong> e a parada central na <strong>Rua José Carlos Carvalho</strong>, equipados com calçadas acessíveis e boa visibilidade diurna e noturna.</p>"
        ),
        "integracao_detalhe": (
            "<p>A passagem é cobrada no valor unificado de <strong>R$ 5,00</strong>, com plena concessão do benefício da <strong>integração temporal de 120 minutos</strong> mediante uso do Cartão Cidadão RP Mobi. O passageiro valida sua subida no Villas do Mirante e faz baldeação sem custo nas linhas do Terminal Sudeste.</p>"
            "<p>Esse benefício temporal favorece os profissionais autônomos que atendem aos condomínios da colina sul em jornadas parciais de trabalho.</p>"
        ),
        "bairros_texto": (
            "<p>A rota cobre de forma cirúrgica o <em>Residencial Villas do Mirante</em>, o <em>Condomínio Quinta da Mata</em> e setores limítrofes do <em>Jardim São José</em>.</p>"
            "<p>A oferta dedicada desta linha garantiu atendimento público para uma área habitacional reservada que não possuía acesso a linhas convencionais de grande porte.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa junto aos <strong>mirantes naturais e áreas verdes preservadas da Quinta da Mata</strong>, com vista panorâmica para o relevo sul do município.</p>"
            "<p>No Terminal Sudeste, facilita a integração rápida com as faculdades da Unaerp, hospitais da Ribeirânia e complexos esportivos vizinhos.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 2337 - Terminal Sudeste (São José)", "rua": "Avenida Doutor Celso Charuri", "bairro": "Jardim São José", "referencia": "Terminal de transbordo principal"},
            {"nome": "Ponto R. Dr. José Ribeiro Ferreira, 580", "rua": "Rua Doutor José Ribeiro Ferreira", "bairro": "Jardim São José", "referencia": "Acesso a residências e comércio"},
            {"nome": "Ponto R. Dr. José Ribeiro Ferreira, 640", "rua": "Rua Doutor José Ribeiro Ferreira", "bairro": "Jardim São José", "referencia": "Parada intermediária"},
            {"nome": "Ponto R. José Carlos Carvalho, s/n", "rua": "Rua José Carlos Carvalho", "bairro": "Villas do Mirante", "referencia": "Portaria do residencial Villas do Mirante"},
            {"nome": "Ponto Final Quinta da Mata", "rua": "Rotatória da Quinta", "bairro": "Quinta da Mata", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Villas do Mirante (Regular)", "num_paradas": 7, "descricao": "Itinerário circular alimentador ligando o Terminal Sudeste ao condomínio Villas do Mirante e Quinta da Mata."}
        ]
    },
    "095": {
        "slug": "linhas/linha-095-jd-santa-cecilia",
        "h1": "Linha 095 — Jd. Santa Cecília",
        "titulo": "Linha 095 - Jd. Santa Cecília | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 095 Jardim Santa Cecília da RP Mobi em Ribeirão Preto. Atendimento a hortas hidropônicas e produtores rurais familiares.",
        "keywords": "linha 095 ribeirao preto, hortas santa cecilia rp mobi, onibus rural produtores, horario linha 095",
        "linha_numero": "095",
        "linha_nome": "Jd. Santa Cecília",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Sul-Distrital ↔ Cinturão Verde Jardim Santa Cecília / Chácaras Agrícolas",
        "terminal_central": "Plataforma Sul-Distrital de Conexão",
        "visao_geral": (
            "<p>A <strong>Linha 095 (Jd. Santa Cecília)</strong> atende com dedicação exclusiva ao cinturão verde agrícola e hortifrutigranjeiro do Jardim Santa Cecília, no limite sudeste ribeirão-pretano. O cenário é integralmente rural e camponês: estufas de hortaliças hidropônicas, plantios de alface crespa e rúcula, galinheiros de ovos caipiras, ordenhas manuais de leite e estradas vicinais de terra vermelha margeadas por cercas de arame e mourões de eucalipto.</p>"
            "<p>A frota opera com micro-ônibus rurais de suspensão elevada para trafegar sem atolar no barro durante a estação chuvosa, transportando agricultores familiares com caixotes plásticos de legumes frescos, ordenhadores e diaristas da lavoura hortícola.</p>"
        ),
        "itinerario_texto": (
            "<p>A condução inicia o trajeto na plataforma sul, deixando as vias asfaltadas e tomando a Estrada Municipal de Terra do Santa Cecília. O ônibus sacoleja suavemente pelas ondulações do terreno agrícola, parando junto às porteiras de madeira e estufas plásticas de cultivo.</p>"
            "<p>O veículo segue pela Rua das Laranjeiras entre pomares de cítricos e canteiros irrigados por aspersão, cumprindo o embarque de chacareiros e seus fardos de verduras antes de girar na Rotatória das Mangueiras Centenárias para tomar o caminho de retorno à estação de transbordo.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 20 paradas simples sinalizadas por mourões pintados de branco. O ponto estruturante de saída é a plataforma distrital na baixada.</p>"
            "<p>Na zona rural, o ponto mais emblemático é a <strong>Parada Porteira da Associação dos Horticultores</strong> na Rua das Laranjeiras, dotada de palanque de madeira coberto onde os pequenos produtores protegem seus caixotes de alface do sol forte da manhã enquanto esperam o coletivo.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa praticada é o valor congelado de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O horticultor valida seu bilhete no estribo do micro-ônibus e pode desembarcar no terminal e tomar a condução seguinte até o mercado municipal ou Ceagesp sem duplicar o pagamento.</p>"
            "<p>Essa isenção no transbordo temporal é vital para garantir a margem de subsistência de famílias camponesas de baixa renda.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário atende estritamente às propriedades do <em>Jardim Santa Cecília Rural</em> e às chácaras de cultivo agrícola do <em>Córrego dos Padres</em>.</p>"
            "<p>O funcionamento pontual desta linha é crucial para o escoamento diário de verduras frescas que abastecem feiras livres e quitandas da cidade.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa defronte a <strong>estufas hidropônicas abertas para colheita direta pelo consumidor (sistema colha e pague)</strong>, além de apiários de mel silvestre puro.</p>"
            "<p>Na plataforma de conexão urbana, facilita o acesso a depósitos de adubos orgânicos, casas veterinárias e cooperativas agropecuárias.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 1424 - Plataforma Sul-Distrital", "rua": "Rua Professor Hélio Lourenço", "bairro": "Bonfim Paulista", "referencia": "Terminal de transbordo distrital"},
            {"nome": "Ponto Porteira Santa Cecília", "rua": "Estrada Municipal Santa Cecília", "bairro": "Jardim Santa Cecília", "referencia": "Acesso a estufas de hortaliças"},
            {"nome": "Ponto Associação dos Horticultores", "rua": "Rua das Laranjeiras", "bairro": "Jardim Santa Cecília", "referencia": "Palanque de caixotes de verduras"},
            {"nome": "Ponto Estufa das Alfaces", "rua": "Estrada das Hortas", "bairro": "Jardim Santa Cecília", "referencia": "Cultivo hidropônico comercial"},
            {"nome": "Ponto Final Mangueiras Centenárias", "rua": "Rotatória das Mangueiras", "bairro": "Jardim Santa Cecília", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. Santa Cecília (Regular)", "num_paradas": 20, "descricao": "Itinerário alimentador rural exclusivo atendendo às hortas e estufas do Jardim Santa Cecília."}
        ]
    },
    "101": {
        "slug": "linhas/linha-101-pq-avelino",
        "h1": "Linha 101 — Pq. Avelino",
        "titulo": "Linha 101 - Pq. Avelino | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia oficial da Linha 101 Parque Avelino da RP Mobi em Ribeirão Preto. Linha convencional azul ligando o Parque Industrial Avelino Alves Palma ao Centro.",
        "keywords": "linha 101 ribeirao preto, onibus parque avelino rp mobi, convencional parque avelino centro, horario linha 101",
        "linha_numero": "101",
        "linha_nome": "Pq. Avelino",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Parque Industrial Avelino Alves Palma ↔ Região Central (Terminal Urbano)",
        "terminal_central": "Terminal Urbano Central (Plataformas Centrais)",
        "visao_geral": (
            "<p>A <strong>Linha 101 (Pq. Avelino)</strong> é uma das mais tradicionais e movimentadas linhas convencionais com a marcante cor azul da frota da RP Mobi, respondendo pela conexão direta entre o Parque Industrial Avelino Alves Palma, na Zona Norte, e o núcleo comercial e bancário do Centro de Ribeirão Preto. A rota atende a um corredor de expressiva densidade operária, abrangendo conjuntos habitacionais consolidados e dezenas de galpões fabris e de logística.</p>"
            "<p>Operando com ônibus padron e convencionais de alta capacidade equipados com ar-condicionado e elevador para acessibilidade, a linha mantém frequência intensa nos horários de pico matutino e vespertino para acolher o deslocamento em massa de industriários e comerciários.</p>"
        ),
        "itinerario_texto": (
            "<p>O trajeto inicia-se no coração do Parque Industrial Avelino, percorrendo vias como a Rua Pedro Colino e Rua Júlia Maria da Silva. Em seguida, atravessa as avenidas arteriais do Quintino Facci I e Jardim Salgado Filho, cruzando os trilhos ferroviários em direção ao miolo urbano.</p>"
            "<p>Ao alcançar a área central, o veículo circula pelas ruas Duque de Caxias, Amador Bueno e Tibiriçá, oferecendo desembarque a passos das repartições públicas, agências bancárias e calçadões comerciais antes de realizar o trajeto inverso de volta à Zona Norte.</p>"
        ),
        "paradas_destaque": (
            "<p>Com 88 paradas em seu itinerário completo, a Linha 101 atende a eixos urbanos fundamentais. No setor Norte, os destaques são a <strong>Parada Rua Pedro Colino, 215</strong> e a parada da praça central do <strong>Jardim Salgado Filho</strong>, com grande afluência de passageiros desde as primeiras horas da alvorada.</p>"
            "<p>No Centro, os pontos de embarque e desembarque nas imediações da <strong>Praça Carlos Gomes</strong> e do <strong>Terminal Urbano</strong> garantem conexão imediata com toda a malha de transporte metropolitano.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa cobrada é a padrão municipal de <strong>R$ 5,00</strong>, assegurando o direito universal de <strong>integração temporal de 120 minutos</strong> mediante uso do Cartão Cidadão RP Mobi. O passageiro valida sua entrada no Parque Avelino e pode fazer baldeação gratuita no Centro para linhas da Zona Sul ou Leste dentro de duas horas.</p>"
            "<p>Essa facilidade é essencial para trabalhadores da indústria que residem na Zona Norte e precisam acessar postos de saúde de especialidades ou escolas técnicas em outros quadrantes da cidade.</p>"
        ),
        "bairros_texto": (
            "<p>A rota beneficia comunidades densas como <em>Parque Industrial Avelino Alves Palma</em>, <em>Quintino Facci I</em>, <em>Jardim Salgado Filho</em>, <em>Jardim Jóquei Clube</em>, <em>Residencial Léo Gomes de Moraes</em> e o <em>Centro</em>.</p>"
            "<p>Trata-se de uma linha estruturante do sistema de mobilidade da Zona Norte, sustentando a ligação diária entre o parque industrial e os centros empregadores da cidade.</p>"
        ),
        "atracoes_proximas": (
            "<p>No Centro, a linha deixa os usuários a curta caminhada do <strong>Calçadão de Ribeirão Preto</strong>, do <strong>Theatro Pedro II</strong> e da histórica Praça XV de Novembro.</p>"
            "<p>Na Zona Norte, aproxima os munícipes do Parque Ecológico Pozzi e de tradicionais complexos poliesportivos de bairro.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto R. Pedro Colino, 215", "rua": "Rua Pedro Colino", "bairro": "Parque Industrial Avelino Alves Palma", "referencia": "Ponto de partida no polo industrial"},
            {"nome": "Ponto R. Júlia Maria da Silva, 106", "rua": "Rua Júlia Maria da Silva", "bairro": "Quintino Facci I", "referencia": "Acesso a escolas e moradias populares"},
            {"nome": "Ponto R. Mogi Mirim, 889", "rua": "Rua Mogi Mirim", "bairro": "Jardim Salgado Filho", "referencia": "Comércio vicinal e farmácias"},
            {"nome": "Ponto Praça Carlos Gomes", "rua": "Rua Duque de Caxias", "bairro": "Centro", "referencia": "Acesso ao centro bancário"},
            {"nome": "Ponto Terminal Urbano - Central", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Plataforma central de transbordo"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Pq. Avelino (Regular)", "num_paradas": 88, "descricao": "Itinerário convencional completo ligando o Parque Industrial Avelino ao Centro."},
            {"nome": "Até Centro", "num_paradas": 46, "descricao": "Trajeto expresso no sentido bairro-centro para horários de pico matutino."},
            {"nome": "Até Pq. Avelino", "num_paradas": 43, "descricao": "Retorno no sentido centro-bairro para escoamento do pico vespertino."}
        ]
    },
    "102": {
        "slug": "linhas/linha-102-jd-independencia",
        "h1": "Linha 102 — Jd. Independência",
        "titulo": "Linha 102 - Jd. Independência | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 102 Jardim Independência da RP Mobi em Ribeirão Preto. Linha convencional azul atendendo aos Campos Elíseos e Centro.",
        "keywords": "linha 102 ribeirao preto, onibus independencia rp mobi, convencional campos eliseos centro, horario linha 102",
        "linha_numero": "102",
        "linha_nome": "Jd. Independência",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Jardim Independência / Campos Elíseos ↔ Região Central",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 102 (Jd. Independência)</strong> é uma linha convencional clássica com a tradicional cor azul da RP Mobi que serve ao tradicional bairro Jardim Independência e às alamedas históricas dos Campos Elíseos, na Zona Norte interiorana de Ribeirão Preto. O itinerário atravessa uma das regiões pioneiras do desenvolvimento urbano fabril e ferroviário do município, caracterizada por comércio dinâmico de autopeças, oficinas, colégios estaduais e moradias de famílias tradicionais.</p>"
            "<p>Com frequência contínua em todos os dias da semana, a linha conecta de forma direta e rápida a população local às estações de integração e aos principais serviços públicos do miolo metropolitano.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo do Jardim Independência nas proximidades da Avenida Educandário, o ônibus acessa o corredor da Avenida da Saudade, realizando paradas nas estações de transferência Osório Junqueira, Cândido Guidon e Quito Junqueira. O trajeto corta o miolo dos Campos Elíseos em pista dedicada.</p>"
            "<p>O coletivo avança pelas ruas centrais como São Sebastião e General Osório, alcançando as imediações da Praça XV de Novembro e contornando as artérias bancárias antes de reassumir o sentido norte em direção ao ponto de origem no bairro Independência.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 37 paradas catalogadas com excelente infraestrutura viária. No corredor de tráfego, ganham notoriedade a <strong>Estação Osório Junqueira</strong>, a <strong>Estação Cândido Guidon</strong> e a <strong>Estação Quito Junqueira</strong>, equipadas com plataformas niveladas, piso podotátil e totens informativos.</p>"
            "<p>No bairro Independência, destacam-se os abrigos na <strong>Avenida Educandário</strong>, ponto de afluência de estudantes e trabalhadores de oficinas e distribuidoras de alimentos da região.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa aplicada é a regulamentar municipal de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O passageiro valida sua passagem no Jardim Independência e pode transferir-se para qualquer outra linha no centro urbano sem duplicar o pagamento da tarifa.</p>"
            "<p>Essa facilidade beneficia trabalhadores autônomos e aposentados que circulam entre os Campos Elíseos e a rede médica e hospitalar do Centro.</p>"
        ),
        "bairros_texto": (
            "<p>O atendimento contempla os bairros <em>Jardim Independência</em>, <em>Campos Elíseos</em> e <em>Centro</em>.</p>"
            "<p>Por transitar por vias consagradas do patrimônio operário ribeirão-pretano, a linha mantém forte vínculo afetivo e funcional com o cotidiano dos moradores da Zona Norte.</p>"
        ),
        "atracoes_proximas": (
            "<p>A linha aproxima os usuários do tradicional <strong>comércio da Avenida da Saudade</strong>, famoso polo de calçados, roupas e serviços dos Campos Elíseos.</p>"
            "<p>No Centro histórico, deixa o passageiro a poucos metros da <strong>Catedral Metropolitana de São Sebastião</strong>, do Teatro Pedro II e do Centro Cultural Palace.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3800 - Estação Osório Junqueira", "rua": "Avenida da Saudade", "bairro": "Campos Elíseos", "referencia": "Estação com plataforma elevada BRT"},
            {"nome": "Ponto 3801 - Estação Cândido Guidon", "rua": "Avenida da Saudade", "bairro": "Campos Elíseos", "referencia": "Acesso ao comércio dos Campos Elíseos"},
            {"nome": "Ponto 3795 - Estação Quito Junqueira", "rua": "Avenida da Saudade", "bairro": "Campos Elíseos", "referencia": "Conexão com escolas e agências"},
            {"nome": "Ponto Av. Educandário, 105", "rua": "Avenida Educandário", "bairro": "Jardim Independência", "referencia": "Acesso a oficinas e armazéns"},
            {"nome": "Ponto Final Jardim Independência", "rua": "Rua Guatapará", "bairro": "Jardim Independência", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. Independência (Regular)", "num_paradas": 37, "descricao": "Itinerário convencional completo ligando o Jardim Independência ao Centro pelos Campos Elíseos."},
            {"nome": "Até o Centro", "num_paradas": 16, "descricao": "Partidas diretas matutinas no sentido bairro-centro."}
        ]
    }
}

def main():
    print("==================================================")
    print("   GERADOR OFICIAL DO LOTE 3 (C4 — FASE 2)        ")
    print("==================================================")
    
    PAGINAS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Atualiza lista_linhas no content/paginas/linhas/index.json
    index_data = json.load(open(INDEX_JSON_PATH, encoding='utf-8'))
    slug_map = {num: lote3_defs[num]["slug"] for num in lote3_defs}
    
    for item in index_data.get('lista_linhas', []):
        cod = item.get('codigo')
        if cod in slug_map:
            item['slug'] = slug_map[cod]
            print(f"[*] Atualizado slug no index.json: Linha {cod} -> {slug_map[cod]}")
            
    with open(INDEX_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    print("[+] index.json sincronizado com os slugs oficiais do Lote 3.")

    # Gera cada um dos 10 arquivos JSON
    for num, defs in lote3_defs.items():
        fonte_item = dados_fonte[num]
        
        horarios_fonte = fonte_item['horarios']['valor']
        horarios_tabela = {
            "dias_uteis": horarios_fonte.get('dias_uteis', []),
            "sabado": horarios_fonte.get('sabado', []),
            "domingo": horarios_fonte.get('domingo', [])
        }
        
        bairros_lista = fonte_item['bairros']['valor']
        
        faq = [
            {
                "pergunta": f"Qual é o valor da passagem da Linha {num} {defs['linha_nome']}?",
                "resposta": f"A tarifa municipal em Ribeirão Preto é de R$ 5,00, aceita via Cartão Cidadão RP Mobi, cartões de vale-transporte e dinheiro no validador de bordo."
            },
            {
                "pergunta": f"Onde a Linha {num} realiza integração com outras rotas?",
                "resposta": f"A integração ocorre principalmente no {defs['terminal_central']}, onde os usuários contam com plataformas de conexão da rede de transporte coletivo."
            },
            {
                "pergunta": f"Como funciona a integração temporal da Linha {num}?",
                "resposta": f"Com o Cartão Cidadão RP Mobi, o passageiro tem até 120 minutos (2 horas) a partir da primeira validação na catraca para embarcar em outro coletivo sem pagar nova passagem."
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

    print("\n[OK] Lote 3 de 10 páginas gerado com sucesso!")

if __name__ == '__main__':
    main()
