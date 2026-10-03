#!/usr/bin/env python3
"""
GERADOR OFICIAL DE PÁGINAS — INFOHAUS RP (scripts/build.py)
Compila dados JSON de content/paginas/ com templates Jinja2 para dist/
Garante canonical absoluto, microdados Schema.org, sitemap.xml e search-index.json.
"""

import os
import sys
import json
import shutil
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Garante saída UTF-8 no Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    print("[ERRO] jinja2 não instalado. Execute: pip install jinja2")
    sys.exit(1)

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / 'content'
PAGINAS_DIR = CONTENT_DIR / 'paginas'
TEMPLATES_DIR = ROOT_DIR / 'templates'
PARTIALS_DIR = ROOT_DIR / 'partials'
ASSETS_DIR = ROOT_DIR / 'assets'
DIST_DIR = ROOT_DIR / 'dist'

def load_json(path, default=None):
    if not path.exists():
        return default
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_schema_graph(page_data, config, canonical_url):
    """Gera o bloco JSON-LD com @graph semântico"""
    graph = []

    # 1. Entidade Principal do Template
    template_type = page_data.get('schema_type', 'WebPage')
    main_entity = {
        "@type": template_type,
        "@id": f"{canonical_url}#entity",
        "name": page_data.get('titulo', ''),
        "description": page_data.get('descricao', ''),
        "url": canonical_url,
        "inLanguage": "pt-BR"
    }

    if 'geo' in page_data:
        main_entity['geo'] = {
            "@type": "GeoCoordinates",
            "latitude": page_data['geo'].get('latitude'),
            "longitude": page_data['geo'].get('longitude')
        }

    if 'endereco' in page_data:
        main_entity['address'] = {
            "@type": "PostalAddress",
            "streetAddress": page_data['endereco'].get('logradouro', ''),
            "addressLocality": "Ribeirão Preto",
            "addressRegion": "SP",
            "addressCountry": "BR"
        }

    if 'imagens' in page_data and page_data['imagens']:
        main_entity['image'] = page_data['imagens'][0].get('url', '')

    graph.append(main_entity)

    # 2. Breadcrumbs
    breadcrumbs = page_data.get('breadcrumbs', [])
    if breadcrumbs and len(breadcrumbs) > 1:
        breadcrumb_elements = []
        for idx, item in enumerate(breadcrumbs, start=1):
            elem = {
                "@type": "ListItem",
                "position": idx,
                "name": item.get('nome', '')
            }
            if item.get('url'):
                elem['item'] = item['url']
            breadcrumb_elements.append(elem)

        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{canonical_url}#breadcrumb",
            "itemListElement": breadcrumb_elements
        })

    # 3. FAQPage (Regra estrita: Somente com 3 ou mais perguntas reais)
    faq_items = page_data.get('faq', [])
    if len(faq_items) >= 3:
        faq_entities = []
        for item in faq_items:
            pergunta = item.get('pergunta') or item.get('question')
            resposta = item.get('resposta') or item.get('answer')
            if pergunta and resposta:
                faq_entities.append({
                    "@type": "Question",
                    "name": pergunta,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": resposta
                    }
                })

        if len(faq_entities) >= 3:
            graph.append({
                "@type": "FAQPage",
                "@id": f"{canonical_url}#faq",
                "mainEntity": faq_entities
            })

    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

def generate_sitemap(ready_pages, config):
    """Gera sitemap.xml canônico em dist/"""
    dominio = config.get('dominio_base', 'https://infohausti.com.br')
    
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for page in ready_pages:
        slug = page['slug']
        loc_url = f"{dominio}/{slug}.html" if slug != "index" else f"{dominio}/"
        
        url_elem = ET.SubElement(urlset, 'url')
        loc_elem = ET.SubElement(url_elem, 'loc')
        loc_elem.text = loc_url
        
        lastmod = page.get('atualizado') or page.get('publicado') or datetime.now().strftime('%Y-%m-%d')
        lastmod_elem = ET.SubElement(url_elem, 'lastmod')
        lastmod_elem.text = lastmod

    sitemap_path = DIST_DIR / 'sitemap.xml'
    tree = ET.ElementTree(urlset)
    tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
    print(f"[+] Sitemap gerado com {len(ready_pages)} URLs em {sitemap_path}")

