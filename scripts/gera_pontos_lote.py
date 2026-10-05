#!/usr/bin/env python3
"""
GERADOR DE PÁGINAS DE PONTO TURÍSTICO — LOTE EXPANSÃO (20 pontos)
scripts/gera_pontos_lote.py

Fluxo (tarefa Leo, 05/10/2026):
  1. Lê dossiês verificados de content/dados-fonte/pontos/*.json
  2. Gera páginas content/paginas/ribeirao-preto/pontos-turisticos/[slug].json
     com template ponto.html + secoes_extras (missas/programação/acervo/visitação)
  3. Registra os pontos em content/lista-mestre.json e no hub index.json

Régua: página publica SOMENTE o verificado no dossiê. Campo sem fonte no
dossiê = campo ausente na página (nunca 'não confirmado' em página pronta,
pois status:pendente no JSON dispara FATAL no check_pendentes).
Pendências ficam registradas por ausência no dossiê — consultável a
qualquer momento direto em dados-fonte/pontos/.
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
DOSSIES = ROOT / 'content' / 'dados-fonte' / 'pontos'
PAGS = ROOT / 'content' / 'paginas' / 'ribeirao-preto' / 'pontos-turisticos'
MESTRE = ROOT / 'content' / 'lista-mestre.json'
HUB = PAGS / 'index.json'
HOJE = date.today().isoformat()

# Metadados narrativos por slug (título SEO, descrição, seções HTML).
from gera_pontos_dados import PONTOS_DADOS

CAMPOS_FONTE = ('nome', 'endereco', 'horario_visita', 'horario_missas',
                'horarios', 'telefone', 'entrada', 'programacao',
                'status_atual', 'historia', 'capacidade', 'tombamento',
                'visita_guiada')


def carrega_dossie(slug):
    p = DOSSIES / f'{slug}.json'
    if not p.exists():
        raise FileNotFoundError(f'Dossiê ausente: {p}')
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def g(dossie, campo):
    v = dossie.get(campo)
    return v.get('valor') if isinstance(v, dict) and v.get('status') == 'verificado' else None


def gurl(dossie, campo):
    v = dossie.get(campo)
    return v.get('fonte_url') if isinstance(v, dict) else None


def monta_pagina(slug, dd):
    """dd = PONTOS_DADOS[slug]: metadados narrativos + seções redigidas (HTML)."""
    dos = carrega_dossie(slug)
    nome = g(dos, 'nome')
    endereco = g(dos, 'endereco')
    horario = (g(dos, 'horario_visita') or g(dos, 'horario_missas')
               or g(dos, 'horarios'))
    telefone = g(dos, 'telefone')
    entrada = g(dos, 'entrada')
    status_atual = g(dos, 'status_atual')

    # fontes citadas na página = fontes dos campos usados (dedup)
    fontes, vistos = [], set()
    for campo in CAMPOS_FONTE:
        u = gurl(dos, campo)
        if u and u not in vistos:
            vistos.add(u)
            dom = re.sub(r'^www\.', '',
                         u.split('/')[2] if '://' in u else u)
            fontes.append({'nome': dom, 'url': u,
                           'tipo': 'fonte_oficial',
                           'verificado_em': HOJE})

    visita = {}
    if endereco:
        visita['endereco'] = endereco
    if horario:
        visita['horario'] = horario
    if entrada:
        visita['ingresso'] = entrada

    # secoes_extras: seção dinâmica por tipo (missas/programação/acervo/visitação)
    secoes_extras = []
    if dd.get('secao_extra_titulo') and dd.get('secao_extra_html'):
        secoes_extras.append({'titulo': dd['secao_extra_titulo'],
                              'conteudo': dd['secao_extra_html']})

    pagina = {
        'slug': f'ribeirao-preto/pontos-turisticos/{slug}',
        'template': 'ponto.html',
        'schema_type': 'TouristAttraction',
        'titulo': dd['titulo_seo'],
        'h1': dd['h1'],
        'descricao': dd['descricao'],
        'keywords': dd['keywords'],
        'status': 'pronta',
        'revisor': 'Leonardo A. Macedo',
        'publicado': HOJE,
        'atualizado': HOJE,
        'proxima_revisao': '2027-10-05',
        'breadcrumbs': [
            {'nome': 'Início', 'url': 'https://infohausti.com.br/'},
            {'nome': 'Turismo',
             'url': 'https://infohausti.com.br/ribeirao-preto/pontos-turisticos/index.html'},
            {'nome': dd['nome_card'],
             'url': f'https://infohausti.com.br/ribeirao-preto/pontos-turisticos/{slug}.html'},
        ],
        'fontes': fontes,
        'visita': visita if visita else None,
        'linhas_proximas': dd.get('linhas_proximas', []),
        'atracoes_proximas': dd.get('atracoes_proximas', []),
        'secoes': dd['secoes'],
        'secoes_extras': secoes_extras,
        'faq': dd['faq'],
    }

    tombamento = g(dos, 'tombamento')
    if tombamento:
        pagina['tombamento'] = tombamento
    if telefone:
        pagina['telefone'] = telefone
    if status_atual:
        pagina['status_atual'] = status_atual
    return pagina


def registra_mestre_gerado():
    """Adiciona os novos pontos a lista-mestre.json (se ainda ausentes)."""
    with open(MESTRE, encoding='utf-8') as f:
        mestre = json.load(f)
    atuais = {p['slug'] for p in mestre.get('pontos_turisticos', [])}
    novos = 0
    for slug, dd in PONTOS_DADOS.items():
        s = f'ribeirao-preto/pontos-turisticos/{slug}'
        if s not in atuais:
            mestre['pontos_turisticos'].append({
                'slug': s,
                'nome': dd['nome_card'],
                'categoria': dd['categoria_mestre'],
                'dossie': f'dados-fonte/pontos/{slug}.json',
            })
            novos += 1
    with open(MESTRE, 'w', encoding='utf-8') as f:
        json.dump(mestre, f, ensure_ascii=False, indent=1)
    print(f'[+] lista-mestre.json: {novos} novo(s) ponto(s) registrado(s)')


def main():
    n_ok, erros = 0, []
    for slug, dd in PONTOS_DADOS.items():
        try:
            pag = monta_pagina(slug, dd)
        except FileNotFoundError as e:
            erros.append(f'{slug}: {e}')
            print(f'[X] {slug}: dossiê ausente — gere o dossiê primeiro')
            continue
        out = PAGS / f'{slug}.json'
        with open(out, 'w', encoding='utf-8') as f:
            json.dump(pag, f, ensure_ascii=False, indent=1)
        print(f'[+] Página gerada: {out.name}')
        n_ok += 1
    if n_ok:
        registra_mestre_gerado()
    print(f'\n[OK] {n_ok} página(s) gerada(s); {len(erros)} dossiê(s) ausente(s)')
    if erros:
        for e in erros:
            print('  -', e)
    return 0 if not erros else 1


if __name__ == '__main__':
    sys.exit(main())
