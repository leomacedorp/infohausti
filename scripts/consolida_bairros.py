#!/usr/bin/env python3
"""
Consolida dossiês dos 10 bairros do Bloco D — Leo/Hermes, 05/10/2026.
Fontes: cruzamento LOCAL (linhas.json, unidades-saude.json, dados-fonte/pontos/)
+ fatos web com URL por campo (Revide série 'Nosso Bairro', Tribuna/Memórias
Notariais, Prefeitura). Campo sem fonte = pendente; NUNCA inventar.
"""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'content' / 'dados-fonte' / 'bairros'
OUT.mkdir(parents=True, exist_ok=True)
HOJE = '2026-10-05'


def norm(s):
    s = unicodedata.normalize('NFD', (s or '').lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


# ---------- cruzamentos locais ----------
LF = json.load(open(ROOT / 'content/dados-fonte/linhas.json', encoding='utf-8'))
US = json.load(open(ROOT / 'content/dados-fonte/unidades-saude.json', encoding='utf-8'))
UNIDADES = US['unidades']

def linhas_do_bairro(nome_variants):
    """Linhas cuja lista de bairros contém alguma das variantes."""
    out = []
    for k, v in LF.items():
        bairros = (v.get('bairros', {}) or {}).get('valor', []) or []
        if any(norm(nv) in norm(b) for b in bairros for nv in nome_variants):
            out.append({'codigo': k, 'nome': v.get('nome') or
                        (v.get('nome_oficial') or {}).get('valor', '')})
    return sorted(out, key=lambda x: x['codigo'])

def unidades_do_bairro(nome_variants, extra_texto=''):
    """Unidades de saúde cujo nome/endereço menciona o bairro."""
    out = []
    for u in UNIDADES:
        blob = norm(json.dumps(u, ensure_ascii=False))
        if any(norm(nv) in blob for nv in nome_variants) or \
           (extra_texto and norm(extra_texto) in blob):
            out.append(u)
    return out

def pontos_no_bairro(nome_variants):
    """Pontos turísticos (dossiês) cujo endereço menciona o bairro."""
    out = []
    for f in sorted((ROOT / 'content/dados-fonte/pontos').glob('*.json')):
        d = json.loads(f.read_text(encoding='utf-8'))
        end = d.get('endereco')
        blob = norm(json.dumps(d, ensure_ascii=False))
        if isinstance(end, dict):
            blob_end = norm(end.get('valor') or '')
        else:
            blob_end = blob
        if any(norm(nv) in blob_end for nv in nome_variants):
            nome = d.get('nome')
            nome = nome.get('valor') if isinstance(nome, dict) else nome
            out.append({'slug': f.stem, 'nome': nome})
    return out


def V(valor, url, nota=None):
    d = {'valor': valor, 'status': 'verificado', 'fonte_url': url,
         'verificado_em': HOJE}
    if nota:
        d['nota'] = nota
    return d


def P(motivo):
    return {'valor': None, 'status': 'pendente', 'motivo': motivo,
            'verificado_em': HOJE}


# ---------- fatos web (URL por campo) ----------
REV = 'https://www.revide.com.br/noticias/nosso-bairro-nossa-historia/'
HIGI = ('https://www.revide.com.br/noticias/curiosidades/'
        'era-uma-vez-um-bairroque-tem-desaparecido-de-documentos-oficiais-'
        'mesmo-presente-na-memoria-de-moradores-e-comerciantes/')
TRIB = ('https://www.tribunaribeirao.com.br/escritura-de-doacao-revela-'
        'detalhes-da-construcao-do-estadio-santa-cruz/')
BOT = REV + 'botanico-e-iraja-onde-a-maturidade-e-a-jovialidade-se-encontram/'
CEPBR = 'https://www.cepsdobrasil.com.br/cep/sp/ribeirao-preto/bairros'

DOCS = {}

DOCS['centro'] = {
    '_doc': 'Centro. Dossiê Bloco D 05/10/2026. Cruzamento local + Revide.',
    'nome': V('Centro', REV + 'centro-onde-tudo-comeca/'),
    'zona': V('Zona Central (quadrilátero histórico)',
              REV + 'centro-onde-tudo-comeca/',
              'Quadrilátero: av. Jerônimo Gonçalves, Francisco Junqueira, '
              'Nove de Julho e Independência'),
    'historia': V(
        'Povoamento iniciado em 1853 após doação de terras à Igreja por seis '
        'proprietários da Fazenda Barra do Retiro; fundação oficial em 19 de '
        'junho de 1856 (legalização do patrimônio da Igreja). O bairro foi '
        'desenhado em área de 2.180.774 m² distribuída em 43 ruas e avenidas '
        'no quadrilátero formado pelas avenidas Jerônimo Gonçalves, Francisco '
        'Junqueira, Nove de Julho e Independência. População estimada em '
        '19.083 pessoas (IBGE 2010). A Praça XV de Novembro foi tombada como '
        'patrimônio histórico em 1993 junto com o Quarteirão Paulista.',
        REV + 'centro-onde-tudo-comeca/'),
    'ceps': V('Faixa 14000-001 a 14015-xxx (quadrilátero central)',
              CEPBR, 'Faixa geral do município; CEPs específicos por rua'),
}

DOCS['higienopolis'] = {
    '_doc': ('Higienópolis. Dossiê Bloco D 05/10/2026. CASO ESPECIAL: '
             'denominação em transição — Prefeitura classifica como antigo '
             'loteamento (Vila Higienópolis), Correios tratam como Centro, '
             'mas Secretaria Municipal da Cultura ainda cataloga monumentos '
             'sob Higienópolis e moradores mantêm a identidade.'),
    'nome': V('Higienópolis (Vila Higienópolis na documentação municipal)',
              HIGI),
    'zona': V('Região central (entre as avenidas Nove de Julho e Independência)',
              HIGI),
    'historia': V(
        'A Prefeitura (Secretaria Municipal de Planejamento) classifica '
        '"Vila Higienópolis" como um antigo loteamento na região das '
        'avenidas Nove de Julho e Independência e ruas Campos Sales e Amadeu '
        'Amaral. Para os Correios, o endereço dos moradores do quadrilátero '
        'consta como Centro. A Secretaria Municipal da Cultura, no "Guia de '
        'Monumentos em Lugares Públicos", mantém capítulo próprio para o '
        'Higienópolis (obelisco do centenário da Independência e busto de '
        'Salvador Spadoni). Moradores e ONG Amigos do Higienópolis preservam '
        'a identidade do bairro, tradicional na cidade.',
        HIGI),
    'ceps': V('CEPs da região central (registrados como Centro pelos Correios)',
              HIGI),
}

DOCS['jardim-paulista'] = {
    '_doc': 'Jardim Paulista. Dossiê Bloco D 05/10/2026. Cruzamento local + Revide.',
    'nome': V('Jardim Paulista', REV + 'jardim-independencia-e-jardim-paulista-nosso-bairro-nossa-historia/'),
    'zona': P('regionalização oficial por zona não localizada em fonte oficial'),
    'historia': V(
        'Bairro desenvolvido ao longo do prolongamento da Avenida '
        'Independência (trechos nomeados Meira Júnior e Cavalheiro Paschoal '
        'Innechi, até o encontro com a Avenida Mogiana), de uso misto e '
        'população tradicional, em processo de verticalização recente. '
        'Integrado ao vizinho Independência na série de história de bairros '
        'da imprensa local, com o qual compartilha o eixo da avenida de três '
        'nomes.',
        REV + 'jardim-independencia-e-jardim-paulista-nosso-bairro-nossa-historia/'),
    'ceps': P('faixa de CEPs predominantes sem fonte específica'),
}

DOCS['ribeirania'] = {
    '_doc': 'Ribeirânia. Dossiê Bloco D 05/10/2026. Cruzamento local + Tribuna/Memórias Notariais.',
    'nome': V('Ribeirânia', TRIB),
    'zona': P('regionalização oficial por zona não localizada'),
    'historia': V(
        'O loteamento Ribeirânia foi implantado pela Imobiliária Nova '
        'Ribeirão Preto S.A. (INORP), que adquiriu as terras de Francisco '
        'Epaminondas de Almeida em agosto de 1965. Em 18 de junho de 1966, '
        'escritura pública lavrada no 4º Tabelionato de Notas formalizou a '
        'doação de duas glebas (mais de 94 mil m²) ao Botafogo Futebol '
        'Clube para a construção do Estádio Santa Cruz, inaugurado em 21 de '
        'janeiro de 1968. O registro notarial do loteamento documenta a '
        'expansão urbana da cidade na região e o desenho majoritariamente '
        'residencial do bairro.',
        TRIB),
    'ceps': P('faixa de CEPs predominantes sem fonte específica'),
}

DOCS['campos-eliseos'] = {
    '_doc': 'Campos Elísios. Dossiê Bloco D 05/10/2026. Cruzamento local + Revide.',
    'nome': V('Campos Elísios', REV + 'campos-eliseos-gigante-invisivel/'),
    'zona': V('Zona Norte/Oeste (Núcleo Colonial Antônio Prado)',
              REV + 'campos-eliseos-gigante-invisivel/'),
    'historia': V(
        'Nasceu do loteamento do Núcleo Colonial Antônio Prado, criado pelo '
        'governo em 1887 para receber imigrantes. O bairro corresponde à '
        'Terceira Sessão do núcleo, conhecida à época como "Barracão de '
        'Baixo" (em oposição ao "Barracão de Cima", atual Ipiranga). '
        'Provavelmente o nome vem do Cemitério da Saudade (1893), o mais '
        'antigo da cidade, em referência aos Campos Elísios da mitologia '
        'grega. É um dos bairros mais populosos da cidade, com a Avenida '
        'Saudade como referência comercial; abriga a Basílica Santo Antônio '
        'de Pádua (1947, elevada a Basílica Menor em 2019), a Santa Casa de '
        'Misericórdia, o Bosque Municipal Fábio Barreto e o campus da USP '
        'no entorno.',
        REV + 'campos-eliseos-gigante-invisivel/'),
    'ceps': P('faixa de CEPs predominantes sem fonte específica'),
}

DOCS['jardim-canada'] = {
    '_doc': 'Jardim Canadá. Dossiê Bloco D 05/10/2026. Cruzamento local.',
    'nome': V('Jardim Canadá', CEPBR,
              'Grafia "Jardim Canadá" conforme registro postal'),
    'zona': V('Zona Sul', 'https://indiceimoveis.com.br/blog/mercado-imobiliario/alto-boa-vista-ribeirao-preto/',
              'Referência imobiliária; zona oficial não localizada'),
    'historia': P('história específica do bairro sem fonte oficial ou reportagem localizada até 05/10/2026'),
    'ceps': P('faixa de CEPs predominantes sem fonte específica (ex.: 14024-210 citado em listagens comerciais)'),
}

DOCS['alto-da-boa-vista'] = {
    '_doc': 'Alto da Boa Vista. Dossiê Bloco D 05/10/2026. Cruzamento local.',
    'nome': V('Alto da Boa Vista', CEPBR),
    'zona': V('Zona Sul', 'https://indiceimoveis.com.br/blog/mercado-imobiliario/alto-boa-vista-ribeirao-preto/',
              'Referência imobiliária; zona oficial não localizada'),
    'historia': V(
        'O bairro originou-se do loteamento implantado por Godofredo Leite '
        'Fiusa, que adquiriu grande área de terras em 1960 e criou o '
        'loteamento que deu forma ao Alto da Boa Vista, definindo padrões '
        'construtivos do futuro bairro. Sua principal via, a Avenida '
        'Professor João Fiúsa, homenageia o pai do loteador, professor '
        'baiano João Fiúsa. Godofredo doou ainda parte das terras para a '
        'construção da Faculdade de Medicina da USP no campus ribeirão-pretano.',
        'https://yamaimoveis.com.br/postagem/avenida-joao-fiusa-ribeirao-preto'),
    'ceps': P('faixa de CEPs predominantes sem fonte específica'),
}

DOCS['jardim-botanico'] = {
    '_doc': 'Jardim Botânico. Dossiê Bloco D 05/10/2026. Cruzamento local + Revide.',
    'nome': V('Jardim Botânico', BOT),
    'zona': V('Subsetor Sul (Zona Sul)', BOT),
    'historia': V(
        'Aprovado em 24 de janeiro de 2002, o Jardim Botânico é um bairro de '
        'uso misto — da mesma geração do Nova Aliança, primeiro bairro de '
        'uso misto da cidade —, idealizado pelo Grupo de Desenvolvimento '
        'Urbano de Ribeirão Preto (GDU), com projeto urbanístico do escritório '
        'Contart e Takano, desenvolvido em meados da década de 1990. O traçado '
        'associa preservação ambiental e arquitetura contemporânea, e o bairro '
        'conecta o Jardim Canadá e a avenida João Fiúsa de um lado e, de outro, '
        'o Anel Viário às avenidas Maurílio Biagi/Francisco Junqueira — '
        'viabilizando o desenvolvimento da região ao norte do Anel Viário.',
        BOT),
    'ceps': P('faixa de CEPs predominantes sem fonte específica'),
}

DOCS['vila-virginia'] = {
    '_doc': 'Vila Virgínia. Dossiê Bloco D 05/10/2026. Cruzamento local.',
    'nome': V('Vila Virgínia', CEPBR),
    'zona': V('Zona Oeste', 'https://www.youtube.com/watch?v=7Byv2jn4_jw',
              'Documentário oficial da Prefeitura ("Vila Virgínia: Roots that tell the story")'),
    'historia': V(
        'A Vila Virgínia é um dos bairros mais tradicionais e populosos da '
        'Zona Oeste, criado por um antigo morador da cidade e nomeado em '
        'homenagem a sua esposa, conforme a série "Nosso Bairro" da '
        'Prefeitura de Ribeirão Preto.',
        'https://www.facebook.com/PrefeituraRP/videos/nosso-bairro-vila-virg%C3%ADnia/167827529656625/'),
    'ceps': P('faixa de CEPs predominantes sem fonte específica'),
}

DOCS['sumarezinho'] = {
    '_doc': 'Sumarezinho. Dossiê Bloco D 05/10/2026. Cruzamento local.',
    'nome': V('Sumarezinho', CEPBR),
    'zona': V('Zona Oeste',
              'https://www.revide.com.br/noticias/cidades/obras-na-avenida-antonio-e-helena-zerrener-estao-em-andamento/',
              '"região oeste de Ribeirão Preto", reportagem local'),
    'historia': V(
        'O Sumarezinho originou-se da Primeira Seção do Núcleo Colonial '
        'Antônio Prado (1887), o mesmo loteamento que deu origem aos '
        'Campos Elísios e ao Ipiranga, conforme reportagem da série de '
        'história de bairros da imprensa local. Bairro tradicional da '
        'região oeste, citado nos registros históricos municipais desde o '
        'final do século XIX.',
        REV + 'campos-eliseos-gigante-invisivel/'),
    'ceps': P('faixa de CEPs predominantes sem fonte específica'),
}

# variantes para cruzamento local
VARIANTS = {
    'centro': ['Centro'],
    'higienopolis': ['Higienópolis'],
    'jardim-paulista': ['Jardim Paulista'],
    'ribeirania': ['Ribeirânia'],
    'campos-eliseos': ['Campos Elíseos', 'Campos Elísios'],
    'jardim-canada': ['Jardim Canadá', 'Jardim Canada'],
    'alto-da-boa-vista': ['Alto da Boa Vista'],
    'jardim-botanico': ['Jardim Botânico', 'Jardim Botanico'],
    'vila-virginia': ['Vila Virgínia', 'Vila Virginia'],
    'sumarezinho': ['Sumarezinho'],
}

n_lin, n_pend = 0, 0
for slug, doc in DOCS.items():
    variants = VARIANTS[slug]
    # linhas (cruzamento local)
    linhas = linhas_do_bairro(variants)
    if linhas:
        doc['linhas'] = {
            'valor': [f"{l['codigo']} — {l['nome']}" for l in linhas],
            'status': 'verificado',
            'fonte_url': 'dados-fonte/linhas.json (banco local RP Mobi)',
            'verificado_em': HOJE,
            'n_total': len(linhas),
        }
        n_lin += len(linhas)
    else:
        doc['linhas'] = P('nenhuma linha do banco local lista o bairro')
    # unidades de saúde
    un = unidades_do_bairro(variants)
    if un:
        doc['servicos_saude'] = {
            'valor': [f"{u.get('nome')} ({u.get('tipo')})" for u in un],
            'status': 'verificado',
            'fonte_url': 'dados-fonte/unidades-saude.json (SMS/CNES, mar/2026)',
            'verificado_em': HOJE,
        }
    # pontos turísticos
    pts = pontos_no_bairro(variants)
    if pts:
        doc['pontos_turisticos'] = {
            'valor': pts,
            'status': 'verificado',
            'fonte_url': 'dados-fonte/pontos/ (dossiês verificados)',
            'verificado_em': HOJE,
        }
    with open(OUT / f'{slug}.json', 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    pend = sum(1 for v in doc.values()
               if isinstance(v, dict) and v.get('status') == 'pendente')
    n_pend += pend
    print(f'[+] {slug}: linhas={len(linhas)}, saude={len(un)}, '
          f'pontos={len(pts)}, pendentes={pend}')

print(f'\n10 dossiês escritos | {n_lin} linhas cruzadas | {n_pend} campos pendentes')
