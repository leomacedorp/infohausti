#!/usr/bin/env python3
"""
check_qualidade_texto.py — Portão de qualidade editorial dos JSONs de conteúdo.

Bloqueia (FATAL) defeitos típicos de texto gerado por LLM "girando" conteúdo para
bater a métrica de similaridade:
- Caracteres CJK / alfabetos estranhos ao PT-BR
- Palavras estrangeiras e erros recorrentes (reflejam, shifts, ...)
- Moldes repetidos e floreios sem fonte ("opera sob a perspectiva", "cordão umbilical", ...)
- Termos proibidos pela política de nomes reais ("condução" como sinônimo de ônibus, etc.)
- <strong> fora de <p> e falta de espaço antes de <strong>
- Seções narrativas de páginas de linha abaixo do mínimo de caracteres

Uso: python scripts/check_qualidade_texto.py [arquivo.json ...]
Sem argumentos, varre content/paginas/**/*.json.
"""
import json
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / 'content' / 'paginas'

MIN_CHARS_SECOES_LINHA = 3000

# Alfabetos que nunca devem aparecer em texto PT-BR
RE_ALFABETO_ESTRANHO = re.compile(r'[\u0400-\u04FF\u0590-\u06FF\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF]')

# (termo, motivo) — busca case-insensitive por palavra/expressão
TERMOS_PROIBIDOS = [
    ("condução", "sinônimo artificial de ônibus/veículo (política de nomes reais)"),
    ("reflejam", "espanhol"),
    ("shifts", "inglês"),
    ("diferenza", "italiano/erro"),
    ("boto de", "erro de geração"),
    ("opera sob a perspectiva", "molde repetido entre páginas"),
    ("cordão umbilical", "floreio sem fonte"),
    ("estudo fascinante", "floreio sem fonte"),
    ("estudo de caso sobre como", "floreio sem fonte"),
    ("ecossistema de produção", "floreio sem fonte"),
    ("corrente humana", "floreio sem fonte"),
    ("centros de troca técnica", "afirmação sem fonte"),
    ("sistema de capacitação contínua", "afirmação sem fonte"),
    ("fábrica ambulante", "floreio sem fonte"),
    ("artéria industrial", "floreio sem fonte"),
    ("bairro ferroviário ocidental", "sinônimo artificial (política de nomes reais)"),
    ("alameda da mogiana", "nome inventado"),
    ("complexo ambulatorial", "sinônimo artificial (política de nomes reais)"),
]

RE_STRONG_FORA_P = re.compile(r'(^|</p>)\s*<strong>[^<]*</strong>\s*<p>')
RE_SEM_ESPACO_STRONG = re.compile(r'[A-Za-zÀ-ÿ0-9,]<strong>')


def iter_textos(obj, caminho=''):
    """Percorre recursivamente todas as strings do JSON, devolvendo (caminho, texto)."""
    if isinstance(obj, str):
        yield caminho, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ('slug', 'url', 'template', 'linha_cor'):
                continue
            yield from iter_textos(v, f'{caminho}.{k}' if caminho else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from iter_textos(v, f'{caminho}[{i}]')


def checar_arquivo(path):
    fatals = []
    rel = path.relative_to(ROOT_DIR) if path.is_absolute() else path
    try:
        dados = json.loads(path.read_text(encoding='utf-8'))
    except ValueError as e:
        return [f"[QUALIDADE] JSON inválido em '{rel}': {e}"]

    for campo, texto in iter_textos(dados):
        if RE_ALFABETO_ESTRANHO.search(texto):
            trecho = RE_ALFABETO_ESTRANHO.search(texto).group(0)
            fatals.append(f"[QUALIDADE] Caractere estranho ao PT-BR ('{trecho}') em '{rel}' campo {campo}.")
        baixo = texto.lower()
        for termo, motivo in TERMOS_PROIBIDOS:
            if termo in baixo:
                fatals.append(f"[QUALIDADE] Termo proibido '{termo}' ({motivo}) em '{rel}' campo {campo}.")
        if RE_STRONG_FORA_P.search(texto):
            fatals.append(f"[QUALIDADE] <strong> usado como rótulo fora de <p> em '{rel}' campo {campo}.")
        if RE_SEM_ESPACO_STRONG.search(texto):
            fatals.append(f"[QUALIDADE] Falta espaço antes de <strong> em '{rel}' campo {campo}.")

    if dados.get('template') == 'linha.html' and isinstance(dados.get('secoes'), dict):
        total = sum(len(v) for v in dados['secoes'].values() if isinstance(v, str))
        if total < MIN_CHARS_SECOES_LINHA:
            fatals.append(f"[AVISO-TAMANHO] Seções narrativas curtas em '{rel}': {total} caracteres (mínimo {MIN_CHARS_SECOES_LINHA}).")
    return fatals


def check_qualidade_texto(arquivos=None):
    """Interface compatível com audit_all: retorna (fatals, avisos)."""
    if arquivos:
        paths = [Path(a).resolve() for a in arquivos]
    else:
        paths = sorted(CONTENT_DIR.glob('**/*.json'))
    fatals, avisos = [], [f"[INFO] {len(paths)} arquivo(s) de conteúdo verificados."]
    for p in paths:
        for msg in checar_arquivo(p):
            (avisos if msg.startswith("[AVISO-TAMANHO]") else fatals).append(msg)
    return fatals, avisos


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    fatals, avisos = check_qualidade_texto(sys.argv[1:])
    for a in avisos:
        print(a)
    for f in fatals:
        print(f)
    if fatals:
        print(f"\n[ERRO] check_qualidade_texto falhou com {len(fatals)} erro(s).")
        sys.exit(1)
    print("\n[OK] Qualidade de texto aprovada.")


if __name__ == '__main__':
    main()
