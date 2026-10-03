#!/usr/bin/env python3
"""
AUDITORIA: check_similaridade.py
Executa análise de similaridade em DUAS PASSADAS (Regras 17, 89 e 90 do Manual v1.2)
1ª Passada: Somente texto narrativo (<p> e headings). Similaridade > 30% = FATAL.
2ª Passada: Inclui tabelas e listas de paradas. Similaridade > 30% = AVISO.
"""

import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / 'dist'

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    print("[ERRO] scikit-learn não instalado. Execute: pip install scikit-learn")
    sys.exit(1)

def extract_narrative_text(html_content):
    """Extrai somente parágrafos e títulos editoriais, excluindo cabeçalho, rodapé e listas/tabelas"""
    # Isola o <main>
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL | re.IGNORECASE)
    content = main_match.group(1) if main_match else html_content

    # Remove tabelas, listas e blocos de scripts
    content = re.sub(r'<table[^>]*>.*?</table>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ul[^>]*>.*?</ul>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ol[^>]*>.*?</ol>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', ' ', content, flags=re.DOTALL | re.IGNORECASE)

    # Extrai parágrafos e headings
    elements = re.findall(r'<(?:p|h[1-6])[^>]*>(.*?)</(?:p|h[1-6])>', content, flags=re.DOTALL | re.IGNORECASE)
    clean_texts = [re.sub(r'<[^>]+>', ' ', el).strip() for el in elements]
    return ' '.join(clean_texts)

def extract_full_content_text(html_content):
    """Extrai todo o texto dentro de <main> incluindo tabelas e listas"""
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL | re.IGNORECASE)
    content = main_match.group(1) if main_match else html_content
    content = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    return re.sub(r'<[^>]+>', ' ', content).strip()

def check_similaridade():
    fatals = []
    avisos = []

    if not DIST_DIR.exists():
        return ["[FATAL] Diretório dist/ não existe."], []

    html_files = [f for f in DIST_DIR.glob('**/*.html') if f.name != '404.html']
    if len(html_files) < 2:
        # Menos de 2 arquivos para comparar
        return [], ["[INFO] Menos de 2 páginas compiladas para cálculo de similaridade."]

    # Carrega textos
    narrative_corpus = []
    full_corpus = []
    file_names = []

    for f in html_files:
        html = f.read_text(encoding='utf-8')
        narrative_text = extract_narrative_text(html)
        full_text = extract_full_content_text(html)

        narrative_corpus.append(narrative_text)
        full_corpus.append(full_text)
        file_names.append(f.relative_to(ROOT_DIR))

    # --- 1ª PASSADA: Texto Narrativo (Fatal se > 30%) ---
    vectorizer_narrative = TfidfVectorizer(min_df=1, stop_words=None)
    try:
        tfidf_narrative = vectorizer_narrative.fit_transform(narrative_corpus)
        sim_matrix_narrative = cosine_similarity(tfidf_narrative)

        for i in range(len(file_names)):
            for j in range(i + 1, len(file_names)):
                sim = sim_matrix_narrative[i][j]
                if sim > 0.30:
                    fatals.append(
                        f"[PASSADA 1 - NARRATIVO] Similaridade alta ({sim:.1%}) entre '{file_names[i]}' e '{file_names[j]}'. Limite máximo: 30%."
                    )
    except ValueError as e:
        avisos.append(f"Passada 1: Corpus insuficiente para TF-IDF: {e}")

    # --- 2ª PASSADA: Inclui Tabelas e Listas de Paradas (Aviso se > 30%) ---
    vectorizer_full = TfidfVectorizer(min_df=1, stop_words=None)
    try:
        tfidf_full = vectorizer_full.fit_transform(full_corpus)
        sim_matrix_full = cosine_similarity(tfidf_full)

        for i in range(len(file_names)):
            for j in range(i + 1, len(file_names)):
                sim = sim_matrix_full[i][j]
                if sim > 0.30:
                    avisos.append(
                        f"[PASSADA 2 - TABELAS/LISTAS] Similaridade combinada ({sim:.1%}) entre '{file_names[i]}' e '{file_names[j]}' (Requer revisão humana)."
                    )
    except ValueError as e:
        avisos.append(f"Passada 2: Corpus insuficiente para TF-IDF: {e}")

    return fatals, avisos

def main():
    fatals, avisos = check_similaridade()
    for a in avisos:
        print(f"[AVISO] {a}")
    for f in fatals:
        print(f"[FATAL] {f}")

    if fatals:
        print(f"\n[ERRO] check_similaridade falhou com {len(fatals)} erro(s) fatal(is).")
        sys.exit(1)
    else:
        print(f"[OK] check_similaridade aprovado em ambas as passadas.")
        sys.exit(0)

if __name__ == '__main__':
    main()
