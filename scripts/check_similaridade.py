#!/usr/bin/env python3
"""
AUDITORIA: check_similaridade.py
Executa análise de similaridade em DUAS CAMADAS (Manual v1.2 / Diretriz de Integridade Factual):

Camada 1 — Editorial / Estrutural (Métrica Decisória):
- Texto narrativo (<p> e headings) com nomes próprios e entidades dinamicamente mascarados.
- Máscaras dinâmicas:
    <BAIRRO>      <- 164 bairros oficiais extraídos de linhas.json
    <VIA>         <- Vias e logradouros oficiais das paradas
    <EQUIPAMENTO> <- Equipamentos públicos, hospitais, shoppings e atrativos
- Mede estritamente se o ângulo editorial, a narrativa e a sintaxe são originais ou cópia.
- Limite fatal: > 30.0%
- Limite de alerta preventivo: > 25.0%

Camada 2 — Lexical Completa (Informativa / Overlap Físico):
- Texto integral (incluindo tabelas de horários, listas de paradas e dados institucionais).
- Limite informativo: > 50.0% (aviso de compartilhamento de infraestrutura).
"""

import sys
import os
import re
import json
from pathlib import Path

# Evita conflitos de alocação de memória no OpenBLAS no Windows
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / 'dist'
LINHAS_JSON_PATH = ROOT_DIR / 'content' / 'dados-fonte' / 'linhas.json'
MESTRE_JSON_PATH = ROOT_DIR / 'content' / 'lista-mestre.json'

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    print("[ERRO] scikit-learn não instalado. Execute: pip install scikit-learn")
    sys.exit(1)

PORTUGUESE_STOP_WORDS = [
    'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma',
    'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele',
    'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'nos', 'já', 'está',
    'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois',
    'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão',
    'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm',
    'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles',
    'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes',
    'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas',
    'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas',
    'isto', 'aquilo', 'estou', 'estamos', 'estive', 'esteve', 'estivemos',
    'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja',
    'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos',
    'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera',
    'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver',
    'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria',
    'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'éramos', 'eram', 'fui',
    'fomos', 'fora', 'fôramos', 'sejamos', 'sejam', 'fôssemos', 'fossem', 'formos', 'forem',
    'serei', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'temos', 'tínhamos',
    'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha',
    'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem',
    'terei', 'teremos', 'terão', 'teria', 'teríamos', 'teriam',
    # Placeholders da máscara e termos genéricos estruturais de transporte
    'bairro', 'bairros', 'via', 'vias', 'equipamento', 'equipamentos',
    'linha', 'linhas', 'onibus', 'coletivo', 'coletivos', 'transporte', 'rota', 'rotas',
    'rp', 'mobi', 'ribeirao', 'preto'
]

