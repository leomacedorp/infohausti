#!/usr/bin/env python3
"""REESCRITA EDITORIAL 310 x 701 (decisão Leo 05/10/2026, item 2).
310 = articulação interbairros; 701 = corredor Via Norte.
Só dados-fonte; parada vs referência; validação check_fontes antes de gravar."""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_fontes_factuais as ck

ROOT = Path(__file__).resolve().parent.parent
PAG = ROOT / "content" / "paginas" / "linhas"

S310 = {
    "visao_geral": (
        "<p>A <strong>Linha 310 (Quintino/Avelino)</strong> é a linha que costura a Zona Norte "
        "residencial de Ribeirão Preto: num único itinerário de 72 paradas, ela conecta os núcleos "
        "habitacionais do <em>Quintino Facci I</em> e <em>Quintino Facci II</em> ao <em>Jardim "
        "Salgado Filho</em>, ao <em>Jardim das Mansões</em>, ao <em>Parque dos Sabiás</em> e ao "
        "<em>Avelino Alves Palma</em>, descendo depois pelo <em>Jardim Botânico</em> e "
        "<em>Recreio Internacional</em> até o <em>Centro</em>.</p>"
        "<p>Para quem mora em um bairro desses e precisa chegar a outro — a escola dos filhos num, "
        "o posto de saúde noutro, o mercado num terceiro — a 310 é o atalho que dispensa a volta "
        "pelo centro: uma articulação direta entre bairros vizinhos que nenhuma outra linha faz "
        "no mesmo desenho. A grade é extensa: 78 partidas em dias úteis (das {h0} às {h1}), 59 aos "
        "sábados e 46 aos domingos.</p>"
    ),
    "itinerario_texto": (
        "<p>O fio condutor do trajeto é a Avenida Gal. Euclydes de Figueiredo — a espinha que liga "
        "os conjuntos do Quintino aos do Avelino Palma. Dela, a linha entra nas ruas internas de cada "
        "núcleo para servir o passageiro porta a porta, com 3 formações de itinerário publicadas: o "
        "percurso completo (72 paradas), o reforço Até Centro (30) e o regresso Até Bairro (43).</p>"
    ),
    "paradas_destaque": (
        "<p>O embarque de partida e o ponto final ficam ambos na Avenida Gal. Euclydes de "
        "Figueiredo — o eixo onde a linha nasce e encerra o circuito. Ao longo do trajeto, as "
        "paradas internas dos bairros é que fazem a diferença: o passageiro desce no coração do "
        "Quintino, do Salgado Filho ou do Avelino Palma sem caminhar até a avenida.</p>"
    ),
    "integracao_detalhe": (
        "<p>Tarifa de <strong>R$ 5,00</strong> com os <strong>120 minutos de integração</strong> "
        "do Cartão Cidadão RP Mobi: quem baldeia no Centro para outra região da cidade não paga "
        "nova passagem dentro do prazo.</p>"
    ),
    "bairros_texto": (
        "<p>De ponta a ponta, a linha atende <em>Avelino Alves Palma</em>, <em>Quintino Facci I</em> "
        "e <em>II</em>, <em>Jardim Salgado Filho</em>, <em>Jardim das Mansões</em>, <em>Parque dos "
        "Sabiás</em>, <em>Jardim Botânico</em>, <em>Recreio Internacional</em>, <em>Vila Brasil</em> "
        "e <em>Centro</em> — a malha residencial setentrional amarrada por um só itinerário, "
        "conforme o cadastro oficial da RP Mobi.</p>"
    ),
    "atracoes_proximas": (
        "<p>A linha passa rente ao cotidiano dos bairros que serve — escolas, praças e comércio "
        "local ficam a pé das paradas internas do trajeto.</p>"
    ),
}

S701 = {
    "visao_geral": (
        "<p>A <strong>Linha 701 (Via Norte)</strong> é o serviço de corredor da Avenida Gal. "
        "Euclydes de Figueiredo: um itinerário único de 48 paradas que acompanha a via expressa "
        "da Zona Norte de Ribeirão Preto, ligando o extremo do <em>Adelino Simioni</em> aos "
        "<em>Campos Elíseos</em> e ao <em>Centro</em>.</p>"
        "<p>Se a 310 é a linha que entra nos bairros, a 701 é a que corre por cima deles: feita "
        "para quem quer velocidade no eixo da Via Norte — o trabalhador do Simioni que desce ao "
        "centro, o passageiro dos Campos Elíseos que embarca direto na avenida. A grade é "
        "enxuta por desenho: 53 partidas em dias úteis, 49 aos sábados e 38 aos domingos.</p>"
    ),
    "itinerario_texto": (
        "<p>Não há desvios: a rota é o próprio corredor — embarque na Avenida Gal. Euclydes de "
        "Figueiredo, 155, no Simioni, e descida contínua pela avenida até o ponto 575, já na "
        "altura dos Campos Elíseos rumo ao Centro. Um itinerário único de 48 paradas, publicado "
        "como 'Via Norte' pela RP Mobi.</p>"
    ),
    "paradas_destaque": (
        "<p>As âncoras do corredor são os dois extremos da avenida: a partida no número 155, no "
        "Adelino Simioni, e o término no número 575, na seqüência da via. Entre eles, todas as "
        "paradas ficam na própria Via Norte — basta estar na avenida para estar na linha.</p>"
    ),
    "integracao_detalhe": (
        "<p>Tarifa de <strong>R$ 5,00</strong> com <strong>120 minutos de integração</strong> "
        "pelo Cartão Cidadão RP Mobi, válidos para baldeação em qualquer ponto do trajeto.</p>"
    ),
    "bairros_texto": (
        "<p>O corredor atende três territórios: <em>Adelino Simioni</em> no extremo norte, "
        "<em>Campos Elíseos</em> no meio do eixo e o <em>Centro</em> como destino final — a "
        "cobertura oficial registrada no cadastro de itinerários da RP Mobi.</p>"
    ),
    "atracoes_proximas": (
        "<p>Serviços e comércio da própria avenida ficam a caminho das paradas; o Terminal "
        "Evangelina Passig fica próximo ao eixo atendido.</p>"
    ),
}

def main():
    l = json.load(open(ROOT / "content" / "dados-fonte" / "linhas.json", encoding="utf-8"))
    h = l["310"]["horarios"]["valor"]["dias_uteis"]
    s310 = dict(S310)
    s310["visao_geral"] = s310["visao_geral"].format(h0=h[1] if len(h) > 1 else h[0], h1=h[-1])

    ok = True
    for num, secoes in (("310", s310), ("701", S701)):
        fatais, _ = ck.verifica_linha(num.zfill(3), l[num.zfill(3)], secoes)
        if fatais:
            print(f"[{num}] {len(fatais)} FATAIS — NAO GRAVA:")
            for f in fatais:
                print("   ", f[:120])
            ok = False
            continue
        alvo = next(PAG.glob(f"linha-{num}-*.json"))
        pag = json.load(open(alvo, encoding="utf-8"))
        pag["secoes"].update(secoes)
        alvo.write_text(json.dumps(pag, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{num}] reescrito e gravado: {alvo.name}")
    print("OK" if ok else "FALHOU — verificar fatais acima")

if __name__ == "__main__":
    main()
