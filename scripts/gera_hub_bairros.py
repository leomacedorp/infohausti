#!/usr/bin/env python3
"""Hub dos bairros — gera content/paginas/bairros/index.json (Bloco D)."""
import json
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
PAGS = ROOT / 'content' / 'paginas' / 'bairros'
HOJE = date.today().isoformat()

NOME = {'centro': 'Centro', 'higienopolis': 'Higienópolis',
        'jardim-paulista': 'Jardim Paulista', 'ribeirania': 'Ribeirânia',
        'campos-eliseos': 'Campos Elísios', 'jardim-canada': 'Jardim Canadá',
        'alto-da-boa-vista': 'Alto da Boa Vista',
        'jardim-botanico': 'Jardim Botânico',
        'vila-virginia': 'Vila Virgínia', 'sumarezinho': 'Sumarezinho'}
DESC = {
    'centro': 'O quadrilátero histórico onde a cidade nasceu em 1856: Praça XV, Quarteirão Paulista, Theatro Pedro II e a maior concentração de linhas de ônibus da cidade.',
    'higienopolis': 'O bairro tradicional da região da Avenida Nove de Julho, com identidade preservada pelos moradores e história documentada.',
    'jardim-paulista': 'Bairro de uso misto ao longo da Avenida Independência, em verticalização e ligado ao eixo da Mogiana.',
    'ribeirania': 'O bairro do Estádio Santa Cruz e do loteamento INORP de 1966, com o Parque Curupira e a Ribeirânia movimentada.',
    'campos-eliseos': 'O gigante nascido do Núcleo Colonial Antônio Prado (1887): Basílica Santo Antônio, Santa Casa, Bosque Fábio Barreto e Avenida Saudade.',
    'jardim-canada': 'Portal da zona sul, vizinho do Jardim Botânico e da Avenida João Fiúsa, com comércio e residências.',
    'alto-da-boa-vista': 'O bairro planejado por Godofredo Leite Fiusa a partir de 1960, na Zona Sul, tendo a Avenida João Fiúsa como eixo.',
    'jardim-botanico': 'Bairro de uso misto aprovado em 2002, idealizado pelo GDU com projeto Contart e Takano — o urbanismo do século XXI.',
    'vila-virginia': 'Bairro tradicional e populoso da Zona Oeste, com UBS e UBDS próprias e linhas de ônibus abundantes.',
    'sumarezinho': 'Raízes do Núcleo Colonial na Zona Oeste: bairro tradicional com UPA e CSE próprios.',
}

cards = ''.join(
    f'\n      <!-- {NOME[s]} -->\n'
    f'      <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:border-amber-500 transition-colors flex flex-col justify-between">\n'
    f'        <div>\n'
    f'          <h3 class="text-xl font-bold text-slate-900 mb-2">\n'
    f'            <a href="/bairros/{s}.html" class="hover:text-amber-700">{NOME[s]}</a>\n'
    f'          </h3>\n'
    f'          <p class="text-sm text-slate-600 leading-relaxed mb-4">\n'
    f'            {DESC[s]}\n'
    f'          </p>\n'
    f'        </div>\n'
    f'        <a href="/bairros/{s}.html" class="text-amber-700 text-sm font-semibold hover:underline">Conhecer o bairro &rarr;</a>\n'
    f'      </div>'
    for s in NOME)

html = f'''<article class="prose prose-slate max-w-none">
  <header class="mb-8">
    <p class="text-xs font-semibold uppercase tracking-wider text-amber-700 mb-2">Território e Cidadania</p>
    <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight mb-4">Bairros de Ribeirão Preto</h1>
    <p class="text-lg text-slate-600 leading-relaxed">Dez bairros da cidade com história verificada, linhas de ônibus que atendem cada região, pontos turísticos e serviços públicos — o retrato territorial de Ribeirão Preto em páginas conectadas ao resto do portal.</p>
  </header>

  <section class="mb-12">
    <h2 class="text-2xl font-bold text-slate-900 mb-6 flex items-center gap-2"><span>🏘️</span> Os Dez Bairros</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">{cards}
    </div>
  </section>

  <section class="mb-10 bg-slate-50 p-6 rounded-xl border border-slate-200">
    <h2 class="text-xl font-bold text-slate-900 mb-3">Como usar estas páginas</h2>
    <p class="text-slate-700 text-sm leading-relaxed mb-4">Cada página de bairro reúne: a história da formação verificada em fontes oficiais e imprensa local; as linhas de ônibus do banco RP Mobi que atendem a região, com link direto para a página de cada linha; os pontos turísticos localizados no bairro, com link para seus guias completos; e as unidades de saúde registradas na base oficial do município.</p>
    <p class="text-slate-700 text-sm leading-relaxed mb-0">A delimitação oficial de bairros é feita pelo município com base nos loteamentos aprovados — e referências postais dos Correios podem variar em relação a essas divisas, como registra a própria Prefeitura.</p>
  </section>
</article>'''

pagina = {
    'slug': 'bairros/index',
    'template': 'base.html',
    'schema_type': 'WebPage',
    'titulo': 'Bairros de Ribeirão Preto',
    'h1': 'Bairros de Ribeirão Preto',
    'descricao': 'Dez bairros de Ribeirão Preto com história verificada, linhas de ônibus, pontos turísticos e serviços públicos em páginas próprias.',
    'keywords': 'bairros ribeirao preto, centro, higienopolis, ribeirania, campos eliseos, vila virginia, sumarezinho',
    'status': 'pronta',
    'revisor': 'Leonardo A. Macedo',
    'publicado': HOJE,
    'atualizado': HOJE,
    'proxima_revisao': '2027-10-05',
    'breadcrumbs': [
        {'nome': 'Início', 'url': 'https://infohausti.com.br/'},
        {'nome': 'Bairros', 'url': 'https://infohausti.com.br/bairros/index.html'},
    ],
    'fontes': [
        {'nome': 'Prefeitura de Ribeirão Preto', 'url': 'https://www.ribeiraopreto.sp.gov.br', 'tipo': 'fonte_oficial', 'verificado_em': HOJE},
        {'nome': 'Revide — Nosso Bairro, Nossa História', 'url': 'https://www.revide.com.br/noticias/categoria/nosso-bairro-nossa-historia/', 'tipo': 'imprensa_local', 'verificado_em': HOJE},
    ],
    'conteudo_html': html,
}

out = PAGS / 'index.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(pagina, f, ensure_ascii=False, indent=1)
print(f'[+] hub bairros/index.json gerado ({len(html)} chars)')
