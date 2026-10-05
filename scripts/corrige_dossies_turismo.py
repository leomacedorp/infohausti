#!/usr/bin/env python3
"""CORREÇÃO DOS 12 DOSSIÊS (dossiê Perplexity verificado, 05/10/2026).
Dossiê é a única verdade com URL; página deriva do dossiê."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "content" / "dados-fonte" / "pontos"

def upd(slug, campos):
    f = P / f"{slug}.json"
    d = json.loads(f.read_text(encoding="utf-8"))
    fonte = campos.pop("_fonte", "")
    for k, v in campos.items():
        if isinstance(v, dict):
            d[k] = v
        elif v is None:
            d[k] = {"valor": None, "status": "nao_confirmado", "fonte_url": fonte, "verificado_em": "2026-10-05"}
        else:
            d[k] = {"valor": v, "status": "verificado", "fonte_url": fonte, "verificado_em": "2026-10-05"}
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[{slug}] OK")

upd("palacete-camilo-de-mattos", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/noticia/palacete-camilo-de-mattos-abre-as-portas-para-visitacao-publica",
    "telefone": None,
    "horario_visita": {"valor": "Visitação permanente não confirmada — imóvel particular tombado; aberturas apenas em eventos especiais anunciados pela Prefeitura (ex.: junho/2024, 9h-12h e 13h-17h)", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/noticia/palacete-camilo-de-mattos-abre-as-portas-para-visitacao-publica", "verificado_em": "2026-10-05"},
    "ingresso": {"valor": "Gratuito nas aberturas públicas oficialmente anunciadas", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/noticia/palacete-camilo-de-mattos-abre-as-portas-para-visitacao-publica", "verificado_em": "2026-10-05"},
    "status_atual": "imovel_particular_eventual",
})

upd("museu-do-cafe", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/complexo-museus/museu-do-cafe-exposicoes",
    "telefone": "(16) 3315-9321",
    "horario_visita": {"valor": "TEMPORARIAMENTE FECHADO — sem horário de visitação vigente; reabertura sem data publicada. Confira no site da Prefeitura", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/complexo-museus/museu-do-cafe-exposicoes", "verificado_em": "2026-10-05"},
    "ingresso": {"valor": "Não aplicável enquanto fechado", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/complexo-museus/museu-do-cafe-exposicoes", "verificado_em": "2026-10-05"},
    "status_atual": "temporariamente_fechado",
})

upd("santuario-sete-capelas", {
    "_fonte": "https://arquidioceserp.org.br/santuario-nossa-senhora-da-medalha-milagrosa-sete-capelas/",
    "nome": {"valor": "Santuário Nossa Senhora da Medalha Milagrosa (Sete Capelas)", "status": "verificado", "fonte_url": "https://arquidioceserp.org.br/santuario-nossa-senhora-da-medalha-milagrosa-sete-capelas/", "verificado_em": "2026-10-05"},
    "telefone": "(16) 3625-0507 (WhatsApp: (16) 99753-3910)",
    "horario_visita": {"valor": "Segunda a sábado, 7h-16h; domingos e feriados, 7h-13h. Missas: seg-sáb 8h; dom 9h30", "status": "verificado", "fonte_url": "https://arquidioceserp.org.br/santuario-nossa-senhora-da-medalha-milagrosa-sete-capelas/", "verificado_em": "2026-10-05"},
    "status_atual": "aberto",
})

upd("theatro-pedro-ii", {
    "_fonte": "https://www.theatropedro2.com.br/comprar-ingresso.php",
    "telefone": "(16) 3977-8111",
    "horario_visita": {"valor": "Bilheteria com horário variável conforme espetáculos (ter-sex 12h-18h sem espetáculo / 12h-20h com espetáculo; sáb 9h-13h sem / 13h-20h com). Administração: seg-sex 9h-17h. Consultar theatropedro2.com.br", "status": "verificado", "fonte_url": "https://www.theatropedro2.com.br/comprar-ingresso.php", "verificado_em": "2026-10-05"},
    "site_oficial": "https://www.theatropedro2.com.br",
    "status_atual": "aberto",
})

upd("bosque-fabio-barreto", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/bosque-zoo/bosque-e-zoologico",
    "telefone": "(16) 3636-2513",
    "horario_visita": {"valor": "Quarta a domingo, das 9h às 16h30. Visitas monitoradas mediante agendamento (educambiental.meioambiente@rp.ribeiraopreto.sp.gov.br)", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/bosque-zoo/bosque-e-zoologico", "verificado_em": "2026-10-05"},
    "status_atual": "aberto",
})

upd("marp-museu-de-arte", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/marp/informacoes-gerais-marp",
    "telefone": "(16) 3635-2421",
    "email": "marp.cultura@rp.ribeiraopreto.sp.gov.br",
    "horario_visita": {"valor": "Terça a sexta, 9h30-12h e 13h-17h30. Sábados apenas nas datas da programação (normalmente 9h-15h). Fechado em feriados e pontos facultativos", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/marp/programacao-marp", "verificado_em": "2026-10-05"},
    "visita_guiada": "Mediante agendamento por telefone ou e-mail",
    "status_atual": "aberto",
})

upd("catedral-metropolitana", {
    "_fonte": "https://catedralrp.com.br/horarios/",
    "endereco": {"valor": "Praça das Bandeiras, s/n, Centro, Ribeirão Preto-SP, CEP 14015-068 (referência: Rua Florêncio de Abreu)", "status": "verificado", "fonte_url": "https://arquidioceserp.org.br/catedral-metropolitana-de-sao-sebastiao-1870/", "verificado_em": "2026-10-05"},
    "telefone": "(16) 3625-0007",
    "email": "secretariacatedralrp@gmail.com",
    "site_oficial": "https://catedralrp.com.br",
    "horario_visita": {"valor": "Missas: seg 18h30; ter-sex 7h30/12h/18h30; sáb 12h/18h30; dom 9h/11h/17h/19h. Secretaria: seg 16h-18h30; ter-sex 9h-18h30; sáb 8h30-12h30. Visitação livre fora dos horários de missa", "status": "verificado", "fonte_url": "https://catedralrp.com.br/horarios/", "verificado_em": "2026-10-05"},
    "status_atual": "aberta",
})

upd("biblioteca-sinha-junqueira", {
    "_fonte": "https://www.revide.com.br/noticias/cultura/biblioteca-sinha-junqueira-sera-aberta-ao-publico-no-proximo-dia-7/",
    "telefone": "(16) 3625-0743",
    "site_oficial": "https://bsj.org.br",
    "horario_visita": {"valor": "Terça a sexta, das 10h às 20h; sábados, domingos e feriados, das 10h às 19h", "status": "verificado", "fonte_url": "https://www.revide.com.br/noticias/cultura/biblioteca-sinha-junqueira-sera-aberta-ao-publico-no-proximo-dia-7/", "verificado_em": "2026-10-05"},
    "status_atual": "aberta",
})

upd("parque-curupira", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/coordenadoria-limpeza/parques-municipais",
    "nome": {"valor": "Parque Municipal Prefeito Luiz Roberto Jábali (Curupira)", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/coordenadoria-limpeza/parques-municipais", "verificado_em": "2026-10-05"},
    "horario_visita": {"valor": "Diariamente, das 6h às 20h", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/coordenadoria-limpeza/parques-municipais", "verificado_em": "2026-10-05"},
    "status_atual": "aberto",
})

upd("parque-maurilio-biagi", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/coordenadoria-limpeza/parques-municipais",
    "nome": {"valor": "Parque Ecológico Maurílio Biagi", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/coordenadoria-limpeza/parques-municipais", "verificado_em": "2026-10-05"},
    "endereco": {"valor": "Rua Felipe Camarão, 292, Vila Tibério (acessos também pela Av. Elpídio Gomes, 327 e Alameda Botafogo)", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/coordenadoria-limpeza/parques-municipais", "verificado_em": "2026-10-05"},
    "horario_visita": {"valor": "Das 6h às 20h", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/coordenadoria-limpeza/parques-municipais", "verificado_em": "2026-10-05"},
    "status_atual": "aberto",
})

upd("praca-xv-de-novembro", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/noticia/fundacao-d-pedro-ii-realiza-manutencao-e-limpeza-no-relogio-da-praca-xv",
    "status_atual": "aberta_espaco_publico",
})

upd("quarteirao-paulista", {
    "_fonte": "https://www.ribeiraopreto.sp.gov.br/portal/centro-cultural-palace/conheca-historia-quarteirao-paulista",
    "composicao": {"valor": "Edifício Meira Júnior (Choperia Pinguim), Theatro Pedro II, Palace Hotel e Praça XV de Novembro — conjunto tombado nas esferas municipal e estadual", "status": "verificado", "fonte_url": "https://www.ribeiraopreto.sp.gov.br/portal/centro-cultural-palace/conheca-historia-quarteirao-paulista", "verificado_em": "2026-10-05"},
    "status_atual": "aberto_espaco_urbano",
})
print("12 dossies atualizados")
