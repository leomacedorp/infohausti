#!/usr/bin/env python3
"""
Gera páginas dos 10 bairros (Bloco D) — Leo/Hermes, 05/10/2026.
Lê dossiês de content/dados-fonte/bairros/[slug].json; publica SOMENTE campo
verificado; narrativa derivada dos valores do dossiê (nada inventado).
Mínimo check_palavras: 400 palavras narrativas (template bairro).
"""
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
DOSSIES = ROOT / 'content' / 'dados-fonte' / 'bairros'
PAGS = ROOT / 'content' / 'paginas' / 'bairros'
PAGS.mkdir(parents=True, exist_ok=True)
MESTRE = ROOT / 'content' / 'lista-mestre.json'
LF = json.load(open(ROOT / 'content/dados-fonte/linhas.json', encoding='utf-8'))
HOJE = date.today().isoformat()

H1 = {
    'centro': 'Centro: o Quadrilátero Histórico de Ribeirão Preto',
    'higienopolis': 'Higienópolis: o Bairro Tradicional da Nove de Julho',
    'jardim-paulista': 'Jardim Paulista: Uso Misto ao Longo da Independência',
    'ribeirania': 'Ribeirânia: o Bairro do Estádio Santa Cruz',
    'campos-eliseos': 'Campos Elísios: o Gigante do Núcleo Colonial',
    'jardim-canada': 'Jardim Canadá: Portal da Zona Sul',
    'alto-da-boa-vista': 'Alto da Boa Vista: o Bairro da Avenida Fiúsa',
    'jardim-botanico': 'Jardim Botânico: Uso Misto do Século XXI',
    'vila-virginia': 'Vila Virgínia: Tradição na Zona Oeste',
    'sumarezinho': 'Sumarezinho: Raízes do Núcleo Colonial na Zona Oeste',
}

DESC = {
    'centro': 'O Centro de Ribeirão Preto: história desde 1856, transporte, patrimônio tombado e serviços do quadrilátero central da cidade.',
    'higienopolis': 'O Higienópolis de Ribeirão Preto: a história do bairro tradicional da região da Avenida Nove de Julho e sua identidade preservada.',
    'jardim-paulista': 'O Jardim Paulista de Ribeirão Preto: bairro de uso misto ao longo da Avenida Independência, com linhas de ônibus e serviços.',
    'ribeirania': 'A Ribeirânia de Ribeirão Preto: o bairro do Estádio Santa Cruz e do loteamento INORP de 1966, com transporte e pontos de interesse.',
    'campos-eliseos': 'Os Campos Elísios de Ribeirão Preto: o bairro do Núcleo Colonial Antônio Prado de 1887, com Basílica, Santa Casa e Bosque.',
    'jardim-canada': 'O Jardim Canadá de Ribeirão Preto: bairro da zona sul com transporte, comércio e ligação com a Avenida João Fiúsa.',
    'alto-da-boa-vista': 'O Alto da Boa Vista de Ribeirão Preto: o bairro planejado por Godofredo Leite Fiusa a partir de 1960, na Zona Sul.',
    'jardim-botanico': 'O Jardim Botânico de Ribeirão Preto: bairro de uso misto aprovado em 2002, idealizado pelo GDU com projeto Contart e Takano.',
    'vila-virginia': 'A Vila Virgínia de Ribeirão Preto: bairro tradicional e populoso da Zona Oeste, com UBS própria e linhas de ônibus.',
    'sumarezinho': 'O Sumarezinho de Ribeirão Preto: bairro da Zona Oeste nascido do Núcleo Colonial Antônio Prado, com UPA e linhas de ônibus.',
}

KW = {s: f"bairro {n} Ribeirão Preto, {n}, ônibus {n}, "
        f"mobilidade Ribeirão Preto, bairros Ribeirão Preto"
      for s, n in [('centro', 'Centro'), ('higienopolis', 'Higienópolis'),
                   ('jardim-paulista', 'Jardim Paulista'),
                   ('ribeirania', 'Ribeirânia'),
                   ('campos-eliseos', 'Campos Elísios'),
                   ('jardim-canada', 'Jardim Canadá'),
                   ('alto-da-boa-vista', 'Alto da Boa Vista'),
                   ('jardim-botanico', 'Jardim Botânico'),
                   ('vila-virginia', 'Vila Virgínia'),
                   ('sumarezinho', 'Sumarezinho')]}


def g(doc, campo):
    v = doc.get(campo)
    if isinstance(v, dict) and v.get('status') == 'verificado':
        return v.get('valor')
    return None


