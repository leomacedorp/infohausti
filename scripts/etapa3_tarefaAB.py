#!/usr/bin/env python3
"""TAREFA A+B — Etapa 3: consolida invenções investigadas + verifica as 10
inclusões sugeridas (distância real <500m via haversine, coordenadas GTFS
das paradas da linha citante + geocode OSM dos endereços das instituições)."""
import json, re, time, urllib.request, urllib.parse, unicodedata
from pathlib import Path
from datetime import datetime
from math import radians, sin, cos, asin, sqrt

ROOT = Path(__file__).resolve().parent.parent
DADOS = ROOT / "content" / "dados-fonte"
REPORTS = ROOT / "reports"

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")

def haversine_m(a, b):
    la1, lo1, la2, lo2 = map(radians, [a[0], a[1], b[0], b[1]])
    h = sin((la2-la1)/2)**2 + cos(la1)*cos(la2)*sin((lo2-lo1)/2)**2
    return 2*6371000*asin(sqrt(h))

linhas = json.load(open(DADOS / "linhas.json", encoding="utf-8"))

def coords_linha(num):
    fonte = linhas.get(num) or linhas.get(num.zfill(3)) or next((linhas[k] for k in linhas if k.lstrip("0")==num.lstrip("0")), None)
    return [(p["lat"], p["lng"]) for p in fonte["paradas"]["valor"] if p.get("lat")]

def dist_min(num, alvo):
    ps = coords_linha(num)
    if not ps or not alvo: return None
    return min(haversine_m(p, alvo) for p in ps)