def generate_search_index(ready_pages, config):
    """Gera índice de busca leve em JSON"""
    dominio = config.get('dominio_base', 'https://infohausti.com.br')
    search_index = []

    for page in ready_pages:
        slug = page['slug']
        url = f"{dominio}/{slug}.html" if slug != "index" else f"{dominio}/"
        search_index.append({
            "title": page.get('titulo', ''),
            "description": page.get('descricao', ''),
            "url": url,
            "keywords": page.get('keywords', '')
        })

    index_path = DIST_DIR / 'search-index.json'
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)
    print(f"[+] Índice de busca gerado com {len(search_index)} itens em {index_path}")

def resolve_internal_links(html, ready_slugs, dist_dir):
    """
    Resolve links internos conforme Regra 6 do Manual de Execução:
    Alvo ainda não construído é omitido, nunca vira link quebrado.
    """
    def replace_link(match):
        full_tag = match.group(0)
        href = match.group(1).strip()
        inner_content = match.group(2)

        # Links externos, âncoras e esquemas especiais permanecem intactos
        if href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
            return full_tag

        clean_path = href.split('?')[0].split('#')[0]
        slug = clean_path.strip('/').replace('.html', '')
        if not slug:
            slug = 'index'

        # Verifica se o slug está marcado como pronto ou já existe em dist/
        is_ready = (
            slug in ready_slugs or
            (dist_dir / f"{slug}.html").exists() or
            (dist_dir / slug / "index.html").exists() or
            (slug == 'index' and (dist_dir / "index.html").exists())
        )

        if is_ready:
            return full_tag
        else:
            # Alvo não construído: omite a tag <a> para evitar link quebrado
            return f'<span class="opacity-75 cursor-default">{inner_content}</span>'

    return re.sub(r'<a\s+[^>]*?href=["\']([^"\']+)["\'][^>]*?>(.*?)</a>', replace_link, html, flags=re.DOTALL | re.IGNORECASE)

