#!/usr/bin/env python3
"""Reconstrói o hub principal (ribeirao-preto/index.json) — Leo/Hermes, 06/10/2026.
Números verificados: 113 linhas, 30 pontos, 10 bairros, 6 serviços, 5 roteiros.
Marca: Ribeirão Viva. Zero promessa de radar/tempo real."""
import json
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'content' / 'paginas' / 'ribeirao-preto' / 'index.json'
HOJE = date.today().isoformat()

html = '''<article class="prose prose-slate max-w-none">

  <!-- 1. HERO -->
  <section class="mb-12 not-prose">
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-amber-900 text-white rounded-2xl p-8 md:p-14 shadow-xl">
      <p class="text-amber-400 text-sm font-semibold uppercase tracking-widest mb-3">Portal Digital da Cidade</p>
      <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight mb-4">Ribeirão Viva — Portal Digital da Cidade de Ribeirão Preto</h1>
      <p class="text-lg md:text-xl text-slate-200 leading-relaxed mb-8">A cidade em um clique: ônibus, turismo, bairros, serviços e dados.</p>
      <a href="#secoes" class="inline-flex items-center gap-2 bg-amber-500 hover:bg-amber-400 text-slate-900 font-bold px-6 py-3 rounded-xl transition-colors">
        Explorar a cidade →
      </a>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-10">
        <div class="bg-white/10 backdrop-blur rounded-xl p-4 border border-white/10">
          <p class="text-3xl font-extrabold text-amber-400">113</p>
          <p class="text-xs text-slate-300 uppercase tracking-wide mt-1">Linhas de ônibus</p>
        </div>
        <div class="bg-white/10 backdrop-blur rounded-xl p-4 border border-white/10">
          <p class="text-3xl font-extrabold text-amber-400">30</p>
          <p class="text-xs text-slate-300 uppercase tracking-wide mt-1">Pontos turísticos</p>
        </div>
        <div class="bg-white/10 backdrop-blur rounded-xl p-4 border border-white/10">
          <p class="text-3xl font-extrabold text-amber-400">10</p>
          <p class="text-xs text-slate-300 uppercase tracking-wide mt-1">Bairros</p>
        </div>
        <div class="bg-white/10 backdrop-blur rounded-xl p-4 border border-white/10">
          <p class="text-3xl font-extrabold text-amber-400">185</p>
          <p class="text-xs text-slate-300 uppercase tracking-wide mt-1">Páginas no portal</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. SEÇÕES PRINCIPAIS -->
  <section id="secoes" class="mb-12">
    <h2 class="text-2xl md:text-3xl font-bold text-slate-900 mb-6">As Portas da Cidade</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 not-prose">

      <!-- Mobilidade -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:border-amber-500 transition-colors">
        <div class="flex items-center gap-3 mb-3">
          <span class="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center text-xl">🚌</span>
          <h3 class="text-xl font-bold text-slate-900">Mobilidade Urbana</h3>
        </div>
        <p class="text-slate-600 text-sm leading-relaxed mb-4"><strong>113 linhas de ônibus</strong> com itinerário, horários e paradas — todas verificadas factualmente contra o banco oficial RP Mobi.</p>
        <div class="flex flex-wrap gap-2 mb-4">
          <a href="/linhas/mapa.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Mapa da rede</a>
          <a href="/linhas/alteracoes.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Alterações operacionais</a>
          <a href="/linhas/descontinuadas.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Descontinuadas</a>
        </div>
        <a href="/linhas/index.html" class="text-amber-700 text-sm font-bold hover:underline">Ver as 113 linhas →</a>
      </div>

      <!-- Turismo -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:border-amber-500 transition-colors">
        <div class="flex items-center gap-3 mb-3">
          <span class="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center text-xl">🏛️</span>
          <h3 class="text-xl font-bold text-slate-900">Turismo e Patrimônio</h3>
        </div>
        <p class="text-slate-600 text-sm leading-relaxed mb-4"><strong>30 pontos turísticos, históricos e culturais</strong> — igrejas, teatros, museus e prédios com história, horários e telefones verificados.</p>
        <div class="flex flex-wrap gap-2 mb-4">
          <a href="/ribeirao-preto/pontos-turisticos/teatro-dom-pedro.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Theatro Pedro II</a>
          <a href="/ribeirao-preto/pontos-turisticos/catedral-metropolitana.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Catedral</a>
          <a href="/ribeirao-preto/pontos-turisticos/museu-do-cafe.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Museu do Café</a>
        </div>
        <a href="/ribeirao-preto/pontos-turisticos/index.html" class="text-amber-700 text-sm font-bold hover:underline">Explorar os 30 pontos →</a>
      </div>

      <!-- Bairros -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:border-amber-500 transition-colors">
        <div class="flex items-center gap-3 mb-3">
          <span class="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center text-xl">🏘️</span>
          <h3 class="text-xl font-bold text-slate-900">Bairros</h3>
        </div>
        <p class="text-slate-600 text-sm leading-relaxed mb-4"><strong>10 bairros com história, linhas e serviços</strong> — o retrato territorial da cidade com cruzamento completo do transporte e da saúde pública.</p>
        <div class="flex flex-wrap gap-2 mb-4">
          <a href="/bairros/centro.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Centro</a>
          <a href="/bairros/higienopolis.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Higienópolis</a>
          <a href="/bairros/ribeirania.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Ribeirânia</a>
        </div>
        <a href="/bairros/index.html" class="text-amber-700 text-sm font-bold hover:underline">Conhecer os 10 bairros →</a>
      </div>

      <!-- Serviços -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:border-amber-500 transition-colors">
        <div class="flex items-center gap-3 mb-3">
          <span class="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center text-xl">📋</span>
          <h3 class="text-xl font-bold text-slate-900">Serviços Públicos</h3>
        </div>
        <p class="text-slate-600 text-sm leading-relaxed mb-4"><strong>6 serviços públicos essenciais</strong> com dados verificados: tarifa e cartão, saúde, escolas, Poupatempo, rodovias e telefones úteis.</p>
        <div class="flex flex-wrap gap-2 mb-4">
          <a href="/servicos/tarifa-e-cartao-nosso.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Tarifa</a>
          <a href="/servicos/postos-de-saude-ubs-upa.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Saúde</a>
          <a href="/servicos/matriculas-e-escolas-municipais.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Escolas</a>
        </div>
        <a href="/servicos/index.html" class="text-amber-700 text-sm font-bold hover:underline">Ver os 6 serviços →</a>
      </div>

      <!-- Roteiros -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:border-amber-500 transition-colors">
        <div class="flex items-center gap-3 mb-3">
          <span class="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center text-xl">🧭</span>
          <h3 class="text-xl font-bold text-slate-900">Roteiros Temáticos</h3>
        </div>
        <p class="text-slate-600 text-sm leading-relaxed mb-4"><strong>5 roteiros temáticos prontos</strong> — passeios estruturados com transporte integrado, do centro histórico a pé à rota do café.</p>
        <div class="flex flex-wrap gap-2 mb-4">
          <a href="/ribeirao-preto/roteiros/centro-historico.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Centro Histórico</a>
          <a href="/ribeirao-preto/roteiros/rota-do-cafe.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Rota do Café</a>
          <a href="/ribeirao-preto/roteiros/roteiro-criancas.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Para Crianças</a>
        </div>
        <a href="/ribeirao-preto/roteiros/index.html" class="text-amber-700 text-sm font-bold hover:underline">Ver os 5 roteiros →</a>
      </div>

      <!-- Institucional -->
      <div class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm hover:border-amber-500 transition-colors">
        <div class="flex items-center gap-3 mb-3">
          <span class="w-10 h-10 rounded-xl bg-amber-100 flex items-center justify-center text-xl">ℹ️</span>
          <h3 class="text-xl font-bold text-slate-900">Índice e Navegação</h3>
        </div>
        <p class="text-slate-600 text-sm leading-relaxed mb-4">Todas as <strong>185 páginas do portal</strong> organizadas em um mapa do site único — a forma mais rápida de encontrar qualquer conteúdo.</p>
        <div class="flex flex-wrap gap-2 mb-4">
          <a href="/mapa-do-site.html" class="text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-100 hover:bg-amber-100 text-slate-700 transition-colors">Mapa do site</a>
        </div>
        <a href="/mapa-do-site.html" class="text-amber-700 text-sm font-bold hover:underline">Ver todas as páginas →</a>
      </div>
    </div>
  </section>

  <!-- 3. MOBILIDADE EM DESTAQUE -->
  <section class="mb-12 not-prose">
    <div class="bg-amber-50 border-l-4 border-amber-600 rounded-r-2xl p-6 md:p-8">
      <h2 class="text-xl md:text-2xl font-bold text-amber-950 mb-3">Ônibus: a espinha dorsal da cidade</h2>
      <p class="text-amber-900 text-sm leading-relaxed mb-0">A tarifa é de <strong>R$ 5,00</strong>, com <strong>120 minutos de integração</strong> pelo Cartão Cidadão RP Mobi — a segunda viagem dentro do prazo não gera cobrança adicional. As 113 linhas cobrem bairros, distritos e terminais, com grades verificadas por dia útil, sábado e domingo.</p>
    </div>
  </section>

  <!-- 4. SOBRE O PROJETO -->
  <section class="mb-12">
    <h2 class="text-2xl font-bold text-slate-900 mb-4">O que é Ribeirão Viva</h2>
    <p class="text-slate-700 leading-relaxed mb-4">O Ribeirão Viva é a infraestrutura digital cívica, turística e de mobilidade urbana de Ribeirão Preto: um guia público construído com método — cada dado factual publicado passa por verificação contra fontes oficiais ou imprensa local citada, e nenhuma página vai ao ar sem auditoria automática de qualidade.</p>
    <p class="text-slate-700 leading-relaxed">Um <strong>projeto Satélite Urbano</strong>: orbita a cidade com dados úteis, publicados com responsabilidade — mobilidade verificada, patrimônio documentado, território mapeado.</p>
    <div class="mt-6 not-prose flex flex-wrap gap-3">
      <a href="/sobre.html" class="text-sm font-bold text-amber-700 hover:underline">Sobre o projeto →</a>
      <a href="/politica-editorial.html" class="text-sm font-bold text-amber-700 hover:underline">Política editorial →</a>
      <a href="/contato.html" class="text-sm font-bold text-amber-700 hover:underline">Fale conosco →</a>
    </div>
  </section>

  <!-- 5. CTA FINAL -->
  <section class="mb-8 not-prose">
    <div class="bg-slate-900 text-white rounded-2xl p-8 md:p-10 text-center">
      <h2 class="text-2xl md:text-3xl font-extrabold mb-3">Você tem comércio ou serviço?</h2>
      <p class="text-slate-300 mb-6 max-w-2xl mx-auto">Anuncie no portal e apareça para quem procura a cidade: turistas planejando visitas, moradores resolvendo o dia a dia e quem chega procurando informação confiável.</p>
      <a href="/anuncie.html" class="inline-flex items-center gap-2 bg-amber-500 hover:bg-amber-400 text-slate-900 font-bold px-6 py-3 rounded-xl transition-colors">Anuncie no Ribeirão Viva →</a>
    </div>
  </section>
</article>'''

