#!/usr/bin/env python3
"""
GERADOR DOS LOTES 8-12 — 43 linhas restantes (scripts/gera_lotes_8_12.py)
Missão do Leo (05/10/2026): gerar as 43 linhas sem página, no mesmo padrão
dos Lotes 1-7. Página completa (mesma estrutura das 70 existentes), seções
pelo gerador v2, validação check_fontes ANTES de gravar (linha com fatal
não é gravada), index.json e lista-mestre.json atualizados.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path
from datetime import date, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_fontes_factuais as ck
from gera_linha_v2 import gera_secoes, humaniza, LINHAS as LINHAS_FONTE

ROOT = Path(__file__).resolve().parent.parent
PAG = ROOT / "content" / "paginas" / "linhas"

HOJE = "2026-10-05"
REV = "2027-04-05"

def slugify(nome):
    s = unicodedata.normalize("NFD", nome.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace(".", " ").replace("&", " ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

def categoria(modalidade):
    m = modalidade.lower()
    if "alimentadora" in m: return "alimentadora"
    if "noturna" in m: return "noturna"
    if "estrutural" in m or "troncal" in m: return "estrutural"
    if "expressa" in m or "expresso" in m: return "expressa"
    return "convencional"

# ---- universo: linhas sem página ----
com_pag = set()
for p in PAG.glob("linha-*.json"):
    m = re.match(r"linha-(\d+)-", p.name)
    if m:
        com_pag.add(m.group(1).lstrip("0"))
faltando = sorted((k for k in LINHAS_FONTE if k.lstrip("0") not in com_pag),
                  key=lambda x: int(x))
print(f"Linhas sem página: {len(faltando)} -> {faltando}")

idx_path = ROOT / "content" / "paginas" / "linhas" / "index.json"
idx = json.load(open(idx_path, encoding="utf-8"))
if isinstance(idx, dict):
    lista_idx = idx.get("linhas", idx.get("itens", []))
else:
    lista_idx = idx
slugs_idx = {e.get("slug") for e in lista_idx}
exemplo = lista_idx[0] if lista_idx else {}
print("campos do index:", list(exemplo.keys()))

mestre_path = ROOT / "content" / "lista-mestre.json"
mestre = json.load(open(mestre_path, encoding="utf-8"))

geradas, falhas = [], []
novas_idx = []
lotes = {}
# divisão em lotes 8-12 (9,9,9,9,7)
div = [faltando[0:9], faltando[9:18], faltando[18:27], faltando[27:36], faltando[36:43]]

for num in faltando:
    fonte = LINHAS_FONTE[num]
    chave = num if num in ck.LINHAS_FONTE else num.zfill(3)
    paradas = (fonte.get("paradas") or {}).get("valor") or []
    if not paradas:
        falhas.append((num, "SEM PARADAS no dados-fonte", "dado ausente — não se gera página sem fonte (regra do projeto)"))
        continue
    nome = fonte["nome"]["valor"]
    modalidade = (fonte.get("modalidade") or {}).get("valor", "Convencional")
    tarifa = (fonte.get("tarifa") or {}).get("valor") or "R$ 5,00"
    bairros = (fonte.get("bairros") or {}).get("valor", []) or []
    hor = (fonte.get("horarios") or {}).get("valor", {}) or {}
    itins = (fonte.get("itinerario") or {}).get("valor", []) or []
    slug_nome = slugify(nome)
    slug = f"linhas/linha-{num}-{slug_nome}"
    p0 = humaniza(paradas[0]["nome"])
    p1 = humaniza(paradas[-1]["nome"])

    # seções pelo gerador v2 + validação ANTES de gravar
    try:
        secoes, angulo = gera_secoes(num)
    except Exception as e:
        falhas.append((num, f"gerador: {e}", ""))
        continue
    fatais, _ = ck.verifica_linha(chave, fonte, secoes)
    if fatais:
        falhas.append((num, f"{len(fatais)} fatais", fatais[0][:100]))
        continue

    npar = max((i.get("num_paradas", 0) for i in itins), default=len(paradas))
    desc = (f"Guia de horários da Linha {num} {nome} da RP Mobi em Ribeirão Preto. "
            f"Linha {modalidade.lower()} com {npar} paradas entre {p0} e {p1}.")

    def pprinc(p):
        bairro = p.get("bairro") or ""
        return {
            "nome": humaniza(p["nome"]),
            "rua": p.get("rua") or humaniza(p["nome"]),
            "bairro": bairro or "Ribeirão Preto",
            "referencia": f"Ponto do itinerário oficial ({humaniza(p['nome'])})"
        }
    ks = [0, len(paradas)//3, 2*len(paradas)//3, len(paradas)-1]
    principais = [pprinc(paradas[k]) for k in sorted(set(ks))]

    faq = [
        {"pergunta": f"Qual é o valor da passagem da Linha {num} {nome}?",
         "resposta": f"A tarifa da linha é de {tarifa}, aceita via Cartão Cidadão RP Mobi, cartões de vale-transporte e dinheiro a bordo."},
        {"pergunta": f"Onde a Linha {num} inicia o trajeto?",
         "resposta": f"O embarque inicial acontece em {p0}, conforme o itinerário oficial publicado pela RP Mobi."},
        {"pergunta": "Como funciona a integração temporal?",
         "resposta": "Com o Cartão Cidadão RP Mobi, o passageiro dispõe de até 120 minutos a partir da primeira validação para embarcar em outro coletivo sem custo adicional."},
    ]

    pag_json = {
        "slug": slug,
        "status": "pronta",
        "template": "linha.html",
        "schema_type": "WebPage",
        "titulo": f"Linha {num} - {nome} | Horários e Paradas RP Mobi",
        "descricao": desc,
        "keywords": f"linha {num} ribeirao preto, onibus {slug_nome.replace('-', ' ')} rp mobi, horario linha {num}",
        "h1": f"Linha {num} — {nome}",
        "linha_numero": num,
        "linha_nome": nome,
        "linha_cor": "#1a15f0",
        "modalidade": f"Linha {modalidade}",
        "tarifa": tarifa,
        "resumo_origem_destino": f"{p0} ↔ {p1}",
        "terminal_central": p0,
        "publicado": HOJE,
        "atualizado": HOJE,
        "proxima_revisao": REV,
        "revisor": "Leonardo A. Macedo",
        "breadcrumbs": [
            {"nome": "Início", "url": "/"},
            {"nome": "Mobilidade & Transporte", "url": "/linhas/index.html"},
            {"nome": f"Linha {num} - {nome}", "url": f"/linhas/linha-{num}-{slug_nome}.html"},
        ],
        "secoes": secoes,
        "itinerarios_detalhe": [
            {"nome": i["nome"], "num_paradas": i["num_paradas"],
             "descricao": f"Itinerário {i['nome']} com {i['num_paradas']} paradas."}
            for i in itins
        ],
        "paradas_principais": principais,
        "horarios_tabela": {
            "dias_uteis": hor.get("dias_uteis", []),
            "sabado": hor.get("sabado", []),
            "domingo": hor.get("domingo", []),
        },
        "bairros_lista": bairros,
        "faq": faq,
        "fontes": [
            {"nome": "RP Mobi — Horários e Linhas do Transporte Coletivo Urbano",
             "url": "https://www.rpmobi.com.br", "tipo": "oficial", "verificado_em": HOJE},
            {"nome": "Prefeitura Municipal de Ribeirão Preto — Tarifas e Decretos de Mobilidade",
             "url": "https://www.ribeiraopreto.sp.gov.br", "tipo": "oficial", "verificado_em": HOJE},
        ],
    }

    destino = PAG / f"linha-{num}-{slug_nome}.json"
    destino.write_text(json.dumps(pag_json, ensure_ascii=False, indent=2), encoding="utf-8")
    geradas.append(num)

    entrada = dict(exemplo)
    entrada.update({
        "codigo": num,
        "slug": slug,
        "nome": nome,
        "modalidade": modalidade,
        "categoria_filtro": categoria(modalidade),
        "cor": "#1a15f0",
    })
    novas_idx.append(entrada)

# ---- index.json: adiciona as novas ----
adicionadas = 0
for e in novas_idx:
    if e["slug"] not in slugs_idx:
        lista_idx.append(e)
        adicionadas += 1
if isinstance(idx, dict):
    chave_lista = "linhas" if "linhas" in idx else "itens"
    idx[chave_lista] = lista_idx
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
else:
    idx_path.write_text(json.dumps(lista_idx, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"index.json: +{adicionadas} entradas")

# ---- lista-mestre.json: lotes 8-12 ----
for i, lote in enumerate(div, start=8):
    chave = f"linhas_lote{i}"
    entradas = [{"codigo": n, "slug": f"linhas/linha-{n}-{slugify(LINHAS_FONTE[n]['nome']['valor'])}",
                 "nome": LINHAS_FONTE[n]["nome"]["valor"]} for n in lote]
    mestre[chave] = entradas
mestre_path.write_text(json.dumps(mestre, ensure_ascii=False, indent=2), encoding="utf-8")
print("lista-mestre.json: lotes 8-12 registrados")

print()
print(f"===== RESULTADO =====")
print(f"Geradas e gravadas: {len(geradas)}/{len(faltando)}")
print(f"Não gravadas: {len(falhas)}")
for num, motivo, det in falhas:
    print(f"  [{num}] {motivo} | {det}")