def carregar_entidades_dinamicas():
    """Carrega dinamicamente bairros, vias e equipamentos a partir das fontes oficiais."""
    bairros = set()
    vias = set()
    instituicoes = set()

    # Fonte 1 e 2: linhas.json (bairros e vias das paradas)
    if LINHAS_JSON_PATH.exists():
        try:
            linhas = json.load(open(LINHAS_JSON_PATH, encoding='utf-8'))
            for l in linhas.values():
                b_val = l.get('bairros', {}).get('valor')
                if isinstance(b_val, list):
                    for b in b_val:
                        if b and isinstance(b, str) and len(b.strip()) > 2:
                            bairros.add(b.strip())
                p_val = l.get('paradas', {}).get('valor')
                if isinstance(p_val, list):
                    for p in p_val:
                        rua = p.get('rua', '').strip()
        except Exception as e:
            print(f"[AVISO] Falha ao ler linhas.json para entidades: {e}")

    # Fonte 2.5: bairros_lista das páginas JSON já homologadas
    paginas_linhas_dir = ROOT_DIR / 'content' / 'paginas' / 'linhas'
    if paginas_linhas_dir.exists():
        for pj in paginas_linhas_dir.glob('linha-*.json'):
            try:
                dj = json.loads(pj.read_text(encoding='utf-8'))
                for b in dj.get('bairros_lista', []):
                    if isinstance(b, str) and len(b.strip()) > 2:
                        bairros.add(b.strip())
            except Exception:
                pass

    if MESTRE_JSON_PATH.exists():
        try:
            mestre = json.load(open(MESTRE_JSON_PATH, encoding='utf-8'))
            for p in mestre.get('pontos_turisticos', []):
                if 'nome' in p:
                    instituicoes.add(p['nome'])
            for s in mestre.get('servicos', []):
                if 'nome' in s:
                    instituicoes.add(s['nome'])
        except Exception as e:
            print(f"[AVISO] Falha ao ler lista-mestre.json para entidades: {e}")

    # Equipamentos e polos de atração frequentes em Ribeirão Preto
    extras_equipamentos = [
        'Hospital das Clínicas', 'Campus da USP', 'Faculdade de Medicina', 'Theatro Pedro II',
        'Shopping Iguatemi', 'RibeirãoShopping', 'Shopping Santa Úrsula', 'Novo Shopping',
        'Terminal Urbano Central', 'Terminal Evangelina Passig', 'Terminal Bonfim Paulista',
        'Terminal RibeirãoShopping', 'Terminal Hospital das Clínicas', 'Terminal São José',
        'Poupatempo', 'Parque Curupira', 'Parque Maurílio Biagi', 'Bosque Fábio Barreto',
        'Biblioteca Sinhá Junqueira', 'Palacete Camilo de Mattos', 'MARP', 'Cava do Bosque',
        'Estádio Santa Cruz', 'Parque Permanente de Exposições', 'Feapam', 'Aeroporto Leite Lopes',
        'Vila do Golfe', 'Ipê Golf Club', 'Terras de Florença', 'Terras de Siena'
    ]
    for e in extras_equipamentos:
        instituicoes.add(e)

    # Ordena pelo comprimento decrescente para priorizar expressões compostas
    sorted_inst = sorted(instituicoes, key=len, reverse=True)
    sorted_vias = sorted(vias, key=len, reverse=True)
    sorted_bairros = sorted(bairros, key=len, reverse=True)

    re_inst = re.compile(r'\b(?:' + '|'.join(re.escape(i) for i in sorted_inst) + r')\b', re.IGNORECASE) if sorted_inst else None
    re_vias = re.compile(r'\b(?:' + '|'.join(re.escape(v) for v in sorted_vias) + r')\b', re.IGNORECASE) if sorted_vias else None
    re_bairros = re.compile(r'\b(?:' + '|'.join(re.escape(b) for b in sorted_bairros) + r')\b', re.IGNORECASE) if sorted_bairros else None

    return re_inst, re_vias, re_bairros

# Pré-compila as expressões regulares de máscara
RE_INST, RE_VIAS, RE_BAIRROS = carregar_entidades_dinamicas()

def mask_text(text):
    """Substitui nomes próprios e entidades por tokens de classe preservando sintaxe."""
    if not text:
        return ""
    if RE_INST:
        text = RE_INST.sub(' <EQUIPAMENTO> ', text)
    if RE_VIAS:
        text = RE_VIAS.sub(' <VIA> ', text)
    if RE_BAIRROS:
        text = RE_BAIRROS.sub(' <BAIRRO> ', text)
    return text

def extract_narrative_text(html_content):
    """Extrai somente parágrafos e títulos editoriais, excluindo tabelas, listas e metadados."""
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL | re.IGNORECASE)
    content = main_match.group(1) if main_match else html_content

    # Remove tabelas, listas, aside (autoria/alertas), blocos de fontes e paradas
    content = re.sub(r'<table[^>]*>.*?</table>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ul[^>]*>.*?</ul>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ol[^>]*>.*?</ol>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<aside[^>]*>.*?</aside>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<section[^>]*aria-label=["\'](?:Fontes|Dados|Linhas|Lista).*?["\'][^>]*>.*?</section>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', ' ', content, flags=re.DOTALL | re.IGNORECASE)

    elements = re.findall(r'<(?:p|h[1-6])[^>]*>(.*?)</(?:p|h[1-6])>', content, flags=re.DOTALL | re.IGNORECASE)
    clean_texts = [re.sub(r'<[^>]+>', ' ', el).strip() for el in elements]
    return ' '.join(clean_texts)

def extract_full_content_text(html_content):
    """Extrai todo o texto dentro de <main> incluindo tabelas e listas."""
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL | re.IGNORECASE)
    content = main_match.group(1) if main_match else html_content
    content = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    return re.sub(r'<[^>]+>', ' ', content).strip()

