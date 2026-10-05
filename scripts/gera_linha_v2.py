#!/usr/bin/env python3
"""
GERADOR NARRATIVO v2.1 — INFOHAUS RP (scripts/gera_linha_v2.py)
Ajustes do Leo (04/10/2026): (1) sem cuspir código GTFS — nomes humanizados;
(2) referência <50m = "ao lado de", >50m = "a X metros de"; (3) sem repetir
o mesmo endereço 3x (cada âncora nomeada aparece 1x, no máximo 2x).
Guardrail 1 + Ajustes 1-4 permanecem: só dado da própria linha/pontos/.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path
from math import radians, sin, cos, asin, sqrt

ROOT = Path(__file__).resolve().parent.parent
FONTES = ROOT / "content" / "dados-fonte"
PONTOS = FONTES / "pontos"

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")

def tokens(nome):
    out = set()
    for t in norm(nome).split():
        t = t.strip(".,;:!?()\"'[]{}«»—–-_…/")
        if len(t) > 4 and not t.isdigit():
            out.add(t)
    return out

def hav(a, b):
    la1, lo1, la2, lo2 = map(radians, [a[0], a[1], b[0], b[1]])
    h = sin((la2-la1)/2)**2 + cos(la1)*cos(la2)*sin((lo2-lo1)/2)**2
    return 2*6371000*asin(sqrt(h))

LINHAS = json.load(open(FONTES / "linhas.json", encoding="utf-8"))
PONTOS_COORD = []
for p in sorted(PONTOS.glob("*.json")):
    d = json.load(open(p, encoding="utf-8"))
    nome = d.get("nome")
    if isinstance(nome, dict):
        nome = nome.get("valor")
    if d.get("lat") is not None and nome:
        PONTOS_COORD.append((nome, d["lat"], d["lng"]))

# ---------- humanização de nomes GTFS (Ajuste 1) ----------
def humaniza(nome_gtfs):
    s = nome_gtfs
    s = re.sub(r"^Ponto \d+\s*-\s*", "", s)
    s = re.sub(r"\s*\((oposto|ao lado)\)", "", s, flags=re.I)
    s = re.sub(r"\s*/\s*Ponto \d+$", "", s)
    s = re.sub(r"\s*/\s*Ponto \d+\s*$", "", s)
    s = s.replace("TU / Plat ", "Terminal Urbano – Plataforma ")
    s = re.sub(r"^R\.\s*", "Rua ", s)
    s = re.sub(r"^Av\.\s*", "Avenida ", s)
    s = re.sub(r"^Al\.\s*", "Alameda ", s)
    s = re.sub(r"^ Estr\.\s*", "Estrada ", s)
    s = s.strip(" .,")
    return s

# ---------- vias reais (com prefixo via e dedup por token-chave) ----------
def vias_da_linha(paradas):
    vias, seen = [], set()
    for p in paradas:
        for campo in ("rua", "nome"):
            v = p.get(campo) or ""
            m = re.match(r"^(R\.|Av\.|Al\.|Estr\.)\s*(.+?)(?:,\s*[\d s/n]+|\s*$)", v)
            if not m:
                continue
            pref, corpo = m.group(1), m.group(2).strip()
            corpo = re.sub(r"\s*\(.*?\)\s*$", "", corpo).strip()
            # fix 003: "Passagem" (e outros tipos não-via) não é nome de logradouro
            if norm(corpo) in ("passagem", "passagem de", "viaduto", "praca", "terminal"):
                continue
            toks = tokens(corpo)
            if not toks:
                continue
            chave = max(toks)  # token mais longo como chave de dedup
            if chave in seen:
                continue
            seen.add(chave)
            prefixo = {"R.": "Rua", "Av.": "Avenida", "Al.": "Alameda", "Estr.": "Estrada"}[pref]
            vias.append(f"{prefixo} {corpo}")
            break
        if len(vias) >= 8:
            break
    return vias

# ---------- Guardrail 1 (similaridade): bancos de frases alternativas ----------
# Seleção determinística por hash do número da linha — reprodutível e variada
import hashlib
def _pick(num, banco):
    h = int(hashlib.sha256(str(num).encode()).hexdigest(), 16)
    return banco[h % len(banco)]

ABERTURA_RADIAL = [
    "A <strong>Linha {num} ({nome})</strong> liga os bairros {b1} ao Centro de Ribeirão Preto todos os dias",
    "A <strong>Linha {num} ({nome})</strong> conecta diariamente {b1} ao coração da cidade",
    "Entre o bairro e o Centro, a <strong>Linha {num} ({nome})</strong> é o caminho cotidiano: atravessa {b1} até a área central",
    "A <strong>Linha {num} ({nome})</strong> é a radial que leva o morador de {b1} ao Centro de Ribeirão Preto",
    "De {b1} ao Centro, a <strong>Linha {num} ({nome})</strong> faz o trajeto todos os dias",
    "A <strong>Linha {num} ({nome})</strong> atravessa {b1} rumo ao Centro de Ribeirão Preto, diariamente",
]
ABERTURA_EXPRESSO = [
    "A <strong>Linha {num} ({nome})</strong> é um serviço de hora marcada: em dias úteis, as partidas acontecem às {grade}",
    "No relógio da <strong>Linha {num} ({nome})</strong>, o dia útil tem horários fixos: {grade}",
    "A <strong>Linha {num} ({nome})</strong> opera no esquema que o nome promete: partidas pontuais às {grade} em dias úteis",
    "Horários certos definem a <strong>Linha {num} ({nome})</strong>: {grade} em dias úteis",
    "Para quem programa o retorno ao bairro, a <strong>Linha {num} ({nome})</strong> parte às {grade} em dias úteis",
]
CORPO_RADIAL = [
    "com a primeira partida às {primeira} e a última às {ultima} em dias úteis. O itinerário completo soma {npar} paradas, do embarque inicial em {p0} até o extremo {p1}.</p><p>É a linha do cotidiano do bairro: a saída de manhã para o trabalho, a consulta no centro, o regresso à noite.",
    "{faixa} em dias úteis. No total, são {npar} paradas entre o embarque em {p0} e o extremo {p1}.</p><p>O dia do passageiro cabe no horário da linha: manhã de trabalho, tarde de compromissos, regresso ao bairro.",
    "com partidas de {primeira} a {ultima} em dias úteis. Do ponto inicial em {p0} ao extremo {p1}, são {npar} paradas de cobertura.</p><p>Trabalho, mercado, escola, saúde: a linha costura o bairro ao centro todos os dias.",
    "{faixa} em dias úteis. Entre {p0} e {p1}, a linha cobre {npar} paradas de porta a porta.</p><p>Manhã de trabalho, tarde de compromissos, regresso ao bairro: o dia inteiro tem lugar na grade.",
]
CORPO_EXPRESSO = [
    "{semfim}. São {npar} paradas ligando {p0} a {p1}, atravessando {b1}.</p><p>Quem trabalha ou estuda no centro pode programar o regresso ao bairro em torno desses horários.",
    "{semfim}. O itinerário único cobre {npar} paradas de {p0} a {p1}, servindo {b1}.</p><p>A programação do dia se faz em torno das partidas publicadas — sem surpresa, sem espera longa.",
    "{semfim}. Entre {p0} e {p1}, são {npar} paradas pelos bairros {b1}.</p><p>O serviço é enxuto por desenho: horários definidos, trajeto direto, retorno programado.",
    "{semfim}. De {p0} até {p1}, o serviço cobre {npar} paradas em {b1}.</p><p>O retorno ao bairro tem hora para acontecer — e ela está na grade.",
]
ABERTURA_CIRCULAR = [
    "A <strong>Linha {num} ({nome})</strong> fecha um laço sobre a cidade: {npar} paradas partindo de {p0} e retornando à origem",
    "A cidade em circuito: a <strong>Linha {num} ({nome})</strong> percorre um laço de {npar} paradas com partida em {p0}",
    "A <strong>Linha {num} ({nome})</strong> desenha o laço no mapa urbano — {npar} paradas saindo de {p0} e voltando ao ponto de partida",
]
CORPO_CIRCULAR = [
    "sem passar obrigatoriamente pelo Terminal Central. No caminho, {b1}.</p><p>O sentido é a escolha do passageiro: embarcar no ponto que antecede o destino evita a volta completa pelo circuito.",
    "contornando o Centro sem depender dele. A rota atravessa {b1}.</p><p>Quem conhece o circuito embarca onde o laço passa — e desce adiante, sem dar a volta inteira.",
    "cortando a cidade de lado a lado por {b1}.</p><p>O laço é a alternativa a quem não quer passar pelo Terminal: pega no ponto certo, desce perto do destino.",
]
IT_INICIO = [
    "O trajeto percorre as vias atendidas pela linha: {vias}.",
    "Pelas vias que servem as paradas da linha, o itinerário passa por: {vias}.",
    "O caminho segue as ruas e avenidas onde estão os pontos de embarque: {vias}.",
    "A rota acompanha as vias do itinerário oficial — {vias}.",
]
IT_SEQ = [
    "Na sequência do percurso, o ônibus ainda passa por {vias} antes de completar o itinerário de volta ao ponto de partida.",
    "Mais adiante no trajeto, a linha serve {vias} até fechar o percurso.",
    "O restante do caminho cobre {vias} antes do retorno ao início.",
]
INTEG_ABERTURA = [
    "A tarifa unitária é de <strong>{tarifa}</strong>, com direito aos <strong>120 minutos de integração temporal</strong> do Cartão Cidadão RP Mobi:",
    "Tarifa de <strong>{tarifa}</strong>, com <strong>120 minutos de integração</strong> no Cartão Cidadão RP Mobi:",
    "Ao validar a <strong>tarifa de {tarifa}</strong>, o passageiro ganha <strong>120 minutos de integração temporal</strong> com o Cartão Cidadão RP Mobi:",
]
INTEG_FECHO = [
    "desembarque no centro e tome outra linha dentro do prazo sem nova cobrança.",
    "a baldeação para qualquer linha da rede é gratuita dentro da janela de duas horas.",
    "uma segunda viagem dentro do prazo não gera cobrança adicional.",
]
BAIRROS_ABRE = [
    "No percurso, a linha atende os bairros {bl} — a área de cobertura real conforme o cadastro oficial de itinerários da RP Mobi.",
    "A cobertura oficial da linha alcança {bl}, conforme o cadastro de itinerários da RP Mobi.",
    "Os bairros servidos pela linha são {bl} — área de atendimento registrada no cadastro da RP Mobi.",
]
REF_INTRO = [
    "Ao longo da rota, o passageiro encontra {refs}.",
    "Pertinho do trajeto: {refs}.",
    "Referências úteis no caminho: {refs}.",
]

def escolhe_angulo(fonte):
    nome = norm(fonte["nome"]["valor"])
    hor = fonte.get("horarios", {}).get("valor", {}) or {}
    grade = hor.get("dias_uteis", []) or []
    itins = fonte.get("itinerario", {}).get("valor", []) or []
    if "circular" in nome:
        return "circular"
    if "expresso" in nome or (len(grade) <= 6 and len(itins) <= 2):
        return "expresso-semidireto"
    return "radial-paradora"

def referencias_proximas(paradas, max_m=500):
    refs = []
    for nome, lat, lng in PONTOS_COORD:
        dmin = None
        for p in paradas:
            if p.get("lat") is None:
                continue
            d = hav((lat, lng), (p["lat"], p["lng"]))
            if dmin is None or d < dmin:
                dmin = d
        if dmin is not None and dmin <= max_m:
            refs.append((nome, dmin))
    return sorted(refs, key=lambda x: x[1])[:4]

# ---------- Ajuste 2: linguagem por distância ----------
ART_MASC = ("Terminal", "Fórum", "Hospital", "Museu", "Entreposto", "Shopping", "Theatro", "Teatro", "Palacete", "Santuário", "Bosque")
def ref_frase(nome, d):
    art = "o" if nome.split()[0] in ART_MASC else "a"
    if d < 50:
        return f"ao lado d{art} {nome}"
    return f"a {d:.0f} metros d{art} {nome}"

def parada_interessante(paradas, usado):
    """Escolhe parada central com nome 'rico' (Estação/Terminal/Shopping) sem repetir âncoras."""
    faixa = paradas[len(paradas)//3: 2*len(paradas)//3] or paradas
    for alvo in ("Estação", "Terminal", "Shopping", "Praça"):
        for p in faixa:
            if alvo in p["nome"] and humaniza(p["nome"]) not in usado:
                return humaniza(p["nome"])
    for p in faixa:
        h = humaniza(p["nome"])
        if h not in usado:
            return h
    return humaniza(faixa[0]["nome"])

def gera_secoes(num):
    fonte = LINHAS.get(num) or LINHAS.get(num.zfill(3)) or next(
        (LINHAS[k] for k in LINHAS if k.lstrip("0") == num.lstrip("0")), None)
    if not fonte:
        raise SystemExit(f"Linha {num} sem fonte")
    nome_linha = fonte["nome"]["valor"]
    paradas = fonte.get("paradas", {}).get("valor", []) or []
    bairros = fonte.get("bairros", {}).get("valor", []) or []
    hor = fonte.get("horarios", {}).get("valor", {}) or []
    hor = fonte.get("horarios", {}).get("valor", {}) or {}
    uteis = hor.get("dias_uteis", []) or []
    itins = fonte.get("itinerario", {}).get("valor", []) or []
    angulo = escolhe_angulo(fonte)
    vias = vias_da_linha(paradas)
    refs = referencias_proximas(paradas)
    n_par = max((i.get("num_paradas", 0) for i in itins), default=len(paradas))
    # Tarifa: valor REAL da fonte por linha (alimentadoras trazem R$ 1,80
    # documentado no RP Mobi; convencionais R$ 5,00). Fallback municipal só
    # quando a fonte não traz o campo. (Correção da decisão anterior de 04/10.)
    tarifa = (fonte.get("tarifa", {}) or {}).get("valor") or "R$ 5,00"

    p0 = humaniza(paradas[0]["nome"])
    p1 = humaniza(paradas[-1]["nome"])
    usado = {p0, p1}  # Ajuste 3: cada âncora nomeada no máximo 2x

    # ---- variação (a): ordem de entrada por ângulo + ritmo de frases ----
    hor_uteis = hor.get("dias_uteis", []) or []
    hor_sab = hor.get("sabado", []) or []
    hor_dom = hor.get("domingo", []) or []

    def grade_semana():
        """Frase rica de grade semanal com dados reais (enriquecimento 902)."""
        partes = []
        if hor_uteis:
            partes.append(f"nos dias úteis ({len(hor_uteis)} partidas, das {hor_uteis[0]} às {hor_uteis[-1]})")
        if hor_sab:
            partes.append(f"aos sábados ({len(hor_sab)} partidas)")
        elif not hor_sab and hor_uteis:
            partes.append("sem partidas aos sábados")
        if hor_dom:
            partes.append(f"aos domingos ({len(hor_dom)} partidas)")
        elif not hor_dom and hor_uteis:
            partes.append("sem circulação dominical")
        return "; ".join(partes) if partes else "conforme a grade oficial"

    b1 = ", ".join(bairros[:3]) + (f" e {', '.join(bairros[3:5])}" if len(bairros) > 5 else "")

    # blocos de conteúdo por ângulo — a ORDEM de montagem varia por hash
    bloco_horario = (f"Grade oficial: {grade_semana()}.")
    bloco_cobertura = (f"São {n_par} paradas ligando {p0} a {p1}, atravessando {b1}.")
    bloco_horario_alt = (f"No relógio da linha, {grade_semana()} — {n_par} paradas do embarque em {p0} ao extremo {p1}.")

    if angulo == "expresso-semidireto":
        # expresso → HORÁRIO primeiro
        grade_txt = ", ".join(uteis) if len(uteis) <= 6 else f"{len(uteis)} partidas diárias"
        sem_fimsemana = ("e não circula aos sábados, domingos e feriados"
                         if not (hor.get("sabado") or hor.get("domingo")) else "")
        vg1 = _pick(num, ABERTURA_EXPRESSO).format(num=num, nome=nome_linha, grade=grade_txt) + " " + \
              _pick(num + "c", CORPO_EXPRESSO).format(semfim=sem_fimsemana, npar=n_par, p0=p0, p1=p1, b1=b1)
        vg2 = (f"<p>A tarifa é {tarifa}, com os 120 minutos de integração do Cartão "
               f"Cidadão RP Mobi válidos como em toda a rede.</p>")
    elif angulo == "circular":
        # circular → PERCURSO primeiro
        vg1 = _pick(num, ABERTURA_CIRCULAR).format(num=num, nome=nome_linha, npar=n_par, p0=p0) + ", " + \
              _pick(num + "c", CORPO_CIRCULAR).format(b1=b1)
        vg2 = (f"<p>Tarifa de {tarifa} e 120 minutos de integração no Cartão Cidadão RP Mobi "
               f"em toda a volta do circuito.</p>")
    else:
        # radial → BAIRROS primeiro, e ordem dos blocos varia por hash
        primeira = uteis[1] if len(uteis) > 1 else (uteis[0] if uteis else None)
        if primeira and uteis:
            faixa = f"com a primeira partida às {primeira} e a última às {uteis[-1]}"
        else:
            faixa = "ao longo do dia"
        ordem = int(hashlib.sha256(f"ord{num}".encode()).hexdigest(), 16) % 3
        meio = _pick(num + "m", [
            bloco_horario,
            bloco_cobertura,
            bloco_horario_alt,
        ])
        fim = _pick(num + "f2", [
            f"Ao longo do dia, a grade cumpre o que promete: {grade_semana()}.",
            f"Do primeiro ao último ponto, a cobertura é contínua: {grade_semana()}.",
            f"Para planejar bem a viagem: {grade_semana()}.",
        ])
        abertura = _pick(num, ABERTURA_RADIAL).format(num=num, nome=nome_linha, b1=b1)
        if ordem == 0:
            vg1 = f"<p>{abertura} {meio}</p>"
            vg2 = f"<p>{_pick(num + 'c', CORPO_RADIAL).format(faixa=faixa, primeira=primeira or '—', ultima=uteis[-1] if uteis else '—', npar=n_par, p0=p0, p1=p1)}</p><p>{fim}</p>"
        elif ordem == 1:
            vg1 = f"<p>{abertura} {_pick(num + 'c', CORPO_RADIAL).format(faixa=faixa, primeira=primeira or '—', ultima=uteis[-1] if uteis else '—', npar=n_par, p0=p0, p1=p1)}</p>"
            vg2 = f"<p>{meio}</p><p>{fim}</p>"
        else:
            vg1 = f"<p>{abertura} {meio}</p><p>{fim}</p>"
            vg2 = f"<p>{_pick(num + 'c', CORPO_RADIAL).format(faixa=faixa, primeira=primeira or '—', ultima=uteis[-1] if uteis else '—', npar=n_par, p0=p0, p1=p1)}</p>"
        vg_final_extra = (f"<p>Tarifa de {tarifa} e 120 minutos de integração pelo Cartão Cidadão "
                          f"RP Mobi em toda a viagem.</p>")
        if ordem == 0:
            vg2 = vg2 + vg_final_extra
        else:
            vg1 = vg1 + vg_final_extra

    # itinerário: só vias reais, sem repetir âncoras
    if vias:
        it1 = "<p>" + _pick(num, IT_INICIO).format(vias=", ".join(vias[:4])) + "</p>"
        resto = vias[4:8]
        it2 = ("<p>" + _pick(num + "i", IT_SEQ).format(vias=", ".join(resto)) + "</p>"
               if resto else "")
    else:
        it1 = f"<p>O trajeto acompanha as paradas publicadas no itinerário oficial da linha.</p>"
        it2 = ""
    itinerario = it1 + it2

    # paradas destaque: âncoras novas (sem repetir p0/p1)
    meio = parada_interessante(paradas, usado)
    usado.add(meio)
    outra = parada_interessante(paradas, usado) if len(paradas) > 10 else None
    pd1 = (f"<p>Para planejar o embarque, três referências do quadro de paradas: o ponto de partida "
           f"em {p0}, a parada {meio} no meio do trajeto"
           + (f" e o ponto {outra}" if outra else "")
           + " — todos com endereço completo no quadro oficial.</p>")
    if refs:
        extras = "".join(f" e {ref_frase(n, d)}" for n, d in refs[1:2])
        pd2 = f"<p>Ao longo da rota, o passageiro encontra {ref_frase(refs[0][0], refs[0][1])}{extras}.</p>"
    else:
        pd2 = "<p>O quadro completo de paradas está publicado no itinerário oficial da linha.</p>"
    paradas_destaque = pd1 + pd2

    integracao = ("<p>" + _pick(num, INTEG_ABERTURA).format(tarifa=tarifa) + " " +
                  _pick(num + "f", INTEG_FECHO).format() + "</p>")

    bl = ", ".join(f"<em>{b}</em>" for b in bairros)
    bairros_texto = "<p>" + _pick(num, BAIRROS_ABRE).format(bl=bl) + "</p>"

    if refs:
        refs_txt = "; ".join(ref_frase(n, d) for n, d in refs)
        atracoes = "<p>" + _pick(num + "r", REF_INTRO).format(refs=refs_txt) + \
                   " As distâncias partem da parada mais próxima de cada ponto.</p>"
    else:
        atracoes = "<p>As atrações e serviços da região ficam a pé das paradas da linha; consulte o mapa do itinerário para planejar o trajeto.</p>"

    return {
        "visao_geral": vg1 + vg2,
        "itinerario_texto": itinerario,
        "paradas_destaque": paradas_destaque,
        "integracao_detalhe": integracao,
        "bairros_texto": bairros_texto,
        "atracoes_proximas": atracoes,
    }, angulo

def main():
    if len(sys.argv) < 2:
        raise SystemExit("uso: gera_linha_v2.py <numero> [--write]")
    num = sys.argv[1]
    write = "--write" in sys.argv
    secoes, angulo = gera_secoes(num)
    if write:
        alvo = next((ROOT / "content" / "paginas" / "linhas").glob(f"linha-{num}-*.json"), None)
        if not alvo:
            raise SystemExit(f"página da linha {num} não existe (use geração de página nova)")
        pag = json.load(open(alvo, encoding="utf-8"))
        pag["secoes"].update(secoes)
        alvo.write_text(json.dumps(pag, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[GRAVADO] {alvo.name}")
    print(json.dumps({"linha": num, "angulo": angulo, "secoes": secoes},
                     ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
