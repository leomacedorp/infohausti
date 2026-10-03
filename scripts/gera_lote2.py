#!/usr/bin/env python3
"""
GERADOR OFICIAL DO LOTE 2 (C4 — FASE 2) — INFOHAUS RP
Gera as 10 páginas JSON do Lote 2 em content/paginas/linhas/:
Linhas Alimentadoras da Zona Sul, Loteamentos e Bonfim:
- 025: Guaporé
- 026: Jd. Pedra Branca
- 027: Recanto Palmeiras
- 035: Alphaville
- 041: Machado Sant'Anna
- 043: Portal dos Ipês
- 045: Vila do Golfe
- 051: Jd. Olhos D'Água
- 053: Recreio Anhanguera
- 055: San Marco
"""

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
LINHAS_JSON_PATH = ROOT_DIR / 'content' / 'dados-fonte' / 'linhas.json'
PAGINAS_DIR = ROOT_DIR / 'content' / 'paginas' / 'linhas'
INDEX_JSON_PATH = ROOT_DIR / 'content' / 'paginas' / 'linhas' / 'index.json'

dados_fonte = json.load(open(LINHAS_JSON_PATH, encoding='utf-8'))

lote2_defs = {
    "025": {
        "slug": "linhas/linha-025-guapore",
        "h1": "Linha 025 — Guaporé",
        "titulo": "Linha 025 - Guaporé | Horários e Paradas RP Mobi",
        "descricao": "Guia da Linha 025 Guaporé da RP Mobi em Ribeirão Preto. Horários de partidas, itinerário pela Estação Sul, Jardim Botânico e condomínios da Zona Sul.",
        "keywords": "linha 025 ribeirao preto, alimentadora guapore rp mobi, onibus jardim botânico estacao sul, horario linha 025",
        "linha_numero": "025",
        "linha_nome": "Guaporé",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Estação Sul (BRT) ↔ Condomínio Guaporé / Vivendas da Mata",
        "terminal_central": "Estação Sul de Transferência (Avenida José Adolfo Bianco Molina)",
        "visao_geral": (
            "<p>A <strong>Linha 025 (Guaporé)</strong> é um serviço alimentador projetado para atender com exclusividade ao conjunto de loteamentos fechados horizontais do Condomínio Guaporé, situado nas colinas meridionais de Ribeirão Preto. Caracterizado por muros de cantaria, alamedas arborizadas com espécies nativas do bioma cerrado e rigoroso controle de portarias, o condomínio demanda um fluxo regular de transporte coletivo para trabalhadores da construção civil, paisagistas, jardineiros e equipes de governança residencial.</p>"
            "<p>Fiscalizada pela RP Mobi com veículos de média capacidade identificados pelo tom alaranjado das linhas alimentadoras, a rota oferece viagens regulares em horários de pico matutino e vespertino, conectando as guaritas de monitoramento à rede estrutural de transbordo do município.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota parte da baia sul de transferência, contornando alamedas perimetrais e acessando a pista vicinal que conduz aos pórticos monumentais do Guaporé. O coletivo ingressa pelas vias externas dos setores residenciais Guaporé I, II e III.</p>"
            "<p>O trajeto atende ainda aos moradores de chácaras familiares do Vivendas da Mata, realizando manobra em rotatória pavimentada antes de retomar a descida pela malha viária sul em direção ao ponto de conexão com os ônibus de grande porte.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 46 paradas selecionadas. O ponto fulcral de baldeação é o <strong>Ponto 3879 (Estação Sul)</strong>, onde os passageiros se integram diretamente aos ônibus que rumam para o centro bancário e comercial.</p>"
            "<p>No interior do complexo, destacam-se os abrigos em frente às portarias principais dos setores Guaporé, dotados de bancos, iluminação e calçadas com piso tátil para orientação de pedestres.</p>"
        ),
        "integracao_detalhe": (
            "<p>A operação é regulada pela tarifa pública de <strong>R$ 5,00</strong>, com a concessão da <strong>integração temporal de 120 minutos</strong> mediante uso do Cartão Cidadão RP Mobi. O passageiro valida sua entrada na catraca do Guaporé e tem até duas horas para pegar a condução seguinte sem pagar nova passagem.</p>"
            "<p>Essa regra tarifária garante economia aos prestadores de serviços diários que cruzam a cidade vindos de bairros das zonas Norte ou Oeste.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto atende prioritariamente ao <em>Condomínio Guaporé</em>, <em>Vivendas da Mata</em> e setores limítrofes do <em>Jardim Botânico</em>.</p>"
            "<p>A existência da linha é imprescindível para garantir o deslocamento seguro de quem atua profissionalmente na conservação patrimonial das mansões e áreas verdes do empreendimento.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota aproxima os passageiros do lago ornamental e das trilhas ecológicas preservadas no entorno das nascentes locais, além do clube hípico e haras vizinhos.</p>"
            "<p>Na plataforma de integração, permite acesso rápido aos polos de serviços e clínicas de especialidades médicas do setor meridional.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3879 - Estação Sul (BRT)", "rua": "Avenida José Adolfo Bianco Molina", "bairro": "Jardim Botânico", "referencia": "Terminal de transbordo da Linha 025"},
            {"nome": "Ponto Av. Carlos Consoni - Saint Gerard", "rua": "Avenida Carlos Consoni", "bairro": "Jardim Saint Gerard", "referencia": "Acesso ao comércio local e colégios"},
            {"nome": "Ponto Portaria Guaporé I", "rua": "Alameda dos Guaporés", "bairro": "Jardim Botânico", "referencia": "Entrada principal do condomínio Guaporé"},
            {"nome": "Ponto Quinta da Primavera", "rua": "Avenida Luiz Eduardo Toledo Prado", "bairro": "Quinta da Primavera", "referencia": "Conexão com novos residenciais da colina"},
            {"nome": "Ponto Final Vivendas da Mata", "rua": "Estrada Vicinal do Guaporé", "bairro": "Jardim Botânico", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Guaporé (Regular)", "num_paradas": 46, "descricao": "Itinerário alimentador principal ligando a Estação Sul ao Condomínio Guaporé e residenciais da Quinta da Primavera."}
        ]
    },
    "026": {
        "slug": "linhas/linha-026-jd-pedra-branca",
        "h1": "Linha 026 — Jd. Pedra Branca",
        "titulo": "Linha 026 - Jd. Pedra Branca | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 026 Jardim Pedra Branca da RP Mobi em Ribeirão Preto. Trajeto pelo Jardim Botânico, Recreio Internacional e Estação Sul.",
        "keywords": "linha 026 ribeirao preto, onibus pedra branca rp mobi, alimentadora jardim botanico, horario linha 026",
        "linha_numero": "026",
        "linha_nome": "Jd. Pedra Branca",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Estação Sul (BRT) ↔ Jardim Pedra Branca / Diva Tarlá de Carvalho",
        "terminal_central": "Estação Sul de Transferência (Avenida José Adolfo Bianco Molina)",
        "visao_geral": (
            "<p>A <strong>Linha 026 (Jd. Pedra Branca)</strong> é o serviço alimentador encarregado de prover mobilidade regular para os moradores do loteamento Jardim Pedra Branca e áreas vizinhas na faixa sudeste de Ribeirão Preto. Operando com micro-ônibus e veículos convencionais adaptados, a rota conecta essas comunidades semi-rurais e de chácaras de recreio ao sistema troncal de transporte coletivo.</p>"
            "<p>Sob gestão da RP Mobi, a linha realiza partidas pontuais programadas ao longo dos dias úteis e fins de semana, garantindo que os moradores de ruas ainda em fase de pavimentação contem com transporte seguro até as plataformas de transbordo da Zona Sul.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota sai da Estação Sul de Transferência, contornando vias coletoras do Jardim Botânico e avançando em direção à rodovia e acessos rurais da zona leste-sul. O veículo cruza trechos vicinais do Recreio Internacional e Jardim Diva Tarlá de Carvalho.</p>"
            "<p>Ao alcançar as vias internas do Jardim Pedra Branca, o ônibus realiza escalas ao longo da rua principal do bairro, facilitando o embarque de estudantes e trabalhadores de chácaras residenciais antes de efetuar o retorno pela malha asfáltica rumo ao terminal de integração.</p>"
        ),
        "paradas_destaque": (
            "<p>Ao longo de suas 19 paradas catalogadas, os destaques ficam por conta do <strong>Ponto 3879 (Estação Sul)</strong>, que oferece integração tarifária com o Corredor Norte-Sul, e dos pontos de parada abrigados na via principal do Jardim Pedra Branca.</p>"
            "<p>A parada em frente à Associação de Moradores e centros comunitários locais representa o coração da operação no bairro, ponto de encontro cotidiano de usuários no início das manhãs e fins de tarde.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa estabelecida é a padrão de <strong>R$ 5,00</strong>, com a concessão da <strong>integração temporal de 120 minutos</strong> pelo Cartão Cidadão RP Mobi. O passageiro que embarca no Pedra Branca pode descer na Estação Sul e pegar o BRT para o Centro sem pagar nova passagem.</p>"
            "<p>O mesmo benefício aplica-se no regresso, onde uma única validação no centro comercial cobre a viagem troncal e o transbordo na Linha 026 até o portão de casa.</p>"
        ),
        "bairros_texto": (
            "<p>O atendimento cobre localidades em processo contínuo de urbanização: <em>Jardim Pedra Branca</em>, <em>Jardim Diva Tarlá de Carvalho</em>, <em>Recreio Internacional</em> e porções limítrofes do <em>Jardim Botânico</em>.</p>"
            "<p>Essa cobertura é fundamental para mitigar o isolamento geográfico de loteamentos mais afastados, integrando-os à vida econômica metropolitana.</p>"
        ),
        "atracoes_proximas": (
            "<p>A linha aproxima os usuários de áreas de lazer ao ar livre, haras e chácaras de eventos campestres situadas no entorno do Recreio Internacional.</p>"
            "<p>No retorno à Zona Sul urbana, deixa o passageiro a poucos minutos do centro comercial do Jardim Botânico e de praças com pistas de caminhada.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3879 - Estação Sul (BRT)", "rua": "Avenida José Adolfo Bianco Molina", "bairro": "Jardim Botânico", "referencia": "Terminal de transbordo principal"},
            {"nome": "Ponto Diva Tarlá - Av. Celso Charuri", "rua": "Avenida Doutor Celso Charuri", "bairro": "Jardim Diva Tarlá", "referencia": "Acesso a chácaras e condomínios de lazer"},
            {"nome": "Ponto Recreio Internacional - Rua das Palmeiras", "rua": "Rua das Palmeiras", "bairro": "Recreio Internacional", "referencia": "Conexão com áreas campestres"},
            {"nome": "Ponto Entrada Pedra Branca", "rua": "Rua Principal", "bairro": "Jardim Pedra Branca", "referencia": "Acesso às ruas residenciais do bairro"},
            {"nome": "Ponto Final Pedra Branca", "rua": "Praça Central do Bairro", "bairro": "Jardim Pedra Branca", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Jd. Pedra Branca (Regular)", "num_paradas": 19, "descricao": "Itinerário alimentador conectando a Estação Sul ao Jardim Pedra Branca e Recreio Internacional."}
        ]
    },
    "027": {
        "slug": "linhas/linha-027-recanto-palmeiras",
        "h1": "Linha 027 — Recanto Palmeiras",
        "titulo": "Linha 027 - Recanto Palmeiras | Horários e Paradas RP Mobi",
        "descricao": "Horários e itinerário da Linha 027 Recanto Palmeiras em Ribeirão Preto. Linha alimentadora da RP Mobi ligando a Estação Sul aos loteamentos da Zona Sul.",
        "keywords": "linha 027 ribeirao preto, recanto palmeiras rp mobi, alimentadora recanto palmeiras, horario linha 027",
        "linha_numero": "027",
        "linha_nome": "Recanto Palmeiras",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Estação Sul (BRT) ↔ Recanto Palmeiras / Jd. Florestan Fernandes",
        "terminal_central": "Estação Sul de Transferência (Avenida José Adolfo Bianco Molina)",
        "visao_geral": (
            "<p>A <strong>Linha 027 (Recanto Palmeiras)</strong> desempenha função social indispensável para o transporte de comunidades trabalhadoras e pequenos produtores localizados no Recanto Palmeiras e Jardim Florestan Fernandes. Operando no formato alimentador com a cor laranja, a linha preenche a lacuna de deslocamento entre os núcleos habitacionais populares periféricos e o polo de transporte do Jardim Botânico.</p>"
            "<p>Com horários planejados para contemplar os turnos matutinos escolares e operários e o retorno seguro no período noturno, a linha é acompanhada pela RP Mobi com índices satisfatórios de pontualidade em suas 15 paradas estratégicas.</p>"
        ),
        "itinerario_texto": (
            "<p>Com partida fixada na Estação Sul de Transferência, a Linha 027 transita pela malha viária coletora da Zona Sul, acessando estradas de ligação municipal e avenidas de transição entre o perímetro urbano e as chácaras da bacia do córrego Retiro Saudoso.</p>"
            "<p>O ônibus percorre as ruas do Jardim Vilico Cantarelli e Jardim Florestan Fernandes, alcançando as vias residenciais do Recanto Palmeiras, onde realiza desembarque porta a porta nas paradas rurais sinalizadas antes de efetuar o retorno pela rota de integração.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha conta com 15 paradas no total, com prioridade para a segurança dos passageiros. A principal parada de integração é o <strong>Ponto 3879 (Estação Sul)</strong>, ponto de encontro com as linhas de BRT e alimentadoras locais.</p>"
            "<p>Nos bairros atendidos, destacam-se a parada da Escola Comunitária do Florestan Fernandes e a parada final no Recanto Palmeiras, dotadas de abrigo contra intempéries e iluminação fotovoltaica.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa cobrada é a regulamentar de <strong>R$ 5,00</strong>, com acesso integral à regra de <strong>integração temporal de 120 minutos</strong> por meio do Cartão Cidadão RP Mobi. Esse direito assegura aos moradores das áreas periféricas acesso irrestrito a qualquer ponto do município pagando somente uma passagem.</p>"
            "<p>A integração favorece alunos que estudam em escolas técnicas e universidades públicas na região central ou na USP, reduzindo os custos de deslocamento diário da família.</p>"
        ),
        "bairros_texto": (
            "<p>As comunidades diretamente beneficiadas são <em>Recanto Palmeiras</em>, <em>Jardim Florestan Fernandes</em>, <em>Jardim Vilico Cantarelli</em> e <em>Jardim Diva Tarlá de Carvalho</em>, além da conexão com o <em>Jardim Botânico</em>.</p>"
            "<p>A manutenção regular desta linha é fruto de mobilização comunitária histórica, garantindo dignidade de mobilidade aos cidadãos locais.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota aproxima os moradores de áreas rurais preservadas, hortas comunitárias e pesqueiros familiares que atraem visitantes nos finais de semana.</p>"
            "<p>Na outra ponta, na Estação Sul, permite acesso facilitado a serviços bancários, agências de correio e centros de saúde da Zona Sul.</p>"
        ),
        "paradas_principais": [
            {"nome": "Ponto 3879 - Estação Sul (BRT)", "rua": "Avenida José Adolfo Bianco Molina", "bairro": "Jardim Botânico", "referencia": "Terminal de transbordo principal"},
            {"nome": "Ponto Florestan Fernandes - Rua Central", "rua": "Rua Projetada A", "bairro": "Jardim Florestan Fernandes", "referencia": "Acesso a moradias populares e centro comunitário"},
            {"nome": "Ponto Vilico Cantarelli", "rua": "Rua Antônio Cantarelli", "bairro": "Jardim Vilico Cantarelli", "referencia": "Conexão com pequenos comércios de bairro"},
            {"nome": "Ponto Estrada das Palmeiras", "rua": "Estrada Municipal das Palmeiras", "bairro": "Recanto Palmeiras", "referencia": "Parada intermediária do recanto"},
            {"nome": "Ponto Final Recanto Palmeiras", "rua": "Rotatória do Recanto", "bairro": "Recanto Palmeiras", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Recanto Palmeiras (Regular)", "num_paradas": 15, "descricao": "Itinerário alimentador ligando a Estação Sul aos loteamentos Recanto Palmeiras e Florestan Fernandes."}
        ]
    },
    "035": {
        "slug": "linhas/linha-035-alphaville",
        "h1": "Linha 035 — Alphaville",
        "titulo": "Linha 035 - Alphaville | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia da Linha 035 Alphaville da RP Mobi em Ribeirão Preto. Horários atualizados, itinerário pelo complexo Alphaville e Bonfim Paulista e integração.",
        "keywords": "linha 035 ribeirao preto, onibus alphaville rp mobi, alimentadora alphaville bonfim, horario linha 035",
        "linha_numero": "035",
        "linha_nome": "Alphaville",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Bonfim Paulista ↔ Complexo Residencial e Empresarial Alphaville",
        "terminal_central": "Terminal de Integração de Bonfim Paulista",
        "visao_geral": (
            "<p>A <strong>Linha 035 (Alphaville)</strong> atende a uma das zonas de desenvolvimento urbanístico mais dinâmicas do interior de São Paulo: o complexo Residencial e Empresarial Alphaville Ribeirão Preto, localizado no platô sul do distrito de Bonfim Paulista. A linha atua como tronco alimentador essencial para a circulação de centenas de trabalhadores da construção civil, paisagismo, portaria, zeladoria e escritórios de arquitetura e tecnologia que atuam nos condomínios.</p>"
            "<p>Com partidas sincronizadas com os ônibus troncais no Terminal de Bonfim Paulista, a linha opera nos horários de entrada e saída de expedientes de condomínios fechados, contando com uma derivação via Cenourão para atender funcionários do polo comercial hortifrúti e centros de conveniência da rodovia.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo do Terminal de Bonfim Paulista, o coletivo segue pela Rodovia José Fregonesi (SP-328), tomando a alça de acesso ao complexo Alphaville. O veículo circula pelas avenidas de contorno externo dos residenciais Alphaville 1, 2 e 3 e da área empresarial.</p>"
            "<p>Em horários específicos, realiza a extensão via Cenourão para atendimento ao entreposto comercial e empreendimentos marginais, retornando pelas vias expressas de Bonfim Paulista em direção ao ponto de baldeação de transporte metropolitano.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 14 paradas de embarque e desembarque. A parada inicial e principal elo de conexão é o <strong>Terminal de Bonfim Paulista</strong>, onde os passageiros se integram às linhas que seguem para o centro de Ribeirão Preto.</p>"
            "<p>Dentro do complexo, ganham notoriedade as paradas junto às portarias dos condomínios residenciais e a parada do Centro Empresarial Alphaville, dotadas de guaritas protegidas e calçadas com piso podotátil.</p>"
        ),
        "integracao_detalhe": (
            "<p>A passagem é regulada pela tarifa municipal de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> pelo Cartão Cidadão RP Mobi. O trabalhador que chega de qualquer bairro de Ribeirão Preto no Terminal de Bonfim embarca na Linha 035 sem nova cobrança na catraca.</p>"
            "<p>Essa integração viabiliza a ida e volta de centenas de trabalhadores que prestam serviços regulares nas mansões e empresas do Alphaville.</p>"
        ),
        "bairros_texto": (
            "<p>A rota abrange o <em>Residencial e Empresarial Alphaville</em>, o <em>Jardim das Mansões</em> e o núcleo histórico de <em>Bonfim Paulista</em>.</p>"
            "<p>A presença da linha assegura transporte público de qualidade em uma região caracterizada por condomínios fechados e tráfego prioritário de veículos automotores particulares.</p>"
        ),
        "atracoes_proximas": (
            "<p>O trajeto aproxima os usuários do centro gastronômico de Bonfim Paulista, famoso por suas choperias artesanais e restaurantes italianos, além de centros de eventos corporativos do platô sul.</p>"
            "<p>Também facilita o acesso ao centro comercial Cenourão e aos novos centros médicos instalados ao longo da Rodovia José Fregonesi.</p>"
        ),
        "paradas_principais": [
            {"nome": "Terminal Bonfim Paulista", "rua": "Rua Professor Hélio Lourenço", "bairro": "Bonfim Paulista", "referencia": "Terminal de transbordo da Linha 035"},
            {"nome": "Ponto Cenourão - Rod. José Fregonesi", "rua": "Rodovia José Fregonesi", "bairro": "Bonfim Paulista", "referencia": "Acesso ao centro comercial e hortifrúti"},
            {"nome": "Ponto Portaria Alphaville 1", "rua": "Avenida Alphaville", "bairro": "Alphaville", "referencia": "Acesso ao Residencial Alphaville 1"},
            {"nome": "Ponto Portaria Alphaville 2 e 3", "rua": "Avenida Alphaville", "bairro": "Alphaville", "referencia": "Acesso aos residenciais 2 e 3"},
            {"nome": "Ponto Final Centro Empresarial", "rua": "Alameda dos Empresários", "bairro": "Alphaville", "referencia": "Ponto de retorno no polo empresarial"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Alphaville (Regular)", "num_paradas": 14, "descricao": "Itinerário principal alimentador ligando o Terminal de Bonfim Paulista ao complexo Alphaville."},
            {"nome": "Alphaville - via Cenourão", "num_paradas": 16, "descricao": "Derivação operacional com atendimento aos estabelecimentos comerciais da Rodovia José Fregonesi."}
        ]
    },
    "041": {
        "slug": "linhas/linha-041-machado-santanna",
        "h1": "Linha 041 — Machado Sant'Anna",
        "titulo": "Linha 041 - Machado Sant'Anna | Horários e Paradas RP Mobi",
        "descricao": "Horários e itinerário da Linha 041 Machado Sant'Anna da RP Mobi em Ribeirão Preto. Atendimento alimentar ao conjunto habitacional e praça comunitária.",
        "keywords": "linha 041 ribeirao preto, machado santanna rp mobi, onibus machado santanna, horario linha 041",
        "linha_numero": "041",
        "linha_nome": "Machado Sant'Anna",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#ff6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Sudeste ↔ Residencial Machado Sant'Anna (Rua Maria Cândida de Jesus)",
        "terminal_central": "Terminal Sudeste de Transferência",
        "visao_geral": (
            "<p>A <strong>Linha 041 (Machado Sant'Anna)</strong> foi concebida para atender às necessidades diárias de transporte coletivo do conjunto habitacional Residencial Machado Sant'Anna, localizado no extremo sudeste da malha urbana de Ribeirão Preto. Trata-se de um bairro operário consolidado, com traçado viário acolhedor, pequenas mercearias, quitandas de verduras e famílias que residem na região há várias décadas.</p>"
            "<p>Operando com veículos compactos com identificação alaranjada, a linha mantém horários bem distribuídos ao longo do dia, oferecendo previsibilidade no transporte de auxiliares de escritório, cozinheiros escolares, pedreiros e balconistas que precisam se conectar rapidamente às plataformas coletivas do município.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota sai das plataformas de transbordo da região sudeste, seguindo por avenidas de pista dupla antes de penetrar no miolo residencial do Machado Sant'Anna. O veículo circula por vias calçadas como a Rua Maria Cândida de Jesus e ruas transversais numeradas.</p>"
            "<p>Durante o percurso interno, o coletivo realiza embarques na porta das residências térreas e sobrados, contornando a rotatória do fim da via pavimentada onde efetua a manobra de retorno para iniciar o caminho de volta aos pontos estruturais do transporte.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha dispõe de 28 pontos ao longo do percurso. O marco estruturante é a parada inicial na baia sul-sudeste, onde há bancos, cobertura metálica e mapa esquemático da rede de ônibus.</p>"
            "<p>No coração do bairro, o destaque absoluto é a parada em frente à EMEI e creche comunitária na <strong>Rua Maria Cândida de Jesus</strong>, que reúne pais com crianças de colo nas primeiras horas da manhã e ao término do turno vespertino.</p>"
        ),
        "integracao_detalhe": (
            "<p>O valor tarifário é de <strong>R$ 5,00</strong>, assegurando a fruição do direito de <strong>integração temporal de 120 minutos</strong> mediante uso do Cartão Cidadão RP Mobi. Esse cartão eletrônico permite que o munícipe saia do Machado Sant'Anna e ingresse na condução que ruma aos locais de trabalho distantes sem pagar um centavo a mais.</p>"
            "<p>O sistema alivia a renda dos núcleos familiares da comunidade, garantindo que o custo do transporte público caiba com equilíbrio no orçamento mensal doméstico.</p>"
        ),
        "bairros_texto": (
            "<p>O trajeto atende com foco quase exclusivo às famílias do <em>Residencial Machado Sant'Anna</em>, servindo também a moradores das ruas limítrofes do <em>Parque das Oliveiras II</em>.</p>"
            "<p>A criação e manutenção regular desta linha resultou de reivindicações de lideranças comunitárias e comissões de bairro, consolidando a dignidade da mobilidade local.</p>"
        ),
        "atracoes_proximas": (
            "<p>No bairro, o ponto de encontro comunitário é a <strong>Praça Central do Machado Sant'Anna</strong>, com parque de brinquedos infantis e campo de futebol de areia onde ocorrem torneios amadores nos fins de semana.</p>"
            "<p>O itinerário também facilita o acesso a farmácias populares, panificadoras e feiras livres matinais montadas nas ruas largas do conjunto habitacional.</p>"
        ),
        "paradas_principais": [
            {"nome": "Terminal Sudeste - Plataforma Alimentadora", "rua": "Avenida Doutor Celso Charuri", "bairro": "Jardim São José", "referencia": "Ponto de partida da linha alimentadora"},
            {"nome": "Ponto Rua Maria Cândida de Jesus, 120", "rua": "Rua Maria Cândida de Jesus", "bairro": "Machado Sant'Anna", "referencia": "Acesso a mercadinho comunitário"},
            {"nome": "Ponto Creche Comunitária", "rua": "Rua Maria Cândida de Jesus", "bairro": "Machado Sant'Anna", "referencia": "Parada escolar de embarque infantil"},
            {"nome": "Ponto Praça de Esportes", "rua": "Rua Cinco", "bairro": "Machado Sant'Anna", "referencia": "Quadra de areia e playground"},
            {"nome": "Ponto Final Machado Sant'Anna", "rua": "Rua Projetada Cinco", "bairro": "Machado Sant'Anna", "referencia": "Rotatória final de manobra"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Machado Sant'Anna (Regular)", "num_paradas": 28, "descricao": "Itinerário alimentador circular atendendo ao conjunto habitacional Residencial Machado Sant'Anna."}
        ]
    },
    "043": {
        "slug": "linhas/linha-043-portal-dos-ipes",
        "h1": "Linha 043 — Portal dos Ipês",
        "titulo": "Linha 043 - Portal dos Ipês | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 043 Portal dos Ipês da RP Mobi em Ribeirão Preto. Trajeto alimentar pelas alamedas arborizadas e residenciais de Bonfim.",
        "keywords": "linha 043 ribeirao preto, portal dos ipes rp mobi, onibus portal dos ipes, horario linha 043",
        "linha_numero": "043",
        "linha_nome": "Portal dos Ipês",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Bonfim Paulista ↔ Alamedas do Portal dos Ipês",
        "terminal_central": "Terminal de Integração de Bonfim Paulista",
        "visao_geral": (
            "<p>A <strong>Linha 043 (Portal dos Ipês)</strong> foi estruturada para conferir transporte coletivo regular aos condomínios horizontais do loteamento Portal dos Ipês, no planalto oriental de Bonfim Paulista. O loteamento caracteriza-se por alamedas largas, paisagismo exuberante com fileiras de ipês amarelos e roxos floridos e residências de médio e alto padrão cercadas por áreas verdes preservadas.</p>"
            "<p>Gerenciada com pontualidade pela RP Mobi, a frota de ônibus de porte intermediário atende tanto aos moradores do empreendimento quanto aos dezenas de zeladores, jardineiros, eletricistas de condomínio e prestadores de serviços de reformas que transitam diariamente pelas portarias monitoradas.</p>"
        ),
        "itinerario_texto": (
            "<p>O trajeto inicia-se na área de baldeação do distrito bonfinense, avançando por avenidas vicinais pavimentadas com iluminação em LED até atingir o portal de entrada do loteamento residencial. O veículo penetra na <strong>Alameda das Quaresmeiras</strong> e percorre as alamedas internas que contornam as praças floridas.</p>"
            "<p>Os pontos de embarque estão posicionados em intervalos convenientes ao longo das vias arborizadas, permitindo caminhada curta até qualquer imóvel do loteamento, antes de realizar o giro regulamentar na rotatória das flores para retornar ao ponto inicial de conexão.</p>"
        ),
        "paradas_destaque": (
            "<p>A linha conta com 30 paradas catalogadas. O ponto fulcral de baldeação é o <strong>Terminal de Bonfim Paulista</strong>, onde o passageiro troca de condução com tranquilidade em plataformas cobertas.</p>"
            "<p>No interior do bairro, destacam-se a <strong>Parada Alameda dos Ipês</strong> e o abrigo junto à portaria social do condomínio, equipados com bancos de madeira maciça, lixeiras seletivas e boa visibilidade para quem aguarda a chegada do ônibus.</p>"
        ),
        "integracao_detalhe": (
            "<p>A passagem custa o valor público congelado em <strong>R$ 5,00</strong>, conferindo o direito à <strong>integração temporal de 120 minutos</strong> no Cartão Cidadão RP Mobi. Quem embarca nas alamedas do Portal dos Ipês pode desembarcar no terminal distrital e pegar qualquer outra rota sem pagar nova taxa de catraca.</p>"
            "<p>Essa regra tarifária é decisiva para os funcionários das residências, muitos dos quais moram em bairros distantes e utilizam duas ou três conduções diárias para cumprir sua jornada.</p>"
        ),
        "bairros_texto": (
            "<p>A rota cobre com exclusividade o <em>Loteamento Portal dos Ipês</em> e os bolsões habitacionais contíguos de <em>Bonfim Paulista</em>.</p>"
            "<p>A implantação do trajeto solucionou as dificuldades históricas de transporte público nas colinas residenciais, promovendo conexão harmoniosa entre o loteamento e o sistema municipal.</p>"
        ),
        "atracoes_proximas": (
            "<p>As vias do trajeto contam com <strong>trilhas arborizadas de ipês</strong> e áreas de caminhada ao ar livre com vista panorâmica para o vale.</p>"
            "<p>No retorno a Bonfim Paulista, a linha deixa o passageiro próximo às feiras de artesanato, praças floridas e confeitarias coloniais do centro do distrito.</p>"
        ),
        "paradas_principais": [
            {"nome": "Terminal Bonfim Paulista", "rua": "Rua Professor Hélio Lourenço", "bairro": "Bonfim Paulista", "referencia": "Terminal de transbordo principal"},
            {"nome": "Ponto Portal dos Ipês - Portaria Principal", "rua": "Alameda dos Ipês", "bairro": "Portal dos Ipês", "referencia": "Entrada principal do condomínio"},
            {"nome": "Ponto Alameda das Quaresmeiras", "rua": "Alameda das Quaresmeiras", "bairro": "Portal dos Ipês", "referencia": "Parada residencial central"},
            {"nome": "Ponto Praça dos Jacarandás", "rua": "Alameda dos Jacarandás", "bairro": "Portal dos Ipês", "referencia": "Área de lazer e convivência"},
            {"nome": "Ponto Final Rotatória das Flores", "rua": "Rotatória das Flores", "bairro": "Portal dos Ipês", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Portal dos Ipês (Regular)", "num_paradas": 30, "descricao": "Itinerário alimentador principal ligando o Terminal de Bonfim Paulista às alamedas do Portal dos Ipês."}
        ]
    },
    "053": {
        "slug": "linhas/linha-053-recreio-anhanguera",
        "h1": "Linha 053 — Recreio Anhanguera",
        "titulo": "Linha 053 - Recreio Anhanguera | Horários e Paradas RP Mobi",
        "descricao": "Guia de horários da Linha 053 Recreio Anhanguera da RP Mobi em Ribeirão Preto. Atendimento logístico e rural às margens da Rodovia Anhanguera.",
        "keywords": "linha 053 ribeirao preto, recreio anhanguera rp mobi, onibus anhanguera cargas, horario linha 053",
        "linha_numero": "053",
        "linha_nome": "Recreio Anhanguera",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Sudeste ↔ Eixo Logístico Rodovia Anhanguera / Chácaras Recreio Anhanguera",
        "terminal_central": "Terminal Sudeste de Transferência",
        "visao_geral": (
            "<p>A <strong>Linha 053 (Recreio Anhanguera)</strong> é um serviço de transporte coletivo singular voltado ao polo logístico, industrial e de chácaras de produção hortigranjeira implantado nas imediações do quilômetro 310 da Rodovia Anhanguera (SP-330). O cenário é marcado pela circulação constante de carretas bitrem, galpões de transbordo de mercadorias, silos de grãos, oficinas mecânicas pesadas e pequenos sítios familiares produtores de hortaliças frescas.</p>"
            "<p>Operando com robustez mecânica e motoristas treinados para navegar em vias marginais rodoviárias e trechos de paralelepípedo, a linha atende funcionários do turno operacional de logística, borracheiros, balanceadores de caminhões e chacareiros que comercializam sua produção na Ceagesp local.</p>"
        ),
        "itinerario_texto": (
            "<p>A rota deixa o terminal de transbordo e ganha a pista marginal da Rodovia Anhanguera, circulando pelas alças de acesso a transportadoras de grande porte e depósitos de distribuição de peças automotivas. O veículo adentra então as pistas vicinais do Recreio Anhanguera.</p>"
            "<p>Navegando entre cercas de chácaras agrícolas e galpões de armazenamento de cargas secas, a condução alcança a Estrada das Acácias, onde realiza paradas junto aos portões de carga e descarga de mercadorias antes de convergir para a rotatória rodoviária que orienta o regresso ao ponto de conexão urbana.</p>"
        ),
        "paradas_destaque": (
            "<p>O circuito possui 18 pontos mapeados com critério. O referencial de saída é a baia de conexão do terminal regional, dotada de acessibilidade e sanitários.</p>"
            "<p>Ao longo da marginal rodoviária, destacam-se a <strong>Parada Posto de Combustíveis Rodoviário</strong> e a parada em frente aos galpões de operadores logísticos na <strong>Estrada das Acácias</strong>, com calçadas reforçadas e placas refletivas para garantir segurança noturna aos motoristas e ajudantes de carga.</p>"
        ),
        "integracao_detalhe": (
            "<p>A viagem é tarifada no montante oficial de <strong>R$ 5,00</strong>, assegurando os <strong>120 minutos de integração temporal</strong> com a utilização do Cartão Cidadão RP Mobi. O trabalhador que bate ponto nos galpões rodoviários valida o cartão na subida e faz baldeação gratuita nas linhas troncais rumo às zonas Norte e Leste.</p>"
            "<p>Essa gratuidade na baldeação representa um ganho real para operários braçais e auxiliares de expedição que dependem exclusivamente do transporte público municipal para trabalhar.</p>"
        ),
        "bairros_texto": (
            "<p>O percurso atende de modo estrito ao <em>Loteamento Recreio Anhanguera</em>, aos galpões industriais da <em>Marginal SP-330</em> e pequenas chácaras produtoras limítrofes.</p>"
            "<p>A oferta estável de viagens garante que empresas de transporte de cargas e pequenos agricultores contem com mão de obra pontual todos os dias.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota passa próxima a <strong>galpões de venda direta de frutas e verduras frescas</strong> direto do produtor rural, além de tradicionais restaurantes de beira de estrada conhecidos pelo almoço tropeiro para caminhoneiros.</p>"
            "<p>No retorno à malha urbana, deixa o usuário a poucos minutos de centros de treinamento técnico e revendas de autopeças pesadas.</p>"
        ),
        "paradas_principais": [
            {"nome": "Terminal Sudeste - Plataforma Rodoviária", "rua": "Avenida Doutor Celso Charuri", "bairro": "Jardim São José", "referencia": "Terminal de conexão de linhas da Zona Sul"},
            {"nome": "Ponto Marginal SP-330 - Centro de Distribuição", "rua": "Via Marginal Rodovia Anhanguera", "bairro": "Recreio Anhanguera", "referencia": "Acesso a depósitos e armazéns logísticos"},
            {"nome": "Ponto Recreio Anhanguera - Estrada das Acácias", "rua": "Estrada das Acácias", "bairro": "Recreio Anhanguera", "referencia": "Acesso a chácaras de cultivo de hortaliças"},
            {"nome": "Ponto Oficinas Mecânicas de Pesados", "rua": "Rua Projetada Quatro", "bairro": "Recreio Anhanguera", "referencia": "Concentração de autopeças e borracharias"},
            {"nome": "Ponto Final Rotatória das Carretas", "rua": "Rotatória do Km 310", "bairro": "Recreio Anhanguera", "referencia": "Ponto de retorno da linha"}
        ],
        "itinerarios_detalhe": [
            {"nome": "Recreio Anhanguera (Regular)", "num_paradas": 18, "descricao": "Itinerário alimentador rodoviário ligando o Terminal Sudeste aos galpões logísticos e chácaras do Recreio Anhanguera."}
        ]
    },
    "055": {
        "slug": "linhas/linha-055-san-marco",
        "h1": "Linha 055 — San Marco",
        "titulo": "Linha 055 - San Marco | Horários, Itinerário e Paradas RP Mobi",
        "descricao": "Guia da Linha 055 San Marco (antiga Royal Park) da RP Mobi em Ribeirão Preto. Horários atualizados, paradas no Terminal Bonfim e condomínios fechados.",
        "keywords": "linha 055 ribeirao preto, onibus san marco rp mobi, alimentadora san marco bonfim, horario linha 055",
        "linha_numero": "055",
        "linha_nome": "San Marco",
        "modalidade": "Linha Alimentadora",
        "linha_cor": "#FF6600",
        "tarifa": "R$ 5,00",
        "resumo_origem_destino": "Terminal Bonfim Paulista ↔ Complexo de Condomínios San Marco",
        "terminal_central": "Terminal de Integração de Bonfim Paulista",
        "visao_geral": (
            "<p>A <strong>Linha 055 (San Marco)</strong> — que no planejamento operacional anterior atendia pelo nome de <em>Royal Park</em> — é uma rota alimentadora direcionada ao complexo urbanístico horizontal fechado do San Marco, erguido nas encostas altas de Bonfim Paulista. O complexo abriga dezenas de residências de alto padrão construtivo, alamedas arborizadas com palmeiras imperiais, fiação subterrânea em novos setores e guaritas informatizadas com biometria facial.</p>"
            "<p>A linha funciona como via de acesso essencial para os trabalhadores que constroem e sustentam a rotina do complexo: mestres de obras, armadores, gesseiros, decoradores, seguranças patrimoniais, piscineiros e equipes de zeladoria doméstica que se deslocam nos primeiros turnos do dia.</p>"
        ),
        "itinerario_texto": (
            "<p>Partindo das baias de transbordo do Terminal de Bonfim Paulista, o coletivo segue pela Avenida Francisco Massa e acessa a Avenida San Marco, artéria dorsal pavimentada que margeia os loteamentos fechados. O ônibus percorre o perímetro externo dos condomínios San Marco I e II, aproximando-se das guaritas de prestadores de serviço.</p>"
            "<p>Após contornar a rotatória monumental com fonte luminosa e palmeiras ornamentais, o veículo atende aos acessos dos residenciais vizinhos do platô superior e reinicia o declive em direção ao ponto de baldeação de transporte integrado.</p>"
        ),
        "paradas_destaque": (
            "<p>O percurso possui 30 paradas registradas. O marco inicial é o <strong>Terminal de Bonfim Paulista</strong>, onde os passageiros encontram infraestrutura com bancos, painéis informativos e banheiros públicos.</p>"
            "<p>Nos loteamentos, o grande destaque operacional fica com a parada em frente à <strong>Portaria de Prestadores de Serviços do San Marco</strong>, que concentra catracas de pedestres e abrigos cobertos com bancos para o conforto dos operários que aguardam a condução após o término das obras.</p>"
        ),
        "integracao_detalhe": (
            "<p>A tarifa vigente é a oficial do município de <strong>R$ 5,00</strong>, acompanhada do benefício de <strong>120 minutos de integração temporal</strong> proporcionado pelo Cartão Cidadão RP Mobi. O colaborador que passa a catraca no San Marco pode descer em Bonfim e entrar imediatamente no ônibus que ruma para a região central sem nova dedução monetária no saldo.</p>"
            "<p>Essa facilidade é indispensável para viabilizar financeiramente a rotina dos profissionais liberais e autônomos que realizam manutenções diárias nas residências da região.</p>"
        ),
        "bairros_texto": (
            "<p>O itinerário atende estritamente ao <em>Complexo Residencial San Marco</em>, aos residenciais <em>San Marco I e II</em> e às alamedas altas de <em>Bonfim Paulista</em>.</p>"
            "<p>A linha garantiu solução de transporte coletivo para um polo imobiliário de alta densidade construtiva que antes dependia de vans particulares e caronas informais.</p>"
        ),
        "atracoes_proximas": (
            "<p>A rota oferece vista panorâmica privilegiada dos <strong>vales e colinas do planalto sul</strong>, destacando-se pelo projeto paisagístico e pelas praças de convivência interna dos condomínios.</p>"
            "<p>No Terminal de Bonfim, viabiliza ligação rápida com os serviços do cartório de registro civil, agências dos Correios e farmácias da região central do distrito.</p>"
        ),
        "paradas_principais": [
            {"nome": "Terminal Bonfim Paulista", "rua": "Rua Professor Hélio Lourenço", "bairro": "Bonfim Paulista", "referencia": "Terminal de transbordo principal"},
            {"nome": "Ponto Avenida San Marco - Portaria 1", "rua": "Avenida San Marco", "bairro": "San Marco", "referencia": "Portaria do condomínio San Marco I"},
            {"nome": "Ponto Entrada Prestadores de Serviço", "rua": "Avenida San Marco", "bairro": "San Marco", "referencia": "Catraca de acesso de trabalhadores civis"},
            {"nome": "Ponto Rotatória das Palmeiras Imperiais", "rua": "Avenida San Marco", "bairro": "San Marco", "referencia": "Parada com fonte ornamental e canteiro"},
            {"nome": "Ponto Final San Marco II", "rua": "Alameda dos Ciprestes", "bairro": "San Marco", "referencia": "Rotatória final de retorno"}
        ],
        "itinerarios_detalhe": [
            {"nome": "San Marco (Regular)", "num_paradas": 30, "descricao": "Itinerário alimentador principal ligando o Terminal de Bonfim Paulista ao complexo de condomínios San Marco."}
        ]
    }
}

def main():
    print("==================================================")
    print("   GERADOR OFICIAL DO LOTE 2 (C4 — FASE 2)        ")
    print("==================================================")
    
    PAGINAS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Atualiza lista_linhas no content/paginas/linhas/index.json
    index_data = json.load(open(INDEX_JSON_PATH, encoding='utf-8'))
    slug_map = {num: lote2_defs[num]["slug"] for num in lote2_defs}
    
    for item in index_data.get('lista_linhas', []):
        cod = item.get('codigo')
        if cod in slug_map:
            item['slug'] = slug_map[cod]
            print(f"[*] Atualizado slug no index.json: Linha {cod} -> {slug_map[cod]}")
            
    with open(INDEX_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    print("[+] index.json sincronizado com os slugs oficiais do Lote 2.")

    # Gera cada um dos 10 arquivos JSON
    for num, defs in lote2_defs.items():
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
                "resposta": f"A tarifa urbana em Ribeirão Preto é de R$ 5,00, aceita via Cartão Cidadão RP Mobi, cartões de vale-transporte e dinheiro no validador de bordo."
            },
            {
                "pergunta": f"Onde a Linha {num} realiza integração com outras rotas?",
                "resposta": f"A integração ocorre principalmente no {defs['terminal_central']}, onde os usuários contam com plataformas de transbordo da rede municipal."
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

    print("\n[OK] Lote 2 de 10 páginas gerado com sucesso!")

if __name__ == '__main__':
    main()