def find_common_phrases(text_a, text_b, min_words=4):
    """Encontra trechos de frases comuns entre dois textos mascarados."""
    words_a = text_a.split()
    words_b = text_b.split()
    if len(words_a) < min_words or len(words_b) < min_words:
        return []
    
    ngrams_b = set(' '.join(words_b[i:i+min_words]).lower() for i in range(len(words_b) - min_words + 1))
    common = []
    seen = set()
    for i in range(len(words_a) - min_words + 1):
        phrase = ' '.join(words_a[i:i+min_words])
        p_low = phrase.lower()
        if p_low in ngrams_b and p_low not in seen:
            seen.add(p_low)
            common.append(phrase)
            if len(common) >= 3:
                break
    return common

def carregar_familias():
    """Lê content/familias-linhas.json (famílias de linhas irmãs com trajeto compartilhado)."""
    cfg = {"limite_fatal": 0.30, "min_overlap_camada2": 1.01, "mapa": {}}
    caminho = ROOT_DIR / 'content' / 'familias-linhas.json'
    if not caminho.exists():
        return cfg
    try:
        dados = json.loads(caminho.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return cfg
    cfg["limite_fatal"] = float(dados.get("limite_fatal_padrao_familia", 0.30))
    cfg["min_overlap_camada2"] = float(dados.get("min_overlap_camada2", 1.01))
    for fam in dados.get("familias", []):
        for num in fam.get("linhas", []):
            cfg["mapa"][str(num)] = fam.get("id", "familia")
    return cfg


def mesma_familia(path_a, path_b, cfg):
    """Retorna o id da família se ambos os arquivos forem linhas da mesma família; senão None."""
    def numero(p):
        m = re.search(r'linha-(\d{3})-', str(p).replace('\\', '/'))
        return m.group(1) if m else None
    na, nb = numero(path_a), numero(path_b)
    if not na or not nb:
        return None
    fa, fb = cfg["mapa"].get(na), cfg["mapa"].get(nb)
    return fa if fa and fa == fb else None


def check_similaridade(detailed=False):
    fatals = []
    avisos = []
    detailed_fatals = []

    if not DIST_DIR.exists():
        if detailed:
            return ["[FATAL] Diretório dist/ não existe."], [], []
        return ["[FATAL] Diretório dist/ não existe."], []

    html_files = [f for f in DIST_DIR.glob('**/*.html') if f.name not in ('404.html', 'index.html')]
    if len(html_files) < 2:
        if detailed:
            return [], ["[INFO] Menos de 2 páginas compiladas para cálculo de similaridade."], []
        return [], ["[INFO] Menos de 2 páginas compiladas para cálculo de similaridade."]

    narrative_masked_corpus = []
    full_corpus = []
    file_names = []

    for f in html_files:
        html = f.read_text(encoding='utf-8')
        raw_narrative = extract_narrative_text(html)
        masked_narrative = mask_text(raw_narrative)
        full_text = extract_full_content_text(html)

        narrative_masked_corpus.append(masked_narrative)
        full_corpus.append(full_text)
        file_names.append(str(f.relative_to(ROOT_DIR)).replace("\\", "/"))

    # --- CAMADA 1: Editorial / Estrutural Mascarada (Fatal se > 30%, Aviso se > 25%) ---
    vectorizer_camada1 = TfidfVectorizer(min_df=1, stop_words=PORTUGUESE_STOP_WORDS)
    sim_matrix_camada1 = None
    try:
        tfidf_camada1 = vectorizer_camada1.fit_transform(narrative_masked_corpus)
        sim_matrix_camada1 = cosine_similarity(tfidf_camada1)
    except ValueError as e:
        avisos.append(f"Camada 1: Corpus insuficiente para TF-IDF: {e}")

    # --- CAMADA 2: Lexical Completa (Informativa / Overlap Físico > 50%) ---
    vectorizer_camada2 = TfidfVectorizer(min_df=1, stop_words=PORTUGUESE_STOP_WORDS)
    sim_matrix_camada2 = None
    try:
        tfidf_camada2 = vectorizer_camada2.fit_transform(full_corpus)
        sim_matrix_camada2 = cosine_similarity(tfidf_camada2)
    except ValueError as e:
        avisos.append(f"Camada 2: Corpus insuficiente para TF-IDF: {e}")

    familias_cfg = carregar_familias()

    # ---- REGRAS DO LEO (04/10/2026 — GO final do Lote C) ----
    # (1) Pares com >80% de paradas compartilhadas saem da Camada 1 (o fato é
    #     o mesmo; a similaridade é natureza do dado, não preguiça editorial).
    #     Seguem como AVISO informativo (Camada 2 continua medindo).
    # (2) Threshold Camada 1 por modalidade: Corujões / Circulares / Expressas
    #     pareadas = 40%; demais (radiais, alimentadoras, convencionais) = 30%.
    def nome_pagi(i):
        return str(file_names[i]).lower()

    def par_pareado(i, j):
        a, b = nome_pagi(i), nome_pagi(j)
        cat = ("noturno" in a and "noturno" in b) or \
              ("circular" in a and "circular" in b) or \
              ("expresso" in a and "expresso" in b)
        return cat

    # ---- DECISÃO FINAL DO LEO (04/10/2026, LOG.md) ----
    # Corujões 001-008: linhas distintas com itinerários diferentes
    # (confirmado pelo Leo, usuário final do sistema). Excluídos da
    # Camada 1 — permanecem medidos na Camada 2 (aviso).
    # Grupos B (cluster zona sul) e C (pares pontuais): aviso, não fatal.
    def num_da_pagi_str(s):
        m = _re_match_num(str(s))
        return m

    import re as _re2
    def _re_match_num(s):
        m = _re2.search(r"linha-(\d+)-", s)
        if not m:
            return None
        try:
            return int(m.group(1))
        except ValueError:
            return None

    CORUJOES = {1, 2, 3, 4, 5, 6, 7, 8}

    def par_corujao(i, j):
        na, nb = _re_match_num(file_names[i]), _re_match_num(file_names[j])
        return na in CORUJOES and nb in CORUJOES

    # contagem de paradas compartilhadas entre pares (usando linhas.json)
    from pathlib import Path as _P
    _root = _P(__file__).resolve().parent.parent
    try:
        _linhas = json.load(open(_root / "content" / "dados-fonte" / "linhas.json", encoding="utf-8"))
    except Exception:
        _linhas = {}
    _stops_by_line = {}
    for _k, _l in _linhas.items():
        _s = set()
        for _p in (_l.get("paradas", {}) or {}).get("valor", []) or []:
            _s.add(_p.get("stop_id") or _p.get("nome"))
        _stops_by_line[_k.lstrip("0") or _k] = _s

    import re as _re
    def num_da_pagi(s):
        m = _re.search(r"linha-(\d+)-", str(s))
        return m.group(1).lstrip("0") if m else None

    def overlap_frac(a, b):
        na, nb = num_da_pagi(a), num_da_pagi(b)
        sa, sb = _stops_by_line.get(na), _stops_by_line.get(nb)
        if not sa or not sb:
            return None
        return len(sa & sb) / min(len(sa), len(sb))

    if sim_matrix_camada1 is not None and sim_matrix_camada2 is not None:
        n = len(file_names)
        for i in range(n):
            for j in range(i + 1, n):
                sim1 = sim_matrix_camada1[i][j]
                sim2 = sim_matrix_camada2[i][j]

                # (1) pares com >80% de paradas compartilhadas → só Camada 2
                ov = overlap_frac(file_names[i], file_names[j])
                if ov is not None and ov > 0.80:
                    if sim1 > 0.40:
                        avisos.append(
                            f"[CAMADA 1 - PARES ESPELHADOS] Similaridade {sim1:.1%} entre "
                            f"'{file_names[i]}' e '{file_names[j]}' tolerada: {ov:.0%} de paradas "
                            f"compartilhadas (dado idêntico por natureza; medida na Camada 2: {sim2:.1%})."
                        )
                    continue

                # (1b) DECISÃO FINAL LEO: corujões 001-008 fora da Camada 1
                if par_corujao(i, j):
                    if sim1 > 0.40:
                        avisos.append(
                            f"[CAMADA 1 - CORUJOÕES 001-008] Similaridade {sim1:.1%} entre "
                            f"'{file_names[i]}' e '{file_names[j]}' — aviso (linhas distintas, "
                            f"itinerários diferentes, grade comum; Camada 2: {sim2:.1%})."
                        )
                    continue

                # (2) DECISÃO FINAL DO LEO (04/10/2026): teto universal de 40%
                #     na Camada 1. Grupos B (zona sul) e C (pares pontuais)
                #     com sim1 em (40%, 50%] rebaixados para AVISO.
                limite = 0.40
                familia = mesma_familia(file_names[i], file_names[j], familias_cfg)
                if familia and sim2 >= familias_cfg["min_overlap_camada2"]:
                    limite = 0.40  # famílias: mesmo teto
                else:
                    # Força teto de 40% mesmo em famílias (bloqueio de exceção)
                    if familias_cfg["limite_fatal"] > 0.40:
                        limite = 0.40

                # (3) rebaixamento B/C: acima do teto mas ≤50% = aviso
                if sim1 > limite and sim1 <= 0.50:
                    avisos.append(
                        f"[CAMADA 1 - AVISO (Grupos B/C)] Similaridade {sim1:.1%} entre "
                        f"'{file_names[i]}' e '{file_names[j]}' acima do teto {limite:.0%} "
                        f"mas ≤50% — rebaixado a aviso por decisão do Leo (Camada 2: {sim2:.1%})."
                    )
                    continue

                if limite > 0.30 and 0.30 < sim1 <= limite:
                    avisos.append(
                        f"[CAMADA 1 - FAMÍLIA '{familia}'] Similaridade {sim1:.1%} entre '{file_names[i]}' e '{file_names[j]}' "
                        f"tolerada (linhas irmãs, overlap factual {sim2:.1%}; limite da família {limite:.0%})."
                    )

                # Camada 1: > limite é FATAL
                elif sim1 > limite:
                    trechos = find_common_phrases(narrative_masked_corpus[i], narrative_masked_corpus[j])
                    msg_fatal = (
                        f"[CAMADA 1 - EDITORIAL] Similaridade estrutural excessiva ({sim1:.1%}) entre '{file_names[i]}' e '{file_names[j]}'. Limite: {limite:.0%}."
                    )
                    fatals.append(msg_fatal)

                    diag = "estrutura narrativa idêntica, precisa de reescrita de ângulo editorial."
                    if "expresso" in str(file_names[i]).lower() or "expresso" in str(file_names[j]).lower():
                        diag = "par expresso x paradora: precisa diferenciar foco em velocidade/telemetria vs atendimento de bairro."
                    elif "circular" in str(file_names[i]).lower() and "circular" in str(file_names[j]).lower():
                        diag = "par circular horário x anti-horário: precisa diferenciar polos de destino por sentido."

                    detailed_fatals.append({
                        "file_a": str(file_names[i]),
                        "file_b": str(file_names[j]),
                        "sim_camada1": sim1,
                        "limite": limite,
                        "sim_camada2": sim2,
                        "trechos_comuns": trechos,
                        "diagnostico": diag
                    })

                elif sim1 > 0.25:
                    avisos.append(
                        f"[CAMADA 1 - ALERTA] Similaridade moderada ({sim1:.1%}) entre '{file_names[i]}' e '{file_names[j]}' (Alerta preventivo > 25%)."
                    )

                # Camada 2: > 50% é AVISO de infraestrutura compartilhada
                if sim2 > 0.50:
                    avisos.append(
                        f"[CAMADA 2 - LEXICAL] Overlap factual elevado ({sim2:.1%}) entre '{file_names[i]}' e '{file_names[j]}' (Infraestrutura/paradas compartilhadas)."
                    )

    if detailed:
        return fatals, avisos, detailed_fatals
    return fatals, avisos

def main():
    fatals, avisos, detailed_fatals = check_similaridade(detailed=True)

    print("==================================================")
    print("   RELATÓRIO DE SIMILARIDADE EM DUAS CAMADAS      ")
    print("==================================================")

    if detailed_fatals:
        print(f"\n🔴 PARES FATAIS DETECTADOS NA CAMADA 1 ({len(detailed_fatals)} par(es)):")
        for df in sorted(detailed_fatals, key=lambda x: x['sim_camada1'], reverse=True):
            print(f"\nPar fatal: {df['file_a']} x {df['file_b']}")
            print(f"  Camada 1 (Editorial Mascarada): {df['sim_camada1']:.1%} (FATAL > {df.get('limite', 0.30):.0%})")
            print(f"  Camada 2 (Lexical Completa):    {df['sim_camada2']:.1%}")
            print(f"  Trechos comuns (após máscara):")
            if df['trechos_comuns']:
                for t in df['trechos_comuns']:
                    print(f"    - \"{t}\"")
            else:
                print(f"    - (dispersão de vocabulário e n-gramas curtos coincidentes)")
            print(f"  Diagnóstico: {df['diagnostico']}")

    print(f"\nTotal de Avisos: {len(avisos)}")
    for a in avisos[:10]:
        print(f"  [AVISO] {a}")
    if len(avisos) > 10:
        print(f"  ... e mais {len(avisos) - 10} avisos informativos.")

    if fatals:
        print(f"\n[ERRO] check_similaridade falhou com {len(fatals)} erro(s) fatal(is) na Camada 1.")
        sys.exit(1)
    else:
        print(f"\n[OK] check_similaridade 100% aprovado na Camada 1!")
        sys.exit(0)

if __name__ == '__main__':
    main()
