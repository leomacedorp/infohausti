#!/usr/bin/env python3
"""REESCRITA EDITORIAL 041 x 204 (decisão Leo 05/10/2026, Tarefa 1).
041 = bairro/moradores/comércio de rua (alimentadora local do Terminal São José);
204 = condomínios de classe média + serviços do entorno (linha do City Ribeirão).
Só dados-fonte; parada vs referência; validação antes de gravar."""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_fontes_factuais as ck

ROOT = Path(__file__).resolve().parent.parent
PAG = ROOT / "content" / "paginas" / "linhas"

S41 = {
    "visao_geral": (
        "<p>A <strong>Linha 041 (Machado Sant'Anna)</strong> é a alimentadora do cotidiano no "
        "extremo sudeste: um trajeto curto de 28 paradas que parte do Terminal Sudeste — São José "
        "e percorre as ruas onde mora o passageiro — <em>Jardim São José</em>, <em>Jardim Manoel "
        "Penna</em>, <em>Jardim Roberto Benedetti</em> e <em>Parque das Oliveiras II</em> — até o "
        "miolo do <em>City Ribeirão</em> e do <em>Recreio Internacional</em>.</p>"
        "<p>É a linha do pão e da farmácia: 19 partidas em dias úteis e 16 aos sábados, sem "
        "circulação aos domingos, desenhada para o morador que resolve a vida no bairro e usa o "
        "terminal para alcançar o resto da cidade. O comércio de rua dos jardins é o cenário "
        "direto do trajeto — a linha passa na porta dos mercadinhos, das barracas e das "
        "oficinas do bairro.</p>"
    ),
    "itinerario_texto": (
        "<p>Do Terminal Sudeste, o itinerário sobe pelas vias internas dos jardins e culmina na "
        "Rua Francisco Evangelista, no limite do bairro — um vaivém de proximidade, sem pressa "
        "de avenida, servindo cada quadra do caminho conforme o cadastro oficial da RP Mobi "
        "(itinerário único 'Machado Sant'Anna', 29 paradas contando os pontos de retorno).</p>"
    ),
    "paradas_destaque": (
        "<p>As duas âncoras do trajeto são o Terminal Sudeste — São José, onde a linha nasce e "
        "conecta com a malha troncal, e o ponto da Rua Francisco Evangelista, o coração do "
        "bairro que dá nome à linha. Entre elas, cada parada é porta de casa ou porta de loja.</p>"
    ),
    "integracao_detalhe": (
        "<p>Tarifa de <strong>R$ 5,00</strong> com <strong>120 minutos de integração</strong> "
        "do Cartão Cidadão RP Mobi — no Terminal Sudeste, o passageiro transfere para as linhas "
        "estruturais sem nova cobrança dentro do prazo.</p>"
    ),
    "bairros_texto": (
        "<p>No percurso, a linha atende <em>Jardim São José</em>, <em>Jardim Manoel Penna</em>, "
        "<em>Jardim Roberto Benedetti</em>, <em>Parque das Oliveiras II</em>, <em>City Ribeirão</em> "
        "e <em>Recreio Internacional</em> — os bairros operários do eixo sudeste, conforme o "
        "cadastro de itinerários da RP Mobi.</p>"
    ),
    "atracoes_proximas": (
        "<p>O trajeto é todo de bairro: padarias, feiras e comércio de rua dos jardins ficam a "
        "passo das paradas internas.</p>"
    ),
}

S204 = {
    "visao_geral": (
        "<p>A <strong>Linha 204 (City Ribeirão)</strong> é a linha do bairro planejado: liga os "
        "condomínios e residenciais de classe média do <em>City Ribeirão</em> ao Centro pela "
        "Avenida Antônio Machado Sant'Anna, com uma grade de dia inteiro — 39 partidas em dias "
        "úteis, 34 aos sábados e 33 aos domingos.</p>"
        "<p>Diferente das alimentadoras de rua estreita, a 204 é o eixo dos serviços do entorno: "
        "o passageiro embarca no portão do condomínio e alcança, na mesma viagem, os comércios "
        "do City, os <em>Campos Elíseos</em>, o <em>Jardim Botânico</em> e o <em>Jardim Irajá</em> "
        "até o Centro — a rota que costura os territórios de serviços do quadrante oeste ao "
        "núcleo da cidade.</p>"
    ),
    "itinerario_texto": (
        "<p>O trajeto é estruturado em três formações publicadas: o percurso completo do City "
        "Ribeirão (60 paradas), o reforço Até Centro (29) e o regresso Até Bairro (32). O fio "
        "condutor é a Avenida Antônio Machado Sant'Anna — embarque no número 480, término no "
        "número 126 — a coluna vertebral que ordena os bairros do caminho.</p>"
    ),
    "paradas_destaque": (
        "<p>As âncoras da linha são as duas pontas da Avenida Machado Sant'Anna (480 na partida, "
        "126 no retorno), com conexões de serviços ao longo dos Campos Elíseos e desembarque "
        "central no fim do trajeto — o desenho completo está no quadro oficial de paradas.</p>"
    ),
    "integracao_detalhe": (
        "<p>Tarifa de <strong>R$ 5,00</strong> com <strong>120 minutos de integração</strong> "
        "no Cartão Cidadão RP Mobi: do Centro, o passageiro segue para qualquer região da "
        "cidade sem pagar nova passagem dentro da janela.</p>"
    ),
    "bairros_texto": (
        "<p>A cobertura oficial da linha atravessa <em>City Ribeirão</em>, <em>Campos Elíseos</em>, "
        "<em>Jardim Botânico</em>, <em>Jardim Irajá</em>, <em>Jardim Mosteiro</em>, <em>Parque "
        "das Oliveiras II</em>, <em>Santa Cruz do José Jacques</em> e <em>Centro</em> — o mapa "
        "de serviços e condomínios do eixo oeste, conforme o cadastro da RP Mobi.</p>"
    ),
    "atracoes_proximas": (
        "<p>Os serviços do entorno — escolas, clínicas e comércios dos bairros de passagem — "
        "ficam a caminho das paradas da avenida e das vias coletoras do trajeto.</p>"
    ),
}

def main():
    ok = True
    for num, secoes in (("041", S41), ("204", S204)):
        fatais, _ = ck.verifica_linha(num, ck.LINHAS_FONTE[num], secoes)
        if fatais:
            print(f"[{num}] {len(fatais)} FATAIS — NAO GRAVA:")
            for f in fatais:
                print("   ", f[:130])
            ok = False
            continue
        alvo = next(PAG.glob(f"linha-{num}-*.json"))
        pag = json.load(open(alvo, encoding="utf-8"))
        pag["secoes"].update(secoes)
        alvo.write_text(json.dumps(pag, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{num}] reescrito e gravado: {alvo.name}")
    print("OK" if ok else "FALHOU")

if __name__ == "__main__":
    main()