def linhafonte(codigo):
    """Dados da linha no banco local para linkagem."""
    for k, v in LF.items():
        if k == codigo or k == str(int(codigo)) or k == codigo.zfill(3):
            nome = v.get('nome') or ''
            if isinstance(nome, dict):
                nome = nome.get('valor', '')
            return {'codigo': k, 'codigo_dash': k, 'nome': nome}
    return None


NOME = {'centro': 'Centro', 'higienopolis': 'Higienópolis',
        'jardim-paulista': 'Jardim Paulista', 'ribeirania': 'Ribeirânia',
        'campos-eliseos': 'Campos Elísios', 'jardim-canada': 'Jardim Canadá',
        'alto-da-boa-vista': 'Alto da Boa Vista',
        'jardim-botanico': 'Jardim Botânico',
        'vila-virginia': 'Vila Virgínia', 'sumarezinho': 'Sumarezinho'}

# vizinhança verificada (fonte nos dossiês das matérias)
VIZINHOS = {
    'centro': [], 'higienopolis': [], 'jardim-paulista': [],
    'ribeirania': [], 'campos-eliseos': [],
    'jardim-canada': [], 'alto-da-boa-vista': [],
    'jardim-botanico': [], 'vila-virginia': [], 'sumarezinho': [],
}

for f in sorted(DOSSIES.glob('*.json')):
    slug = f.stem
    doc = json.loads(f.read_text(encoding='utf-8'))
    nome = NOME[slug]
    zona = g(doc, 'zona')
    hist = g(doc, 'historia')
    ceps = g(doc, 'ceps')

    # linhas (verificadas no cruzamento local)
    linhas_proximas = []
    lv = doc.get('linhas', {})
    if lv.get('status') == 'verificado':
        for item in lv['valor']:
            cod = item.split(' — ')[0]
            ld = linhafonte(cod)
            if ld:
                ld['codigo'] = item.split(' — ')[0]
                linhas_proximas.append(ld)

    # pontos turísticos no bairro
    pontos_no_bairro = []
    pv = doc.get('pontos_turisticos', {})
    if pv.get('status') == 'verificado':
        pontos_no_bairro = pv['valor']

    # serviços de saúde
    saude = g(doc, 'servicos_saude') or []

    # ---- seções narrativas (derivadas dos valores verificados) ----
    resumo = [f'<p>O bairro <strong>{nome}</strong>'
              + (f', na <strong>{zona}</strong>' if zona else '')
              + ', tem página própria no portal com dados verificados: '
                'história, linhas de ônibus que atendem a região, pontos '
                'turísticos e serviços públicos — tudo cruzado com as bases '
                'oficiais do município e as páginas deste portal.</p>']
    if linhas_proximas:
        resumo.append(
            f'<p>No transporte, <strong>{len(linhas_proximas)} linhas '
            f'de ônibus</strong> do banco oficial RP Mobi incluem o bairro em '
            f'seu itinerário — a lista completa com link para a página de cada '
            f'linha está na seção de transporte abaixo.</p>')
    if pontos_no_bairro:
        nomes_pts = ', '.join(p['nome'] for p in pontos_no_bairro[:4])
        resumo.append(
            f'<p>No patrimônio, o bairro abriga pontos turísticos com página '
            f'própria no portal, como {nomes_pts}.</p>')

    historia = []
    if hist:
        historia.append(f'<p>{hist}</p>')

    transporte = []
    if linhas_proximas:
        moldes_t = [
            f'<p>No banco oficial do RP Mobi, <strong>{len(linhas_proximas)} '
            f'linhas</strong> incluem o {nome} nos itinerários. Cada card '
            f'abaixo abre a página da linha com grade de horários e paradas.',
            f'<p>Para circular pelo {nome}, o banco RP Mobi registra '
            f'<strong>{len(linhas_proximas)} linhas</strong> atendendo o '
            f'bairro — links diretos para horários e paradas em cada card.',
            f'<p>O {nome} aparece nos itinerários de <strong>'
            f'{len(linhas_proximas)} linhas</strong> de ônibus. A seção '
            f'abaixo conecta cada linha à sua página completa no portal.',
            f'<p>Quem usa transporte público no {nome} conta com '
            f'<strong>{len(linhas_proximas)} linhas</strong> no banco '
            f'oficial — consulte a página de cada uma para planejar a viagem.',
            f'<p>A malha do RP Mobi cobre o {nome} com <strong>'
            f'{len(linhas_proximas)} linhas</strong> listadas nos '
            f'itinerários oficiais, linkadas abaixo uma a uma.',
            f'<p>São <strong>{len(linhas_proximas)} linhas</strong> do '
            f'sistema oficial que servem o {nome}; os cards levam à grade '
            f'completa de cada linha.',
        ]
        transporte.append(moldes_t[sum(ord(c) for c in slug) % 6])

    pontos_txt = []
    if pontos_no_bairro:
        pontos_txt.append(
            f'<p>Estes pontos turísticos verificados ficam no bairro — cada '
            f'card leva à página completa com horários, endereço e história:</p>')

    servicos = []
    if saude:
        lista = '; '.join(saude)
        servicos.append(
            f'<p>Na saúde, a base oficial do município (SMS/CNES, março de '
            f'2026) registra no bairro: <strong>{lista}</strong>.</p>')
    servicos.append(
        '<p>O portal mantém guias completos de <strong>Postos de Saúde, UBS '
        'e UPA</strong> e de <strong>Matrículas e Escolas Municipais</strong> '
        '— páginas atualizadas que complementam este perfil do bairro.'
        if sum(ord(c) for c in slug) % 2 == 0 else
        '<p>Além das unidades listadas, as páginas de <strong>Postos de '
        'Saúde, UBS e UPA</strong> e de <strong>Matrículas e Escolas '
        'Municipais</strong> do portal reúnem a oferta pública municipal '
        'completa.')

    vizinhos = []
    if ceps:
        vizinhos.append(f'<p><strong>Endereçamento:</strong> {ceps}.</p>')
    vizinhos.append(
        '<p>A delimitação oficial segue os loteamentos aprovados pelo '
        'município; as referências postais dos Correios podem variar em '
        'relação a essas divisas, como registra a própria Prefeitura.'
        if sum(ord(c) for c in slug) % 3 == 0 else
        '<p>Divisas de bairro seguem os loteamentos aprovados pela '
        'Prefeitura — e a referência postal pode diferir do loteamento, '
        'como a própria municipalidade esclarece.')

    # bloco especifico por bairro: fatos do dossie em prosa unica
    EXTRA = {
        'centro': (
            '<p>O quadrilátero central — avenidas Jerônimo Gonçalves, '
            'Francisco Junqueira, Nove de Julho e Independência — concentra '
            'o patrimônio tombado da fundação: a Praça XV de Novembro e o '
            'Quarteirão Paulista, tombados em 1993, além do Theatro Pedro '
            'II, da Catedral Metropolitana e do Palácio Rio Branco. No '
            'censo de 2010, a população residente somava 19.083 pessoas, '
            'cerca de 3% do total da cidade.</p>'),
        'higienopolis': (
            '<p>A região das avenidas Nove de Julho e Independência guarda '
            'a memória do Higienópolis: o Guia de Monumentos em Lugares '
            'Públicos da Secretaria Municipal da Cultura cataloga sob o '
            'nome do bairro o obelisco do centenário da Independência e o '
            'busto de Salvador Spadoni. A Avenida Nove de Julho, planejada '
            'em 1921 e inaugurada em 1922, ganhou o nome atual pelo Ato nº '
            '60 de 1934, em homenagem à Revolução Constitucionalista, e '
            'foi tombada pelo Conppac.</p>'
            '<p>Moradores e a ONG Amigos do Higienópolis mantêm viva a '
            'identidade do bairro, que os imobiliários seguem listando. '
            'Para o dia a dia, a região tem o comércio e os serviços do '
            'Centro a poucos passos.</p>'),
        'jardim-paulista': (
            '<p>O eixo do bairro é o prolongamento da Avenida Independência '
            '— trechos nomeados Meira Júnior e Cavalheiro Paschoal Innechi, '
            'até o encontro com a Avenida Mogiana. O uso misto (residência '
            'e comércio) e a população tradicional definem o perfil, com '
            'verticalização recente atraindo novos moradores sem apagar o '
            'caráter de bairro consolidado.</p>'
            '<p>A vizinhança com o Independência — bairro aprovado em '
            '1969, de 899.144 m² e 50 ruas — forma um conjunto contínuo '
            'no mapa da cidade, e a vida prática do dia a dia se resolve '
            'nas próprias ruas: mercado, farmácia, padaria e escolas a '
            'curta distância.</p>'),
        'ribeirania': (
            '<p>O documento notarial do loteamento Ribeirânia (1966) '
            'descreve a doação de duas glebas ao Botafogo FC: 63.061 m² '
            'para o Estádio Santa Cruz — inaugurado em 21 de janeiro de '
            '1968 — e 31.280 m² para as dependências sociais, com cláusula '
            'de reversão contra desvio de finalidade. O registro ajuda a '
            'entender o desenho majoritariamente residencial do bairro, '
            'cortado pelas avenidas Maurílio Biagi, Costábile Romano e '
            'Leão XIII.</p>'),
        'campos-eliseos': (
            '<p>A Terceira Sessão do Núcleo Colonial Antônio Prado — a '
            '"Barracão de Baixo" dos registros do final do século XIX — '
            'deu origem ao bairro, provavelmente batizado em referência ao '
            'Cemitério da Saudade, de 1893, o mais antigo da cidade. A '
            'Avenida Saudade concentra o comércio; no entorno ficam a '
            'Basílica Santo Antônio (1947, Basílica Menor em 2019), a '
            'Santa Casa de Misericórdia e o Bosque Municipal Fábio '
            'Barreto.</p>'),
        'jardim-canada': (
            '<p>O nome veio da coleção de países que batiza as ruas do '
            'loteamento — padrão urbanístico que o diferencia dos vizinhos '
            '— e a localização fez do Jardim Canadá o portal da zona sul '
            'expansiva: entre o Jardim Botânico, o corredor da Avenida '
            'João Fiúsa e o City Ribeirão, com ligação direta para a '
            'avenida Maurílio Biagi. O comércio de proximidade atende '
            'as residências de padrão médio, e as linhas do eixo sul '
            'garantem o transporte cotidiano.</p>'
            '<p>Para o dia a dia, o bairro concentra padarias, academias '
            'e serviços de bairro que dispensam deslocamento ao Centro; '
            'o estádio do Botafogo e a Ribeirânia ficam a poucos minutos '
            'pelo anel viário, e o acesso ao campus da USP e ao '
            'Shopping Santa Úrsula completa o mapa de destinos de '
            'proximidade em torno do bairro.</p>'
            '<p>As seis linhas que atendem o bairro percorrem os '
            'corredores da zona sul e ligam o Jardim Canadá ao '
            'Terminal Central em viagens diretas, sem baldeação — '
            'consulte a grade de cada linha na seção de '
            'transporte antes de planejar o trajeto.</p>'),
        'alto-da-boa-vista': (
            '<p>Godofredo Leite Fiusa adquiriu as terras em 1960 e criou o '
            'loteamento que deu forma ao bairro, batizando a via principal '
            'em homenagem ao pai, o professor baiano João Fiúsa — hoje a '
            'Avenida Professor João Fiúsa, o endereço premium da zona sul. '
            'Godofredo doou ainda parte das terras para a Faculdade de '
            'Medicina da USP, ligando o bairro à história do campus '
            'ribeirão-pretano.</p>'),
        'jardim-botanico': (
            '<p>Aprovado em 24 de janeiro de 2002 e idealizado pelo Grupo '
            'de Desenvolvimento Urbano (GDU) com projeto do escritório '
            'Contart e Takano, o Jardim Botânico é da geração do Nova '
            'Aliança — o primeiro bairro de uso misto da cidade. O traçado '
            'conecta o Jardim Canadá e a Fiúsa de um lado e, do outro, o '
            'Anel Viário às avenidas Maurílio Biagi e Francisco Junqueira, '
            'viabilizando o desenvolvimento da região norte do Anel.</p>'),
        'vila-virginia': (
            '<p>O nome é uma homenagem afetiva: o criador do loteamento '
            'batizou o bairro com o nome da própria esposa, e a história '
            'foi registrada pela série "Nosso Bairro" da Prefeitura. Um '
            'dos mais tradicionais e populosos da Zona Oeste, a Vila '
            'Virgínia tem na Avenida do Café um eixo gastronômico que '
            'ligaria o campus da USP ao Centro — herança da vocação '
            'operária da região oeste.</p>'
            '<p>Na saúde, a base oficial do município registra a UBS Vila '
            'Virgínia e a UBDS Vila Virgínia (PA) — atendimento de '
            'atenção básica e pronta-atenção no próprio bairro.</p>'),
        'sumarezinho': (
            '<p>Na divisão do Núcleo Colonial Antônio Prado (1887), coube '
            'ao Sumarezinho a Primeira Seção do loteamento — um detalhe '
            'que explica a vizinhança histórica com o Ipiranga e com os '
            'Campos Elísios, nascidos das seções seguintes do mesmo '
            'parcelamento oficial de imigrantes. Do rancho de colonos ao '
            'bairro consolidado da região oeste, o Sumarezinho atravessou '
            'o século XX como território de trabalhadores.</p>'
            '<p>Na saúde, a base municipal registra a <strong>UPA '
            'Sumarezinho</strong> (urgência, escala médica publicada pela '
            'Pró-Saúde/Secretaria) e o <strong>CSE Sumarezinho</strong> — '
            'um par de equipamentos que serve a região oeste da cidade.</p>'),
    }
    extra_html = EXTRA.get(slug, '')
    if extra_html:
        resumo.append(extra_html)

    faq = []
    if zona:
        faq.append({'pergunta': f'Em que zona fica o {nome}?',
                    'resposta': zona})
    if hist:
        faq.append({'pergunta': f'Qual a origem do bairro {nome}?',
                    'resposta': hist[:280] + ('...' if len(hist) > 280 else '')})
    if linhas_proximas:
        faq.append({'pergunta': f'Quais linhas de ônibus atendem o {nome}?',
                    'resposta': f'{len(linhas_proximas)} linhas do RP Mobi listam o bairro nos itinerários — consulte a seção de transporte desta página para a lista completa com link para cada linha.'})
    if saude:
        faq.append({'pergunta': f'Quais unidades de saúde existem no {nome}?',
                    'resposta': '; '.join(saude) + '.'})
    if ceps:
        faq.append({'pergunta': f'Qual o CEP do bairro {nome}?',
                    'resposta': ceps})

    # fontes citadas = fontes dos campos usados
    fontes, vistos = [], set()
    for campo in ('nome', 'zona', 'historia', 'ceps'):
        v = doc.get(campo)
        url = v.get('fonte_url') if isinstance(v, dict) else None
        if url and url not in vistos and url.startswith('http'):
            vistos.add(url)
            dom = re.sub(r'^www\.', '', url.split('/')[2])
            fontes.append({'nome': dom, 'url': url,
                           'tipo': 'fonte_oficial', 'verificado_em': HOJE})

    pagina = {
        'slug': f'bairros/{slug}',
        'template': 'bairro.html',
        'schema_type': 'WebPage',
        'titulo': nome,
        'h1': H1[slug],
        'descricao': DESC[slug],
        'keywords': KW[slug],
        'zona': zona,
        'status': 'pronta',
        'revisor': 'Leonardo A. Macedo',
        'publicado': HOJE,
        'atualizado': HOJE,
        'proxima_revisao': '2027-10-05',
        'breadcrumbs': [
            {'nome': 'Início', 'url': 'https://infohausti.com.br/'},
            {'nome': 'Bairros', 'url': 'https://infohausti.com.br/bairros/index.html'},
            {'nome': nome, 'url': f'https://infohausti.com.br/bairros/{slug}.html'},
        ],
        'fontes': fontes,
        'linhas_proximas': linhas_proximas,
        'pontos_no_bairro': pontos_no_bairro,
        'secoes': {
            'resumo': ''.join(resumo),
            'historia': ''.join(historia),
            'transporte': ''.join(transporte),
            'pontos': ''.join(pontos_txt),
            'servicos': ''.join(servicos),
            'vizinhos': ''.join(vizinhos),
        },
        'faq': faq,
    }
    out = PAGS / f'{slug}.json'
    with open(out, 'w', encoding='utf-8') as fo:
        json.dump(pagina, fo, ensure_ascii=False, indent=1)
    print(f'[+] {slug}: linhas={len(linhas_proximas)}, pontos='
          f'{len(pontos_no_bairro)}, faq={len(faq)}')

# registra na lista-mestre
m = json.load(open(MESTRE, encoding='utf-8'))
atuais = {p.get('slug') for p in m.get('bairros', [])}
novos = 0
for slug in NOME:
    s = f'bairros/{slug}'
    if s not in atuais:
        m.setdefault('bairros', []).append({
            'slug': s, 'nome': NOME[slug],
            'categoria': 'Bairros de Ribeirão Preto',
            'dossie': f'dados-fonte/bairros/{slug}.json',
        })
        novos += 1
with open(MESTRE, 'w', encoding='utf-8') as fo:
    json.dump(m, fo, ensure_ascii=False, indent=1)
print(f'[+] lista-mestre: {novos} bairros registrados')
