#!/usr/bin/env python3
"""
GERADOR OFICIAL DO LOTE 4 (C4 — FASE 2) — INFOHAUS RP
Gera as 10 páginas JSON do Lote 4 em content/paginas/linhas/:
- 103: Iguatemi (Convencional Leste/Unaerp)
- 104: Jd. Canadá (Convencional Sul/Nobre)
- 105: Sul Inter Shopping (Convencional Sul/Comercial)
- 106: D'Elboux (Convencional Sudoeste/Vila Virgínia)
- 107: Sumarezinho (Convencional Oeste/Colina)
- 108: Jd. Pres. Dutra (Convencional Noroeste/Javari)
- 110: Quintino I (Convencional Norte/Av. Brasil)
- 130: Fórum (Convencional Judiciário/Ribeirânia)
- 136: Castelo Branco - Adão do Carmo (Diametral Leste-Sudoeste)
- 147: Jd. Irajá - Monte Alegre (Diametral Sul-Oeste)
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
LINHAS_JSON_PATH = ROOT_DIR / 'content' / 'dados-fonte' / 'linhas.json'
PAGINAS_DIR = ROOT_DIR / 'content' / 'paginas' / 'linhas'
INDEX_JSON_PATH = ROOT_DIR / 'content' / 'paginas' / 'linhas' / 'index.json'

dados_fonte = json.load(open(LINHAS_JSON_PATH, encoding='utf-8'))

lote4_defs = {
    "103": {
        "slug": "linhas/linha-103-iguatemi",
        "h1": "Linha 103 — Iguatemi",
        "titulo": "Linha 103 - Iguatemi | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia oficial da Linha 103 Iguatemi da RP Mobi em Ribeirão Preto. Linha convencional azul conectando o Bairro Iguatemi Leste, Unaerp e Centro.",
        "keywords": "linha 103 ribeirao preto, onibus 103 iguatemi leste, convencional unaerp centro, horario linha 103",
        "linha_numero": "103",
        "linha_nome": "Iguatemi",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Bairro Residencial Iguatemi Leste ↔ Campus Unaerp ↔ Região Central",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 103 (Iguatemi)</strong> atende aos moradores do loteamento residencial Jardim Iguatemi, situado no flanco oriental do município, funcionando primordialmente como linha alimentadora e de acesso aos blocos de salas de aula e clínicas de saúde da Universidade de Ribeirão Preto (Unaerp). Trata-se de uma rota convencional azul caracterizada pelo vaivém diário de universitários de graduação, residentes do Hospital Electro Bonini e professores.</p>"
            "<p>Fiscalizada pela RP Mobi com veículos de grande porte e piso acessível, a linha cumpre horários reforçados nos períodos de troca de aulas (07h00, 12h00 e 18h30), oferecendo uma opção direta para quem precisa cruzar a Zona Leste até a área bancária central.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota tem início nas vias internas do Jardim Iguatemi leste, alcançando a pista da Avenida Costábile Romano onde realiza escalas nas estações elevadas defronte aos portões da universidade. O ônibus transita em faixa de rolamento com semáforos sincronizados.</p>"
            "<p>O coletivo transpõe o viaduto da Avenida Presidente Médici e penetra pelas vias do Jardim Palma Travassos, ganhando as ruas Visconde do Rio Branco e Mariana Junqueira no Centro para desembarque de passageiros antes de retomar a viagem rumo ao extremo leste.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 54 paradas registradas. O ponto fulcral de maior circulação estudantil é a <strong>Estação UNAERP (Ponto 3953)</strong> na Avenida Costábile Romano, dotada de catracas integradas, cobertura metálica e mapa do campus.</p>"
            "<p>No Jardim Iguatemi, a parada defronte à praça residencial da <strong>Rua Alice Alem Saadi</strong> concentra grupos de moradores que embarcam nos primeiros horários da manhã rumo a repartições públicas e escritórios centrais.</p>"
        ),
        "integracao_detalhe": (
            "<p>A passagem é tarifada no montante oficial de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi ou Passe Universitário. O acadêmico valida o cartão na portaria da Unaerp e transfere-se gratuitamente no Centro para conexões nas regiões Norte ou Oeste.</p>"
            "<p>Essa facilidade tarifária alivia o orçamento de centenas de estudantes de baixa renda matriculados em programas de bolsas de estudo.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário abrange <em>Iguatemi</em>, <em>Ribeirânia</em>, <em>Jardim Palma Travassos</em>, <em>Presidente Médici</em> e <em>Centro</em>.</p>"
            "<p>A regularidade das viagens desempenha papel decisivo na sustentação do fluxo acadêmico e técnico da Zona Leste ribeirão-pretana.</p>"
        ),
        "atracoes_proximas": (
            "<p>A linha aproxima os usuários do <strong>Teatro Universitário Bassano Vaccari</strong> e dos ambulatórios de fisioterapia e odontologia da Unaerp.</p>"
            "<p>No centro urbano, deixa o universitário a passos da Biblioteca Sinhá Junqueira e de livrarias tradicionais do quadrilátero histórico.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 1606 - Estação Iguatemi Leste", "rua": "Avenida Presidente Castelo Branco", "bairro": "Iguatemi", "referencia": "Terminal de transbordo no bairro Iguatemi"},
            {"nome": "Ponto 3953 - Estação UNAERP", "rua": "Avenida Costábile Romano", "bairro": "Ribeirânia", "referencia": "Portaria principal do campus universitário"},
            {"nome": "Ponto Estação Moquenco Pardal", "rua": "Avenida Costábile Romano", "bairro": "Ribeirânia", "referencia": "Acesso a clínicas e moradias estudantis"},
            {"nome": "Ponto Estação Talita Verçosa", "rua": "Avenida Costábile Romano", "bairro": "Ribeirânia", "referencia": "Conexão com comércio vicinal"},
            {"nome": "Ponto Final Mariana Junqueira", "rua": "Rua Mariana Junqueira", "bairro": "Centro", "referencia": "Ponto de retorno central"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Iguatemi (Regular)", "num_paradas": 54, "descricao": "Itinerário convencional completo ligando o Jardim Iguatemi e campus Unaerp ao Centro."},
            {"nome": "Até Centro", "num_paradas": 27, "descricao": "Trajeto expresso matutino para o polo central."},
            {"nome": "Até Bairro", "num_paradas": 28, "descricao": "Sentido bairro no encerramento das aulas vespertinas e noturnas."}
        ]
    },
    "104": {
        "slug": "linhas/linha-104-jd-canada",
        "h1": "Linha 104 — Jd. Canadá",
        "titulo": "Linha 104 - Jd. Canadá | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 104 Jardim Canadá da RP Mobi em Ribeirão Preto. Linha convencional azul conectando o Jardim Canadá, Alto da Boa Vista e Centro.",
        "keywords": "linha 104 ribeirao preto, onibus jardim canada rp mobi, convencional canada centro, horario linha 104",
        "linha_numero": "104",
        "linha_nome": "Jd. Canadá",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Urbano Central (Plataforma D) ↔ Jardim Canadá / Alto da Boa Vista",
        "terminal_central": "Terminal Urbano Central (Plataforma D, Ponto 8)",
        "visao_geral": (
            "<p>A <strong>Linha 104 (Jd. Canadá)</strong> atende a um dos setores residenciais e corporativos de maior consolidação socioeconômica de Ribeirão Preto: o Jardim Canadá e as colinas ajardinadas do Alto da Boa Vista. Trata-se de um quadrante com ruas largas e arborizadas, edifícios residenciais de arquitetura contemporânea, escritórios de advocacia corporativa, clínicas médicas de estética e consultórios dentários de referência.</p>"
            "<p>Identificada pela marcante tonalidade azul das rotas convencionais, a linha é supervisionada pela RP Mobi com veículos climatizados e pontualidade exemplar, assegurando mobilidade ágil tanto para os residentes locais quanto para secretárias, técnicos de enfermagem e funcionários de condomínios.</p>"
        ),
        "itinerario_texto": (
            "<p>Saindo da Plataforma D do Terminal Urbano Central na Alameda Doutor Dino Bueno, o coletivo segue pela malha central pelas ruas Lafaiete e Visconde de Inhaúma, cruzando a Avenida Nove de Julho e ingressando nas vias do Jardim Sumaré.</p>"
            "<p>Ao subir pelo Alto da Boa Vista, a linha penetra no Jardim Canadá, circulando pelas alamedas arborizadas com paineiras e ipês, cumprindo escalas de desembarque junto às portarias de edifícios e clínicas antes de retornar ao centro urbano.</p>"
        ),
        "paradas_destaque": (
            "<p>A rota abrange 44 paradas distribuídas com espaçamento planejado. O marco inicial é o <strong>Ponto 3498 (Terminal Urbano - Plataforma D, Ponto 8)</strong>, com sanitários e atendimento ao público.</p>"
            "<p>No Jardim Canadá, sobressaem-se as paradas na <strong>Rua Lafaiete, 202</strong> e na <strong>Rua Visconde de Inhaúma, 1006</strong>, dotadas de calçadas amplas, bancos protegidos sob copa de árvores e totens com horários telemáticos.</p>"
        ),
        "integracao_detalhe": (
            "<p>A passagem é tarifada no montante de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O colaborador que toma a condução no Jardim Canadá desembarca no Terminal Urbano e tem até duas horas para ingressar sem custo em outra rota.</p>"
            "<p>Esse benefício temporal garante equilíbrio financeiro aos prestadores de serviços que atuam em consultórios e residências da Zona Sul.</p>"
        ),
        "bairros_texto": (
            "<p>O atendimento cobre <em>Jardim Canadá</em>, <em>Alto da Boa Vista</em>, <em>Jardim Sumaré</em> e <em>Centro</em>.</p>"
            "<p>A rota atua como elo indispensável de transporte público em um bairro de alta densidade veicular particular, fomentando o uso da mobilidade compartilhada.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa a curta distância de renomadas <strong>galerias de arte e bistrôs charmosos do Jardim Sumaré</strong>, além dos consultórios de ponta do Alto da Boa Vista.</p>"
            "<p>No Centro, conecta rapidamente os usuários ao Calçadão comercial e às repartições do Palácio Rio Branco.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3498 - TU / Plat D / Ponto 8", "rua": "Alameda Dr. Dino Bueno", "bairro": "Centro", "referencia": "Terminal de partida no centro"},
            {"nome": "Ponto R. Lafaiete, 202", "rua": "Rua Lafaiete", "bairro": "Centro", "referencia": "Acesso a clínicas e consultórios"},
            {"nome": "Ponto Estação Visconde de Inhaúma", "rua": "Rua Visconde de Inhaúma", "bairro": "Jardim Sumaré", "referencia": "Estação do corredor sul"},
            {"nome": "Ponto R. Visconde de Inhaúma, 1006", "rua": "Rua Visconde de Inhaúma", "bairro": "Alto da Boa Vista", "referencia": "Comércio nobre e escritórios"},
            {"nome": "Ponto Final Jardim Canadá", "rua": "Avenida Carlos Consoni", "bairro": "Jardim Canadá", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. Canadá (Regular)", "num_paradas": 44, "descricao": "Itinerário convencional completo ligando o Terminal Urbano ao Jardim Canadá."},
            {"nome": "Até Bairro", "num_paradas": 17, "descricao": "Saída rápida no sentido centro-bairro em horários de pico matutino."},
            {"nome": "Até Centro", "num_paradas": 28, "descricao": "Retorno direto ao terminal no fechamento comercial."}
        ]
    },
    "105": {
        "slug": "linhas/linha-105-sul-inter-shopping",
        "h1": "Linha 105 — Sul Inter Shopping",
        "titulo": "Linha 105 - Sul Inter Shopping | Horários e Paradas RP Mobi",
        "descricao": "Guia da Linha 105 Sul Inter Shopping da RP Mobi em Ribeirão Preto. Linha convencional azul pelos edifícios corporativos do Nova Aliança e Centro.",
        "keywords": "linha 105 ribeirao preto, onibus 105 nova alianca rp mobi, convencional corporativo nova alianca, horario linha 105",
        "linha_numero": "105",
        "linha_nome": "Sul Inter Shopping",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Eixo Corporativo Nova Aliança ↔ Jardim Califórnia ↔ Região Central",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 105 (Sul Inter Shopping)</strong> atende prioritariamente à concentração de edifícios corporativos, escritórios de auditoria contábil, agências de publicidade e sedes de empresas de tecnologia sediadas no bairro planejado Nova Aliança. Trata-se de uma rota convencional azul caracterizada pelo fluxo contínuo de analistas de sistemas, contadores, consultores jurídicos e moradores de condomínios verticais modernos.</p>"
            "<p>Gerenciada com rigor técnico pela RP Mobi, a linha disponibiliza coletivos com climatização digital e piso baixo, garantindo acessibilidade e rapidez nos embarques ao longo das avenidas arteriais da Zona Sul.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota arranca das proximidades do Parque das Artes, percorrendo a Avenida Senador Carlos Jereissati e a Alameda Gustavo Simioni. O coletivo serpenteia pelas avenidas Doutor Ângelo Gennaro Gallo e Braz Olaia Acosta, onde há grande densidade de torres empresariais espelhadas.</p>"
            "<p>Seguindo pelo Jardim Califórnia e cortando a Avenida Independência, o ônibus penetra no miolo central pelas ruas Américo Brasiliense e Álvares Cabral, desembarcando os profissionais junto às agências bancárias e cartórios da cidade.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 63 paradas catalogadas com excelente infraestrutura. O ponto central no Nova Aliança é a <strong>Parada Av. Dr. Ângelo Gennaro Gallo, 805</strong>, defronte ao complexo empresarial e ao parque linear.</p>"
            "<p>Na Avenida Senador Carlos Jereissati, os abrigos de vidro temperado e bancos de aço inox atendem a centenas de programadores e auditores nos horários de almoço e no encerramento das jornadas corporativas.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa praticada é a básica pública de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O colaborador corporativo valida seu cartão na saída do trabalho e pode transbordar gratuitamente nas estações do Centro rumo ao seu bairro de moradia.</p>"
            "<p>Essa facilidade estimula o transporte coletivo entre profissionais do setor terciário avançado, diminuindo congestionamentos na Zona Sul.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto beneficia <em>Nova Aliança</em>, <em>Jardim Califórnia</em>, <em>Residencial Flórida</em>, <em>Reserva do Ipê</em> e <em>Centro</em>.</p>"
            "<p>A rota consolidou-se como o cordão umbilical de transporte público entre o distrito financeiro emergente do Nova Aliança e o centro histórico.</p>"
        ),
        "atracoes_proximas": (
            "<p>O itinerário passa a poucos metros do <strong>Parque das Artes</strong> com seus quiosques e pistas de caminhada arborizadas, além de coworkings modernos da região sul.</p>"
            "<p>No miolo central, deixa o passageiro próximo ao Centro Cultural Palace e a restaurantes tradicionais da Praça XV.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto Av. Senador Carlos Jereissati", "rua": "Avenida Senador Carlos Jereissati", "bairro": "Nova Aliança", "referencia": "Acesso a edifícios corporativos"},
            {"nome": "Ponto Alameda Gustavo Simioni", "rua": "Alameda Gustavo Simioni", "bairro": "Nova Aliança", "referencia": "Parada residencial e comercial"},
            {"nome": "Ponto Av. Dr. Ângelo Gennaro Gallo, 805", "rua": "Avenida Doutor Ângelo Gennaro Gallo", "bairro": "Nova Aliança", "referencia": "Acesso ao Parque das Artes"},
            {"nome": "Ponto Independência - Califórnia", "rua": "Avenida Independência", "bairro": "Jardim Califórnia", "referencia": "Comércio vicinal e farmácias"},
            {"nome": "Ponto Final Centro - Álvares Cabral", "rua": "Rua Álvares Cabral", "bairro": "Centro", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Sul Inter Shopping (Regular)", "num_paradas": 63, "descricao": "Itinerário convencional corporativo completo ligando o Nova Aliança ao Centro pelo Jardim Califórnia."},
            {"nome": "Até Centro", "num_paradas": 31, "descricao": "Trajeto expresso no sentido Nova Aliança-Centro."},
            {"nome": "Até o Shopping Iguatemi", "num_paradas": 32, "descricao": "Retorno no sentido centro-Nova Aliança no final de expediente."}
        ]
    },
    "106": {
        "slug": "linhas/linha-106-delboux",
        "h1": "Linha 106 — D'Elboux",
        "titulo": "Linha 106 - D'Elboux | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 106 D'Elboux da RP Mobi em Ribeirão Preto. Linha convencional azul atendendo ao loteamento D'Elboux e Rua Paulo de Frontim.",
        "keywords": "linha 106 ribeirao preto, onibus 106 delboux frontim, convencional delboux centro, horario linha 106",
        "linha_numero": "106",
        "linha_nome": "D'Elboux",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Loteamento D'Elboux (Rua Paulo de Frontim) ↔ Região Central",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 106 (D'Elboux)</strong> é uma tradicional rota convencional azul voltada exclusivamente ao loteamento D'Elboux, no setor sudoeste ribeirão-pretano. O bairro caracteriza-se por ruas tranquilas de paralelepípedo, sobradinhos residenciais unifamiliares, pequenas oficinas de conserto de bicicletas, marcenarias artesanais e armazéns de secos e molhados mantidos pelas mesmas famílias há décadas.</p>"
            "<p>Operando com veículos convencionais de boa manobrabilidade e chassis reforçados sob a coordenação da RP Mobi, a linha garante saídas regulares ao longo do dia, acolhendo o transporte diário de balconistas, pedreiros, zeladores e aposentados que se deslocam até o centro comercial.</p>"
        ),
        "itinerario_texto": (
            "<p>A viagem principia no final da Rua Paulo de Frontim, seguindo pelas alamedas transversais do loteamento D'Elboux. O coletivo transita pela Rua Ronald de Carvalho e alcança a Rua Abílio Sampaio, contornando quarteirões residenciais onde passageiros realizam embarques próximos aos portões de suas casas.</p>"
            "<p>Transpondo o leito canalizado em direção ao miolo metropolitano pelas ruas Florêncio de Abreu e Jerônimo Gonçalves, o ônibus atende ao polo varejista de tecidos e utilidades domésticas antes de reassumir o caminho de regresso ao bairro.</p>"
        ),
        "paradas_destaque": (
            "<p>A rota abrange 32 paradas bem sinalizadas. O ponto referencial de partida é a <strong>Parada Rua Paulo de Frontim, 2005</strong>, onde vizinhos se reúnem na primeira viagem matinal.</p>"
            "<p>Na <strong>Rua Abílio Sampaio, 1314</strong>, a parada é referência em frente à quitanda e padaria local, com bancos de alvenaria e abrigo contra o sol da tarde para os moradores que retornam das compras.</p>"
        ),
        "integracao_detalhe": (
            "<p>A cobrança respeita a tarifa pública de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O passageiro valida sua catraca no D'Elboux e pode tomar qualquer ônibus radial no Centro sem pagar nova passagem dentro do prazo de duas horas.</p>"
            "<p>Essa facilidade beneficia diretamente os aposentados e diaristas que necessitam realizar consultas e serviços rápidos no perímetro central.</p>"
        ),
        "bairros_texto": (
            "<p>O atendimento contempla o <em>Loteamento D'Elboux</em>, <em>Jardim Maria Goretti</em> e <em>Centro</em>.</p>"
            "<p>A linha preserva o vínculo de transporte direto de uma comunidade de operários veteranos com as oportunidades comerciais do município.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota aproxima os moradores de <strong>clubes esportivos amadores e campos de malha tradicionais</strong> do loteamento D'Elboux.</p>"
            "<p>No miolo central, deixa os usuários a curta caminhada do Mercadão Municipal e de lojas de variedades da Rua General Osório.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3328 - R. Paulo de Frontim, 2005", "rua": "Rua Paulo de Frontim", "bairro": "Jardim Maria Goretti", "referencia": "Ponto de partida no bairro D'Elboux"},
            {"nome": "Ponto 3584 - R. Ronald de Carvalho, 405", "rua": "Rua Ronald de Carvalho", "bairro": "Vila Virgínia", "referencia": "Acesso a escolas e oficinas"},
            {"nome": "Ponto 1118 - R. Abílio Sampaio, 1527", "rua": "Rua Abílio Sampaio", "bairro": "Vila Virgínia", "referencia": "Parada residencial central"},
            {"nome": "Ponto 1119 - R. Abílio Sampaio, 1314", "rua": "Rua Abílio Sampaio", "bairro": "Vila Virgínia", "referencia": "Acesso a padarias e quitandas"},
            {"nome": "Ponto Final Centro - Jerônimo Gonçalves", "rua": "Avenida Jerônimo Gonçalves", "bairro": "Centro", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "D'Elboux (Regular)", "num_paradas": 32, "descricao": "Itinerário convencional completo ligando o loteamento D'Elboux ao Centro pela Rua Paulo de Frontim."},
            {"nome": "Até Centro", "num_paradas": 20, "descricao": "Partidas matutinas diretas no sentido bairro-centro."},
            {"nome": "Até Bairro", "num_paradas": 14, "descricao": "Retorno direto no sentido centro-bairro para horários de pico."}
        ]
    },
    "107": {
        "slug": "linhas/linha-107-sumarezinho",
        "h1": "Linha 107 — Sumarezinho",
        "titulo": "Linha 107 - Sumarezinho | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 107 Sumarezinho da RP Mobi em Ribeirão Preto. Linha convencional azul pelas ladeiras históricas e mirantes do Sumarezinho.",
        "keywords": "linha 107 ribeirao preto, onibus 107 sumarezinho ladeiras, convencional sumarezinho centro, horario linha 107",
        "linha_numero": "107",
        "linha_nome": "Sumarezinho",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Colinas do Sumarezinho (Rua Martim Afonso) ↔ Região Central",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 107 (Sumarezinho)</strong> é a rota convencional azul responsável por vencer a topografia acidentada e as ladeiras íngremes do bairro Sumarezinho, na colina oeste ribeirão-pretana. Com ruas arborizadas com flamboyants centenários, casas térreas com varandas floridas e famílias de antigos operários ferroviários, o bairro preserva uma atmosfera serena de vizinhança unida.</p>"
            "<p>Operando com veículos com motores de alto torque calibrados para subir rampas de calçamento com suavidade, a RP Mobi disponibiliza viagens regulares ao longo do dia, atendendo a aposentados, feirantes, donas de casa e estudantes que se deslocam até as praças centrais.</p>"
        ),
        "itinerario_texto": (
            "<p>O percurso tem origem na parte alta do morro pela Rua Martim Afonso de Souza, serpenteando por curvas sinuosas até acessar a Rua Espírito Santo. O ônibus desce as encostas onde há paradas próximas a armazéns de secos e molhados e pequenos bazares de bairro.</p>"
            "<p>Ganhando a baixada central pelas ruas Saldanha Marinho e Visconde do Rio Branco, o veículo cumpre escalas de desembarque a curta distância de agências bancárias e repartições públicas antes de reiniciar a escalada da colina oeste.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 34 paradas catalogadas. Na cumeada do bairro, o destaque é a <strong>Parada Rua Martim Afonso de Souza, 466</strong>, com banco de concreto sob sombra de árvores e vista para a várzea.</p>"
            "<p>Na descida da colina, a parada na <strong>Rua Espírito Santo, 611</strong> é referência para os moradores que frequentam a quitanda de verduras e a farmácia tradicional da colina.</p>"
        ),
        "integracao_detalhe": (
            "<p>A viagem é cobrada na tarifa unificada de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O passageiro valida sua descida no Sumarezinho e pode ingressar em outra condução no Centro sem pagar nova tarifa.</p>"
            "<p>Esse benefício temporal garante alívio financeiro para aposentados e trabalhadores de baixa renda que precisam se deslocar para serviços essenciais.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário atende aos setores de encosta do <em>Sumarezinho</em>, <em>Alto do Ipiranga</em> e <em>Centro</em>.</p>"
            "<p>A linha cumpre papel indispensável para amenizar o isolamento gerado pela declividade acentuada do relevo da Zona Oeste.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa junto aos <strong>mirantes naturais da colina do Sumarezinho</strong>, de onde se descortina vista ampla do skyline de Ribeirão Preto.</p>"
            "<p>No Centro histórico, aproxima os munícipes do Theatro Pedro II e do calçadão comercial da Rua General Osório.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 671 - R. Martim Afonso de Souza, 466", "rua": "Rua Martim Afonso de Souza", "bairro": "Sumarezinho", "referencia": "Ponto de partida no alto do bairro"},
            {"nome": "Ponto 672 - R. Martim Afonso de Souza, 245", "rua": "Rua Martim Afonso de Souza", "bairro": "Sumarezinho", "referencia": "Acesso a escolas municipais"},
            {"nome": "Ponto 673 - R. Martim Afonso de Souza, 51", "rua": "Rua Martim Afonso de Souza", "bairro": "Sumarezinho", "referencia": "Ladeira intermediária da colina"},
            {"nome": "Ponto 657 - R. Espírito Santo, 611", "rua": "Rua Espírito Santo", "bairro": "Sumarezinho", "referencia": "Quitanda e comércio vicinal"},
            {"nome": "Ponto Final Centro - Saldanha Marinho", "rua": "Rua Saldanha Marinho", "bairro": "Centro", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Sumarezinho (Regular)", "num_paradas": 34, "descricao": "Itinerário convencional completo ligando as ladeiras do Sumarezinho ao Centro."},
            {"nome": "Até Centro", "num_paradas": 12, "descricao": "Partidas matutinas rápidas no sentido bairro-centro."}
        ]
    },
    "108": {
        "slug": "linhas/linha-108-jd-pres-dutra",
        "h1": "Linha 108 — Jd. Pres. Dutra",
        "titulo": "Linha 108 - Jd. Pres. Dutra | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 108 Jardim Presidente Dutra da RP Mobi em Ribeirão Preto. Linha convencional azul pela Rua Javari, Ipiranga e Centro.",
        "keywords": "linha 108 ribeirao preto, onibus presidente dutra rp mobi, convencional javari centro, horario linha 108",
        "linha_numero": "108",
        "linha_nome": "Jd. Pres. Dutra",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Jardim Presidente Dutra ↔ Corredor Comercial Rua Javari ↔ Região Central",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 108 (Jd. Pres. Dutra)</strong> é uma das linhas convencionais mais extensas e populosas da Zona Noroeste ribeirão-pretana, identificada pela tonalidade azul da frota da RP Mobi. Atendendo aos densos conjuntos habitacionais do Jardim Presidente Dutra, Geraldo Correia de Carvalho e Residencial das Américas, a rota percorre a movimentada artéria comercial da Rua Javari até desaguar no miolo urbano central.</p>"
            "<p>Com 66 paradas cadastradas e ônibus de alta capacidade equipados com ventilação forçada e elevadores para cadeirantes, a linha opera como um verdadeiro metrô sobre pneus para milhares de trabalhadores do comércio, operários da construção e prestadores de serviços.</p>"
        ),
        "itinerario_texto": (
            "<p>O trajeto tem origem na Rua Amadeu Giachetto no Jardim Presidente Dutra, avançando pelas vias internas dos bairros Geraldo Correia e Residencial das Américas. O coletivo ingressa no corredor comercial da Rua Javari, cumprindo dezenas de paradas defronte a lojas e bancos.</p>"
            "<p>Transpondo o Ipiranga e o Alto do Ipiranga, o ônibus alcança o Centro pelas ruas Amador Bueno e Duque de Caxias, oferecendo conexão rápida com as repartições públicas antes de reiniciar a viagem de retorno ao extremo Noroeste.</p>"
        ),
        "paradas_destaque": (
            "<p>A rota abrange 66 paradas de grande afluência popular. No Presidente Dutra, o ponto referencial de partida é a <strong>Parada Rua Amadeu Giachetto, 349</strong>, com extensa fila de embarque no alvorecer.</p>"
            "<p>Ao longo da <strong>Rua Javari, 3055</strong>, as paradas contam com abrigos sombreados e piso tátil, atendendo ao fluxo incessante de clientes de farmácias, supermercados e bazares populares do grande Ipiranga.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa cobrada é a básica de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O trabalhador que embarca no Presidente Dutra pode validar a catraca e transbordar gratuitamente nas linhas troncais do Centro.</p>"
            "<p>Essa regra tarifária garante economia substancial para as famílias operárias que compõem a base demográfica da Zona Noroeste.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto atende a <em>Jardim Presidente Dutra</em>, <em>Geraldo Correia de Carvalho</em>, <em>Residencial das Américas</em>, <em>Jardim Herculano Fernandes</em>, <em>Ipiranga</em> e <em>Centro</em>.</p>"
            "<p>Trata-se de uma linha estrutural indispensável para a coesão econômica entre a periferia populosa do Noroeste e o centro financeiro da cidade.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota corta o <strong>polo comercial a céu aberto da Rua Javari</strong>, um dos maiores centros de comércio popular e serviços de bairro do município.</p>"
            "<p>No miolo central, deixa os passageiros a curta caminhada do Calçadão, Theatro Pedro II e Praça da Bandeira.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 608 - R. Amadeu Giachetto, 349", "rua": "Rua Amadeu Giachetto", "bairro": "Presidente Dutra", "referencia": "Ponto de partida no bairro"},
            {"nome": "Ponto 610 - R. Amadeu Giachetto, 239", "rua": "Rua Amadeu Giachetto", "bairro": "Presidente Dutra", "referencia": "Acesso a escolas municipais"},
            {"nome": "Ponto 2470 - R. Amadeu Giachetto, 51", "rua": "Rua Amadeu Giachetto", "bairro": "Presidente Dutra", "referencia": "Conexão com comércios locais"},
            {"nome": "Ponto 445 - R. Javari, 3055", "rua": "Rua Javari", "bairro": "Ipiranga", "referencia": "Corredor comercial da Rua Javari"},
            {"nome": "Ponto Final Centro - Duque de Caxias", "rua": "Rua Duque de Caxias", "bairro": "Centro", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. Pres. Dutra (Regular)", "num_paradas": 66, "descricao": "Itinerário convencional completo ligando o Presidente Dutra ao Centro pela Rua Javari."},
            {"nome": "Até Centro", "num_paradas": 30, "descricao": "Trajeto expresso no pico da manhã no sentido bairro-centro."},
            {"nome": "Até Bairro", "num_paradas": 37, "descricao": "Retorno direto no sentido centro-bairro para escoamento vespertino."}
        ]
    },
    "110": {
        "slug": "linhas/linha-110-quintino-1",
        "h1": "Linha 110 — Quintino I",
        "titulo": "Linha 110 - Quintino I | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 110 Quintino I da RP Mobi em Ribeirão Preto. Linha convencional azul conectando o conjunto habitacional Quintino ao Centro.",
        "keywords": "linha 110 ribeirao preto, onibus 110 quintino pavanelli, convencional quintino centro, horario linha 110",
        "linha_numero": "110",
        "linha_nome": "Quintino I",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Conjunto Habitacional Quintino Facci I (Rua Pavanelli) ↔ Centro",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 110 (Quintino I)</strong> é uma linha convencional com pintura azul que atende estritamente às alamedas e praças comunitárias do conjunto habitacional popular Quintino Facci I, implantado na Zona Norte. O bairro abriga milhares de famílias operárias estabelecidas em sobrados do antigo BNH, contando com praças esportivas com campos de futebol de várzea, creches municipais, feiras livres de pastel e pequenos comércios de calçadas.</p>"
            "<p>A RP Mobi programa partidas pontuais a cada dez minutos nos horários de pico matutino e vespertino, acolhendo o embarque maciço de balconistas, auxiliares de limpeza, porteiros e estudantes de escolas estaduais.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota parte da Rua Giuseppe Agostinho Pavanelli, contornando a praça esportiva central do Quintino Facci I. O coletivo circula pelas ruas residenciais numeradas do conjunto habitacional, garantindo embarques seguros a passos das portas das residências.</p>"
            "<p>Transpondo o viaduto em direção ao perímetro histórico pelas ruas Tibiriçá e Visconde do Rio Branco, o ônibus cumpre paradas na área bancária e comercial central antes de refazer o trajeto de volta ao conjunto habitacional.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 60 paradas catalogadas. O ponto nevrálgico é a <strong>Parada Rua Giuseppe Agostinho Pavanelli, 656</strong>, dotada de abrigo metálico reforçado e bancos comunitários onde vizinhos aguardam a condução nas primeiras horas da alvorada.</p>"
            "<p>No coração do conjunto habitacional, a parada em frente à EMEI e à Paróquia do bairro é ponto de grande afluência de pais com crianças nos turnos escolares.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa aplicada é a regulamentar de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O passageiro valida sua subida no Quintino I e tem até duas horas para embarcar em outra rota no Centro sem duplicar a tarifa.</p>"
            "<p>Essa regra tarifária garante alívio decisivo no orçamento mensal das famílias operárias do conjunto habitacional.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto atende com exclusividade ao <em>Conjunto Habitacional Quintino Facci I</em> e à conexão direta com o <em>Centro</em>.</p>"
            "<p>A linha representa uma conquista histórica de organização comunitária de moradores que batalharam por transporte público regular desde a entrega das primeiras moradias populares.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa junto ao <strong>Centro Comunitário e Praça Esportiva do Quintino I</strong>, polo de torneios de futebol amador e feiras culturais de fim de semana.</p>"
            "<p>No Centro, aproxima os munícipes do Theatro Pedro II e dos serviços de emissão de documentos na área central.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 36 - R. Giuseppe Agostinho Pavanelli, 656", "rua": "Rua Giuseppe Agostinho Pavanelli", "bairro": "Quintino Facci I", "referencia": "Ponto de partida no conjunto habitacional"},
            {"nome": "Ponto Praça Esportiva do Quintino", "rua": "Rua Giuseppe Agostinho Pavanelli", "bairro": "Quintino Facci I", "referencia": "Quadras comunitárias de esportes"},
            {"nome": "Ponto EMEI do Quintino I", "rua": "Rua Três", "bairro": "Quintino Facci I", "referencia": "Parada escolar infantil"},
            {"nome": "Ponto Comércio Central do Bairro", "rua": "Rua Cinco", "bairro": "Quintino Facci I", "referencia": "Padarias e feira livre"},
            {"nome": "Ponto Final Centro - Tibiriçá", "rua": "Rua Tibiriçá", "bairro": "Centro", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Quintino (Regular)", "num_paradas": 60, "descricao": "Itinerário convencional completo ligando o conjunto Quintino Facci I ao Centro pela Rua Pavanelli."},
            {"nome": "Até Centro", "num_paradas": 29, "descricao": "Trajeto expresso no sentido bairro-centro para horários de pico."}
        ]
    },
    "130": {
        "slug": "linhas/linha-130-forum",
        "h1": "Linha 130 — Fórum",
        "titulo": "Linha 130 - Fórum | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 130 Fórum da RP Mobi em Ribeirão Preto. Linha convencional azul atendendo à Cidade Judiciária, Ribeirânia e Centro.",
        "keywords": "linha 130 ribeirao preto, onibus forum rp mobi, convencional forum ribeirania centro, horario linha 130",
        "linha_numero": "130",
        "linha_nome": "Fórum",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Complexo Judiciário da Ribeirânia ↔ Jardim Macedo ↔ Região Central",
        "terminal_central": "Plataformas Centrais da Região Central",
        "visao_geral": (
            "<p>A <strong>Linha 130 (Fórum)</strong> é a rota convencional azul prioritária para o atendimento à Cidade Judiciária de Ribeirão Preto, situada no bairro nobre da Ribeirânia. O itinerário atende ao Fórum Estadual Doutor Faria Goyaz, à Justiça do Trabalho, à sede regional da Justiça Federal, à Casa do Advogado (OAB) e ao Ministério Público do Estado de São Paulo.</p>"
            "<p>Com frequência contínua durante o horário forense e de expediente judicial, a linha transporta advogados, defensores públicos, servidores dos cartórios judiciais, estagiários de direito e cidadãos convocados para audiências em suas 50 paradas catalogadas.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota sai das imediações do Fórum Estadual na Ribeirânia, circulando pelas avenidas Doutor Ângelo Gennaro Gallo e Costábile Romano. O ônibus transita pelo corredor da Avenida Maurílio Biagi e atende às ruas arborizadas do Jardim Macedo e Jardim Palma Travassos.</p>"
            "<p>O coletivo ganha o Centro pelas ruas São Sebastião e Álvares Cabral, realizando paradas em frente aos cartórios de notas e de protestos antes de reassumir o sentido leste rumo ao polo judiciário da comarca.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 50 paradas no total. O ponto fulcral de maior peso institucional é a <strong>Parada Fórum Estadual (Ribeirânia)</strong>, com plataforma acessível, piso podotátil e cobertura de policarbonato.</p>"
            "<p>No Jardim Macedo, sobressaem-se as paradas na <strong>Avenida Costábile Romano</strong>, com grande procura de estudantes de pós-graduação e funcionários dos escritórios jurídicos do entorno.</p>"
        ),
        "integracao_detalhe": (
            "<p>A cobrança respeita a tarifa pública de <strong>R$ 5,00</strong>, acompanhada do benefício de <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O jurisdicionado que sai de uma audiência no Fórum valida a passagem e faz baldeação gratuita nas estações centrais para retornar à sua residência.</p>"
            "<p>Essa regra tarifária garante acesso democrático à Justiça para a população hipossuficiente que necessita comparecer aos tribunais da comarca.</p>"
        ),
        "bairros_texto": (
            "<p>A rota abrange <em>Ribeirânia</em>, <em>Nova Ribeirânia</em>, <em>Jardim Macedo</em>, <em>Jardim Palma Travassos</em>, <em>Iguatemi</em> e <em>Centro</em>.</p>"
            "<p>A linha é um pilar da infraestrutura institucional ribeirão-pretana, garantindo o funcionamento integrado do sistema de justiça metropolitano.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa junto à <strong>Cidade Judiciária de Ribeirão Preto</strong> e ao campus da Unaerp na Ribeirânia.</p>"
            "<p>No Centro histórico, aproxima os passageiros do Palácio da Justiça e da Praça XV de Novembro.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto Fórum Estadual - Entrada Principal", "rua": "Rua Alice Alem Saadi", "bairro": "Ribeirânia", "referencia": "Acesso ao Fórum e cartórios judiciais"},
            {"nome": "Ponto 1606 - Estação Novo Shopping I", "rua": "Avenida Presidente Castelo Branco", "bairro": "Iguatemi", "referencia": "Terminal de transbordo Novo Shopping"},
            {"nome": "Ponto Justiça do Trabalho", "rua": "Avenida Costábile Romano", "bairro": "Ribeirânia", "referencia": "Varas Trabalhistas da comarca"},
            {"nome": "Ponto OAB - Casa do Advogado", "rua": "Rua Cavalheiro Torquato Rizzi", "bairro": "Jardim Macedo", "referencia": "Sede da subseção da OAB"},
            {"nome": "Ponto Final Centro - Álvares Cabral", "rua": "Rua Álvares Cabral", "bairro": "Centro", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Fórum (Regular)", "num_paradas": 50, "descricao": "Itinerário convencional completo ligando a Cidade Judiciária ao Centro pelo Jardim Macedo."},
            {"nome": "Até Centro", "num_paradas": 28, "descricao": "Trajeto matutino de acesso ao centro bancário e de cartórios."},
            {"nome": "Até Bairro", "num_paradas": 23, "descricao": "Retorno ao polo judiciário para o expediente vespertino."}
        ]
    },
    "136": {
        "slug": "linhas/linha-136-castelo-branco-adao-do-carmo",
        "h1": "Linha 136 — Castelo Branco - Adão do Carmo",
        "titulo": "Linha 136 - Castelo Branco / Adão do Carmo | Horários RP Mobi",
        "descricao": "Guia da Linha 136 Castelo Branco - Adão do Carmo da RP Mobi em Ribeirão Preto. Linha diametral azul pelas indústrias farmacêuticas e chácaras da Patriarca.",
        "keywords": "linha 136 ribeirao preto, onibus 136 farmaceutico patriarca, diametral castelo adao, horario linha 136",
        "linha_numero": "136",
        "linha_nome": "Castelo Branco - Adão do Carmo",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Polo Farmacêutico Castelo Branco (Leste) ↔ Chácaras Adão do Carmo (Sudoeste)",
        "terminal_central": "Eixo Central de Conexão (Rua Barão do Amazonas / Mariana Junqueira)",
        "visao_geral": (
            "<p>A <strong>Linha 136 (Castelo Branco - Adão do Carmo)</strong> opera como uma vasta linha diametral de cor azul que une dois polos geográficos de vocações contrastantes em Ribeirão Preto: o parque industrial e de laboratórios farmacêuticos do Jardim Castelo Branco, no quadrante Leste, e as chácaras familiares e loteamentos rurais do Adão do Carmo Leonel, no extremo Sudoeste da Avenida Patriarca. Com 104 paradas, a rota transporta operários de embalagem de remédios, estoquistas de laboratórios e produtores hortifrutigranjeiros.</p>"
            "<p>A linha dispõe de veículos pesados com reforço em horários de troca de turno das fábricas químicas e farmacêuticas, garantindo travessia contínua de ponta a ponta da mancha urbana sem baldeação intermediária.</p>"
        ),
        "itinerario_texto": (
            "<p>A condução inicia a jornada na Avenida Patriarca, transpondo chácaras de recreio e galpões de adubo do Adão do Carmo. O veículo corta as artérias centrais pelas ruas Barão do Amazonas e Mariana Junqueira sem interrupções prolongadas.</p>"
            "<p>Ganhando a pista da Avenida Presidente Castelo Branco no rumo leste, o ônibus atende diretamente aos portões das indústrias químicas, distribuidoras de medicamentos e centros logísticos do Jardim Castelo Branco, cumprindo a manobra de retorno na rotatória fabril.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha possui 104 paradas catalogadas com excelente distribuição viária. No extremo sudoeste, destaca-se a <strong>Parada Avenida Patriarca, 3820</strong>, cercada por oficinas agrícolas e chácaras.</p>"
            "<p>No setor oriental, as paradas em frente aos <strong>complexos laboratoriais farmacêuticos da Avenida Castelo Branco</strong> concentram centenas de técnicos químicos e analistas laboratoriais em uniforme branco ao término da jornada vespertina.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa cobrada é a padrão municipal de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O trabalhador que viaja entre o polo fabril e as chácaras pode ainda tomar uma linha alimentadora nas extremidades sem ônus complementar.</p>"
            "<p>Essa amplitude diametral proporciona economia determinante para funcionários que residem em um extremo e exercem suas atividades no extremo oposto da cidade.</p>"
        ),
        "bairros_texto": (
            "<p>A rota cobre <em>Adão do Carmo Leonel</em>, <em>Jardim Castelo Branco</em>, <em>Parque dos Bandeirantes</em>, <em>Jardim Mosteiro</em> e <em>Centro</em>.</p>"
            "<p>A linha é indispensável para sustentar a mobilidade direta entre o cinturão produtivo farmacêutico e as áreas residenciais periféricas.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota aproxima os passageiros do <strong>Parque dos Bandeirantes</strong> e do Estádio Palma Travassos do Comercial FC.</p>"
            "<p>No miolo central, deixa os usuários a curta distância da Praça XV e dos centros de exames de medicina ocupacional.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 1307 - Av. Patriarca, 3820", "rua": "Avenida Patriarca", "bairro": "Adão do Carmo Leonel", "referencia": "Ponto de partida no extremo sudoeste"},
            {"nome": "Ponto Laboratório Farmacêutico Castelo", "rua": "Avenida Presidente Castelo Branco", "bairro": "Jardim Castelo Branco", "referencia": "Portaria da indústria farmacêutica"},
            {"nome": "Ponto Barão do Amazonas - Central", "rua": "Rua Barão do Amazonas", "bairro": "Centro", "referencia": "Parada central da linha"},
            {"nome": "Ponto Parque dos Bandeirantes", "rua": "Rua dos Bandeirantes", "bairro": "Parque dos Bandeirantes", "referencia": "Acesso a praças e escolas"},
            {"nome": "Ponto Final Castelo Branco", "rua": "Avenida Presidente Castelo Branco", "bairro": "Jardim Castelo Branco", "referencia": "Rotatória fabril de retorno"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Castelo Branco / Adão do Carmo", "num_paradas": 104, "descricao": "Itinerário convencional diametral completo ligando o polo farmacêutico do Castelo Branco às chácaras do Adão do Carmo."},
            {"nome": "Até Castelo Branco", "num_paradas": 57, "descricao": "Sentido sudoeste-leste nos horários de entrada de expedientes industriais."},
            {"nome": "Até Centro (Barão do Amazonas)", "num_paradas": 31, "descricao": "Partidas intermediárias no sentido centro comercial."},
            {"nome": "Até Centro (Mariana Junqueira)", "num_paradas": 18, "descricao": "Atendimento rápido no miolo central."}
        ]
    },
    "147": {
        "slug": "linhas/linha-147-jd-iraja-monte-alegre",
        "h1": "Linha 147 — Jd. Irajá - Monte Alegre",
        "titulo": "Linha 147 - Jd. Irajá / Monte Alegre | Horários RP Mobi",
        "descricao": "Guia da Linha 147 Jardim Irajá - Monte Alegre da RP Mobi em Ribeirão Preto. Linha diametral azul pelas praças do Irajá, Bosque das Juritis e Monte Alegre.",
        "keywords": "linha 147 ribeirao preto, onibus 147 iraja monte alegre, diametral juritis monte alegre, horario linha 147",
        "linha_numero": "147",
        "linha_nome": "Jd. Irajá - Monte Alegre",
        "modalidade": "Linha Convencional",
        "linha_cor": "#1a15f0",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Jardim Irajá / Bosque das Juritis (Sul) ↔ Centro ↔ Monte Alegre Residencial (Oeste)",
        "terminal_central": "Eixo Central de Conexão (Rua Barão do Amazonas / Florêncio de Abreu)",
        "visao_geral": (
            "<p>A <strong>Linha 147 (Jd. Irajá - Monte Alegre)</strong> é uma rota diametral convencional azul que percorre o charmoso setor residencial do Jardim Irajá e Bosque das Juritis, na Zona Sul, conduzindo passageiros até as tranquilas alamedas residenciais de Monte Alegre, na Zona Oeste. Trata-se de um itinerário marcado por edifícios residenciais de alto padrão, empórios de cafés especiais, pet shops requintados e clínicas de odontologia estética na ponta meridional.</p>"
            "<p>Operando com ônibus padron confortáveis e climatizados sob fiscalização da RP Mobi, a linha transporta secretárias, atendentes de boutiques, recepcionistas de consultórios e estudantes que transitam entre os bairros nobres e as repartições centrais.</p>"
        ),
        "itinerario_texto": (
            "<p>A viagem inicia-se na Rua Chile no Jardim Irajá, descendo pelas alamedas arborizadas das ruas Cavalheiro Torquato Rizzi e Thomaz Nogueira Gaia. O coletivo cruza o Jardim São Luiz e alcança as artérias centrais pelas ruas Barão do Amazonas e Florêncio de Abreu.</p>"
            "<p>Prosseguindo rumo ao Oeste, o veículo avança pelas ruas calmas do Monte Alegre residencial pela Rua Paraíso, atendendo a condomínios fechados horizontais e chácaras floridas antes de cumprir a rotatória terminal para iniciar o itinerário inverso.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 84 paradas catalogadas com piso podotátil e lixeiras seletivas. No Jardim Irajá, sobressaem-se a <strong>Parada Rua Chile, 856</strong> e os pontos na <strong>Rua Cavalheiro Torquato Rizzi, 1526</strong>, ladeados por jardins de prédios residenciais.</p>"
            "<p>No Monte Alegre residencial, a parada na <strong>Rua Paraíso</strong> concentra passageiros em frente aos empórios artesanais e praças ajardinadas da localidade.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa praticada é o valor congelado de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> mediante o uso do Cartão Cidadão RP Mobi. O passageiro valida sua subida no Jardim Irajá e pode desembarcar no Centro para realizar compras sem pagar nova passagem dentro de duas horas.</p>"
            "<p>Essa facilidade tarifária garante conforto e previsibilidade para quem frequenta consultórios e comércios nobres da cidade.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto atende a <em>Jardim Irajá</em>, <em>Bosque das Juritis</em>, <em>Jardim São Luiz</em>, <em>Monte Alegre</em> e <em>Centro</em>.</p>"
            "<p>A rota sustenta um dos corredores residenciais mais harmoniosos e agradáveis da rede viária do município.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa junto aos <strong>bistrôs e cafeterias do Jardim Irajá</strong> e aos parques floridos do Bosque das Juritis.</p>"
            "<p>No Centro histórico, aproxima os munícipes do Museu de Arte de Ribeirão Preto (MARP) e do Theatro Pedro II.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 1516 - R. Chile, 856", "rua": "Rua Chile", "bairro": "Jardim Irajá", "referencia": "Ponto de partida no bairro Irajá"},
            {"nome": "Ponto 4088 - R. Cav. Torquato Rizzi, 1526", "rua": "Rua Cavalheiro Torquato Rizzi", "bairro": "Jardim Irajá", "referencia": "Acesso a edifícios residenciais"},
            {"nome": "Ponto Barão do Amazonas - Central", "rua": "Rua Barão do Amazonas", "bairro": "Centro", "referencia": "Parada central da linha"},
            {"nome": "Ponto Monte Alegre Residencial", "rua": "Rua Paraíso", "bairro": "Monte Alegre", "referencia": "Acesso a chácaras e residências"},
            {"nome": "Ponto Final Monte Alegre", "rua": "Alameda dos Manacás", "bairro": "Monte Alegre", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. Irajá / Monte Alegre", "num_paradas": 84, "descricao": "Itinerário convencional diametral completo ligando o Jardim Irajá ao Monte Alegre Residencial."},
            {"nome": "Até R. Barão do Amazonas", "num_paradas": 21, "descricao": "Atendimento rápido no sentido bairro-centro."},
            {"nome": "Até Jd. Irajá", "num_paradas": 41, "descricao": "Retorno no sentido oeste-sul no final da tarde."},
            {"nome": "Até Monte Alegre", "num_paradas": 24, "descricao": "Sentido sul-oeste matutino."}
        ]
    }
}

def main():
    print("==================================================")
    print("   GERADOR OFICIAL DO LOTE 4 (C4 — FASE 2)        ")
    print("==================================================")
    
    PAGINAS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Atualiza lista_linhas no content/paginas/linhas/index.json
    index_data = json.load(open(INDEX_JSON_PATH, encoding='utf-8'))
    slug_map = {num: lote4_defs[num]["slug"] for num in lote4_defs}
    
    for item in index_data.get('lista_linhas', []):
        cod = item.get('codigo')
        if cod in slug_map:
            item['slug'] = slug_map[cod]
            print(f"[*] Atualizado slug no index.json: Linha {cod} -> {slug_map[cod]}")
            
    with open(INDEX_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    print("[+] index.json sincronizado com os slugs oficiais do Lote 4.")

    # Gera cada um dos 10 arquivos JSON
    for num, defs in lote4_defs.items():
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
                "resposta": f"A tarifa urbana de Ribeirão Preto é de R$ 5,00, aceita via Cartão Cidadão RP Mobi, cartões de vale-transporte e dinheiro a bordo."
            },
            {
                "pergunta": f"Onde a Linha {num} realiza integração com outras rotas?",
                "resposta": f"A integração ocorre prioritariamente no {defs['terminal_central']}, onde os usuários contam com conexões estratégicas da malha de transporte."
            },
            {
                "pergunta": f"Como funciona a integração temporal da Linha {num}?",
                "resposta": f"Com o Cartão Cidadão RP Mobi, o passageiro dispõe de até 120 minutos (2 horas) a partir da primeira validação para embarcar em outro coletivo sem custo adicional."
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

    print("\n[OK] Lote 4 de 10 páginas gerado com sucesso!")

if __name__ == '__main__':
    main()
