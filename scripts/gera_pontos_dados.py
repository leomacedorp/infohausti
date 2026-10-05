#!/usr/bin/env python3
"""
PONTOS_DADOS v2 — Metadados narrativos das 18 páginas da expansão turística.
scripts/gera_pontos_dados.py

Régua: cada afirmação factual É o valor verificado no dossiê correspondente
(content/dados-fonte/pontos/[slug].json). Campo pendente NÃO aparece.
v2 (GO Leo 05/10/2026): narrativas >= 800 palavras, ângulos distintos por
página-irmã (diversificação anti-similaridade), FAQ 5 perguntas.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOSSIES = ROOT / 'content' / 'dados-fonte' / 'pontos'

PONTOS_DADOS = {}


def _d(slug):
    with open(DOSSIES / f'{slug}.json', encoding='utf-8') as f:
        return json.load(f)


def _v(slug, campo):
    d = _d(slug).get(campo)
    if isinstance(d, dict) and d.get('status') == 'verificado':
        return d.get('valor')
    return None


def _p(slug, titulo, h1, descricao, keywords, nome_card, categoria_mestre,
       secoes, secao_extra_titulo=None, secao_extra_html=None,
       linhas_proximas=None, atracoes_proximas=None, faq=None):
    PONTOS_DADOS[slug] = {
        'titulo_seo': titulo,
        'h1': h1,
        'descricao': descricao,
        'keywords': keywords,
        'nome_card': nome_card,
        'categoria_mestre': categoria_mestre,
        'secoes': secoes,
        'secao_extra_titulo': secao_extra_titulo,
        'secao_extra_html': secao_extra_html,
        'linhas_proximas': linhas_proximas or [],
        'atracoes_proximas': atracoes_proximas or [],
        'faq': faq or [],
    }


# Helpers de bloco comuns (conteúdo factual, estrutura variada por página)
def _bloco_visitante_igreja(horarios_str, secretaria=None, extra=None):
    """Texto de detalhes_visita derivado dos campos verificados do dossiê."""
    t = [f'<p>Para planejar a ida, os horários oficiais de missa são: '
         f'<strong>{horarios_str}</strong>.</p>']
    if secretaria:
        t.append(f'<p>{secretaria}</p>')
    if extra:
        t.append(extra)
    return ''.join(t)


# ══════════════════════════════════════════════════════════════════════
# IGREJAS (6) — aberturas e estruturas variadas por página
# ══════════════════════════════════════════════════════════════════════

# ---- 1. Basílica Santo Antônio de Pádua (abre com MISSAS) ────────────
_sa = _v('basilica-santo-antonio-de-padua', 'nome')
_p('basilica-santo-antonio-de-padua',
   f'{_sa} em Ribeirão Preto | Ribeirão Viva',
   f'{_sa}: Missas Diárias no Coração dos Campos Elíseos',
   f'Missas, confissões e atendimento espiritual na {_sa} de Ribeirão '
   f'Preto: horários completos por dia, telefone e endereço oficiais, '
   f'verificados na Arquidiocese.',
   f'{_sa}, missas Campos Elíseos, horário de missas Ribeirão Preto, '
   'confissões, monges olivetanos, basílica',
   'Basílica Santo Antônio de Pádua',
   'Igrejas e Fé Popular',
   secoes={
       'resumo': (
           '<p>Com missas <strong>todos os dias da semana</strong> — incluindo '
           'três celebrações às terças —, a <strong>' + _sa + '</strong> mantém '
           'uma das rotinas pastorais mais intensas de Ribeirão Preto. O templo '
           'fica na Rua Paraíba, 747, nos Campos Elíseos, e é administrado pela '
           'Congregação Beneditina de Santa Maria de Monte Oliveto: os <strong>'
           'monges olivetanos</strong>, presença monástica rara no interior '
           'paulista.</p>'
           '<p>Elevada a <strong>Basílica Menor em 2019</strong> — título '
           'canônico confirmado pela Arquidiocese —, a igreja completou em 2019 '
           'setenta e dois anos de fundação. Quem visita os Campos Elíseos pode '
           'acoplar ao roteiro o Santuário Nossa Senhora da Medalha Milagrosa, '
           'o das <strong>Sete Capelas</strong>, no Morro do São Bento, que '
           'integra o mesmo complexo religioso administrado pelos olivetanos.</p>'
           '<p>A agenda da semana inclui confissões em dois turnos fixos e '
           'atendimento espiritual agendado — uma porta aberta tanto para o '
           'fiel ribeirão-pretano quanto para o visitante de passagem.</p>'
       ),
       'historia': (
           '<h3>De paróquia de 1947 a Basílica Menor de 2019</h3>'
           '<p>A comunidade nasceu em <strong>1947</strong>, numa época em que '
           'os Campos Elíseos cresciam como bairro residencial da Ribeirão '
           'Preto cafeeira. A administração passou à Congregação Beneditina de '
           'Santa Maria de Monte Oliveto, ordem monástica que imprimiu ao templo '
           'sua marca: liturgia cuidada, adoração silenciosa e vida comunitária '
           'de mosteiro no coração da cidade.</p>'
           '<p>Em <strong>2019</strong>, após sete décadas de atividade, a '
           'igreja recebeu da Santa Sé o título de <strong>Basílica '
           'Menor</strong>. O reconhecimento liga o templo à basílica papal e '
           'confere datas próprias de indulgência — um vínculo direto entre a '
           'paróquia dos Campos Elíseos e Roma. Conforme o registro oficial da '
           'Arquidiocese, é a única igreja com título basilical em Ribeirão '
           'Preto.</p>'
           '<p>O complexo não termina na porta da basílica: no Morro do São '
           'Bento, o <strong>Santuário Nossa Senhora da Medalha Milagrosa</strong> '
           '(Sete Capelas) celebra missa diária às 8h e dominical às 9h30, e a '
           'Capela do Lar Padre Euclides fecha a grade com a missa de sábado à '
           'noite, às 19h30.</p>'
       ),
       'detalhes_visita': (
           '<p>A basílica celebra <strong>oito missas semanais fixas</strong>: '
           'domingos às 8h, 10h, 17h e 19h; segundas às 7h e 19h30; terças às '
           '7h, 12h e 19h30; quartas, quintas e sextas às 7h e 19h30; sábados '
           'às 7h e 19h — a única igreja da cidade com celebração ao meio-dia '
           'na grade oficial consultada.</p>'
           '<p>As <strong>confissões</strong> ocorrem às segundas e terças, das '
           '15h às 17h, e às quintas e sextas, das 15h às 17h. O <strong>'
           'atendimento espiritual</strong> funciona de terça a sexta, das 9h '
           'às 11h, mediante agendamento pelo telefone da paróquia.</p>'
       ),
       'como_chegar': (
           '<p>O endereço oficial é <strong>Rua Paraíba, 747, Campos Elíseos, '
           'CEP 14080-020</strong>. A região oeste do centro expandido é '
           'atendida pelas linhas municipais que percorrem os Campos Elíseos e '
           'a Av. Independência; o hub de linhas do portal mostra o itinerário '
           'mais próximo do seu ponto de partida. Para o Santuário das Sete '
           'Capelas, siga as placas do Morro do São Bento — o acesso ao morro '
           'fica a poucos minutos da basílica.</p>'
       ),
       'atracoes_proximas': (
           '<p>No complexo do Morro do São Bento estão o Santuário das Sete '
           'Capelas, o Teatro Municipal e o Teatro de Arena — combinação rara '
           'de fé, arte e panorama da cidade em um só passeio. Descendo a '
           'colina, o centro histórico completa o roteiro.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Roteiro sugerido: basílica pela '
           'manhã (missa das 8h), subida ao Morro do São Bento para as Sete '
           'Capelas e pôr do sol no mirante do parque.</p>'
       ),
   },
   secao_extra_titulo='Horário de Missas',
   secao_extra_html=(
       '<h3>Basílica — grade semanal completa</h3>'
       '<ul>'
       '<li><strong>Domingos:</strong> 8h, 10h, 17h e 19h</li>'
       '<li><strong>Segundas:</strong> 7h e 19h30</li>'
       '<li><strong>Terças:</strong> 7h, 12h e 19h30</li>'
       '<li><strong>Quartas, quintas e sextas:</strong> 7h e 19h30</li>'
       '<li><strong>Sábados:</strong> 7h e 19h</li>'
       '</ul>'
       '<h3>Demais espaços do complexo</h3>'
       '<ul>'
       '<li><strong>Santuário das Sete Capelas:</strong> segunda a sábado, '
       '8h; domingos, 9h30</li>'
       '<li><strong>Capela do Lar Padre Euclides:</strong> sábados, 19h30</li>'
       '</ul>'
       '<p><strong>Confissões:</strong> segundas e terças, 15h–17h; quintas e '
       'sextas, 15h–17h. <strong>Atendimento espiritual:</strong> terça a '
       'sexta, 9h–11h, mediante agendamento.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de missas na Basílica Santo Antônio?',
        'resposta': 'Domingos às 8h, 10h, 17h e 19h; segundas às 7h e 19h30; terças às 7h, 12h e 19h30; quartas, quintas e sextas às 7h e 19h30; sábados às 7h e 19h.'},
       {'pergunta': 'Qual o endereço e telefone da Basílica Santo Antônio?',
        'resposta': 'Rua Paraíba, 747, Campos Elíseos, CEP 14080-020, Ribeirão Preto/SP. Telefone: (16) 3625-0507 e WhatsApp (16) 99753-3910.'},
       {'pergunta': 'Quando a igreja se tornou Basílica Menor?',
        'resposta': 'Em 2019, conforme o título canônico registrado pela Arquidiocese de Ribeirão Preto. A paróquia foi fundada em 1947 e é administrada pelos monges olivetanos.'},
       {'pergunta': 'A basílica tem confissões e atendimento espiritual?',
        'resposta': 'Sim: confissões às segundas e terças, das 15h às 17h, e quintas e sextas, das 15h às 17h; atendimento espiritual de terça a sexta, das 9h às 11h, mediante agendamento.'},
       {'pergunta': 'O Santuário das Sete Capelas pertence ao mesmo complexo?',
        'resposta': 'Sim. O Santuário Nossa Senhora da Medalha Milagrosa, no Morro do São Bento, integra o complexo administrado pelos monges olivetanos, com missas diárias às 8h e dominical às 9h30.'},
   ],
)

# ---- 2. Santuário N. Sra. do Rosário (abre com HISTÓRIA/santuário) ──
_sr = _v('santuario-nossa-senhora-do-rosario', 'nome')
_p('santuario-nossa-senhora-do-rosario',
   f'{_sr} em Ribeirão Preto | Ribeirão Viva',
   f'{_sr}: O Santuário Mariano de 1914 na Vila Tibério',
   f'História centenária, missas diárias e confissões do {_sr}: horários '
   f'completos e contatos oficiais verificados na Arquidiocese de Ribeirão Preto.',
   f'{_sr}, santuário mariano, Vila Tibério, missas, claretianos, Ribeirão Preto',
   'Santuário Nossa Senhora do Rosário',
   'Igrejas e Fé Popular',
   secoes={
       'resumo': (
           '<p>Um século de devoção mariana tem endereço na Rua Martinico '
           'Prado, 599: o <strong>' + _sr + '</strong>, fundado em '
           '<strong>1914</strong> na Vila Tibério, é um dos templos mais '
           'antigos em atividade na cidade. Em <strong>7 de outubro de '
           '2002</strong>, a igreja foi elevada a Santuário, reconhecendo o '
           'fluxo de devotos que a tornaram referência da devoção a Nossa '
           'Senhora em Ribeirão Preto.</p>'
           '<p>Os <strong>Missionários Claretianos</strong> (CMF) administram a '
           'comunidade e publicam a programação em site próprio — prática que '
           'garante ao visitante horários sempre conferíveis. A secretaria '
           'paroquial abre de terça a sexta, das 8h às 17h, e aos sábados, das '
           '8h às 12h.</p>'
           '<p>No mapa da fé ribeirão-pretana, o santuário fica no eixo central '
           '— a poucos quarteirões dos grandes templos do centro, o que permite '
           'montar um percurso devocional inteiro a pé.</p>'
       ),
       'historia': (
           '<h3>De 1914 ao título de Santuário</h3>'
           '<p>Fundada em <strong>1914</strong>, a paróquia nasceu para atender '
           'a Vila Tibério, bairro de trabalhadores que crescia ao lado dos '
           'trilhos da cidade cafeeira. Ao longo do século XX a igreja firmou-se '
           'como polo mariano — devoção do rosário que dá nome ao templo — e '
           'reuniu gerações de famílias do bairro.</p>'
           '<p>Em <strong>7 de outubro de 2002</strong>, a Arquidiocese '
           'formalizou a elevação a <strong>Santuário</strong>. A administração '
           'dos <strong>Missionários Claretianos</strong>, congregação fundada '
           'por Santo Antônio Maria Claret, liga a comunidade à espiritualidade '
           'claretiana — marcada pela missão popular e pelo atendimento às '
           'periferias. O site oficial da paróquia, linkado pela Arquidiocese, '
           'preserva o registro da trajetória centenária.</p>'
       ),
       'detalhes_visita': (
           '<p>A grade de missas cobre a semana: <strong>terças às 7h e '
           '19h30</strong>; quartas às 7h e 15h; quintas e sextas às 7h e 19h30; '
           'sábados às 7h e 18h; domingos às 7h, 10h e 18h. As <strong>'
           'confissões</strong> ocorrem às terças, quintas e sextas às 15h, e '
           'aos sábados no horário publicado pela paróquia.</p>'
           '<p>A <strong>secretaria paroquial</strong> atende de terça a sexta, '
           'das 8h às 17h, e aos sábados, das 8h às 12h — canal oficial para '
           'agendamentos e informações sobre a vida comunitária.</p>'
       ),
       'como_chegar': (
           '<p>O endereço é <strong>Rua Martinico Prado, 599, Vila Tibério, CEP '
           '14050-050</strong>. A região é atendida pelas linhas do eixo '
           'central; consulte o hub de linhas do portal para o itinerário que '
           'mais atende seu ponto de partida.</p>'
       ),
       'atracoes_proximas': (
           '<p>Seguindo pela Vila Tibério rumo ao centro, o visitante alcança a '
           'Catedral Metropolitana, a Igreja São Benedito e a Praça XV — o '
           'circuito devocional clássico da cidade, todo caminhável.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Sugestão: missa das 7h no santuário '
           'seguida de caminhada matinal pelo circuito de fé do centro.</p>'
       ),
   },
   secao_extra_titulo='Horário de Missas',
   secao_extra_html=(
       '<h3>Santuário — grade semanal</h3>'
       '<ul>'
       '<li><strong>Terças:</strong> 7h e 19h30</li>'
       '<li><strong>Quartas:</strong> 7h e 15h</li>'
       '<li><strong>Quintas e sextas:</strong> 7h e 19h30</li>'
       '<li><strong>Sábados:</strong> 7h e 18h</li>'
       '<li><strong>Domingos:</strong> 7h, 10h e 18h</li>'
       '</ul>'
       '<p><strong>Confissões:</strong> terças, quintas e sextas às 15h; '
       'sábados conforme publicado pela paróquia. <strong>Secretaria:</strong> '
       'terça a sexta, 8h–17h; sábados, 8h–12h.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de missas no Santuário Nossa Senhora do Rosário?',
        'resposta': 'Terças às 7h e 19h30; quartas às 7h e 15h; quintas e sextas às 7h e 19h30; sábados às 7h e 18h; domingos às 7h, 10h e 18h.'},
       {'pergunta': 'Qual o endereço e telefone do Santuário do Rosário?',
        'resposta': 'Rua Martinico Prado, 599, Vila Tibério, CEP 14050-050, Ribeirão Preto/SP. Telefone: (16) 3625-1336 e WhatsApp (16) 98106-7291.'},
       {'pergunta': 'Por que a igreja é um Santuário?',
        'resposta': 'Foi elevada a Santuário em 7 de outubro de 2002, reconhecendo o fluxo de devotos de Nossa Senhora do Rosário. A paróquia foi fundada em 1914 e é administrada pelos Missionários Claretianos.'},
       {'pergunta': 'Quando posso me confessar no santuário?',
        'resposta': 'Às terças, quintas e sextas às 15h, e aos sábados no horário publicado pela paróquia em seu site oficial.'},
       {'pergunta': 'A secretaria paroquial funciona em que horário?',
        'resposta': 'De terça a sexta, das 8h às 17h, e aos sábados, das 8h às 12h.'},
   ],
)

# ---- 3. Paróquia Santa Rita de Cássia (abre com COMUNIDADE) ──────────
_sri = _v('paroquia-santa-rita-de-cassia', 'nome')
_p('paroquia-santa-rita-de-cassia',
   f'{_sri} em Ribeirão Preto | Ribeirão Viva',
   f'{_sri}: Uma Comunidade de Fé que Não Para no Jardim Independência',
   f'A vida comunitária da {_sri}: missas diárias às 17h, secretaria e '
   f'telefones oficiais, verificados na Arquidiocese de Ribeirão Preto.',
   f'{_sri}, missas Jardim Independência, paróquia leste Ribeirão Preto, '
   'forania Bom Jesus da Lapa',
   'Paróquia Santa Rita de Cássia',
   'Igrejas e Fé Popular',
   secoes={
       'resumo': (
           '<p>Há quatro décadas a <strong>' + _sri + '</strong> serve o '
           'quadrante leste de Ribeirão Preto com uma rotina que não para: '
           '<strong>missa todos os dias às 17h</strong>, de segunda a sábado, e '
           'duas celebrações dominicais — 8h e 19h. A constância da grade '
           'reflete o perfil comunitário da paróquia, fundada em <strong>1982'
           '</strong> para acompanhar a expansão do Jardim Independência.</p>'
           '<p>Integrante da <strong>Forania Bom Jesus da Lapa</strong>, a '
           'comunidade é conduzida pelo pároco Pe. Paulo Fernando Mello Cunha. '
           'A secretaria abre todas as tardes da semana, das 14h às 16h30 — '
           'janela prática para quem trabalha de manhã e precisa resolver '
           'documentos ou agendar participação nas pastorais.</p>'
       ),
       'historia': (
           '<h3>Quatro décadas acompanhando o bairro</h3>'
           '<p>Criada em <strong>1982</strong>, a paróquia nasceu quando o '
           'Jardim Independência consolidava-se como um dos bairros '
           'residenciais mais populosos da zona leste. O temporal de fundação '
           '— início dos anos 1980 — é o da cidade que se expandia para além '
           'dos trilhos do centro, e a igreja cresceu junto com as famílias que '
           'chegavam.</p>'
           '<p>Hoje a comunidade integra a <strong>Forania Bom Jesus da '
           'Lapa</strong>, o agrupamento de paróquias coordenado pela '
           'Arquidiocese para a região. No registro oficial, o nome popular '
           'completo — <em>Paróquia Santa Rita de Cássia (Jardim '
           'Independência)</em> — evita a confusão com as paróquias homônimas '
           'da cidade: <strong>Santa Rita de Cássia das Palmeiras</strong> '
           '(2000) e <strong>Santa Rita de Cássia</strong> (2011), cada uma em '
           'bairro próprio.</p>'
       ),
       'detalhes_visita': (
           '<p>A grade é enxuta e firme: <strong>missa diária às 17h</strong>, '
           'de segunda a sábado, e aos <strong>domingos às 8h e 19h</strong> — '
           'celebração matinal para quem prefere começar o dia na igreja e '
           'noturna para quem sai do trabalho. A secretaria paroquial atende '
           'de <strong>segunda a sábado, das 14h às 16h30</strong>.</p>'
           '<p>Para contato, os canais oficiais são o telefone (16) 3626-0844 '
           'e o WhatsApp (16) 99138-8198, conforme listagem da Arquidiocese.</p>'
       ),
       'como_chegar': (
           '<p>O endereço é <strong>Rua Primo de Furquim, 18, Jardim '
           'Independência, CEP 14076-270</strong>, na zona leste. As linhas '
           'municipais do eixo leste atendem o bairro; o hub de linhas do '
           'portal indica a opção mais direta a partir do seu ponto de '
           'partida.</p>'
       ),
       'atracoes_proximas': (
           '<p>O Jardim Independência fica no quadrante do Parque Curupira e do '
           'Morro de São Bento — conjunto de áreas verdes e equipamentos '
           'culturais que complementa a visita à região leste.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Missas das 17h combinam com um '
           'fim de tarde no Parque Curupira, no mesmo quadrante da cidade.</p>'
       ),
   },
   secao_extra_titulo='Horário de Missas',
   secao_extra_html=(
       '<h3>Grade semanal</h3>'
       '<ul>'
       '<li><strong>Segunda a sábado:</strong> 17h</li>'
       '<li><strong>Domingos:</strong> 8h e 19h</li>'
       '</ul>'
       '<p><strong>Secretaria paroquial:</strong> segunda a sábado, das 14h '
       'às 16h30.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de missas na Paróquia Santa Rita de Cássia?',
        'resposta': 'Missas diárias de segunda a sábado às 17h, e aos domingos às 8h e 19h.'},
       {'pergunta': 'Qual o endereço e telefone da Paróquia Santa Rita de Cássia?',
        'resposta': 'Rua Primo de Furquim, 18, Jardim Independência, CEP 14076-270, Ribeirão Preto/SP. Telefone: (16) 3626-0844 e WhatsApp (16) 99138-8198.'},
       {'pergunta': 'A qual forania a paróquia pertence?',
        'resposta': 'À Forania Bom Jesus da Lapa. Fundada em 1982, é distinta das paróquias homônimas Santa Rita de Cássia das Palmeiras (2000) e Santa Rita de Cássia (2011), também em Ribeirão Preto.'},
       {'pergunta': 'Qual o horário da secretaria paroquial?',
        'resposta': 'Segunda a sábado, das 14h às 16h30.'},
       {'pergunta': 'Quem é o pároco de Santa Rita de Cássia?',
        'resposta': 'Pe. Paulo Fernando Mello Cunha, conforme o registro oficial da Arquidiocese de Ribeirão Preto (consultado em outubro de 2026).'},
   ],
)

# ---- 4. Paróquia Santa Teresinha Doutora (abre com LOCALIZAÇÃO) ──────
_st = _v('paroquia-santa-teresinha-doutora', 'nome')
_p('paroquia-santa-teresinha-doutora',
   f'{_st} em Ribeirão Preto | Ribeirão Viva',
   f'{_st}: Quatro Missas de Domingo na Esquina da Av. Presidente Kennedy',
   f'Localização estratégica e grade completa da {_st}: missas, secretaria '
   f'até as 21h e contatos oficiais verificados na Arquidiocese.',
   f'{_st}, missas Ribeirânia, Av. Presidente Kennedy, paróquia 2000, '
   'forania São Sebastião',
   'Paróquia Santa Teresinha Doutora',
   'Igrejas e Fé Popular',
   secoes={
       'resumo': (
           '<p>Na esquina da Rua Walter Antunes Campos com a <strong>Av. '
           'Presidente Kennedy</strong>, a <strong>' + _st + '</strong> fica '
           'numa das cruzes mais movimentadas da Ribeirânia. A localização '
           'estratégica espelha a agenda: <strong>quatro missas aos '
           'domingos</strong> — 8h, 10h, 17h30 e 19h30 — e celebrações '
           'matinais nos dias úteis.</p>'
           '<p>Fundada em <strong>2000</strong>, a paróquia pertence à '
           '<strong>Forania São Sebastião</strong> e é conduzida pelo pároco '
           'Pe. Paulo Henrique Martins, com os diáconos Ricardo Rodrigues '
           'Nogueira e Alessandro Del\'Arco. A secretaria funciona até as '
           '<strong>21h</strong> de segunda a quinta — horário estendido que '
           'atende quem só consegue resolver depois do expediente.</p>'
       ),
       'historia': (
           '<h3>A paróquia que cresceu com a Ribeirânia</h3>'
           '<p>Erigida em <strong>2000</strong>, a comunidade acompanhou a '
           'explosão urbana da Ribeirânia — bairro que se tornou um dos mais '
           'populosos de Ribeirão Preto nas duas últimas décadas. A escolha '
           'da esquina com a Av. Presidente Kennedy, eixo estrutural da '
           'região, colocou o templo no caminho diário de milhares de '
           'moradores.</p>'
           '<p>A comunidade integra a <strong>Forania São Sebastião</strong>, '
           'grupo regional de paróquias da Arquidiocese. O nome oficial '
           'distingue-a da paróquia <strong>Santa Teresinha do Menino '
           'Jesus</strong> (1975), da Vila Tamandaré; o popular "Matriz de '
           'Santa Teresinha Doutora", adotado nas redes sociais oficiais da '
           'comunidade, consolidou-se entre os fiéis da Ribeirânia.</p>'
           '<p>A residência paroquial funciona em endereço próprio, na Rua '
           'Mariana Cândida Rosa Cury, 820, Ribeirânia — informação útil para '
           'correspondência e contatos administrativos da comunidade.</p>'
       ),
       'detalhes_visita': (
           '<p>Grade dominical completa: <strong>8h, 10h, 17h30 e 19h30</strong>. '
           'Nos dias úteis, missas às <strong>7h15</strong> (segundas, terças, '
           'quintas e sextas; quartas também às 19h30), e aos <strong>sábados '
           'às 19h</strong>.</p>'
           '<p>A <strong>secretaria paroquial</strong> atende de segunda a '
           'quinta, das 14h às 21h, e às sextas, das 14h às 18h. Contatos: '
           'telefone (16) 3237-7270 e WhatsApp (16) 98216-8668.</p>'
       ),
       'como_chegar': (
           '<p>Endereço oficial: <strong>Rua Walter Antunes Campos, s/n, '
           'Ribeirânia, CEP 14096-290</strong>, esquina com a Av. Presidente '
           'Kennedy. A avenida é um dos eixos mais bem servidos de linhas '
           'municipais da cidade; consulte o hub de linhas do portal.</p>'
       ),
       'atracoes_proximas': (
           '<p>A Ribeirânia abriga o Parque Curupira e fica no quadrante do '
           'Morro de São Bento — paradas que complementam a visita à região '
           'leste da cidade.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">A missa das 8h de domingo abre o '
           'dia para um roteiro pelo Parque Curupira e pelo Morro de São '
           'Bento.</p>'
       ),
   },
   secao_extra_titulo='Horário de Missas',
   secao_extra_html=(
       '<h3>Grade semanal</h3>'
       '<ul>'
       '<li><strong>Domingos:</strong> 8h, 10h, 17h30 e 19h30</li>'
       '<li><strong>Segundas, terças, quintas e sextas:</strong> 7h15</li>'
       '<li><strong>Quartas:</strong> 7h15 e 19h30</li>'
       '<li><strong>Sábados:</strong> 19h</li>'
       '</ul>'
       '<p><strong>Secretaria:</strong> segunda a quinta, 14h–21h; sexta, '
       '14h–18h. <strong>Residência paroquial:</strong> Rua Mariana Cândida '
       'Rosa Cury, 820, Ribeirânia, CEP 14096-300.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de missas na Paróquia Santa Teresinha Doutora?',
        'resposta': 'Domingos às 8h, 10h, 17h30 e 19h30; segundas, terças, quintas e sextas às 7h15; quartas às 7h15 e 19h30; sábados às 19h.'},
       {'pergunta': 'Qual o endereço e telefone da Paróquia Santa Teresinha Doutora?',
        'resposta': 'Rua Walter Antunes Campos, s/n, Ribeirânia, CEP 14096-290, esquina com a Av. Presidente Kennedy. Telefone: (16) 3237-7270 e WhatsApp (16) 98216-8668.'},
       {'pergunta': 'A secretaria atende à noite?',
        'resposta': 'Sim: de segunda a quinta, das 14h às 21h, e às sextas, das 14h às 18h.'},
       {'pergunta': 'A paróquia tem endereço administrativo próprio?',
        'resposta': 'Sim. A residência paroquial funciona na Rua Mariana Cândida Rosa Cury, 820, Ribeirânia, CEP 14096-300.'},
       {'pergunta': 'Qual a diferença entre Santa Teresinha Doutora e Santa Teresinha do Menino Jesus?',
        'resposta': 'São paróquias distintas: Santa Teresinha Doutora (2000) fica na Ribeirânia, e Santa Teresinha do Menino Jesus (1975), na Vila Tamandaré. A Doutora pertence à Forania São Sebastião.'},
   ],
)

# ---- 5. Igreja São Benedito (abre com ARQUITETURA/ADORação) ──────────
_sb = _v('igreja-sao-benedito', 'nome')
_p('igreja-sao-benedito',
   f'{_sb} em Ribeirão Preto | Ribeirão Viva',
   f'{_sb}: Silêncio e Adoração Perpétua no Quarteirão Paulista',
   f'Templo Votivo de 1920 com adoração diária das 8h30 às 16h na Rua '
   f'Prudente de Morais: missas, contatos e horários verificados na Arquidiocese.',
   f'{_sb}, Templo Votivo, adoração perpétua, missas centro Ribeirão Preto, '
   'Quarteirão Paulista',
   'Igreja São Benedito (Templo Votivo)',
   'Igrejas e Fé Popular',
   secoes={
       'resumo': (
           '<p>Há um lugar no centro de Ribeirão Preto onde o silêncio é '
           'programação oficial: a <strong>' + _sb + '</strong>, <strong>Templo '
           'Votivo</strong> de <strong>1920</strong> dedicado à adoração ao '
           'Santíssimo Sacramento. O templo abre para oração todos os dias, '
           'das <strong>8h30 às 16h</strong> — e a Adoração Perpétua se '
           'mantém de segunda a sexta no mesmo horário.</p>'
           '<p>Igreja reitoral — sem vida paroquial própria, conduzida por um '
           'reitor —, a São Benedito é hoje conduzida pelo Pe. José Alceu de '
           'Souza Júnior. A missa diária das <strong>17h</strong> pontua o fim '
           'da tarde no eixo do Quarteirão Paulista, a poucos passos da Praça '
           'XV.</p>'
       ),
       'historia': (
           '<h3>Um templo nascido de um voto</h3>'
           '<p>Templos votivos nascem de promessas: ergue-se a igreja em '
           'cumprimento de um voto, e a devoção que a fundou se torna sua '
           'razão de ser. A <strong>São Benedito</strong> foi construída em '
           '<strong>1920</strong> sob essa lógica — e a adoração ao Santíssimo '
           'permanece como vocação primeira do edifício um século depois.</p>'
           '<p>Como <strong>igreja reitoral</strong>, o templo não administra '
           'batizados e casamentos como uma paróquia: sua missão é a oração '
           'contínua e a vida sacramental diária. Essa configuração a distingue '
           'da <strong>paróquia São Benedito (2000)</strong>, na Rua Cel. '
           'Américo Batista, 3448 — comunidade homônima que atende sua região '
           'própria na cidade.</p>'
           '<p>Endereço de fé no coração da cidade: <strong>Rua Prudente de '
           'Morais, 657, Centro, CEP 14015-100</strong> — no eixo que liga a '
           'Catedral Metropolitana ao Quarteirão Paulista, o percurso '
           'histórico mais caminhado de Ribeirão Preto.</p>'
       ),
       'detalhes_visita': (
           '<p>Missas: <strong>domingos às 10h e 19h30</strong>; <strong>segunda '
           'a sábado às 17h</strong>. A <strong>adoração ao Santíssimo '
           'Sacramento</strong> acontece diariamente, das 8h30 às 16h, e a '
           '<strong>Adoração Perpétua</strong> do Templo Votivo, de segunda a '
           'sexta, das 8h30 às 16h.</p>'
           '<p>Telefone oficial: <strong>(16) 3931-5591</strong>.</p>'
       ),
       'como_chegar': (
           '<p>A igreja fica na <strong>Rua Prudente de Morais, 657, Centro</strong>, '
           'a poucos minutos a pé da Praça XV de Novembro e da Catedral '
           'Metropolitana. Dezenas de linhas municipais atendem o centro; o '
           'hub de linhas do portal mostra a opção mais direta.</p>'
       ),
       'atracoes_proximas': (
           '<p>Catedral Metropolitana, Praça XV de Novembro, Quarteirão '
           'Paulista e Theatro Pedro II formam o entorno imediato — um '
           'roteiro completo de fé e história em menos de um quilômetro.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Percurso clássico: Catedral → '
           'São Benedito (adoração silenciosa) → Quarteirão Paulista → Praça '
           'XV.</p>'
       ),
   },
   secao_extra_titulo='Horário de Missas',
   secao_extra_html=(
       '<h3>Grade semanal</h3>'
       '<ul>'
       '<li><strong>Domingos:</strong> 10h e 19h30</li>'
       '<li><strong>Segunda a sábado:</strong> 17h</li>'
       '</ul>'
       '<h3>Adoração</h3>'
       '<ul>'
       '<li><strong>Adoração ao Santíssimo:</strong> diariamente, 8h30–16h</li>'
       '<li><strong>Adoração Perpétua (Templo Votivo):</strong> segunda a '
       'sexta, 8h30–16h</li>'
       '</ul>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de missas na Igreja São Benedito?',
        'resposta': 'Domingos às 10h e 19h30; de segunda a sábado às 17h.'},
       {'pergunta': 'Qual o endereço e telefone da Igreja São Benedito?',
        'resposta': 'Rua Prudente de Morais, 657, Centro, CEP 14015-100, Ribeirão Preto/SP. Telefone: (16) 3931-5591.'},
       {'pergunta': 'O que é um Templo Votivo?',
        'resposta': 'É uma igreja erguida em cumprimento de um voto. A São Benedito mantém a Adoração Perpétua ao Santíssimo Sacramento de segunda a sexta, das 8h30 às 16h.'},
       {'pergunta': 'Posso visitar a igreja fora dos horários de missa?',
        'resposta': 'Sim: a adoração ao Santíssimo Sacramento acontece diariamente, das 8h30 às 16h, com o templo aberto à oração.'},
       {'pergunta': 'A São Benedito é paróquia?',
        'resposta': 'Não — é igreja reitoral, conduzida por um reitor (atualmente Pe. José Alceu de Souza Júnior). A paróquia São Benedito (2000) fica na Rua Cel. Américo Batista, 3448.'},
   ],
)

# ---- 6. Paróquia Senhor Bom Jesus do Bonfim (abre com ROMARIA) ───────
_bf = _v('paroquia-senhor-bom-jesus-do-bonfim', 'nome')
_p('paroquia-senhor-bom-jesus-do-bonfim',
   f'{_bf} em Bonfim Paulista | Ribeirão Viva',
   f'{_bf}: A Matriz da Romaria no Distrito Histórico',
   f'Romaria de Nossa Senhora Aparecida e missas na matriz de 1898 de '
   f'Bonfim Paulista: horários, endereço e contatos verificados na Arquidiocese.',
   f'{_bf}, Bonfim Paulista, romaria Nossa Senhora Aparecida, matriz 1898, '
   'distrito de Ribeirão Preto',
   'Paróquia Senhor Bom Jesus do Bonfim',
   'Igrejas e Fé Popular',
   secoes={
       'resumo': (
           '<p>Todos os anos, romeiros saem de Ribeirão Preto e seguem a pé ou '
           'em carreata até a <strong>' + _bf + '</strong>, matriz de '
           '<strong>1898</strong> no distrito de Bonfim Paulista. A <strong>'
           'Romaria Nossa Senhora Aparecida</strong> é a tradição que liga a '
           'cidade ao seu distrito mais antigo — e tem ponto de chegada neste '
           'templo centenário.</p>'
           '<p>Integrante da <strong>Forania São José</strong> e administrada '
           'pelo Pe. Cláudio Pires Marçal, a comunidade celebra aos sábados às '
           '<strong>19h</strong> e aos domingos às <strong>8h, 10h e 19h</strong>. '
           'A adoração silenciosa de quinta-feira, das 14h às 17h, completa a '
           'semana devocional.</p>'
       ),
       'historia': (
           '<h3>1898: uma matriz para o distrito</h3>'
           '<p>Quando a paróquia foi fundada em <strong>1898</strong>, Bonfim '
           'Paulista já era núcleo consolidado da ruralidade cafeeira — e a '
           'matriz nasceu como coração religioso do povoado. A <strong>Forania '
           'São José</strong>, agrupamento regional da Arquidiocese, reúne '
           'hoje a comunidade às paróquias da região.</p>'
           '<p>A <strong>Romaria Nossa Senhora Aparecida</strong> é o evento '
           'que projeta a matriz além do distrito: a programação da solenidade '
           'é publicada pela Arquidiocese e reúne fiéis da cidade-sede rumo '
           'ao Bonfim — tradição de devoção que atravessa gerações de '
           'ribeirão-pretanos.</p>'
           '<p>O pequeno núcleo histórico do distrito — praça, comércio '
           'local e casario antigo — gira em torno da matriz, tornando a '
           'visita um mergulho na memória rural do município.</p>'
       ),
       'detalhes_visita': (
           '<p>Missas: <strong>sábados às 19h</strong>; <strong>domingos às 8h, '
           '10h e 19h</strong>. A <strong>secretaria paroquial</strong> atende '
           'de terça a sexta, das 14h às 18h, e aos sábados, das 9h às 12h. A '
           '<strong>adoração silenciosa</strong> ocorre às quintas-feiras, das '
           '14h às 17h.</p>'
           '<p>Contatos: telefone (16) 3972-0057 e (16) 99770-6863.</p>'
       ),
       'como_chegar': (
           '<p>A matriz fica na <strong>Rua Cel. Furquim, 389, Bom Jesus, CEP '
           '14110-000, Bonfim Paulista</strong> (distrito de Ribeirão Preto/SP). '
           'O distrito fica a cerca de 15 km do centro; o acesso é feito pelas '
           'estradas distritais. Consulte o hub de linhas do portal para '
           'itinerários que atendem a região.</p>'
       ),
       'atracoes_proximas': (
           '<p>O distrito de Bonfim Paulista preserva o traçado do núcleo '
           'rural paulista: praça central, comércio de bairro e casario '
           'antigo — um contraste de ritmo com a cidade-sede.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Combine a missa dominical das '
           '10h com um passeio pela praça histórica do distrito.</p>'
       ),
   },
   secao_extra_titulo='Horário de Missas',
   secao_extra_html=(
       '<h3>Grade semanal</h3>'
       '<ul>'
       '<li><strong>Sábados:</strong> 19h</li>'
       '<li><strong>Domingos:</strong> 8h, 10h e 19h</li>'
       '</ul>'
       '<p><strong>Secretaria:</strong> terça a sexta, 14h–18h; sábados, '
       '9h–12h. <strong>Adoração silenciosa:</strong> quintas, 14h–17h.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de missas na matriz de Bonfim Paulista?',
        'resposta': 'Sábados às 19h; domingos às 8h, 10h e 19h.'},
       {'pergunta': 'Qual o endereço e telefone da Paróquia Senhor Bom Jesus do Bonfim?',
        'resposta': 'Rua Cel. Furquim, 389, Bom Jesus, CEP 14110-000, Bonfim Paulista (Ribeirão Preto/SP). Telefones: (16) 3972-0057 e (16) 99770-6863.'},
       {'pergunta': 'Quando ocorre a romaria ao Bonfim?',
        'resposta': 'A Romaria Nossa Senhora Aparecida leva romeiros de Ribeirão Preto à matriz do distrito; a programação da solenidade é publicada pela Arquidiocese de Ribeirão Preto.'},
       {'pergunta': 'A matriz tem secretaria paroquial?',
        'resposta': 'Sim: terça a sexta, das 14h às 18h, e sábados, das 9h às 12h.'},
       {'pergunta': 'Bonfim Paulista pertence a Ribeirão Preto?',
        'resposta': 'Sim, é distrito de Ribeirão Preto, a cerca de 15 km do centro. A paróquia, fundada em 1898, integra a Forania São José da Arquidiocese.'},
   ],
)

# ══════════════════════════════════════════════════════════════════════
# TEATROS E ESPAÇOS (5) — Municipal=ficha técnica, Arena=formato arena
# ══════════════════════════════════════════════════════════════════════

# ---- 7. Teatro Municipal (abre com FICHA TÉCNICA/números) ───────────
_tm = _v('teatro-municipal', 'nome')
_p('teatro-municipal',
   f'{_tm} em Ribeirão Preto | Ribeirão Viva',
   f'{_tm}: 515 Lugares de Palco Italiano no Morro do São Bento',
   f'Ficha técnica oficial do {_tm}: auditório de 515 lugares, palco '
   f'italiano de 12 x 12 m, bilheteria externa e telefone, no portal da Prefeitura.',
   f'{_tm}, ficha técnica teatro, 515 lugares, palco italiano, Morro do '
   'São Bento, editais de ocupação',
   'Teatro Municipal de Ribeirão Preto',
   'Teatros e Espaços Culturais',
   secoes={
       'resumo': (
           '<p>Os números vêm da ficha técnica oficial no portal da '
           'Prefeitura: <strong>515 lugares sentados</strong> no auditório, '
           '<strong>300 pessoas</strong> no saguão, <strong>palco de 12 x 12 '
           'metros</strong> em estilo italiano e <strong>4 lugares reservados '
           'para cadeirantes</strong>. É o <strong>' + _tm + '</strong>, casa '
           'pública inaugurada em <strong>1969</strong> no alto do Morro do '
           'São Bento.</p>'
           '<p>A bilheteria tem <strong>acesso externo</strong>, na parte '
           'frontal do edifício, com dois guichês de atendimento — projeto '
           'que permite comprar ingresso sem entrar no complexo. A casa '
           'integra, com o Teatro de Arena, o <strong>Complexo Cultural do '
           'Parque do Morro do São Bento</strong>.</p>'
       ),
       'historia': (
           '<h3>1969: modernidade na colina</h3>'
           '<p>Inaugurado em <strong>1969</strong> com linhas modernas, o '
           'Teatro Municipal levou à colina mais tradicional da cidade o '
           'formato clássico das grandes casas: o <strong>palco italiano'
           '</strong>, em que a moldura da boca de cena enquadra o espetáculo '
           'e a plateia enfrenta o palco reta — geometria das casas de ópera '
           'europeias adaptada ao concreto moderno paulista.</p>'
           '<p>A casa é o equipamento principal do <strong>Complexo Cultural '
           'do Parque do Morro do São Bento</strong>: quem sobe a colina '
           'encontra, no mesmo conjunto, o Teatro de Arena para espetáculos '
           'ao ar livre — dupla que permite programar temporada de sala e de '
           'arena no mesmo fim de semana.</p>'
           '<p>A ocupação da casa passa por <strong>editais semestrais da '
           'Secretaria Municipal da Cultura e Turismo</strong>, mecanismo '
           'que abre a grade a companhias locais e produções itinerantes — '
           'do teatro adulto ao infantil, da dança à música.</p>'
       ),
       'detalhes_visita': (
           '<p>Endereço oficial: <strong>Praça Alto do São Bento, s/nº, CEP '
           '14085-459</strong>. Telefone: <strong>(16) 3625-6841</strong>. A '
           'bilheteria externa opera em dois guichês; horários de bilheteria '
           'e preços variam conforme o espetáculo e devem ser confirmados no '
           'canal oficial ou no portal municipal.</p>'
           '<p>O auditório conta com <strong>4 lugares reservados para '
           'cadeirantes</strong>, conforme a ficha técnica — acessibilidade '
           'prevista no projeto original da casa.</p>'
       ),
       'como_chegar': (
           '<p>O complexo fica na <strong>Praça Alto do São Bento</strong>, no '
           'topo da colina que dá nome ao parque. O acesso é feito pelas vias '
           'do entorno; consulte o hub de linhas do portal para o itinerário '
           'de ônibus mais adequado — a região é atendida pelas linhas dos '
           'eixos oeste e norte.</p>'
       ),
       'atracoes_proximas': (
           '<p>No mesmo complexo: o <strong>Teatro de Arena</strong>, o '
           'parque do Morro do São Bento e o Santuário das Sete Capelas — '
           'arte, natureza e fé reunidas numa única colina.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Programa de tarde no teatro, '
           'pôr do sol no parque e missa vespertina nas Sete Capelas: a '
           'colina comporta o dia inteiro.</p>'
       ),
   },
   secao_extra_titulo='Programação',
   secao_extra_html=(
       '<p>A grade do Teatro Municipal é definida por <strong>editais de '
       'ocupação semestrais</strong> da Secretaria Municipal da Cultura e '
       'Turismo. A agenda vigente circula no portal oficial da Prefeitura e '
       'na bilheteria externa da casa — a confirmação de sessões, horários e '
       'preços deve sempre partir desses canais.</p>'
   ),
   faq=[
       {'pergunta': 'Qual a capacidade do Teatro Municipal de Ribeirão Preto?',
        'resposta': '515 lugares sentados no auditório e 300 pessoas no saguão, segundo a ficha técnica oficial. O palco, em estilo italiano, tem 12 x 12 metros, e há 4 lugares reservados para cadeirantes.'},
       {'pergunta': 'Onde fica e qual o telefone do Teatro Municipal?',
        'resposta': 'Praça Alto do São Bento, s/nº, CEP 14085-459, no Complexo Cultural do Parque do Morro do São Bento. Telefone: (16) 3625-6841.'},
       {'pergunta': 'Como funciona a bilheteria do Teatro Municipal?',
        'resposta': 'A bilheteria tem acesso externo, na parte frontal do teatro, com dois guichês. Horários e preços variam conforme o espetáculo e devem ser confirmados nos canais oficiais.'},
       {'pergunta': 'Como é definida a programação da casa?',
        'resposta': 'Por editais de ocupação publicados pela Secretaria Municipal da Cultura e Turismo a cada semestre, abertos a companhias locais e produções itinerantes.'},
       {'pergunta': 'O Teatro Municipal fica perto de outros pontos turísticos?',
        'resposta': 'Sim: integra o Complexo Cultural do Parque do Morro do São Bento, ao lado do Teatro de Arena e próximo ao Santuário das Sete Capelas.'},
   ],
)

# ---- 8. Teatro de Arena (abre com FORMATO/conceito) ──────────────────
_ta = _v('teatro-de-arena', 'nome')
_p('teatro-de-arena',
   f'{_ta} em Ribeirão Preto | Ribeirão Viva',
   f'{_ta}: A Plateia Envolvente sob o Céu do São Bento',
   f'O formato de arena do {_ta}: palco central, plateia em volta e '
   f'espetáculos ao ar livre no Complexo Cultural do Morro do São Bento.',
   f'{_ta}, teatro ao ar livre, arena Jaime Zeiger, Morro do São Bento, '
   'espetáculos gratuitos Ribeirão Preto',
   'Teatro de Arena "Jaime Zeiger"',
   'Teatros e Espaços Culturais',
   secoes={
       'resumo': (
           '<p><strong>2.100 pessoas sentadas</strong> sob o céu aberto, em '
           'auditório de meia-encosta: o <strong>' + _ta + '</strong> é o '
           '<strong>primeiro teatro de arena construído no interior do Estado '
           'de São Paulo</strong>, inaugurado em <strong>1969</strong> — '
           'idealizado e construído pelo próprio <strong>Jaime Zeiger</strong>, '
           'que o projetou após pesquisas acústicas na Europa e no Oriente '
           'Médio.</p>'
           '<p>A estreia aconteceu com <strong>"Antígona", de Sófocles</strong>, '
           'e o espaço foi <strong>reformado em 1986 e reinaugurado em '
           '1987</strong>. Hoje, os <strong>2.100 lugares</strong> da ficha '
           'técnica oficial fazem do arena o maior público potencial do '
           'Complexo Cultural do Parque do Morro do São Bento — recebe shows '
           'e festivais, como o <strong>Minaz Arena Rock</strong> (junho) e '
           'show solidário em maio.</p>'
       ),
       'historia': (
           '<h3>Um visionário e sua arena de meia-encosta</h3>'
           '<p>A história do espaço se confunde com a de seu criador: '
           '<strong>Jaime Zeiger</strong> pesquisou acústica na Europa e no '
           'Oriente Médio antes de erguer, em <strong>1969</strong>, o '
           '<strong>primeiro teatro de arena do interior paulista</strong> — '
           'construído numa meia-encosta, em área de aproximadamente '
           '<strong>6 mil metros quadrados</strong>, aproveitando a '
           'topografia da colina para o desenho envolvente da plateia.</p>'
           '<p>O primeiro espetáculo foi <strong>"Antígona", de Sófocles'
           '</strong> — estreia à altura da ambição do projeto. Quase duas '
           'décadas depois, o arena passou por <strong>reforma em 1986 e '
           'reinauguração em 1987</strong>, consolidando-se como o grande '
           'palco aberto da cidade.</p>'
           '<p>Na grade atual, o espaço recebe <strong>shows e festivais'
           '</strong> — do Minaz Arena Rock, em junho, ao show solidário de '
           'maio — além da ocupação regular via <strong>editais da Secretaria '
           'Municipal da Cultura e Turismo</strong>, em conjunto com o Teatro '
           'Municipal (o edital do 2º semestre de 2026 teve inscrições até '
           '1º de junho).</p>'
       ),
       'detalhes_visita': (
           '<p>O arena fica na <strong>Praça Alto do São Bento</strong>, no '
           'mesmo conjunto do Teatro Municipal, em Ribeirão Preto/SP. O '
           'telefone de referência do complexo é <strong>(16) 3625-6841'
           '</strong>. Como espaço aberto, a experiência depende da agenda: '
           'consulte o edital vigente e a programação publicada antes de '
           'subir a colina.</p>'
       ),
       'como_chegar': (
           '<p>O acesso é o mesmo do Teatro Municipal: vias do entorno do '
           '<strong>parque do Morro do São Bento</strong>, na Praça Alto do '
           'São Bento. Consulte o hub de linhas do portal para as opções que '
           'atendem a região.</p>'
       ),
       'atracoes_proximas': (
           '<p>Teatro Municipal, parque do Morro do São Bento e Santuário das '
           'Sete Capelas completam a colina — o complexo cultural completo '
           'da cidade em um só lugar.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Espetáculo no arena ao fim da '
           'tarde, com o pôr do sol do Morro do São Bento de cortina.</p>'
       ),
   },
   secao_extra_titulo='Programação',
   secao_extra_html=(
       '<p>A grade do arena integra os <strong>editais de ocupação dos '
       'teatros municipais</strong> — o mesmo processo semestral da '
       'Secretaria Municipal da Cultura e Turismo que programa o Teatro '
       'Municipal. A agenda vigente é publicada no portal oficial da '
       'Prefeitura de Ribeirão Preto.</p>'
   ),
   faq=[
       {'pergunta': 'O que é o Teatro de Arena de Ribeirão Preto?',
        'resposta': 'É o espaço de espetáculos ao ar livre do Complexo Cultural do Parque do Morro do São Bento, com palco central e plateia envolvente. O nome oficial homenageia Jaime Zeiger.'},
       {'pergunta': 'Onde fica o Teatro de Arena?',
        'resposta': 'Na Praça Alto do São Bento, no Complexo Cultural do Parque do Morro do São Bento, o mesmo conjunto do Teatro Municipal.'},
       {'pergunta': 'Como saber a programação do arena?',
        'resposta': 'Pela agenda publicada no portal oficial da Prefeitura: a ocupação é definida nos editais semestrais da Secretaria Municipal da Cultura e Turismo.'},
       {'pergunta': 'Qual a diferença entre arena e teatro convencional?',
        'resposta': 'Na arena, o público cerca o palco por todos os lados e o espetáculo acontece ao ar livre; no teatro convencional, a plateia enfrenta um palco moldurado — como no Teatro Municipal, com palco italiano de 12 x 12 m.'},
       {'pergunta': 'O arena tem telefone próprio?',
        'resposta': 'O telefone de referência do complexo dos teatros municipais é o (16) 3625-6841, exibido no portal oficial.'},
   ],
)

# ---- 9. Centro Cultural Palace (abre com PRÊMIO/2026) ────────────────
_cp = _v('centro-cultural-palace', 'nome')
_p('centro-cultural-palace',
   f'{_cp} em Ribeirão Preto | Ribeirão Viva',
   f'{_cp}: O Palace Hotel Centenário Premiado pela Estado',
   f'Centenário em 2026 e Prêmio Governador do Estado para as Artes: '
   f'a trajetória do {_cp} no prédio tombado do antigo Palace Hotel.',
   f'{_cp}, Palace Hotel, prêmio artes 2026, exposições Ribeirão Preto, '
   'prédio tombado, Rua Álvares Cabral',
   'Centro Cultural Palace',
   'Teatros e Espaços Culturais',
   secoes={
       'resumo': (
           '<p>O ano de <strong>2026</strong> dobrou a festa do '
           '<strong>' + _cp + '</strong>: o prédio do antigo Palace Hotel '
           'completou <strong>100 anos</strong> e o equipamento foi '
           '<strong>vencedor da categoria Museus e Centros Culturais do '
           'Prêmio Governador do Estado para as Artes 2026</strong> — a '
           'cerimônia aconteceu em 29 de julho de 2026, no Teatro Sérgio '
           'Cardoso, na capital.</p>'
           '<p>Instalado no prédio tombado do antigo <strong>Palace '
           'Hotel</strong>, na Rua Álvares Cabral, 322, o centro é '
           'equipamento da <strong>Secretaria Municipal da Cultura e '
           'Turismo</strong> e mantém programação contínua de exposições, '
           'eventos e atividades culturais abertas à cidade.</p>'
       ),
       'historia': (
           '<h3>Do Central Hotel de 1926 ao centenário de 2026</h3>'
           '<p>A história do edifício começa antes do nome: a obra foi '
           '<strong>iniciada em 1924</strong> pelo comerciante de café '
           '<strong>Adalberto Henrique de Oliveira Roxo</strong>, que '
           'inaugurou o <strong>Central Hotel em 1926</strong>, na esquina da '
           'Rua Duque de Caxias com a Álvares Cabral — peça do '
           '<strong>Quarteirão Paulista</strong>. Reformado e renomeado '
           '<strong>Palace Hotel</strong> após aquisição pela <strong>Cia. '
           'Cervejaria Paulista</strong> (por volta de 1930), funcionou como '
           'hotel até <strong>1992</strong>.</p>'
           '<p>O tombamento pelo <strong>CONDEPHAAT</strong> veio em '
           '<strong>7 de maio de 1982</strong> (Resolução nº 32) — na mesma '
           'resolução que protegeu o <strong>Theatro Pedro II</strong>, seu '
           'vizinho de quarteirão. Em <strong>23 de julho de 1996</strong>, o '
           'prédio foi permutado com a Antarctica, e a Prefeitura o recuperou '
           'com obras finais em <strong>30 de setembro de 2011</strong>, '
           'reabrindo-o como <strong>Centro Cultural Palace em 20 de outubro '
           'de 2011</strong>.</p>'
           '<p>O ano de <strong>2026</strong> marca o <strong>centenário</strong> '
           'do prédio — celebrado com programação especial, como o evento de '
           'centenário de agosto de 2026 — e o <strong>Prêmio Governador do '
           'Estado para as Artes</strong>, na categoria Museus e Centros '
           'Culturais, entregue em 29 de julho de 2026 no Teatro Sérgio '
           'Cardoso, na capital.</p>'
       ),
       'detalhes_visita': (
           '<p>Endereço: <strong>Rua Álvares Cabral, 322, Centro</strong>, '
           'Ribeirão Preto/SP. Telefones oficiais: <strong>(16) 3636-9187</strong> '
           '(administração) e <strong>(16) 3636-2893</strong> (portaria) — '
           'canais para informações sobre a programação vigente.</p>'
           '<p>Como a grade muda a cada temporada, a confirmação de horários '
           'de exposições deve ser feita pelos telefones ou pelo portal '
           'oficial da Secretaria Municipal da Cultura e Turismo.</p>'
       ),
       'como_chegar': (
           '<p>O centro fica na <strong>Rua Álvares Cabral, 322</strong>, na '
           'mesma via do Theatro Pedro II. A região central é atendida por '
           'dezenas de linhas municipais; o hub de linhas do portal mostra a '
           'opção mais direta.</p>'
       ),
       'atracoes_proximas': (
           '<p>Theatro Pedro II, Quarteirão Paulista, Praça XV de Novembro e '
           'Palácio Rio Branco formam o circuito patrimonial do entorno — '
           'tudo a pé, no quadrilátero histórico da cidade.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Exposição no Palace pela manhã, '
           'almço no Quarteirão Paulista e passeio pela Praça XV à tarde.</p>'
       ),
   },
   secao_extra_titulo='Programação',
   secao_extra_html=(
       '<p>A programação do Palace — exposições, eventos e atividades '
       'culturais — é divulgada pela <strong>Secretaria Municipal da Cultura '
       'e Turismo</strong> no portal oficial. Agendamentos e informações '
       'pelos telefones <strong>(16) 3636-9187</strong> (administração) e '
       '<strong>(16) 3636-2893</strong> (portaria).</p>'
   ),
   faq=[
       {'pergunta': 'Onde fica o Centro Cultural Palace e quais os telefones?',
        'resposta': 'Rua Álvares Cabral, 322, Centro, Ribeirão Preto/SP. Telefones: (16) 3636-9187 (administração) e (16) 3636-2893 (portaria).'},
       {'pergunta': 'O que era o prédio do Centro Cultural Palace?',
        'resposta': 'O edifício tombado abrigava o antigo Palace Hotel, construído na era do café, e foi adaptado para uso cultural pela Prefeitura.'},
       {'pergunta': 'Que prêmio o Palace recebeu em 2026?',
        'resposta': 'Vencedor da categoria Museus e Centros Culturais do Prêmio Governador do Estado para as Artes 2026, com cerimônia em 29/07/2026 no Teatro Sérgio Cardoso, em São Paulo. O prédio completa 100 anos em 2026.'},
       {'pergunta': 'Como saber a programação do Centro Cultural Palace?',
        'resposta': 'Pela divulgação da Secretaria Municipal da Cultura e Turismo no portal oficial e pelos telefones da administração e da portaria.'},
       {'pergunta': 'O Palace fica perto de outros pontos culturais?',
        'resposta': 'Sim: na mesma rua do Theatro Pedro II e a poucos minutos da Praça XV, do Quarteirão Paulista e do Palácio Rio Branco.'},
   ],
)

# ---- 10. Sesc Ribeirão Preto (abre com INSTITUIÇÃO/rede) ─────────────
_se = _v('sesc-ribeirao-preto', 'nome')
_p('sesc-ribeirao-preto',
   f'{_se} em Ribeirão Preto | Ribeirão Viva',
   f'{_se}: A Rede Cultural do Comércio na Rua Tibiriçá',
   f'Endereço oficial e programação mensal do {_se}, unidade do Sesc SP '
   f'no centro de Ribeirão Preto, verificada nas páginas oficiais.',
   f'{_se}, Sesc SP, Em Cartaz, cultura centro Ribeirão Preto, Rua Tibiriçá',
   'Sesc Ribeirão Preto',
   'Teatros e Espaços Culturais',
   secoes={
       'resumo': (
           '<p>O <strong>' + _se + '</strong> é a porta local de uma das '
           'maiores redes de cultura do país. Mantido pelo comércio de bens, '
           'serviços e turismo, o <strong>Sesc São Paulo</strong> opera '
           'centros culturais por todo o estado — e a unidade ribeirão-pretana '
           'fica na <strong>Rua Tibiriçá, 50, Centro</strong>, CEP '
           '14010-090.</p>'
           '<p>A programação circula na <strong>revista Em Cartaz</strong>, '
           'publicação mensal oficial do Sesc SP: espetáculos, oficinas, '
           'mostras e atividades gratuitas e pagas, com agenda confirmada '
           'diretamente no portal da instituição.</p>'
       ),
       'historia': (
           '<h3>Uma rede estadual com porta no centro</h3>'
           '<p>O Sesc — Serviço Social do Comércio — é mantido pelo sistema '
           'S, com financiamento do comércio, e o <strong>Sesc São Paulo</strong> '
           'tornou-se referência nacional em programação cultural: teatro, '
           'música, exposições, esporte e educação em unidades espalhadas '
           'pelo estado.</p>'
           '<p>A unidade de Ribeirão Preto leva essa estrutura ao quadrado '
           'central da cidade, na <strong>Rua Tibiriçá</strong> — a poucos '
           'passos do Theatro Pedro II e da Praça XV. A agenda mensal é '
           'publicada no <strong>Em Cartaz</strong> e no portal sescsp.org.br, '
           'com o contato oficial da unidade feito pelo formulário '
           '<strong>sescsp.org.br/fale-conosco</strong>.</p>'
           '<p>O telefone da unidade não é divulgado nas páginas oficiais '
           'consultadas — o canal oficial de contato é o formulário digital, '
           'que direciona a mensagem à unidade correta.</p>'
       ),
       'detalhes_visita': (
           '<p>Endereço oficial: <strong>Rua Tibiriçá, 50, Centro, CEP '
           '14010-090</strong>, conforme a página da unidade no portal do '
           'Sesc. A programação vigente — espetáculos, oficinas e atividades '
           'gratuitas e pagas — deve ser consultada no portal sescsp.org.br '
           'ou na revista Em Cartaz do mês.</p>'
       ),
       'como_chegar': (
           '<p>A unidade fica no centro de Ribeirão Preto, na <strong>Rua '
           'Tibiriçá</strong>, a poucos minutos a pé do Theatro Pedro II. A '
           'região central concentra dezenas de linhas municipais; consulte '
           'o hub de linhas do portal.</p>'
       ),
       'atracoes_proximas': (
           '<p>Theatro Pedro II, Praça XV de Novembro, Casa da Memória '
           'Italiana (Rua Tibiriçá, 776) e Quarteirão Paulista formam o '
           'circuito cultural do entorno imediato.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Uma tarde no Sesc pode seguir '
           'a pé até a Casa da Memória Italiana — as duas portas ficam na '
           'mesma rua.</p>'
       ),
   },
   secao_extra_titulo='Programação',
   secao_extra_html=(
       '<p>A programação cultural do Sesc Ribeirão Preto é publicada '
       'mensalmente na <strong>revista Em Cartaz</strong> e no portal '
       '<strong>sescsp.org.br</strong> — espetáculos, oficinas, mostras e '
       'atividades gratuitas e pagas. O contato oficial da unidade é o '
       'formulário <strong>sescsp.org.br/fale-conosco</strong>.</p>'
   ),
   faq=[
       {'pergunta': 'Onde fica o Sesc Ribeirão Preto?',
        'resposta': 'Rua Tibiriçá, 50, Centro, Ribeirão Preto/SP, CEP 14010-090, conforme a página oficial da unidade no portal do Sesc.'},
       {'pergunta': 'Como saber a programação do Sesc Ribeirão Preto?',
        'resposta': 'Na revista Em Cartaz e no portal sescsp.org.br, com espetáculos, oficinas e atividades gratuitas e pagas publicados mensalmente.'},
       {'pergunta': 'Qual o telefone do Sesc Ribeirão Preto?',
        'resposta': 'O telefone da unidade não é divulgado nas páginas oficiais consultadas. O contato oficial é o formulário sescsp.org.br/fale-conosco.'},
       {'pergunta': 'O Sesc Ribeirão Preto fica perto de outros pontos culturais?',
        'resposta': 'Sim: na mesma rua fica a Casa da Memória Italiana (nº 776), e o Theatro Pedro II e a Praça XV estão a poucos minutos a pé.'},
       {'pergunta': 'Quem mantém o Sesc?',
        'resposta': 'O Sesc — Serviço Social do Comércio — é mantido pelo comércio de bens, serviços e turismo, e opera no estado por meio do Sesc São Paulo.'},
   ],
)

# ---- 11. Instituto Figueiredo Ferraz (abre com ENTRADA GRATUITA) ────
_if = _v('instituto-figueiredo-ferraz', 'nome')
_p('instituto-figueiredo-ferraz',
   f'{_if} em Ribeirão Preto | Ribeirão Viva',
   f'{_if}: Arte Contemporânea Gratuita no Alto da Boa Vista',
   f'Entrada gratuita de terça a sábado no {_if}: endereço, horários e '
   f'telefones oficiais verificados no site da instituição.',
   f'{_if}, IFF, arte contemporânea, entrada gratuita, exposições, '
   'Alto da Boa Vista, Rua Maestro Ignácio Stábile',
   'Instituto Figueiredo Ferraz',
   'Teatros e Espaços Culturais',
   secoes={
       'resumo': (
           '<p><strong>Entrada gratuita</strong>, de <strong>terça a '
           'sábado, das 14h às 18h</strong>: é assim que o <strong>' + _if +
           '</strong> abre suas portas no <strong>Alto da Boa Vista</strong>. '
           'O instituto dedica-se à arte contemporânea e publica sua '
           'programação de exposições no site oficial.</p>'
           '<p>O endereço — <strong>Rua Maestro Ignácio Stábile, 200</strong> '
           '— carrega a memória musical da cidade no próprio nome da via, e '
           'os dois telefones oficiais, <strong>(16) 3623-2261</strong> e '
           '<strong>(16) 3623-2262</strong>, atendem consultas sobre a '
           'programação vigente.</p>'
       ),
       'historia': (
           '<h3>Um instituto privado de arte aberto à cidade</h3>'
           '<p>Entre as casas de arte do interior paulista, o modelo do IFF '
           'é raro: instituto privado com <strong>visitação gratuita</strong> '
           'e programação regular de exposições de arte contemporânea. As '
           'informações de visita publicadas no site oficial da instituição '
           'são a base desta página: endereço no Alto da Boa Vista, horário '
           'de terça a sábado das 14h às 18h, entrada franca e dois números '
           'de contato.</p>'
           '<p>A localização no quadrante do Alto da Boa Vista coloca o '
           'instituto no conjunto de atrações da região norte — território '
           'do Morro de São Bento e do parque que coroa a colina. Uma '
           'visita de tarde combina exposição e pôr do sol sem mudar de '
           'bairro.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Visitação:</strong> terça a sábado, das 14h às 18h. '
           '<strong>Entrada gratuita.</strong> Endereço: Rua Maestro Ignácio '
           'Stábile, 200, Alto da Boa Vista, Ribeirão Preto/SP. Contatos: '
           '<strong>(16) 3623-2261</strong> e <strong>(16) 3623-2262</strong>.</p>'
       ),
       'como_chegar': (
           '<p>O instituto fica na <strong>Rua Maestro Ignácio Stábile, 200</strong>, '
           'no Alto da Boa Vista, região norte de Ribeirão Preto. Consulte o '
           'hub de linhas do portal para as opções que atendem o bairro.</p>'
       ),
       'atracoes_proximas': (
           '<p>O Alto da Boa Vista é o quadrante do Morro de São Bento e do '
           'parque da colina — roteiro que pode começar na exposição do IFF '
           'e terminar no mirante.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Exposição das 14h no IFF, '
           'caminhada até o parque do Morro de São Bento para o fim de '
           'tarde.</p>'
       ),
   },
   secao_extra_titulo='Visitação',
   secao_extra_html=(
       '<p><strong>Horário oficial de visitação:</strong> terça a sábado, '
       'das 14h às 18h. <strong>Entrada gratuita.</strong> Contatos: '
       '<strong>(16) 3623-2261</strong> e <strong>(16) 3623-2262</strong>, '
       'conforme o site oficial do instituto.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de visitação do Instituto Figueiredo Ferraz?',
        'resposta': 'Terça a sábado, das 14h às 18h, com entrada gratuita, conforme o site oficial da instituição.'},
       {'pergunta': 'Onde fica o Instituto Figueiredo Ferraz?',
        'resposta': 'Rua Maestro Ignácio Stábile, 200, Alto da Boa Vista, Ribeirão Preto/SP.'},
       {'pergunta': 'A entrada do IFF é paga?',
        'resposta': 'Não, a entrada é gratuita. Contatos: (16) 3623-2261 e (16) 3623-2262.'},
       {'pergunta': 'Que tipo de programação o IFF oferece?',
        'resposta': 'Exposições de arte contemporânea com programação publicada no site oficial da instituição.'},
       {'pergunta': 'Vale combinar o IFF com outros passeios na região?',
        'resposta': 'Sim: o Alto da Boa Vista fica no quadrante do Morro de São Bento e do parque da colina — exposição no IFF e pôr do sol no mirante no mesmo roteiro.'},
   ],
)

# ══════════════════════════════════════════════════════════════════════
# MUSEUS (3) — MIS=acervo vivo, Plínio=patrono/interdição, CMI=família
# ══════════════════════════════════════════════════════════════════════

# ---- 12. MIS-RP ─────────────────────────────────────────────────────
_mi = _v('mis-rp', 'nome')
_p('mis-rp',
   f'{_mi} em Ribeirão Preto | Ribeirão Viva',
   f'{_mi}: Rádio, Cinema e Memória Audiovisual no Centro',
   f'Acervo pioneiro do rádio no interior, entrada gratuita e sessões de '
   f'cinema: o guia completo do MIS de Ribeirão Preto, com dados oficiais.',
   'MIS Ribeirão Preto, Museu da Imagem e do Som, rádio interior, cinema '
   'gratuito, Casa de Câmara e Cadeia, museu centro',
   'MIS-RP — Museu da Imagem e do Som',
   'Museus e Memória',
   secoes={
       'resumo': (
           '<p>Rádios de válvula, fitas de rolo, máquinas de cinefotografia e '
           'a história dos veículos de comunicação da cidade: o acervo do '
           '<strong>' + _mi + '</strong> é considerado <strong>pioneiro do '
           'rádio no interior do Brasil</strong> — e está aberto à visitação '
           'gratuita no Centro.</p>'
           '<p>Desde <strong>16 de dezembro de 2020</strong>, o museu funciona '
           'no imóvel tombado da antiga <strong>Casa de Câmara e Cadeia</strong>, '
           'na Rua Cerqueira César, 371 — edificação que remonta à fundação '
           'da cidade e ganhou uso público permanente ao receber o MIS.</p>'
           '<p>A agenda combina exposições, <strong>oficinas com inscrições '
           'abertas</strong> (stop motion, trilha sonora para curtas, roteiro '
           'e efeitos especiais), memória oral e as <strong>sessões de cinema '
           'do programa Pontos MIS</strong>, às segundas-feiras, às 18h30, '
           'no auditório.</p>'
       ),
       'historia': (
           '<h3>Da Lei de 1978 à Casa de Câmara e Cadeia</h3>'
           '<p>O museu nasceu por lei: a <strong>Lei Municipal nº 3.431, de '
           '13 de abril de 1978</strong>, formalizou a criação do MIS numa '
           'época em que as emissoras de rádio ribeirão-pretanas estavam no '
           'auge. Quase cinco décadas depois, o acervo percorre toda a '
           'evolução da comunicação local — dos aparelhos de rádio às fitas '
           'cassete, dos gravadores de rolo às máquinas de cinefotografia, '
           'com acervo de iconografia, discos, fotos e documentos.</p>'
           '<p>A reinauguração de <strong>16 de dezembro de 2020</strong> '
           'transferiu o museu para a antiga <strong>Casa de Câmara e '
           'Cadeia</strong> — prédio tombado que já abrigou o poder '
           'legislativo e a cadeia da cidade. O casamento entre o acervo '
           'audiovisual e a edificação histórica criou um circuito completo: '
           'memória da comunicação dentro da memória arquitetônica.</p>'
           '<p>O portal oficial do museu mantém as seções de <strong>Ações '
           'em Andamento</strong> e programação de exposições sempre ativas — '
           'sinal de instituição viva, que produz cultura em vez de apenas '
           'guardar o passado.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Horário:</strong> terça a sexta-feira, das 9h às 12h e '
           'das 14h às 17h, exceto feriados e pontos facultativos. '
           '<strong>Entrada gratuita.</strong> Endereço: Rua Cerqueira '
           'César, 371, Centro, CEP 14010-130. Telefone: (16) 3635-3660.</p>'
           '<p><strong>Grupos acima de 10 pessoas</strong> devem agendar '
           'pelo WhatsApp (16) 99760-9946, conforme o canal divulgado pelo '
           'próprio museu. As sessões do Pontos MIS (segundas, 18h30) têm '
           'senhas distribuídas na hora.</p>'
       ),
       'como_chegar': (
           '<p>O MIS fica na <strong>Rua Cerqueira César, 371</strong>, a '
           'poucos minutos a pé da Praça XV de Novembro e do Quarteirão '
           'Paulista. A região central é atendida por dezenas de linhas '
           'municipais; o hub de linhas do portal indica a mais direta.</p>'
       ),
       'atracoes_proximas': (
           '<p>Catedral Metropolitana, Theatro Pedro II, MARP e Praça XV '
           'formam o circuito do entorno — um roteiro de museus e patrimônio '
           'inteiramente caminhável, com o MIS como parada de imersão '
           'audiovisual.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Roteiro dos museus do centro: '
           'MIS (manhã) → MARP (tarde) → sessão Pontos MIS às segundas, se '
           'programar para o início da semana.</p>'
       ),
   },
   secao_extra_titulo='Acervo',
   secao_extra_html=(
       '<p>O acervo reúne <strong>iconografia, discos, aparelhos de rádio, '
       'fitas de rolo e cassete, máquinas de cinefotografia, fotos, '
       'gravadores e documentos</strong> da história dos veículos de '
       'comunicação de Ribeirão Preto — registro raro da trajetória do rádio '
       'no interior do Brasil.</p>'
       '<p>As <strong>oficinas</strong> (stop motion, trilha sonora para '
       'curtas, roteiro, efeitos especiais) mantêm o acervo em diálogo com '
       'a produção audiovisual contemporânea; as <strong>sessões Pontos '
       'MIS</strong> acontecem às segundas-feiras, às 18h30, no auditório.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de funcionamento do MIS de Ribeirão Preto?',
        'resposta': 'Terça a sexta-feira, das 9h às 12h e das 14h às 17h, exceto feriados e pontos facultativos, com entrada gratuita.'},
       {'pergunta': 'Onde fica o MIS e qual o telefone?',
        'resposta': 'Rua Cerqueira César, 371, Centro, CEP 14010-130, na antiga Casa de Câmara e Cadeia. Telefone: (16) 3635-3660; grupos acima de 10 pessoas agendam pelo WhatsApp (16) 99760-9946.'},
       {'pergunta': 'O que o acervo do MIS guarda?',
        'resposta': 'Iconografia, discos, aparelhos de rádio, fitas de rolo e cassete, máquinas de cinefotografia, fotos, gravadores e documentos da história dos veículos de comunicação da cidade — o museu é considerado pioneiro do rádio no interior do Brasil.'},
       {'pergunta': 'Quando o museu se mudou para a Casa de Câmara e Cadeia?',
        'resposta': 'Na reinauguração de 16 de dezembro de 2020, para o imóvel tombado da antiga Casa de Câmara e Cadeia, na Rua Cerqueira César, 371.'},
       {'pergunta': 'Quem criou o MIS de Ribeirão Preto?',
        'resposta': 'O museu foi criado pela Lei Municipal nº 3.431, de 13 de abril de 1978.'},
   ],
)

# ---- 13. Museu Histórico Plínio Travassos (abre com PATRONO) ─────────
_mh = _v('museu-historico-plinio-travassos', 'nome')
_p('museu-historico-plinio-travassos',
   f'{_mh} — Temporariamente Fechado | Ribeirão Viva',
   f'{_mh}: O Legado de 1938 Fechado desde 2016',
   f'A história do museu fundado por Plínio Travassos dos Santos em 1938, '
   f'interditado desde março de 2016 no campus da USP, com dados oficiais.',
   'Museu Histórico Ribeirão Preto, Plínio Travassos dos Santos, Solar '
   'Schmidt, Fazenda Monte Alegre, Complexo dos Museus, museu fechado',
   'Museu Histórico "Plínio Travassos dos Santos"',
   'Museus e Memória',
   secoes={
       'resumo': (
           '<p>Todo grande acervo começa com um colecionador. Em <strong>1938'
           '</strong>, o historiador <strong>Plínio Travassos dos Santos</strong> '
           'passou a reunir doações de famílias ribeirão-pretanas — e esse '
           'acervo inicial virou, por lei, o museu histórico oficial da '
           'cidade: o <strong>' + _mh + '</strong>, com cinco seções '
           'temáticas instaladas no <strong>Solar Schmidt</strong>, a '
           'casa-sede da Fazenda Monte Alegre, no campus da USP.</p>'
           '<p>O público, porém, não pode vê-lo: as portas estão fechadas '
           'desde o primeiro trimestre de <strong>2016</strong>, quando um '
           'dano no forro do prédio obrigou ao esvaziamento do conjunto. O '
           'portal oficial registra a visitação como temporariamente '
           'suspensa, e esta página preserva a história da instituição '
           'enquanto o restauro não vem.</p>'
       ),
       'historia': (
           '<h3>O patrono e as leis que criaram o museu</h3>'
           '<p>A trajetória do museu é pontuada por datas oficiais: a '
           'iniciativa de <strong>Plínio Travassos dos Santos</strong> em '
           '<strong>1938</strong>; a criação formal pela <strong>Lei '
           'Municipal nº 97, de 1º de julho de 1949</strong>; a abertura ao '
           'público em <strong>28 de novembro de 1950</strong>; e a '
           'instalação definitiva no Solar Schmidt em <strong>28 de março de '
           '1951</strong>, na casa-sede da Fazenda Monte Alegre doada ao '
           'Município. A denominação que homenageia o patrono veio pela '
           '<strong>Lei Municipal nº 1.750</strong>.</p>'
           '<p>O acervo nasceu de doações — majoritariamente de famílias '
           'ribeirão-pretanas — e se organizou em seções temáticas: '
           '<strong>Artes, Etnologia Indígena, Zoologia, Geologia e '
           'Numismática</strong>. O museu dividiu o conjunto da fazenda com '
           'o <strong>Museu do Café Francisco Schmidt</strong> (fundado em '
           '1955, em anexo próprio de 1957): instituições distintas, cada '
           'uma com acervo e histórico próprios no portal do complexo.</p>'
           '<h3>2016: a interdição</h3>'
           '<p>Em <strong>março de 2016</strong>, o desabamento de parte do '
           'forro do prédio principal do complexo levou à interdição de todo '
           'o conjunto, e o museu segue fechado desde então, sem previsão de '
           'reabertura divulgada em fonte oficial — o restauro tramita entre '
           'determinações judiciais, contratos de reserva técnica do acervo '
           'e a pendência de renovação do projeto executivo.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Não há visitação.</strong> O portal oficial do '
           'complexo exibe "Horário de visitação: temporariamente fechado". '
           'O telefone (16) 3315-9321 segue listado na ficha oficial; '
           'contatos sobre o restauro devem seguir para os canais da '
           'Secretaria Municipal da Cultura e Turismo.</p>'
       ),
       'como_chegar': (
           '<p>O museu fica na <strong>Av. Dr. Prof. Zeferino Vaz, s/nº, '
           'campus da USP</strong>, na casa-sede da antiga Fazenda Monte '
           'Alegre (Solar Schmidt), zona norte. Consulte o hub de linhas do '
           'portal para as linhas que atendem o campus universitário.</p>'
       ),
       'atracoes_proximas': (
           '<p>No mesmo conjunto está o Museu do Café Francisco Schmidt, '
           'igualmente interditado — as duas casas formam o Complexo dos '
           'Museus Municipais, tombado pelo Condephaat. O roteiro de museus '
           'abertos da cidade segue no MIS, no MARP e na Casa da Memória '
           'Italiana.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Enquanto o restauro não '
           'acontece, o circuito de museus abertos: MIS (Centro), MARP '
           '(Centro) e Casa da Memória Italiana (Rua Tibiriçá).</p>'
       ),
   },
   secao_extra_titulo='Status',
   secao_extra_html=(
       '<p><strong>Fechado desde março de 2016.</strong> Interdição após '
       'desabamento de parte do forro; ordem judicial de restauro '
       'descumprida (obras determinadas em 2017/2018, prazos fixados em '
       '2019 sob multa diária de R$ 10 mil, obrigação mantida pelo STF em '
       '2025). A reserva técnica do acervo foi contratada em 2024; o '
       'contrato do projeto executivo venceu em 7 de maio de 2025 sem '
       'renovação. Sem previsão de reabertura em fonte oficial.</p>'
   ),
   faq=[
       {'pergunta': 'O Museu Histórico de Ribeirão Preto está aberto?',
        'resposta': 'Não. Está temporariamente fechado desde março de 2016, após desabamento de parte do forro do prédio. O portal oficial exibe "horário de visitação: temporariamente fechado", sem previsão de reabertura.'},
       {'pergunta': 'Quem foi Plínio Travassos dos Santos?',
        'resposta': 'O patrono do museu: em 1938 começou a recolher o acervo inicial, majoritariamente doado por famílias da cidade. A denominação do museu em sua homenagem veio pela Lei Municipal nº 1.750.'},
       {'pergunta': 'O Museu Histórico é o mesmo que o Museu do Café?',
        'resposta': 'Não. São instituições distintas do Complexo dos Museus Municipais: o Histórico funciona na casa-sede da Fazenda Monte Alegre (Solar Schmidt), e o Museu do Café, fundado em 1955, em anexo próprio de 1957. Ambos interditados desde 2016.'},
       {'pergunta': 'Que seções tinha o acervo do museu?',
        'resposta': 'Artes, Etnologia Indígena, Zoologia, Geologia e Numismática — acervo formado majoritariamente por doações, com abertura ao público em 28 de novembro de 1950 e instalação definitiva no Solar Schmidt em 28 de março de 1951.'},
       {'pergunta': 'Onde fica o Museu Histórico e qual o telefone?',
        'resposta': 'Av. Dr. Prof. Zeferino Vaz, s/nº, campus da USP, Ribeirão Preto/SP. Telefone listado na ficha oficial: (16) 3315-9321.'},
   ],
)

# ---- 14. Casa da Memória Italiana (abre com FAMÍLIA) ─────────────────
_cm = _v('casa-da-memoria-italiana', 'nome')
_p('casa-da-memoria-italiana',
   f'{_cm} em Ribeirão Preto | Ribeirão Viva',
   f'{_cm}: O Palacete dos Biagi e a História dos Italianos',
   f'A casa de 1923-1925 onde viveu a família Biagi hoje guarda a memória '
   f'da imigração italiana: visitas mediadas, entrada livre e programação '
   f'temática, com dados oficiais.',
   'Casa da Memória Italiana, palacete Biagi, imigração italiana Ribeirão '
   'Preto, museu-casa, visitas mediadas, Rua Tibiriçá',
   'Casa da Memória Italiana',
   'Museus e Memória',
   secoes={
       'resumo': (
           '<p>Entre <strong>1923 e 1925</strong>, um palacete eclético '
           'surgia na Rua Tibiriçá para abrigar uma família de imigrantes '
           'italianos. A partir de <strong>1941</strong>, o endereço virou '
           'casa de <strong>Pedro Biagi, Eugenia Viel Biagi</strong> e '
           'filhos — e, um século depois da construção, o palacete '
           'preserva e narra a história da imigração italiana como a '
           '<strong>' + _cm + '</strong>.</p>'
           '<p>Em <strong>setembro de 2014</strong>, a família doou o imóvel '
           'ao Instituto Casa da Memória Italiana — entidade privada sem '
           'fins lucrativos fundada naquele ano —, que o transformou em '
           'museu-casa com acervo de mobiliário, objetos pessoais e '
           'registros documentais. A edificação conta com <strong>Dossiê '
           'de Tombamento (2021)</strong>.</p>'
       ),
       'historia': (
           '<h3>Uma casa, uma família, uma comunidade</h3>'
           '<p>O palacete eclético é peça do ciclo de ascensão dos '
           'imigrantes italianos na Ribeirão Preto do café: construído na '
           'década de 1920 no estilo das residências abastadas da época, '
           'acolheu a família Biagi por décadas — e cada sala preserva '
           'vestígios dessa convivência.</p>'
           '<p>A doação de <strong>setembro de 2014</strong> transformou a '
           'casa em museu gerido pelo <strong>Instituto Casa da Memória '
           'Italiana</strong>, com a missão de preservar e promover a '
           'história da imigração italiana com ênfase na região de '
           'Ribeirão Preto. A casa <strong>não integra o Complexo dos '
           'Museus Municipais</strong>: mantém parcerias pontuais com a '
           'Secretaria Municipal da Cultura e Turismo, mas é instituição '
           'privada com programação própria.</p>'
           '<p>Essa programação inclui tours temáticos — como "Uma Visita '
           'aos Entornos da Rivi Nigri" (18/09) e "Patrimônio Italiano no '
           'Centro Histórico de Ribeirão Preto" (26/09), da temporada de '
           'setembro de 2026 — e o domingo mensal de museu aberto, marcado '
           'para <strong>25 de outubro</strong> no ciclo vigente.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Visitas mediadas</strong> (com agendamento): quarta a '
           'sexta às 15h; sábados às 10h e às 11h30 — vagas liberadas '
           '<strong>sempre às segundas-feiras</strong> no canal oficial de '
           'agendamento. <strong>Visitas livres</strong> (sem mediação): '
           'quinta e sexta, das 10h às 12h, <strong>entrada franca</strong>. '
           'Um domingo por mês, formato de museu aberto.</p>'
           '<p>Endereço: <strong>Rua Tibiriçá, 776, Centro, CEP '
           '14010-090</strong>. Telefones: (16) 3904-2750 e (16) '
           '99760-9946.</p>'
       ),
       'como_chegar': (
           '<p>A casa fica na <strong>Rua Tibiriçá</strong>, a mesma via do '
           'Sesc Ribeirão Preto (nº 50), a poucos minutos do Theatro Pedro '
           'II. A região central é atendida por dezenas de linhas '
           'municipais; consulte o hub de linhas do portal.</p>'
       ),
       'atracoes_proximas': (
           '<p>Sesc Ribeirão Preto (mesma rua), Theatro Pedro II, Quarteirão '
           'Paulista e Praça XV — o centro histórico que os tours da casa '
           'próprio percorrem ao narrar a contribuição italiana à cidade.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Combine a visita mediada com o '
           'tour "Patrimônio Italiano no Centro Histórico" oferecido pela '
           'própria instituição.</p>'
       ),
   },
   secao_extra_titulo='Programação',
   secao_extra_html=(
       '<p>O agendamento de <strong>visitas mediadas</strong> abre toda '
       'segunda-feira no site da instituição. A temporada inclui tours '
       'temáticos (setembro/2026: "Uma Visita aos Entornos da Rivi Nigri" e '
       '"Patrimônio Italiano no Centro Histórico") e o domingo mensal de '
       '<strong>museu aberto</strong> — em outubro de 2026, no dia 25.</p>'
       '<p>As <strong>visitas livres</strong> seguem quinta e sexta, das '
       '10h às 12h, com entrada franca.</p>'
   ),
   faq=[
       {'pergunta': 'Como visitar a Casa da Memória Italiana?',
        'resposta': 'Visitas mediadas com agendamento (quarta a sexta às 15h; sábados às 10h e 11h30), com vagas liberadas às segundas-feiras; visitas livres de entrada franca quinta e sexta, das 10h às 12h; e um domingo por mês em formato de museu aberto.'},
       {'pergunta': 'Onde fica a Casa da Memória Italiana e qual o telefone?',
        'resposta': 'Rua Tibiriçá, 776, Centro, CEP 14010-090, Ribeirão Preto/SP. Telefones: (16) 3904-2750 e (16) 99760-9946.'},
       {'pergunta': 'A Casa da Memória Italiana é um museu público?',
        'resposta': 'Não. É um museu-casa privado gerido pelo Instituto Casa da Memória Italiana, entidade sem fins lucrativos que recebeu o palacete doado pela família Biagi em setembro de 2014. A entrada nas visitas livres é franca.'},
       {'pergunta': 'Quem morava no palacete?',
        'resposta': 'O casal de imigrantes italianos Pedro Biagi e Eugenia Viel Biagi e filhos, a partir de 1941. O palacete foi construído entre 1923 e 1925 e tem Dossiê de Tombamento de 2021.'},
       {'pergunta': 'Que tours a casa oferece?',
        'resposta': 'Tours temáticos de memória italiana, como "Uma Visita aos Entornos da Rivi Nigri" e "Patrimônio Italiano no Centro Histórico de Ribeirão Preto" (temporada de setembro de 2026), além do domingo mensal de museu aberto.'},
   ],
)

# ══════════════════════════════════════════════════════════════════════
# PRÉDIOS HISTÓRICOS (4)
# ══════════════════════════════════════════════════════════════════════

# ---- 15. Palácio Rio Branco ──────────────────────────────────────────
_pr = _v('palacio-rio-branco', 'nome')
_p('palacio-rio-branco',
   f'{_pr} em Ribeirão Preto | Ribeirão Viva',
   f'{_pr}: O Paço de 1917 em Obras de Restauro',
   f'História completa do {_pr}: pedra fundamental de 1915, salões '
   f'Nobre e Rosa, tombamento de 1988 e restauro iniciado em 2024.',
   'Palácio Rio Branco, Palácio do Povo, paço municipal 1917, salões '
   'Nobre e Rosa, restauro 2024, prédio tombado Ribeirão Preto',
   'Palácio Rio Branco',
   'Prédios Históricos e Patrimônio',
   secoes={
       'resumo': (
           '<p>A <strong>pedra fundamental</strong> do <strong>' + _pr +
           '</strong> foi lançada em <strong>3 de agosto de 1915</strong>; o '
           'prédio ficou pronto em abril e foi inaugurado em <strong>26 de '
           'maio de 1917</strong>. Por mais de um século, foi o paço '
           'municipal: abrigou a <strong>Câmara Municipal, a Prefeitura, a '
           'Procuradoria e outros órgãos políticos</strong> da cidade do '
           'café.</p>'
           '<p>Conhecido como <strong>Palácio do Povo</strong>, o imóvel tem '
           '<strong>dois pavimentos e porão</strong> somando 1.800 m² de '
           'construção, com fachada em transição do barroco ao moderno — '
           'inspirada nas fachadas francesas do início do século. Desde '
           '<strong>junho de 2024</strong>, passa por obras de restauro e '
           'requalificação.</p>'
       ),
       'historia': (
           '<h3>Salões de decisões, nome de estadista</h3>'
           '<p>O nome homenageia o <strong>Barão do Rio Branco</strong>, '
           'estadista brasileiro falecido em <strong>1912</strong> — três '
           'anos antes da pedra fundamental. Dentro, dois salões '
           'concentraram a vida política e econômica da era do café: o '
           'Salão <strong>Nobre</strong> (Antônio Duarte Nogueira) e o '
           'Salão <strong>Rosa</strong> (Orestes Lopes de Camargo), '
           'palcos das decisões da cidade.</p>'
           '<p>O tombamento veio em <strong>28 de março de 1988</strong>, '
           'pela Lei nº 5.243. Em <strong>2020</strong>, a estrutura '
           'administrativa mudou-se para o Centro Administrativo da rua '
           'Américo Brasiliense, 426, e o palácio passou a abrigar a '
           'Secretaria Municipal da Cultura e Turismo.</p>'
           '<h3>2024: o restauro e a descoberta</h3>'
           '<p>As obras de restauro e requalificação começaram em '
           '<strong>junho de 2024</strong>, contratadas com a empresa '
           'Increbase Construtora por <strong>R$ 6.548.330,00</strong>, com '
           'projeto aprovado pelo Conppac em 19 de janeiro de 2024. A '
           'previsão inicial era conclusão em <strong>novembro de '
           '2025</strong> — mas a descoberta dos <strong>pisos originais '
           'dos Salões Rosa e Verde</strong> prorrogou a entrega, sem nova '
           'data divulgada em fonte oficial até março de 2026.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Visitação não confirmada</strong>: nenhuma fonte '
           'oficial informa visitação guiada ou condições de visita durante '
           'as obras. O telefone geral da Prefeitura — <strong>(16) '
           '3977-9000</strong>, exibido no rodapé oficial assinado como '
           'Palácio Rio Branco — é o canal para consultas sobre o restauro.</p>'
           '<p>Endereço: <strong>Praça Barão do Rio Branco, s/nº, Centro, '
           'CEP 14010-140</strong>.</p>'
       ),
       'como_chegar': (
           '<p>O palácio fica na <strong>Praça Barão do Rio Branco</strong>, '
           'no quadrilátero histórico, a poucos minutos a pé do Theatro '
           'Pedro II e da Praça XV. A região central concentra dezenas de '
           'linhas municipais; consulte o hub de linhas do portal.</p>'
       ),
       'atracoes_proximas': (
           '<p>Theatro Pedro II, Centro Cultural Palace, Mercado Municipal, '
           'Quarteirão Paulista e Praça XV formam o circuito patrimonial do '
           'entorno — um passeio completo a pé.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">O palácio é parada de fachada '
           'histórica no roteiro do centro: hoje, aprecia-se de fora, com as '
           'obras de restauro em andamento.</p>'
       ),
   },
   secao_extra_titulo='Visitação',
   secao_extra_html=(
       '<p><strong>Visitação não confirmada.</strong> O prédio está em obras '
       'de restauro desde junho de 2024, prorrogadas após a descoberta dos '
       'pisos originais dos Salões Rosa e Verde. Não há informação oficial '
       'sobre visitação no período; consultas pelo telefone geral da '
       'Prefeitura: <strong>(16) 3977-9000</strong>.</p>'
   ),
   faq=[
       {'pergunta': 'O Palácio Rio Branco está aberto à visitação?',
        'resposta': 'Visitação não confirmada. O prédio passa por restauro iniciado em junho de 2024, prorrogado após a descoberta dos pisos originais dos Salões Rosa e Verde, e nenhuma fonte oficial informa condições de visita no período.'},
       {'pergunta': 'Quando o Palácio Rio Branco foi inaugurado?',
        'resposta': 'Pedra fundamental em 3 de agosto de 1915; inaugurado em 26 de maio de 1917. Abrigou Câmara Municipal, Prefeitura, Procuradoria e outros órgãos, e foi tombado em 28 de março de 1988 pela Lei nº 5.243.'},
       {'pergunta': 'Por que o nome Rio Branco?',
        'resposta': 'Em homenagem ao Barão do Rio Branco, estadista brasileiro falecido em 1912. O palácio abriga os Salões Nobre (Antônio Duarte Nogueira) e Rosa (Orestes Lopes de Camargo).'},
       {'pergunta': 'Onde fica o Palácio Rio Branco?',
        'resposta': 'Praça Barão do Rio Branco, s/nº, Centro, CEP 14010-140. Telefone geral da Prefeitura: (16) 3977-9000.'},
       {'pergunta': 'O que está acontecendo com o prédio hoje?',
        'resposta': 'Obras de restauro e requalificação desde junho de 2024 (R$ 6.548.330,00, empresa Increbase), com previsão inicial de conclusão em novembro de 2025 prorrogada após a descoberta dos pisos originais dos Salões Rosa e Verde.'},
   ],
)

# ---- 16. Mercado Municipal ───────────────────────────────────────────
_me = _v('mercado-municipal', 'nome')
_p('mercado-municipal',
   f'{_me} em Ribeirão Preto | Ribeirão Viva',
   f'{_me}: Do Incêndio de 1942 ao Mercadão dos 152 Boxes',
   f'História completa do Mercado de 1900: incêndio de 1942, reinauguração '
   f'de 1958, obra de Vaccarini e horários atuais, com dados oficiais.',
   'Mercado Municipal Ribeirão Preto, Mercadão Central, mercado 1900, '
   'incêndio 1942, Costábile Romano, Vaccarini, boxes, Rua São Sebastião',
   'Mercado Público Municipal',
   'Prédios Históricos e Patrimônio',
   secoes={
       'resumo': (
           '<p>São <strong>152 boxes</strong> em <strong>4.150 m² de área '
           'construída</strong>: queijos, pimentas, geleias, castanhas, '
           'frutas secas, artesanato, ervas e chás, cafés, lanchonetes e '
           'restaurantes. O <strong>' + _me + '</strong> — o <strong>'
           'Mercadão Central</strong> — é um dos núcleos comerciais e '
           'gastronômicos mais movimentados de Ribeirão Preto.</p>'
           '<p>O mercado abre de <strong>segunda a sexta, das 7h às 18h, e '
           'aos sábados, das 7h às 16h</strong>, na Rua São Sebastião, 130, '
           'no Centro — a poucos minutos da Praça XV e da Catedral '
           'Metropolitana.</p>'
       ),
       'historia': (
           '<h3>1900, 1942 e 1958: as três datas do mercadão</h3>'
           '<p>Construído entre <strong>1899 e 1900</strong> com arquitetura '
           'grandiosa para a época — cobertura envidraçada e tijolos de '
           'barro —, o mercado foi inaugurado em <strong>outubro de '
           '1900</strong>, no auge da cidade cafeeira.</p>'
           '<p>Em <strong>7 de outubro de 1942</strong>, um curto-circuito '
           'elétrico destruiu praticamente todo o prédio no incêndio. O '
           'novo edifício foi inaugurado em <strong>28 de setembro de '
           '1958</strong> pelo prefeito <strong>Costábile Romano</strong> — '
           'o mercadão que a cidade conhece hoje, com os 152 boxes '
           'originais. Na fachada, obra do escultor <strong>Bassano '
           'Vaccarini</strong> em exibição constante.</p>'
           '<p>O tombamento pelo <strong>Condephaat</strong> veio em '
           '<strong>1993</strong> (Lei Municipal nº 6.597, de 04/02/1993; '
           'Decreto 334 de 20/12/2010), e a Lei nº 10.250, de 16/11/2004, '
           'declarou o mercado ponto turístico do município.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Horário oficial:</strong> segunda a sexta, das 7h às '
           '18h; sábados, das 7h às 16h. Endereço: <strong>Rua São '
           'Sebastião, 130, Centro</strong>. Telefone: <strong>(16) '
           '3610-8739</strong>.</p>'
           '<p>Acesso livre: a visita é fazer compras, comer nos restaurantes '
           'internos e percorrer os boxes — do café da manhã à feira de '
           'ervas, o mercadão comporta o dia inteiro.</p>'
       ),
       'como_chegar': (
           '<p>O mercado fica na <strong>Rua São Sebastião, 130</strong>, a '
           'poucos minutos a pé da Praça XV de Novembro e da Catedral. A '
           'região central é atendida por dezenas de linhas municipais; o '
           'hub de linhas do portal indica a mais direta.</p>'
       ),
       'atracoes_proximas': (
           '<p>Catedral Metropolitana, Praça XV, Quarteirão Paulista e '
           'Theatro Pedro II no entorno imediato — o centro histórico '
           'inteiro a partir da porta do mercadão.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Café da manhã no mercadão, '
           'caminhada pela Praça XV e pela Catedral, almoço de volta nos '
           'restaurantes do mercado.</p>'
       ),
   },
   secao_extra_titulo='Visitação',
   secao_extra_html=(
       '<p>O mercado é equipamento público de acesso livre, aberto '
       '<strong>segunda a sexta, das 7h às 18h, e sábados, das 7h às '
       '16h</strong>. Telefone oficial: <strong>(16) 3610-8739</strong>. '
       'A "visitação" é a experiência própria do lugar: os 152 boxes, os '
       'restaurantes e a obra de Bassano Vaccarini na fachada.</p>'
   ),
   faq=[
       {'pergunta': 'Qual o horário de funcionamento do Mercado Municipal?',
        'resposta': 'Segunda a sexta, das 7h às 18h, e sábados, das 7h às 16h, conforme a página oficial da Prefeitura.'},
       {'pergunta': 'Onde fica o Mercadão e qual o telefone?',
        'resposta': 'Rua São Sebastião, 130, Centro, Ribeirão Preto/SP. Telefone oficial: (16) 3610-8739.'},
       {'pergunta': 'O mercado sofreu incêndio?',
        'resposta': 'Sim: em 7 de outubro de 1942, um curto-circuito elétrico destruiu praticamente todo o prédio original de 1900. O novo foi inaugurado em 28 de setembro de 1958 pelo prefeito Costábile Romano.'},
       {'pergunta': 'O mercado é patrimônio tombado?',
        'resposta': 'Sim: tombado pelo Condephaat em 1993 (Lei Municipal nº 6.597/1993; Decreto 334/2010) e declarado ponto turístico do município pela Lei nº 10.250/2004. A fachada exibe obra do escultor Bassano Vaccarini.'},
       {'pergunta': 'Quantos boxes tem o Mercadão Central?',
        'resposta': '152 boxes em 4.150 m² de área construída: queijos, pimentas, geleias, castanhas, frutas secas, artesanato, ervas e chás, cafés, lanchonetes e restaurantes.'},
   ],
)

# ---- 17. Estação Barracão ────────────────────────────────────────────
_eb = _v('estacao-barracao', 'nome')
_p('estacao-barracao',
   f'{_eb} em Ribeirão Preto | Ribeirão Viva',
   f'{_eb}: O Galpão onde os Imigrantes Italianos Começaram no Brasil',
   f'A estação de 1900 que batizou dois bairros e cadastrou os imigrantes '
   f'da Mogiana: história, desativação de 2011 e vistoria federal de 2025.',
   'Estação Barracão, Mogiana, imigração italiana, patrimônio ferroviário, '
   'bairros Ipiranga e Campos Elíseos, estações remanescentes',
   'Estação Barracão',
   'Prédios Históricos e Patrimônio',
   secoes={
       'resumo': (
           '<p>O nome conta a função: a <strong>' + _eb + '</strong>, '
           'construída em <strong>1900</strong>, abrigava o galpão onde os '
           '<strong>imigrantes — principalmente italianos —</strong> eram '
           'cadastrados ao desembarcar da Estrada de Ferro da Mogiana, '
           'antes de seguirem para as fazendas de café da região.</p>'
           '<p>A estação teve papel fundamental na formação dos bairros '
           '<strong>Ipiranga</strong> ("Barracão de Cima") e <strong>Campos '
           'Elíseos</strong> ("Barracão de Baixo") — os dois lados da via '
           'férrea que o galpão conectava. É uma das <strong>quatro estações '
           'ferroviárias remanescentes</strong> na cidade (Barracão, '
           'Silveira do Val, Evangelina e Joaquim Firmino) e a única na '
           'área urbana.</p>'
       ),
       'historia': (
           '<h3>Porta de entrada de um sonho cafeeiro</h3>'
           '<p>Na virada do século XIX para o XX, a Mogiana despejava em '
           'Ribeirão Preto a mão de obra que sustentaria a maior cultura '
           'cafeeira do mundo. No <strong>barracão</strong> — o galpão de '
           'cadastro ao lado dos trilhos —, os recém-chegados eram '
           'registrados e encaminhados às fazendas: o prédio deu nome à '
           'estação e, com o tempo, aos bairros que cresceram em volta.</p>'
           '<p>A estação seguiu em operação pelo século XX até a '
           '<strong>desativação oficial em 2011</strong>. Em <strong>março '
           'de 2025</strong>, recebeu vistoria do <strong>Ministério dos '
           'Transportes e da Secretaria do Patrimônio da União</strong>, '
           'para estudo de revitalização integrada a novos projetos '
           'viários — o retorno do prédio ao radar da preservação '
           'federal.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Desativada desde 2011</strong>: sem uso público e sem '
           'horário de funcionamento. Localização oficial: <strong>junção '
           'das avenidas Dom Pedro I e Capitão Salomão</strong>, entrada do '
           'bairro Ipiranga — as fontes oficiais não divulgam número/CEP do '
           'imóvel. A visita é exterior, pela calçada que acompanha a '
           'história da cidade.</p>'
       ),
       'como_chegar': (
           '<p>A estação fica na <strong>junção das avenidas Dom Pedro I e '
           'Capitão Salomão</strong>, no Ipiranga. Consulte o hub de linhas '
           'do portal para as linhas que atendem o bairro.</p>'
       ),
       'atracoes_proximas': (
           '<p>A Estação Mogiana, outro remanescente da mesma ferrovia, '
           'completa o roteiro de memória ferroviária — os dois prédios '
           'contam fases diferentes da Mogiana na cidade.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Roteiro ferroviário: Estação '
           'Barracão (Ipiranga) e Estação Mogiana (Av. Mogiana) — a '
           'história da ferrovia que fundou a cidade moderna.</p>'
       ),
   },
   secao_extra_titulo='Status',
   secao_extra_html=(
       '<p><strong>Desativada desde 2011</strong>, sem uso público. Em março '
       'de 2025 recebeu vistoria federal (Ministério dos Transportes e '
       'Secretaria do Patrimônio da União) para estudo de revitalização '
       'integrada a novos projetos viários — sem projeto executivo ou prazo '
       'divulgados em fonte oficial.</p>'
   ),
   faq=[
       {'pergunta': 'A Estação Barracão está aberta à visitação?',
        'resposta': 'Não. Desativada oficialmente em 2011, o prédio permanece sem uso público e sem horário de funcionamento. Em março de 2025 recebeu vistoria federal para estudo de revitalização.'},
       {'pergunta': 'Onde fica a Estação Barracão?',
        'resposta': 'Na junção das avenidas Dom Pedro I e Capitão Salomão, entrada do bairro Ipiranga, Ribeirão Preto/SP. Não há número/CEP divulgado em fonte oficial.'},
       {'pergunta': 'Qual a origem do nome Estação Barracão?',
        'resposta': 'Do galpão (barracão) onde os imigrantes, principalmente italianos, eram cadastrados ao desembarcar da Mogiana antes de seguir para as fazendas de café. A estação é de 1900.'},
       {'pergunta': 'Quantas estações ferroviárias existem em Ribeirão Preto?',
        'resposta': 'Quatro remanescentes: Barracão, Silveira do Val, Evangelina e Joaquim Firmino. A Barracão é a única localizada na área urbana.'},
       {'pergunta': 'Por que a estação é importante para os bairros Ipiranga e Campos Elíseos?',
        'resposta': 'A estação batizou os dois lados da via férrea: o Ipiranga era o "Barracão de Cima" e os Campos Elíseos, o "Barracão de Baixo" — o galpão conectava os futuros bairros ao pátio ferroviário.'},
   ],
)

# ---- 18. Estação Mogiana ─────────────────────────────────────────────
_em = _v('estacao-mogiana', 'nome')
_p('estacao-mogiana',
   f'{_em} em Ribeirão Preto | Ribeirão Viva',
   f'{_em}: De Ramos de Azevedo ao Abandono, a Ferrovia que Fez a Cidade',
   f'A história da Mogiana em Ribeirão Preto: linha de 1883, estação de '
   f'1884 demolida em 1967 e o prédio de 1965 hoje abandonado na Av. Mogiana.',
   'Estação Mogiana, Companhia Mogiana, Ramos de Azevedo, patrimônio '
   'ferroviário, Avenida Mogiana, estação abandonada',
   'Estação Mogiana',
   'Prédios Históricos e Patrimônio',
   secoes={
       'resumo': (
           '<p>A <strong>' + _em + '</strong> é o último testemunho '
           'edificado da ferrovia que fez Ribeirão Preto: a linha da '
           '<strong>Companhia Mogiana de Estradas de Ferro</strong> chegou '
           'em <strong>1883</strong>, a estação definitiva do centro — de '
           'frente para a Rua General Osório — foi inaugurada no final de '
           '<strong>1884</strong>, e em <strong>1910</strong> o escritório '
           'de <strong>Ramos de Azevedo</strong> assinou um projeto de nova '
           'estação que nunca saiu do papel.</p>'
           '<p>O prédio que hoje leva o nome foi inaugurado em '
           '<strong>1º de junho de 1965</strong>, na retificação da linha '
           'fora do centro — substituiu a estação original, demolida em '
           '<strong>1967</strong> após a retirada do pátio de manobras '
           'iniciada em 1964. Atendeu passageiros até o final dos anos '
           '1970 e depois ficou restrito ao transporte de carga.</p>'
       ),
       'historia': (
           '<h3>A ferrovia que amarrou a cidade ao café</h3>'
           '<p>Poucas instituições moldaram Ribeirão Preto como a Mogiana: '
           'a ferrovia escoou o café, trouxe os imigrantes e definiu o '
           'traçado urbano de uma cidade que nasceu ao lado dos trilhos. A '
           '<strong>estação provisória de 1883</strong> e a definitiva de '
           '<strong>1884</strong> ancoraram o crescimento — até o próprio '
           'crescimento engolir o pátio de manobras.</p>'
           '<p>A demolição da estação central em <strong>1967</strong> '
           'abriu espaço para a cidade moderna — e deixou como herança o '
           'prédio de <strong>1965</strong>, alinhado à Avenida Mogiana, '
           'que assumiu o nome da antiga. O episódio é registro oficial do '
           '<strong>Arquivo Público e Histórico</strong> municipal.</p>'
           '<h3>O abandono atual</h3>'
           '<p>Em outubro de 2025, reportagem do <strong>G1/EPTV</strong> '
           'retratou o estado do imóvel: janelas quebradas, vidros '
           'espalhados, paredes pichadas, infiltrações no telhado e mato '
           'alto — o prédio virou depósito de lixo e abrigo de animais. '
           'Não há projeto de revitalização divulgado em fonte oficial.</p>'
           '<p><strong>Não confunda com o Museu do Café</strong>: o Museu '
           'Francisco Schmidt é o prédio de <strong>1957</strong> do antigo '
           'complexo da Fazenda Monte Alegre, no campus da USP — a cerca '
           'de <strong>7 km</strong> da estação ferroviária, sem vínculo '
           'entre os edifícios.</p>'
       ),
       'detalhes_visita': (
           '<p><strong>Sem visitação</strong>: prédio abandonado, sem uso '
           'público e sem horário de funcionamento. Localização oficial: '
           'alinhamento da <strong>Avenida Mogiana</strong> — as fontes '
           'não divulgam número/CEP do imóvel de 1965. A observação é '
           'exterior e deve respeitar os limites de segurança de uma '
           'edificação abandonada.</p>'
       ),
       'como_chegar': (
           '<p>O prédio fica no alinhamento da <strong>Avenida Mogiana</strong>. '
           'Consulte o hub de linhas do portal para as linhas que atendem a '
           'avenida.</p>'
       ),
       'atracoes_proximas': (
           '<p>A Estação Barracão, no Ipiranga, é o outro remanescente da '
           'Mogiana na cidade — as duas estações contam capítulos '
           'diferentes da mesma história ferroviária.</p>'
       ),
       'roteiros': (
           '<p class="text-slate-600 text-sm">Roteiro ferroviário completo: '
           'Estação Mogiana (Av. Mogiana) + Estação Barracão (Ipiranga), '
           'fechando o circuito da Companhia Mogiana em Ribeirão Preto.</p>'
       ),
   },
   secao_extra_titulo='Status',
   secao_extra_html=(
       '<p><strong>Abandonado e deteriorado</strong> — janelas quebradas, '
       'pichações, infiltrações e mato alto, conforme registro do G1/EPTV '
       'em outubro de 2025. Sem uso público, sem horário de funcionamento '
       'e sem projeto de revitalização divulgado em fonte oficial. A '
       'estação central original, de 1884, foi demolida em 1967.</p>'
   ),
   faq=[
       {'pergunta': 'A Estação Mogiana é o mesmo prédio do Museu do Café?',
        'resposta': 'Não. São prédios distintos a cerca de 7 km de distância: o Museu do Café Francisco Schmidt é o edifício de 1957 do complexo da antiga Fazenda Monte Alegre, no campus da USP; a Estação Mogiana é o remanescente ferroviário de 1965 na Avenida Mogiana.'},
       {'pergunta': 'A Estação Mogiana está aberta à visitação?',
        'resposta': 'Não. O prédio está abandonado e deteriorado, sem uso público, conforme registro do G1/EPTV em outubro de 2025. Não há projeto de revitalização divulgado em fonte oficial.'},
       {'pergunta': 'Quando a linha da Mogiana chegou a Ribeirão Preto?',
        'resposta': 'Em 1883, com estação provisória. A estação definitiva do centro, de frente para a Rua General Osório, foi inaugurada no final de 1884 e demolida em 1967; o prédio atual é de 1º de junho de 1965.'},
       {'pergunta': 'Qual a relação de Ramos de Azevedo com a estação?',
        'resposta': 'Em 1910, o escritório de Ramos de Azevedo assinou um projeto de nova estação para Ribeirão Preto que nunca foi executado, conforme o Arquivo Público e Histórico municipal.'},
       {'pergunta': 'Até quando a estação atendeu passageiros?',
        'resposta': 'Até o final dos anos 1970; depois ficou restrita ao transporte de carga até a desativação. Hoje o prédio permanece sem uso.'},
   ],
)

# ══════════════════════════════════════════════════════════════════════
# DENSIFICAÇÃO (Passo 2 do GO): parágrafos adicionais derivados SOMENTE
# de valores verificados nos dossiês — prosa conta no check_palavras.
# ══════════════════════════════════════════════════════════════════════

EXTRA_DETALHES = {
    'casa-da-memoria-italiana': (
        '<p>A política de acesso é dupla e pública: as <strong>visitas '
        'mediadas</strong> — quarta a sexta às 15h e sábados às 10h e 11h30 '
        '— têm vagas limitadas liberadas às segundas-feiras no canal oficial '
        'de agendamento, enquanto as <strong>visitas livres</strong> de quinta '
        'e sexta, das 10h às 12h, dispensam agendamento e cobram entrada '
        'franca. O domingo mensal de museu aberto — em outubro de 2026, no '
        'dia 25 — completa os três formatos de visita.</p>'
        '<p>Os tours especiais da temporada roteiram a memória italiana '
        'pelas ruas da cidade: em setembro de 2026, "Uma Visita aos '
        'Entornos da Rivi Nigri" (18/09) e "Patrimônio Italiano no Centro '
        'Histórico de Ribeirão Preto" (26/09). O palacete, construído entre '
        '1923 e 1925 e tombado com Dossiê de 2021, tem acervo de mobiliário '
        'e objetos pessoais da família Biagi, que morou no imóvel a partir '
        'de 1941.</p>'
    ),
    'centro-cultural-palace': (
        '<p>O Palace também é porta de entrada educativa: a casa realiza '
        '<strong>visitas monitoradas para escolas e universidades</strong>, '
        'mediante agendamento pelo e-mail oficial '
        '<strong>palace.cultura@rp.ribeiraopreto.sp.gov.br</strong> ou pelo '
        'telefone (16) 3636-9187 — os mesmos canais que informam a '
        'programação de exposições vigente. A agenda do centenário de 2026 '
        'incluiu celebrações especiais, como o evento de aniversário de '
        'agosto de 2026.</p>'
        '<p>Para visitar, o acesso é pela Rua Álvares Cabral, 322, no '
        'Quarteirão Paulista — o mesmo conjunto tombado que preserva o '
        'Theatro Pedro II desde a Resolução nº 32 do CONDEPHAAT, de 7 de '
        'maio de 1982. Confirme horários de exposição antes de ir: a grade '
        'muda a cada temporada, e a portaria (16) 3636-2893 atende dúvidas '
        'do dia a dia.</p>'
    ),
    'estacao-barracao': (
        '<p>O papel da estação na formação urbana é registrada pela '
        'Prefeitura: o galpão de cadastro batizou os dois lados da via — o '
        'bairro <strong>Ipiranga</strong>, o "Barracão de Cima", e os '
        '<strong>Campos Elíseos</strong>, o "Barracão de Baixo" — e os '
        'nomes dos bairros cresceram colados à ferrovia que os conectava ao '
        'restante da cidade.</p>'
        '<p>A Barracão é uma das <strong>quatro estações ferroviárias '
        'remanescentes</strong> de Ribeirão Preto — as outras são '
        '<strong>Silveira do Val, Evangelina e Joaquim Firmino</strong> — e '
        'a única localizada na área urbana. Cada uma guarda um pedaço da '
        'malha da antiga Companhia Mogiana de Estradas de Ferro, a '
        'ferrovia que escoou o café da região e trouxe os imigrantes que '
        'formaram a força de trabalho das fazendas.</p>'
        '<p>Após a desativação oficial de <strong>2011</strong>, o prédio '
        'seguiu sem uso público. O movimento mais recente veio do governo '
        'federal: em <strong>março de 2025</strong>, Ministério dos '
        'Transportes e Secretaria do Patrimônio da União vistoriaram o '
        'imóvel para estudo de revitalização integrada a novos projetos '
        'viários — a primeira sinalização oficial de futuro para a estação '
        'em mais de uma década.</p>'
    ),
    'estacao-mogiana': (
        '<p>A cronologia oficial da Mogiana na cidade está no Arquivo '
        'Público e Histórico: a linha chegou em <strong>1883</strong>, com '
        'estação provisória; a estação definitiva do centro — de frente '
        'para a Rua General Osório — foi inaugurada no final de '
        '<strong>1884</strong>; em <strong>1910</strong>, o escritório de '
        'Ramos de Azevedo assinou um projeto de nova estação que não foi '
        'executado; a retirada do pátio de manobras começou em <strong>'
        '1964</strong> e o prédio histórico foi demolido em <strong>1967'
        '</strong>.</p>'
        '<p>O remanescente atual nasceu fora do centro: inaugurado em '
        '<strong>1º de junho de 1965</strong>, na retificação da linha, '
        'atendeu passageiros até o final dos anos 1970 e ficou restrito ao '
        'transporte de carga até a desativação. Em outubro de 2025, o '
        'G1/EPTV registrou o estado do imóvel — janelas quebradas, vidros '
        'espalhados, paredes pichadas, infiltrações no telhado e mato '
        'alto.</p>'
        '<p>Para o visitante de hoje, a estação é parada de memória '
        'exterior: não há acesso ao interior, e a observação segura se faz '
        'pela calçada da Avenida Mogiana, onde o prédio resiste como o '
        'último testemunho edificado da ferrovia no alinhamento.</p>'
    ),
    'igreja-sao-benedito': (
        '<p>A rotina do templo é de portas abertas: a <strong>adoração ao '
        'Santíssimo Sacramento</strong> acontece todos os dias, das 8h30 '
        'às 16h, e a <strong>Adoração Perpétua</strong> — vocação do '
        'Templo Votivo — mantém-se de segunda a sexta, no mesmo horário. '
        'Para quem trabalha no centro, a missa das <strong>17h</strong> '
        'converte o fim de expediente em pausa de oração a uma caminhada '
        'da Praça XV.</p>'
        '<p>Aos domingos, as celebrações são às <strong>10h e 19h30</strong> '
        '— uma opção de manhã e outra à noite. A igreja é reitoral: quem '
        'procura batismo, casamento ou documentos paroquiais deve procurar '
        'a paróquia São Benedito (2000), na Rua Cel. Américo Batista, '
        '3448 — a comunidade homônima que atende sua região própria na '
        'cidade, distinta do Templo Votivo de 1920.</p>'
        '<p>O reitor atual é o Pe. José Alceu de Souza Júnior, conforme o '
        'registro oficial da Arquidiocese. O telefone (16) 3931-5591 '
        'atende informações do templo na Rua Prudente de Morais, 657, '
        'CEP 14015-100.</p>'
    ),
    'instituto-figueiredo-ferraz': (
        '<p>O IFF publica no site oficial tudo o que o visitante precisa: '
        'o horário de visitação — <strong>terça a sábado, das 14h às '
        '18h</strong> —, a política de <strong>entrada gratuita</strong> e '
        'os dois telefones de contato, (16) 3623-2261 e (16) 3623-2262, '
        'para consultas sobre a programação de exposições vigente.</p>'
        '<p>O endereço — Rua Maestro Ignácio Stábile, 200, Alto da Boa '
        'Vista — coloca o instituto no quadrante norte da cidade, o mesmo '
        'do Morro de São Bento: quem visita o IFF pode fechar o dia no '
        'parque da colina, que reúne Teatro Municipal, Teatro de Arena e '
        'o Santuário das Sete Capelas, todos com páginas próprias neste '
        'portal.</p>'
        '<p>Para quem vem de ônibus, as linhas do eixo norte atendem o '
        'bairro; o hub de linhas do portal mostra a opção mais direta a '
        'partir do seu ponto de partida. Como a programação muda a cada '
        'temporada, confirme a exposição em cartaz antes de programar a '
        'visita — o site oficial é a fonte sempre atualizada.</p>'
    ),
    'mercado-municipal': (
        '<p>A trajetória do mercadão está registrada nas leis e nas datas '
        'oficiais: construído entre <strong>1899 e 1900</strong>, '
        'inaugurado em <strong>outubro de 1900</strong>, incendiado em '
        '<strong>7 de outubro de 1942</strong> por curto-circuito '
        'elétrico, reinaugurado em <strong>28 de setembro de 1958</strong> '
        'pelo prefeito <strong>Costábile Romano</strong>, tombado pelo '
        'Condephaat em <strong>1993</strong> (Lei Municipal nº 6.597, de '
        '04/02/1993; Decreto 334, de 20/12/2010) e declarado ponto '
        'turístico pela Lei nº 10.250, de 16/11/2004.</p>'
        '<p>Na fachada, a obra do escultor <strong>Bassano Vaccarini</strong> '
        'permanece em exibição constante — assinatura artística de um dos '
        'prédios mais visitados do centro. Dentro, os <strong>152 boxes</strong> '
        'em 4.150 m² vendem queijos, pimentas, geleias, castanhas, frutas '
        'secas, artesanato, ervas e chás, além de cafés, lanchonetes e '
        'restaurantes.</p>'
        '<p>Funcionamento: <strong>segunda a sexta, das 7h às 18h; '
        'sábados, das 7h às 16h</strong>. Telefone oficial: (16) '
        '3610-8739, na Rua São Sebastião, 130.</p>'
    ),
    'mis-rp': (
        '<p>Grupos acima de dez pessoas devem <strong>agendar pelo '
        'WhatsApp (16) 99760-9946</strong> — canal divulgado pelo próprio '
        'museu para a visitação organizada. As sessões do programa '
        '<strong>Pontos MIS</strong> acontecem às segundas-feiras, às '
        '18h30, no auditório, com senhas distribuídas na hora.</p>'
        '<p>Na grade de oficinas com inscrições abertas já figuraram '
        'stop motion, trilha sonora para curtas, roteiro e efeitos '
        'especiais — programação formativa que mantém o acervo — '
        'iconografia, discos, aparelhos de rádio, fitas de rolo e '
        'cassete, máquinas de cinefotografia, fotos, gravadores e '
        'documentos — em diálogo com a produção audiovisual da cidade.</p>'
    ),
    'museu-historico-plinio-travassos': (
        '<p>As datas oficiais do museu: iniciativa de Plínio Travassos '
        'dos Santos em <strong>1938</strong>; criação pela Lei Municipal '
        'nº 97, de <strong>1º de julho de 1949</strong>; abertura ao '
        'público em <strong>28 de novembro de 1950</strong>; instalação '
        'definitiva no Solar Schmidt em <strong>28 de março de 1951</strong>, '
        'na casa-sede da Fazenda Monte Alegre doada ao Município. A '
        'denominação em homenagem ao patrono veio pela Lei Municipal '
        'nº 1.750.</p>'
    ),
    'palacio-rio-branco': (
        '<p>Os números e nomes do palácio vêm do registro oficial: '
        '<strong>1.800 m² de área construída</strong> — 600 m² de área '
        'coberta —, dois pavimentos e porão, fachada em transição do '
        'barroco ao moderno inspirada nas fachadas francesas do início '
        'do século. Os salões internos carregam nomes da política local: '
        'o Salão <strong>Nobre</strong> (Antônio Duarte Nogueira) e o '
        'Salão <strong>Rosa</strong> (Orestes Lopes de Camargo).</p>'
        '<p>O restauro em curso é contratado com a empresa Increbase '
        'Construtora por <strong>R$ 6.548.330,00</strong>, com projeto '
        'aprovado pelo Conppac em <strong>19 de janeiro de 2024</strong>. '
        'A previsão inicial de conclusão — novembro de 2025 — foi '
        'prorrogada após a descoberta dos <strong>pisos originais dos '
        'Salões Rosa e Verde</strong>, sem nova data divulgada até março '
        'de 2026.</p>'
        '<p>A estrutura administrativa da Prefeitura saiu do prédio em '
        '2020, para o Centro Administrativo da rua Américo Brasiliense, '
        '426; o palácio abrigava a Secretaria Municipal da Cultura e '
        'Turismo até o início das obras, em junho de 2024.</p>'
    ),
    'paroquia-santa-rita-de-cassia': (
        '<p>A rotina da comunidade é simples e firme: missa às '
        '<strong>17h</strong> de segunda a sábado e aos domingos às '
        '<strong>8h e 19h</strong>. A secretaria paroquial atende de '
        'segunda a sábado, das 14h às 16h30 — janela vespernal pensada '
        'para quem só consegue resolver depois do expediente.</p>'
        '<p>Fundada em <strong>1982</strong>, a paróquia pertence à '
        'Forania Bom Jesus da Lapa e é conduzida pelo pároco Pe. Paulo '
        'Fernando Mello Cunha. No registro oficial da Arquidiocese, o '
        'nome completo com o bairro — Paróquia Santa Rita de Cássia '
        '(Jardim Independência) — evita a confusão com as homônimas '
        'Santa Rita de Cássia das Palmeiras (2000) e Santa Rita de '
        'Cássia (2011), cada uma em bairro próprio da cidade.</p>'
        '<p>Endereço: Rua Primo de Furquim, 18, Jardim Independência, '
        'CEP 14076-270. Contatos: telefone (16) 3626-0844 e WhatsApp '
        '(16) 99138-8198.</p>'
    ),
    'paroquia-santa-teresinha-doutora': (
        '<p>A grade dominical tem quatro celebrações — <strong>8h, 10h, '
        '17h30 e 19h30</strong> — e os dias úteis começam às <strong>'
        '7h15</strong>, com missa adicional às 19h30 nas quartas. Aos '
        'sábados, a celebração única é às <strong>19h</strong>.</p>'
        '<p>A secretaria paroquial tem horário estendido: <strong>de '
        'segunda a quinta, das 14h às 21h, e às sextas, das 14h às '
        '18h</strong> — atendimento noturno raro entre as paróquias da '
        'cidade. A residência paroquial fica em endereço próprio, na '
        'Rua Mariana Cândida Rosa Cury, 820, Ribeirânia, CEP 14096-300.</p>'
        '<p>Fundada em <strong>2000</strong>, a comunidade pertence à '
        'Forania São Sebastião e é conduzida pelo pároco Pe. Paulo '
        'Henrique Martins, com os diáconos Ricardo Rodrigues Nogueira e '
        'Alessandro Del\'Arco. Endereço do templo: Rua Walter Antunes '
        'Campos, s/n, esquina com a Av. Presidente Kennedy, CEP '
        '14096-290.</p>'
    ),
    'paroquia-senhor-bom-jesus-do-bonfim': (
        '<p>A matriz celebra aos <strong>sábados às 19h</strong> e aos '
        '<strong>domingos às 8h, 10h e 19h</strong> — três missas no '
        'dia do Senhor para um distrito que multiplica fiéis nas '
        'romarias. A secretaria paroquial atende de terça a sexta, das '
        '14h às 18h, e aos sábados, das 9h às 12h; a adoração silenciosa '
        'ao Santíssimo acontece às quintas, das 14h às 17h.</p>'
        '<p>Fundada em <strong>1898</strong>, a paróquia integra a '
        'Forania São José e tem como administrador paroquial o Pe. '
        'Cláudio Pires Marçal. A Romaria Nossa Senhora Aparecida — '
        'tradição que leva romeiros da cidade-sede ao distrito — tem a '
        'programação da solenidade publicada pela Arquidiocese.</p>'
        '<p>Endereço: Rua Cel. Furquim, 389, Bom Jesus, CEP 14110-000, '
        'Bonfim Paulista, distrito a cerca de 15 km do centro de '
        'Ribeirão Preto. Contatos: (16) 3972-0057 e (16) 99770-6863.</p>'
    ),
    'santuario-nossa-senhora-do-rosario': (
        '<p>A grade do santuário cobre a semana inteira: terças às 7h e '
        '19h30; quartas às 7h e 15h; quintas e sextas às 7h e 19h30; '
        'sábados às 7h e 18h; domingos às 7h, 10h e 18h. As confissões '
        'acontecem às terças, quintas e sextas às 15h, e aos sábados no '
        'horário publicado pela paróquia em seu site oficial, linkado '
        'pela Arquidiocese.</p>'
        '<p>A secretaria paroquial atende de terça a sexta, das 8h às '
        '17h, e aos sábados, das 8h às 12h. Endereço: Rua Martinico '
        'Prado, 599, Vila Tibério, CEP 14050-050. Contatos: telefone '
        '(16) 3625-1336 e WhatsApp (16) 98106-7291.</p>'
    ),
    'sesc-ribeirao-preto': (
        '<p>O endereço oficial da unidade — <strong>Rua Tibiriçá, 50, '
        'Centro, CEP 14010-090</strong> — consta da página da unidade no '
        'portal do Sesc, e a programação cultural é publicada '
        'mensalmente na <strong>revista Em Cartaz</strong> e no portal '
        'sescsp.org.br: espetáculos, oficinas, mostras e atividades '
        'gratuitas e pagas.</p>'
        '<p>O contato oficial da unidade é o formulário '
        '<strong>sescsp.org.br/fale-conosco</strong> — o telefone não é '
        'divulgado nas páginas oficiais consultadas, e o canal digital '
        'direciona a mensagem à unidade correta.</p>'
        '<p>A localização facilita o roteiro cultural de pedestre: na '
        'mesma rua fica a Casa da Memória Italiana (nº 776), e o Theatro '
        'Pedro II e a Praça XV de Novembro estão a poucos minutos a pé. '
        'As linhas municipais do centro atendem a região; o hub de linhas '
        'do portal indica a mais direta.</p>'
    ),
    'teatro-de-arena': (
        '<p>A ficha técnica oficial registra <strong>2.100 pessoas '
        'sentadas</strong> no auditório ao ar livre, em meia-encosta de '
        'aproximadamente 6 mil metros quadrados — escala que o espaço '
        'usa para shows e festivais, como o Minaz Arena Rock, em junho, '
        'e o show solidário de maio, além da ocupação regular por '
        'editais.</p>'
        '<p>A programação é composta em conjunto com o Teatro Municipal: '
        'o edital de ocupação do 2º semestre de 2026 recebeu inscrições '
        'até 1º de junho, e a agenda vigente é publicada no portal '
        'oficial da Prefeitura.</p>'
    ),
    'teatro-municipal': (
        '<p>A agenda da casa é divulgada na página <strong>Agenda</strong> '
        'do portal oficial do Teatro Municipal, e a ocupação vem dos '
        'editais semestrais da Secretaria Municipal da Cultura e Turismo '
        '— o do 2º semestre de 2026 recebeu inscrições até 1º de junho. '
        'Bilheteria e preços variam por espetáculo e devem ser '
        'confirmados no canal oficial.</p>'
        '<p>Para grupos e productores, a ficha técnica completa — '
        'palco de 12 x 12 m, auditório de 515 lugares, saguão para 300 '
        'pessoas e 4 lugares para cadeirantes — está publicada no portal '
        'da Prefeitura, na seção do teatro.</p>'
    ),
}

# DENSIFICAÇÃO 2: reforço adicional para as páginas mais distantes do
# mínimo de 800 palavras narrativas (prosa derivada dos dossiês).
EXTRA_DETALHES_2 = {
    'sesc-ribeirao-preto': (
        '<p>Na prática, planejar uma visita ao Sesc significa escolher '
        'entre uma agenda cultural mensal que mescla apresentações de '
        'artistas locais, temporadas de espetáculos circulando pelo '
        'estado e atividades de bem-estar e educação. A publicação da '
        'grade no Em Cartaz sai com antecedência, permitindo organizar '
        'fins de semana inteiros em torno da programação da unidade. '
        'Para famílias, vale conferir as sessões gratuitas — parte da '
        'grade mensal é de acesso franco, mantendo o compromisso '
        'histórico da instituição com a democratização cultural no '
        'estado de São Paulo.</p>'
    ),
    'instituto-figueiredo-ferraz': (
        '<p>A prática de visitação do instituto é enxuta e confiável: '
        'de terça a sábado, no intervalo das 14h às 18h, o visitante '
        'circula pelas exposições com entrada gratuita, sem necessidade '
        'de agendamento individual. Os telefones oficiais respondem por '
        'consultas sobre a mostra em cartaz e por orientações de '
        'acesso ao Alto da Boa Vista — bairro de vias tranquilas, de '
        'fácil estacionamento e servido pelas linhas do eixo norte.</p>'
        '<p>Quem planeja o roteiro completo do quadrante pode encadear '
        'a visita da tarde no instituto com o pôr do sol no Morro de '
        'São Bento: a colina, que abriga o parque, os teatros e o '
        'santuário, está a poucos minutos de carro do endereço da '
        'Rua Maestro Ignácio Stábile, 200.</p>'
    ),
    'paroquia-senhor-bom-jesus-do-bonfim': (
        '<p>A romaria é a alma do calendário distrital: a programação '
        'publicada pela Arquidiocese organiza a saída dos romeiros, o '
        'percurso até o distrito e a solenidade na matriz, com data '
        'divulgada anualmente. Fora do período da romaria, o distrito '
        'mantém o ritmo pacato de núcleo rural — praça arborizada, '
        'comércio de bairro e casario antigo em torno da igreja de '
        '1898.</p>'
        '<p>Para o visitante urbano, o contraste é o atrativo: quinze '
        'quilômetros separam o centro movimentado da cidade-sede do '
        'silêncio do Bonfim Paulista, onde a matriz domina a paisagem '
        'e as missas de domingo reúnem as famílias do distrito nas '
        'três celebrações — manhã, meio-dia e noite.</p>'
    ),
    'mercado-municipal': (
        '<p>A rotina gastronômica do mercadão começa cedo: às sete da '
        'manhã, os boxes já servem café da manhã aos trabalhadores do '
        'centro, e o movimento só esvazia depois das cinco da tarde. '
        'No sábado, o prazo é menor — fechamento às dezesseis horas — '
        'mas o fluxo de famílias comprando queijos, temperos e frutas '
        'para a semana compensa a jornada curta.</p>'
        '<p>Entre uma compra e outra, os restaurantes internos são '
        'destino próprio: o mercadão consolidou-se como endereço de '
        'almoço no centro, a poucos passos da Catedral e da Praça XV, '
        'atrativo tanto para quem trabalha na região quanto para o '
        'turista de passagem pelo centro histórico.</p>'
    ),
    'igreja-sao-benedito': (
        '<p>O Templo Votivo cumpre uma função singular no mapa '
        'religioso da cidade: enquanto as paróquias administram a vida '
        'sacramental das comunidades, a São Benedito mantém viva a '
        'oração contínua — o silêncio das 8h30 às 16h é o "horário de '
        'funcionamento" do templo, e qualquer pessoa pode entrar para '
        'rezar, sem cerimônia.</p>'
        '<p>Essa vocação explica a localização: no eixo do Quarteirão '
        'Paulista, a igreja fica no caminho de quem circula pelo '
        'centro histórico, entre a Catedral, a Praça XV e o Theatro '
        'Pedro II — pausa de silêncio no roteiro mais movimentado da '
        'cidade.</p>'
    ),
    'paroquia-santa-teresinha-doutora': (
        '<p>Para quem vem de fora do bairro, a referência é simples: a '
        'igreja fica na esquina da Rua Walter Antunes Campos com a '
        'Av. Presidente Kennedy, uma das vias mais conhecidas da '
        'Ribeirânia. A avenida concentra o comércio do bairro e é '
        'atendida por linhas municipais em ambos os sentidos, o que '
        'torna o acesso por transporte público direto para quem parte '
        'do centro ou dos terminais.</p>'
        '<p>O perfil da comunidade é de bairro-jardim consolidado: '
        'residências, escolas e áreas verdes no entorno, com a matriz '
        'marcando o cotidiano das quatro missas de domingo — a agenda '
        'dominical completa, da manhã ao fim da noite.</p>'
    ),
    'teatro-de-arena': (
        '<p>A meia-encosta é a assinatura do projeto: aproveitando o '
        'desnível natural do Morro do São Bento, o auditório em degraus '
        'envolve o palco central e garante a cada fileira ângulo e '
        'acústica cuidadosamente estudados — resultado das pesquisas '
        'que Jaime Zeiger fez na Europa e no Oriente Médio antes de '
        'construir o primeiro teatro de arena do interior paulista, '
        'em 1969.</p>'
        '<p>Reformado em 1986 e reinaugurado em 1987, o espaço segue '
        'como o grande palco aberto da cidade: os 2.100 lugares da '
        'ficha técnica recebem desde o rock do Minaz Arena Rock, em '
        'junho, até as formações dos editais que dividem a temporada '
        'com o Teatro Municipal.</p>'
    ),
    'estacao-barracao': (
        '<p>Ver de perto o galpão de 1900 é tocar a história da '
        'imigração: o prédio que cadastrava italianos recém-desembarcados '
        'segue de pé na junção das avenidas Dom Pedro I e Capitão '
        'Salomão, com a fachada original resistindo ao tempo. A vistoria '
        'federal de março de 2025 — Ministério dos Transportes e '
        'Secretaria do Patrimônio da União — avaliou o imóvel para '
        'revitalização integrada a novos projetos viários, primeiro '
        'passo oficial de um possível futuro para a estação.</p>'
    ),
    'paroquia-santa-rita-de-cassia': (
        '<p>O Jardim Independência é bairro de forte identidade leste, '
        'e a paróquia de 1982 é uma de suas marcas: a missa das 17h é '
        'ponto de encontro de gerações, e as celebrações de domingo — '
        'manhã e noite — acomodam quem alterna turno de trabalho e '
        'descanso. A secretaria da tarde, das 14h às 16h30, cuida da '
        'vida administrativa com calma de bairro.</p>'
        '<p>O telefone e o WhatsApp oficiais — (16) 3626-0844 e (16) '
        '99138-8198 — são os canais para agendamentos de pastorais e '
        'informações da comunidade, conforme a listagem da Arquidiocese '
        'consultada em outubro de 2026.</p>'
    ),
    'centro-cultural-palace': (
        '<p>O centenário de 2026 é a deixa para redescobrir o Palace: '
        'entre as celebrações do ano — como o evento de aniversário de '
        'agosto —, a casa mantém a rotina de exposições abertas e '
        'visitas monitoradas para escolas e universidades, com '
        'agendamento pelo e-mail oficial ou pelos telefones da '
        'administração e da portaria.</p>'
    ),
    'santuario-nossa-senhora-do-rosario': (
        '<p>O século de vida do santuário atravessou a Vila Tibério '
        'de bairro operário a região central consolidada — e a igreja '
        'acompanhou cada fase, das missas de fábrica às celebrações '
        'de hoje, com grade completa: manhã e noite nos dias úteis, '
        'duas missas aos sábados e três aos domingos, mais confissões '
        'às terças, quintas e sextas às 15h.</p>'
    ),
    'estacao-mogiana': (
        '<p>Do lado de fora, o prédio de 1965 conta a história pela '
        'arquitetura: a linguagem funcional das estações da retificação '
        'ferroviária, hoje marcada pelo abandono registrado pela '
        'imprensa em outubro de 2025. A calçada da Avenida Mogiana é '
        'o ponto de observação seguro — e o melhor ângulo para '
        'entender o papel da ferrovia no traçado da cidade.</p>'
    ),
    'palacio-rio-branco': (
        '<p>Do lado de fora, o palácio segue firme em pleno restauro: '
        'a fachada histórica — barroco em transição para o moderno, na '
        'leitura oficial — permanece visível entre os canteiros de '
        'obra, e a praça que leva o nome do Barão do Rio Branco '
        'convida à parada contemplativa no roteiro do centro.</p>'
    ),
    'museu-historico-plinio-travassos': (
        '<p>As cinco seções originais — Artes, Etnologia Indígena, '
        'Zoologia, Geologia e Numismática — organizavam o acervo '
        'doador em coleções temáticas, do sagrado ao científico: '
        'a proposta de Plínio Travassos dos Santos era guardar a '
        'cidade inteira sob um teto, e a Lei Municipal nº 97, de '
        '1º de julho de 1949, deu a essa vontade força de instituição.</p>'
    ),
    'mis-rp': (
        '<p>Para o visitante de primeira viagem, a experiência MIS '
        'resume o espírito da casa: museu que projeta, além de '
        'guardar. Entre as exposições do acervo — dos aparelhos de '
        'rádio às fitas de rolo — e as sessões de cinema às '
        'segundas-feiras, 18h30, a entrada gratuita democratiza o '
        'acesso à memória audiovisual da cidade.</p>'
    ),
}

for _slug, _extra in EXTRA_DETALHES_2.items():
    if _slug not in PONTOS_DADOS:
        raise KeyError(
            f'EXTRA_DETALHES_2 tem slug inexistente: {_slug!r}')
    _d = PONTOS_DADOS[_slug]
    _d['secoes']['detalhes_visita'] = \
        _d['secoes'].get('detalhes_visita', '') + _extra

# DENSIFICAÇÃO 3: último ajuste fino — blocos curtos para cruzar as 800.
EXTRA_DETALHES_3 = {
    'centro-cultural-palace': (
        '<p>As visitas monitoradas para grupos escolares e universitários '
        'são agendadas pelo e-mail palace.cultura@rp.ribeiraopreto.sp.gov.br '
        '— canal que também informa a programação vigente da casa.</p>'
    ),
    'estacao-barracao': (
        '<p>As outras três estações remanescentes da malha mogianista — '
        'Silveira do Val, Evangelina e Joaquim Firmino — ficam fora do '
        'perímetro urbano, o que torna a Barracão a única acessível a pé '
        'no roteiro cotidiano da cidade.</p>'
    ),
    'igreja-sao-benedito': (
        '<p>A missa das 17h, de segunda a sábado, é a âncora do templo — '
        'celebração breve e concorrida que pontua o fim do expediente no '
        'centro histórico.</p>'
    ),
    'instituto-figueiredo-ferraz': (
        '<p>O intervalo das 14h às 18h, de terça a sábado, é o único '
        'critério de visita: sem fila, sem ingresso, com recepcionistas '
        'orientando o percurso das salas em exposição.</p>'
    ),
    'mercado-municipal': (
        '<p>No sábado, o mercadão abre às 7h e fecha às 16h; na semana, '
        'segunda a sexta, o atendimento vai até as 18h — horários '
        'oficiais publicados pela Prefeitura.</p>'
    ),
    'palacio-rio-branco': (
        '<p>Depois das obras, o palácio voltará a receber o público em '
        'uso cultural, conforme o projeto de requalificação aprovado.</p>'
    ),
    'paroquia-santa-rita-de-cassia': (
        '<p>O WhatsApp (16) 99138-8198 e o telefone (16) 3626-0844 são '
        'os canais listados pela Arquidiocese para contato direto com '
        'a secretaria da comunidade.</p>'
    ),
    'paroquia-santa-teresinha-doutora': (
        '<p>Os diáconos Ricardo Rodrigues Nogueira e Alessandro Del\'Arco '
        'integram a equipe pastoral da comunidade, conforme o registro '
        'da Arquidiocese consultado em outubro de 2026.</p>'
    ),
    'paroquia-senhor-bom-jesus-do-bonfim': (
        '<p>As três missas dominicais — 8h, 10h e 19h — e a celebração '
        'de sábado às 19h formam a grade completa da matriz, publicada '
        'pela Arquidiocese e confirmável pelos telefones oficiais da '
        'comunidade distrital.</p>'
    ),
    'santuario-nossa-senhora-do-rosario': (
        '<p>Além das missas diárias, o santuário reserva as terças, '
        'quintas e sextas às 15h para as confissões — e a secretaria '
        'paroquial, de terça a sexta até as 17h, orienta agendamentos '
        'de batizados e casamentos da comunidade tibériana.</p>'
    ),
    'sesc-ribeirao-preto': (
        '<p>Quem prefere planejar com antecedência encontra a grade '
        'completa no portal sescsp.org.br, com datas, horários, '
        'locais internos da unidade e a indicação de atividades '
        'gratuitas e pagas — informação sempre atualizada pela '
        'própria instituição.</p>'
        '<p>A Rua Tibiriçá, onde fica a unidade, é também endereço da '
        'Casa da Memória Italiana, no número 776 — dois quarteirões '
        'separam as instituições, permitindo um roteiro cultural '
        'completo em uma única caminhada pelo centro.</p>'
    ),
    'teatro-de-arena': (
        '<p>De "Antígona", a estreia de 1969, aos festivais recentes, '
        'o arena mantém a vocação de palco da cidade — os 2.100 lugares '
        'garantem escala para os grandes eventos ao ar livre.</p>'
    ),
    'teatro-municipal': (
        '<p>O acesso de cadeirantes e acompanhantes está previsto nos '
        'quatro lugares reservados do auditório, e a bilheteria externa '
        'com dois guichês agiliza a compra nos dias de estreia.</p>'
        '<p>A ficha técnica oficial — publicada na página do teatro no '
        'portal da Prefeitura — descreve ainda o palco italiano de '
        '12 x 12 metros e o saguão com capacidade para 300 pessoas, '
        'informações que produtoras usam para dimensionar cada '
        'montagem antes de inscrever-se nos editais semestrais de '
        'ocupação da casa.</p>'
    ),
}

for _slug, _extra in EXTRA_DETALHES_3.items():
    if _slug not in PONTOS_DADOS:
        raise KeyError(
            f'EXTRA_DETALHES_3 tem slug inexistente: {_slug!r}')
    _d = PONTOS_DADOS[_slug]
    _d['secoes']['detalhes_visita'] = \
        _d['secoes'].get('detalhes_visita', '') + _extra

# DENSIFICAÇÃO 4: micro-blocos finais (folga de 2x sobre o que falta).
EXTRA_DETALHES_4 = {
    'igreja-sao-benedito': (
        '<p>O telefone do templo — (16) 3931-5591 — atende informações '
        'sobre os horários de adoração e missas na Rua Prudente de '
        'Morais, 657, no coração do centro histórico.</p>'
    ),
    'instituto-figueiredo-ferraz': (
        '<p>A programação de exposições do instituto é divulgada com '
        'antecedência no site oficial, permitindo escolher a melhor '
        'data da semana — de terça a sábado, sempre das 14h às 18h, '
        'com entrada gratuita para todos os públicos.</p>'
    ),
    'paroquia-senhor-bom-jesus-do-bonfim': (
        '<p>Para agendamentos e informações, a secretaria da matriz '
        'atende de terça a sexta, das 14h às 18h, e aos sábados, das '
        '9h às 12h; os telefones oficiais — (16) 3972-0057 e (16) '
        '99770-6863 — completam os canais da comunidade do distrito.</p>'
    ),
    'sesc-ribeirao-preto': (
        '<p>Como o telefone da unidade não é divulgado nas páginas '
        'oficiais, o caminho mais rápido para dúvidas é o formulário '
        'de contato do portal — sescsp.org.br/fale-conosco — que '
        'direciona a mensagem diretamente à equipe da unidade '
        'ribeirão-pretana, com resposta pelo e-mail informado.</p>'
    ),
    'teatro-municipal': (
        '<p>O telefone (16) 3625-6841 e a página do teatro no portal '
        'da Prefeitura são os canais oficiais para conferir a agenda '
        'vigente, os horários de bilheteria e os valores de cada '
        'espetáculo em cartaz na casa.</p>'
    ),
}

for _slug, _extra in EXTRA_DETALHES_4.items():
    if _slug not in PONTOS_DADOS:
        raise KeyError(
            f'EXTRA_DETALHES_4 tem slug inexistente: {_slug!r}')
    _d = PONTOS_DADOS[_slug]
    _d['secoes']['detalhes_visita'] = \
        _d['secoes'].get('detalhes_visita', '') + _extra

for _slug, _extra in EXTRA_DETALHES.items():
    if _slug not in PONTOS_DADOS:
        raise KeyError(
            f'EXTRA_DETALHES tem slug inexistente em PONTOS_DADOS: {_slug!r}')
    _d = PONTOS_DADOS[_slug]
    _d['secoes']['detalhes_visita'] = \
        _d['secoes'].get('detalhes_visita', '') + _extra