def main():
    print("==================================================")
    print("   MOTOR DE COMPILAÇÃO INFOHAUS RP (build.py)    ")
    print("==================================================")

    # 1. Carrega configurações e correções
    config = load_json(CONTENT_DIR / 'config.json', {})
    correcoes = load_json(CONTENT_DIR / 'correcoes.json', [])
    status_map = load_json(CONTENT_DIR / 'status.json', {})

    dominio_base = config.get('dominio_base', 'https://infohausti.com.br')

    # 2. Configura Jinja2 com templates e partials
    env = Environment(
        loader=FileSystemLoader([str(ROOT_DIR), str(TEMPLATES_DIR), str(PARTIALS_DIR)]),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # 3. Cria pasta dist/ limpa
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # 4. Copia assets e arquivos da raiz
    if ASSETS_DIR.exists():
        dist_assets = DIST_DIR / 'assets'
        if dist_assets.exists():
            shutil.rmtree(dist_assets)
        shutil.copytree(ASSETS_DIR, dist_assets)
        print(f"[+] Assets copiados para {dist_assets}")

    for root_file in ['robots.txt', 'ads.txt']:
        src = ROOT_DIR / root_file
        if src.exists():
            shutil.copy2(src, DIST_DIR / root_file)
            print(f"[+] {root_file} copiado para dist/{root_file}")

    # Copia favicons para a raiz de dist/
    for fav in ['favicon.ico', 'favicon-16x16.png', 'favicon-32x32.png', 'apple-touch-icon.png']:
        fav_src = ASSETS_DIR / 'img' / fav
        if fav_src.exists():
            shutil.copy2(fav_src, DIST_DIR / fav)
            print(f"[+] {fav} copiado para dist/{fav}")

    # 5. Escaneia páginas JSON
    all_pages = []
    if PAGINAS_DIR.exists():
        for json_file in PAGINAS_DIR.glob('**/*.json'):
            try:
                page_data = load_json(json_file)
                if page_data and isinstance(page_data, dict):
                    page_data['_file_path'] = json_file
                    all_pages.append(page_data)
            except Exception as e:
                print(f"[!] Erro ao carregar {json_file}: {e}")

    # 6. Mapeia páginas prontas por slug para resolução segura de links internos
    ready_slugs = {}
    ready_pages = []
    for p in all_pages:
        slug = p.get('slug')
        st = p.get('status') or status_map.get(slug, 'rascunho')
        if st == 'pronta':
            ready_slugs[slug] = p
            ready_pages.append(p)

    print(f"[*] Total de páginas encontradas: {len(all_pages)} (Prontas: {len(ready_pages)})")

    # 7. Renderiza cada página pronta
    for page in ready_pages:
        slug = page['slug']
        template_name = page.get('template', 'base.html')

        # Se template for nome puro como 'ponto.html' ou 'base.html'
        tpl_file = TEMPLATES_DIR / template_name
        if not tpl_file.exists():
            tpl_path = f"templates/{template_name}" if not template_name.startswith('templates/') else template_name
        else:
            tpl_path = f"templates/{template_name}"

        try:
            template = env.get_template(tpl_path)
        except Exception:
            # Fallback para base.html
            template = env.get_template('templates/base.html')

        # Canonical absoluto
        canonical_url = f"{dominio_base}/{slug}.html" if slug != "index" else f"{dominio_base}/"

        # Schema JSON-LD
        schema_json = build_schema_graph(page, config, canonical_url)

        # Correções específicas para esta página
        correcoes_pagina = [c for c in correcoes if c.get('slug') == slug]

        # Contexto de renderização
        context = {
            "base_url": "",
            "canonical_url": canonical_url,
            "site_nome": config.get('nome_site', 'Ribeirão Preto | Cidade Viva'),
            "titulo": page.get('titulo', ''),
            "descricao": page.get('descricao', ''),
            "keywords": page.get('keywords', ''),
            "h1": page.get('h1', page.get('titulo', '')),
            "autor_nome": page.get('autor', {}).get('nome', config.get('autor_padrao', {}).get('nome', 'Leonardo A. Macedo')),
            "autor_bio": page.get('autor', {}).get('bio', config.get('autor_padrao', {}).get('bio', '')),
            "autor_foto": page.get('autor', {}).get('foto', config.get('autor_padrao', {}).get('foto', '')),
            "revisor_nome": page.get('revisor', 'Leonardo A. Macedo'),
            "publicado_em": page.get('publicado', ''),
            "atualizado_em": page.get('atualizado', ''),
            "proxima_revisao": page.get('proxima_revisao', ''),
            "versao": config.get('versao', '1.0.0'),
            "email_contato": config.get('email_contato', 'infohausti@gmail.com'),
            "email_correcoes": config.get('email_correcoes', 'infohausti@gmail.com'),
            "fontes": page.get('fontes', []),
            "breadcrumbs": page.get('breadcrumbs', []),
            "schema_json": schema_json,
            "correcoes_pagina": correcoes_pagina,
            "active_nav": page.get('active_nav', ''),
            "secoes": page.get('secoes', {}),
            "ready_slugs": ready_slugs
        }

        # Adiciona campos específicos da página
        context.update(page)

        rendered_html = template.render(**context)
        rendered_html = resolve_internal_links(rendered_html, ready_slugs, DIST_DIR)

        # Define arquivo de saída
        if slug == "index":
            out_file = DIST_DIR / "index.html"
        else:
            out_file = DIST_DIR / f"{slug}.html"

        out_file.parent.mkdir(parents=True, exist_ok=True)
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

        print(f"[+] Renderizado: {out_file.relative_to(ROOT_DIR)}")

    # 8. Gera sitemap e índice de busca
    generate_sitemap(ready_pages, config)
    generate_search_index(ready_pages, config)

    print("\n[OK] Build concluído com sucesso!")
    return True

if __name__ == '__main__':
    main()
