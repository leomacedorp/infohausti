#!/usr/bin/env python3
"""
ENGROSSA PÁGINAS DE PONTOS TURÍSTICOS COM DADOS VERIFICADOS — 2026-10-06
Contexto: 13 páginas abaixo do mínimo de 800 palavras narrativas.
Método: adiciona secoes_extras com dados 'verificado' dos dossiês
(content/dados-fonte/pontos/[slug].json). Nada inventado: cada linha deriva
de campo verificado com fonte_url. Campo pendente NÃO aparece.
Edita os JSON de página (content/paginas/ribeirao-preto/pontos-turisticos/).
Depois: regenerar via gera_pontos_lote.py é desnecessário — o build lê o JSON.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOSSIES = ROOT / 'content' / 'dados-fonte' / 'pontos'
PAGES = ROOT / 'content' / 'paginas' / 'ribeirao-preto' / 'pontos-turisticos'

# slug -> (titulo da seção extra, [(campo do dossiê, rótulo na página)])
PLANO = {
    'basilica-santo-antonio-de-padua': (
        'Planeje sua visita à Basílica',
        [('horario_visita', 'Horário de missas'),
         ('programacao', 'Confissões e atendimento'),
         ('telefone', 'Telefone'),
         ('status_atual', 'Status paroquial')]),
    'centro-cultural-palace': (
        'Detalhes operacionais',
        [('programacao', 'Programação'),
         ('telefone', 'Telefones'),
         ('status_atual', 'Status atual'),
         ('historia', 'História documentada')]),
    'estacao-barracao': (
        'Detalhes operacionais',
        [('status_atual', 'Status e intervenções recentes'),
         ('historia', 'História documentada')]),
    'igreja-sao-benedito': (
        'Planeje sua visita',
        [('horario_visita', 'Missas'),
         ('programacao', 'Adoração ao Santíssimo'),
         ('telefone', 'Telefone'),
         ('status_atual', 'Status paroquial')]),
    'mercado-municipal': (
        'Detalhes operacionais',
        [('horario_visita', 'Horário de funcionamento'),
         ('capacidade', 'Boxes e estrutura'),
         ('telefone', 'Telefone'),
         ('status_atual', 'Status atual')]),
    'palacio-rio-branco': (
        'Detalhes operacionais',
        [('status_atual', 'Status — obras em andamento'),
         ('capacidade', 'Dimensões documentadas'),
         ('telefone', 'Telefone'),
         ('historia', 'História documentada')]),
    'paroquia-santa-rita-de-cassia': (
        'Planeje sua visita',
        [('horario_visita', 'Missas por dia da semana'),
         ('programacao', 'Secretaria paroquial'),
         ('telefone', 'Telefone'),
         ('status_atual', 'Status paroquial')]),
    'paroquia-santa-teresinha-doutora': (
        'Planeje sua visita',
        [('horario_visita', 'Missas por dia da semana'),
         ('programacao', 'Secretaria paroquial'),
         ('telefone', 'Telefone'),
         ('status_atual', 'Status paroquial')]),
    'santuario-nossa-senhora-do-rosario': (
        'Planeje sua visita',
        [('horario_visita', 'Missas por dia da semana'),
         ('programacao', 'Secretaria paroquial'),
         ('telefone', 'Telefone'),
         ('status_atual', 'Status paroquial')]),
    'sesc-ribeirao-preto': (
        'Detalhes operacionais',
        [('programacao', 'Programação'),
         ('status_atual', 'Status atual'),
         ('historia', 'História documentada')]),
    'teatro-de-arena': (
        'Detalhes operacionais',
        [('capacidade', 'Capacidade e estrutura'),
         ('programacao', 'Programação'),
         ('status_atual', 'Reabertura e status'),
         ('historia', 'História documentada')]),
    'teatro-municipal': (
        'Detalhes operacionais',
        [('capacidade', 'Capacidade do auditório'),
         ('programacao', 'Programação'),
         ('status_atual', 'Status atual'),
         ('historia', 'História documentada')]),
}


def valor_verificado(dossie, campo):
    """Retorna o valor apenas se status == 'verificado' e valor não vazio."""
    f = dossie.get(campo)
    if isinstance(f, dict) and f.get('status') == 'verificado' and f.get('valor'):
        return f['valor']
    return None


def montar_conteudo(dossie, campos):
    partes = []
    for campo, rotulo in campos:
        val = valor_verificado(dossie, campo)
        if val:
            partes.append(f'<p><strong>{rotulo}:</strong> {val}</p>')
    if not partes:
        return None
    return ''.join(partes)


def aplicar(slug, titulo, campos):
    page_path = PAGES / f'{slug}.json'
    dossie_path = DOSSIES / f'{slug}.json'
    if not page_path.exists():
        print(f'[skip] {slug}: página não existe')
        return False
    if not dossie_path.exists():
        print(f'[skip] {slug}: dossiê não existe')
        return False
    dossie = json.loads(dossie_path.read_text(encoding='utf-8'))
    page = json.loads(page_path.read_text(encoding='utf-8'))
    conteudo = montar_conteudo(dossie, campos)
    if conteudo is None:
        print(f'[skip] {slug}: nenhum dado verificado a acrescentar')
        return False
    secoes = page.get('secoes_extras')
    if not isinstance(secoes, list):
        secoes = []
    # substitui seção de mesmo título, se já existir (idempotente)
    secoes = [s for s in secoes if isinstance(s, dict) and s.get('titulo') != titulo]
    secoes.append({'titulo': titulo, 'conteudo': conteudo})
    page['secoes_extras'] = secoes
    page_path.write_text(json.dumps(page, ensure_ascii=False, indent=1), encoding='utf-8')
    n = len(conteudo.split('</p>')) - 1
    print(f'[ok] {slug}: seção "{titulo}" com {n} blocos verificados')
    return True


def main():
    total = 0
    for slug, (titulo, campos) in PLANO.items():
        if aplicar(slug, titulo, campos):
            total += 1
    print(f'\n[RESUMO] {total} página(s) engrossada(s) com dados verificados dos dossiês')


if __name__ == '__main__':
    main()