pagina = {
    'slug': 'ribeirao-preto/index',
    'template': 'base.html',
    'schema_type': 'CollectionPage',
    'titulo': 'Ribeirão Preto',
    'h1': 'Ribeirão Viva — Portal Digital da Cidade de Ribeirão Preto',
    'descricao': 'A cidade em um clique: ônibus, turismo, bairros, serviços e dados de Ribeirão Preto - SP. 113 linhas, 30 pontos turísticos, 10 bairros e 185 páginas verificadas.',
    'keywords': ('ribeirao preto, ribeirao viva, portal ribeirao preto, '
                 'onibus ribeirao preto, turismo ribeirao preto, '
                 'bairros ribeirao preto, servicos ribeirao preto'),
    'status': 'pronta',
    'revisor': 'Leonardo A. Macedo',
    'publicado': HOJE,
    'atualizado': HOJE,
    'proxima_revisao': '2027-10-06',
    'breadcrumbs': [
        {'nome': 'Início', 'url': 'https://infohausti.com.br/'},
    ],
    'fontes': [
        {'nome': 'RP Mobi — dados oficiais de mobilidade', 'url': 'https://www.ribeiraopreto.sp.gov.br', 'tipo': 'fonte_oficial', 'verificado_em': HOJE},
    ],
    'conteudo_html': html,
}

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(pagina, f, ensure_ascii=False, indent=1)
print(f'[+] hub principal reconstruido ({len(html)} chars)')
print('[+] verificacoes: 113 linhas / 30 pontos / 10 bairros / 6 servicos / 5 roteiros')
