#!/usr/bin/env python3
"""AJUSTE FINAL — MUSEU DO CAFÉ (decisão Leo, 05/10/2026).
FONTE ÚNICA: artigo 'O pó do café' — Revide, 03/05/2026.
https://www.revide.com.br/noticias/cultura/o-po-do-cafe/
Remove TODO dado não presente no artigo (telefone, endereço, e-mail, site,
horário, ingresso, como chegar). Página vira: status + história + situação."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTE = "https://www.revide.com.br/noticias/cultura/o-po-do-cafe/"
VERIF = "2026-10-05"

# ---------- dossiê (fonte única) ----------
dossie = {
    "_doc": "Museu do Café Francisco Schmidt. FONTE ÚNICA (decisão Leo 05/10/2026): artigo 'O pó do café', Revide, 03/05/2026. Campos não cobertos pelo artigo não são publicados.",
    "nome": {"valor": "Museu do Café Francisco Schmidt", "status": "verificado", "fonte_url": FONTE, "verificado_em": VERIF},
    "status_atual": {"valor": "fechado_desde_2016", "status": "verificado", "fonte_url": FONTE, "verificado_em": VERIF},
    "status_detalhe": {"valor": "Interdição em março de 2016, após desabamento de parte do forro do Museu Histórico. Fechado há quase dez anos, sem previsão de reabertura", "status": "verificado", "fonte_url": FONTE, "verificado_em": VERIF},
    "situacao_judicial": {"valor": "Ordem judicial de restauração sem cumprimento desde 2021. Justiça determinou início das obras em até 90 dias (2017), mantida pelo TJ em 2018. Em janeiro de 2019, prazo de dois anos para a reforma dos prédios e de um ano para o restauro do acervo, sob multa diária de R$ 10 mil. Em 2025, o STF negou recurso do município e manteve a obrigação de restaurar", "status": "verificado", "fonte_url": FONTE, "verificado_em": VERIF},
    "situacao_administrativa": {"valor": "Projeto de restauro estimado em R$ 15 milhões apresentado em 2021, com captação indefinida até 2023. Contrato nº 141/2020 (projeto executivo de arquitetura e engenharia) venceu em 7 de maio de 2025 e não foi renovado; a empresa responsável afirma ter entregue integralmente os materiais e não recebeu justificativa formal da Prefeitura. Conppac aponta paralisação por tempo indeterminado e possível necessidade de nova licitação", "status": "verificado", "fonte_url": FONTE, "verificado_em": VERIF},
    "reserva_tecnica": {"valor": "Reserva técnica contratada em 2024 para abrigar o acervo: valor inicial de R$ 4.862.000, prazo de 15 meses; em 2025, reajustada para R$ 5.076.804,12 e prorrogada até fevereiro de 2026, em fase final com previsão de inauguração em poucos meses, segundo a Secretaria de Cultura", "status": "verificado", "fonte_url": FONTE, "verificado_em": VERIF},
    "contexto_historico": {"valor": "O complexo tem origem na antiga casa-sede da Fazenda Monte Alegre (Solar Schmidt), cedida ao município em 1950. Plínio Travassos dos Santos iniciou a formação do acervo em 1938; o Museu Histórico foi oficializado em 1949; o Museu do Café foi inaugurado em 1955 e, em 1957, ganhou prédio próprio. O acervo reúne milhares de peças ligadas à história do café e da cidade", "status": "verificado", "fonte_url": FONTE, "verificado_em": VERIF},
}
d_path = ROOT / "content" / "dados-fonte" / "pontos" / "museu-do-cafe.json"
d_path.write_text(json.dumps(dossie, ensure_ascii=False, indent=1), encoding="utf-8")
print("[dossie] museu-do-cafe.json reescrito com fonte única Revide")

# ---------- página ----------
p_path = ROOT / "content" / "paginas" / "ribeirao-preto" / "pontos-turisticos" / "museu-do-cafe.json"
p = json.loads(p_path.read_text(encoding="utf-8"))

p["titulo"] = "Museu do Café Francisco Schmidt — Fechado"
p["h1"] = "Museu do Café Francisco Schmidt"
p["descricao"] = ("Museu do Café Francisco Schmidt, em Ribeirão Preto: fechado desde março de 2016, "
                  "com ordem judicial de restauração pendente. História do complexo, situação atual "
                  "do impasse e obras da reserva técnica.")
p["status"] = "fechado"
p.pop("telefone", None)
p.pop("status_atual", None)
p.pop("visita", None)            # sem endereço/horário/ingresso: não existem no artigo
p.pop("linhas_proximas", None)   # 'como chegar' não faz sentido — museu fechado
p["atualizado"] = VERIF
p["fontes"] = [{
    "nome": "Revide — 'O pó do café' (03/05/2026): Museus Histórico e do Café seguem fechados há quase dez anos sem cumprir ordem judicial de restauro",
    "url": FONTE,
    "tipo": "imprensa_local",
    "verificado_em": VERIF,
}]

p["secoes"] = {
    "resumo": (
        "<p>O <strong>Museu do Café Francisco Schmidt</strong>, em Ribeirão Preto, está "
        "<strong>fechado desde março de 2016</strong>, quando a interdição ocorreu após o "
        "desabamento de parte do forro do Museu Histórico — e segue sem previsão de reabertura, "
        "quase dez anos depois.</p>"
        "<p>A página reúne a história do complexo e a situação atual do impasse judicial e "
        "administrativo, conforme apuração da Revide publicada em 3 de maio de 2026. Enquanto "
        "o museu não reabre, nenhuma informação de visitação é publicada aqui — não há horário, "
        "endereço de acesso ou bilheteria em funcionamento.</p>"
    ),
    "status": (
        "<h3>Status: fechado</h3>"
        "<p><strong>Museu temporariamente fechado desde março de 2016.</strong> A interdição "
        "veio após o desabamento de parte do forro do Museu Histórico. Não há previsão de "
        "reabertura publicada.</p>"
    ),
    "historia": (
        "<p>O complexo tem origem na antiga casa-sede da <strong>Fazenda Monte Alegre</strong>, "
        "o <strong>Solar Schmidt</strong>, cujo imóvel foi cedido ao município em 1950. A formação "
        "do acervo começou antes: <strong>Plínio Travassos dos Santos</strong> iniciou a coleção "
        "em 1938, e o <strong>Museu Histórico foi oficializado em 1949</strong>.</p>"
        "<p>O <strong>Museu do Café foi inaugurado em 1955</strong> e, em <strong>1957</strong>, "
        "ganhou prédio próprio no complexo. O acervo reúne milhares de peças ligadas à história "
        "do café e da cidade de Ribeirão Preto.</p>"
    ),
    "situacao_atual": (
        "<h3>Situação atual: impasse judicial e administrativo</h3>"
        "<p>Existe <strong>ordem judicial de restauração sem cumprimento desde 2021</strong>. "
        "Em 2017, a Justiça determinou o início das obras em até 90 dias — decisão mantida pelo "
        "Tribunal de Justiça em 2018. Em janeiro de 2019, foi fixado prazo de dois anos para a "
        "reforma dos prédios e de um ano para o restauro do acervo, sob <strong>multa diária de "
        "R$ 10 mil</strong>.</p>"
        "<p>Em 2021, o município apresentou um projeto de restauro estimado em <strong>R$ 15 "
        "milhões</strong>, mas a captação de recursos permaneceu indefinida até 2023. Em 2025, o "
        "<strong>Supremo Tribunal Federal negou recurso do município</strong> e manteve a "
        "obrigação de restaurar o complexo.</p>"
        "<p>O contrato administrativo <strong>nº 141/2020</strong>, responsável pelo projeto "
        "executivo de arquitetura e engenharia, <strong>venceu em 7 de maio de 2025 e não foi "
        "renovado</strong>. A empresa responsável afirma que cumpriu as exigências técnicas e "
        "entregou integralmente os materiais, sem receber justificativa formal da Prefeitura "
        "para a não renovação. O Conppac aponta paralisação por tempo indeterminado e a "
        "possibilidade de nova licitação.</p>"
        "<p>Avanço registrado na apuração: a <strong>reserva técnica</strong> destinada a abrigar "
        "o acervo foi contratada em 2024 por <strong>R$ 4.862.000</strong>, com prazo de 15 meses; "
        "em 2025, o valor foi atualizado para <strong>R$ 5.076.804,12</strong> e o prazo estendido "
        "até fevereiro de 2026. A obra entrou na fase final, com previsão de inauguração em "
        "poucos meses, segundo a Secretaria de Cultura.</p>"
    ),
}
p["faq"] = [
    {"pergunta": "O Museu do Café está aberto?",
     "resposta": "Não. O museu está fechado desde março de 2016, após o desabamento de parte do forro do Museu Histórico, e não tem previsão de reabertura."},
    {"pergunta": "Existe ordem judicial sobre o museu?",
     "resposta": "Sim. Há ordem judicial de restauração sem cumprimento desde 2021. Em 2019, a Justiça fixou prazo de dois anos para a reforma e um ano para o restauro do acervo, sob multa diária de R$ 10 mil. Em 2025, o STF negou recurso do município e manteve a obrigação de restaurar."},
    {"pergunta": "Quando o museu reabre?",
     "resposta": "Não há previsão publicada. O contrato do projeto executivo de restauro (nº 141/2020) venceu em maio de 2025 e não foi renovado; a reserva técnica para o acervo está em fase final de construção."},
]
p_path.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
print("[pagina] museu-do-cafe.json reescrita: status + historia + situacao, sem visita/como-chegar")