# geocode OSM (Nominatim) — 1 req/s
def geocode(q):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": q, "format": "json", "limit": 1, "countrycodes": "br"})
    req = urllib.request.Request(url, headers={"User-Agent": "InfohausRP-audit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        return (float(d[0]["lat"]), float(d[0]["lon"]), d[0]["display_name"]) if d else None
    except Exception as e:
        return None

rel = ["# ETAPA 3 — TAREFA A (invenções investigadas) + TAREFA B (10 inclusões, distância real)",
       f"Gerado: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]

# ---------------- TAREFA A ----------------
rel += ["## TAREFA A — AS 7 'INVENÇÕES' (verificadas individualmente)", ""]
A = [
 ("Fórum Estadual 'Doutor Faria Goyaz' (linha 130)",
  "REAL-COM-OUTRO-NOME", 
  "Fórum oficial: 'Desembargador João Alves Meira Júnior', Rua Alice Alem Saadi, 1010, Nova Ribeirânia. 'Faria Goyaz' não existe.",
  "https://cnbsp.org.br/wp-content/uploads/2025/05/Diario-Oficial-08-05-2025.pdf"),
 ("Núcleo Bancário Acadêmico Rocha Lima (linha 207)",
  "INEXISTENTE (fusão de referências reais)",
  "'Praça José Orlando Rocha Lima' é real (Vila Brasil, CEP 14075-539) mas é logradouro industrial, sem 'núcleo bancário'. A USP tem 'Cidade Universitária' em outro eixo. Nome composto fabricado.",
  "https://applocal.com.br/endereco/praca-jose-orlando-rocha-lima/ribeirao-preto/sp"),
 ("Paróquia São Geraldo Majella (linha 206)",
  "INEXISTENTE EM RP",
  "Não consta no catálogo da Arquidiocese de RP nem em buscas; paróquias homônimas existem em Fortaleza, Sorocaba, Santo André e Bálsamo-SP — nenhuma em Ribeirão Preto. Vila Virgínia (bairro da 206) tem paróquias próprias a verificar.",
  "https://arquidioceserp.org.br/paroquias"),
 ("Estação Brasil Expressa (linha 211)",
  "INEXISTENTE",
  "'Brasil Expressa' não é estação de RP. Os terminais reais: Terminal Urbano Central, Terminal Oeste (Francisco Luciano Lepera), Terminal Leste, Terminal Evangelina Passig, Terminal HC. Nenhuma fonte cita 'Brasil Expressa' como estação.",
  "https://www.rpmobilidade.com.br/prourbano/nossas-unidades/"),
 ("Terminal RibeirãoShopping (linhas 156/902)",
  "REAL-COM-OUTRO-NOME",
  "Existe ponto/terminal junto ao Ribeirão Shopping: protocolo Transerp 202204380 menciona 'TERMINAL DO BAIRRO SÃO JOSÉ, RIBEIRÃO SHOPPING'; Moovit registra 'Ponto Ônibus Ribeirão Shopping' (Av. José Adolfo Bianco Molina). Nome formal: Terminal São José / terminal do bairro São José.",
  "https://www.ribeiraopreto.sp.gov.br/portal/pdf/transerp1040202301.pdf"),
 ("Praça Rotary Club (linha 303)",
  "REAL",
  "Praça Rotary Club, City Ribeirão, CEP 14021-355.",
  "https://www.cepsdobrasil.com.br/cep/sp/ribeirao-preto/praca-rotary-club"),
 ("Parque Linear (linha 073)",
  "REAL-COM-OUTRO-NOME",
  "Parques lineais reais de RP: Parque Linear Ulysses Guimarães (Via Norte / Av. Eduardo Andrea Matarazzo, Lei 6709/1993 + notícia da gestão Dárcy Vera) e Parque Linear Retiro Saudoso Ministro Sérgio Motta (Viaduto Ayrton Senna–Av. Ianguerá). 'Parque Linear' genérico na 073 precisa do nome específico para ser validado.",
  "https://www.ribeiraopreto.sp.gov.br/portal/noticia/moradores-e-comerciantes-comemoram-construcao-do-parque-linear-da-via-norte"),
]
for nome, classe, nota, url in A:
    rel += [f"### {nome}", f"- **Classificação: {classe}**", f"- {nota}", f"- Fonte: {url}", ""]

# ---------------- TAREFA B ----------------
rel += ["## TAREFA B — 10 INCLUSÕES SUGERIDAS EM dados-fonte/pontos/ (com distância real à linha citante)", ""]
B = [
 ("hospital-electro-bonini", "Hospital Electro Bonini", "Av. Leão XIII, 1000, Ribeirânia", "004", "103", "https://cnes2.datasus.gov.br (CNES 3314766)"),
 ("santuario-nossa-senhora-do-rosario", "Santuário Nossa Senhora do Rosário", "Rua Tibiriçá, 879, Centro", "199", "299", "https://arquidioceserp.org.br/paroquias"),
 ("forum-des-joao-alves-meira-junior", "Fórum Des. João Alves Meira Júnior", "Rua Alice Alem Saadi, 1010, Nova Ribeirânia", "130", "103", "https://cnbsp.org.br/wp-content/uploads/2025/05/Diario-Oficial-08-05-2025.pdf"),
 ("terminal-evangelina-passig", "Terminal Evangelina Passig", "Terminal Urbano, zona norte (Av. Mouraria/Plant H)", "730", "730", "https://www.marcospapa.com.br/diligencia-mostra-frota-sucateada/"),
 ("terminal-oeste-francisco-luciano-lepera", "Terminal Oeste Francisco Luciano Lepera", "Av. Octávio Golfeto, 100, Jd. José Sampaio", "079", "079", "https://www.rpmobilidade.com.br/prourbano/nossas-unidades/"),
 ("terminal-hospital-das-clinicas", "Terminal Hospital das Clínicas", "Av. Prof. Hélio Lourenço, campus USP", "187", "207", "https://site.hcrp.usp.br/localizacaodirecoes/"),
 ("museu-de-anatomia-fmrp", "Museu de Anatomia (FMRP-USP)", "Prédio Central FMRP, Av. Bandeirantes, 3900, Monte Alegre", "187", "207", "https://jornal.usp.br/campus-ribeirao-preto/"),
 ("ceagesp-ribeirao-preto", "Entreposto CEAGESP Ribeirão Preto", "Av. Ceagesp, 1780", "053", "095", "https://ceagesp.gov.br/entrepostos/interior/ribeirao-preto/"),
 ("faculdade-reges", "Faculdade Reges Ribeirão Preto", "R. Dr. Benjamim Anderson Stauffer, 801, Jd. Botânico", "730", "730", "https://reges.com.br/ribeiraopreto/a-faculdade/"),
 ("faculdade-de-filosofia-ffclrp", "Faculdade de Filosofia FFCLRP-USP", "Av. Bandeirantes, 3900, Monte Alegre", "187", "207", "https://www.ffclrp.usp.br/"),
]
rel += ["| # | Ponto | Endereço | Linha citante | Dist. mín. real | <500m? | Fonte |",
        "|---|-------|-----------|---------------|-----------------|--------|-------|"]
resultados = []
for slug, nome, end, l1, l2, url in B:
    g = geocode(end + ", Ribeirão Preto, SP")
    if g:
        d1, d2 = dist_min(l1, g[:2]), dist_min(l2, g[:2])
        ok = (d1 is not None and d1 <= 500) or (d2 is not None and d2 <= 500)
        dist_txt = f"{min(x for x in [d1,d2] if x is not None):.0f}m (L{l1}: {d1:.0f}m, L{l2}: {d2:.0f}m)" if (d1 or d2) else "—"
        resultados.append((slug, nome, end, l1, l2, dist_txt, "SIM" if ok else "NÃO", url))
        rel.append(f"| {len(resultados)} | {nome} | {end} | {l1}/{l2} | {dist_txt} | {'✅ SIM' if ok else '❌ NÃO'} | {url} |")
    else:
        resultados.append((slug, nome, end, l1, l2, "geocode falhou", "?", url))
        rel.append(f"| — | {nome} | {end} | {l1}/{l2} | geocode falhou | ? | {url} |")
    time.sleep(1.1)

rel += ["", "## RECOMENDAÇÃO POR ITEM (para aprovação do Leo)", ""]
for i, (slug, nome, end, l1, l2, dist, ok, url) in enumerate(resultados, 1):
    if ok == "SIM":
        acao = "INCLUIR em dados-fonte/pontos/ (real e ≤500m da linha citante)"
    elif ok == "NÃO":
        acao = f"NÃO INCLUIR para a linha citante — real, mas a >500m ({dist}); citar apenas em páginas de linha que passem perto"
    else:
        acao = "INCLUIR com coordenada a obter manualmente (geocode falhou); distância a validar"
    rel.append(f"{i}. **{nome}** — {acao}. Fonte: {url}")

rel += ["", "---",
        "DECISÃO PENDENTE (Leo): aprovar inclusões? A ação 'INCLUIR' só grava o JSON em dados-fonte/pontos/ após OK explícito."]
out = REPORTS / "etapa3_tarefaAB_invencoes_e_inclusoes.md"
out.write_text("\n".join(rel), encoding="utf-8")
print("\n".join(rel))
print(f"\n[Gravado: {out}]")
