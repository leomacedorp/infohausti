#!/usr/bin/env python3
"""
ORQUESTRADOR GERAL DE AUDITORIA — INFOHAUS RP (scripts/audit_all.py)
Executa todas as verificações de conformidade do Manual v1.2:
- Links internos e proibição de href="#" (check_links)
- SEO, títulos e canonical absoluto (check_seo)
- Schema.org JSON-LD e regra de 3+ perguntas no FAQ (check_schema)
- Acessibilidade WCAG 2.1 AA (check_a11y)
- Similaridade em duas passadas (check_similaridade)
- Bloqueio de dados pendentes em páginas prontas (check_pendentes)
- Mínimos de palavras por template (check_palavras)

Classifica em FATAL (impeditivo) e AVISO (revisão humana).
Grava relatório em reports/ e retorna código de saída diferente de zero se houver fatal.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT_DIR / 'reports'

# Importa módulos de checagem
try:
    from check_links import check_links
    from check_seo import check_seo
    from check_schema import check_schema
    from check_a11y import check_a11y
    from check_similaridade import check_similaridade
    from check_pendentes import check_pendentes
    from check_palavras import check_palavras
    from check_qualidade_texto import check_qualidade_texto
    from check_dist_stale import check_dist_stale
    from check_fontes_factuais import check_fontes_factuais_suite
    from check_fontes_factuais import check_pontos_factuais_suite
    from check_fontes_factuais import check_bairros_factuais_suite
except ImportError:
    # Adiciona pasta scripts ao path
    sys.path.insert(0, str(ROOT_DIR / 'scripts'))
    from check_links import check_links
    from check_seo import check_seo
    from check_schema import check_schema
    from check_a11y import check_a11y
    from check_similaridade import check_similaridade
    from check_pendentes import check_pendentes
    from check_palavras import check_palavras
    from check_qualidade_texto import check_qualidade_texto
    from check_dist_stale import check_dist_stale
    from check_fontes_factuais import check_fontes_factuais_suite
    from check_fontes_factuais import check_pontos_factuais_suite
    from check_fontes_factuais import check_bairros_factuais_suite

def run_full_audit():
    print("==================================================")
    print("   SUÍTE DE AUDITORIA AUTOMÁTICA (audit_all.py)   ")
    print("   Base: Manual de Execução em Blocos v1.2       ")
    print("==================================================")

    all_fatals = []
    all_avisos = []

    checks = [
        ("Links e Âncoras", check_links),
        ("SEO e Canonical Absoluto", check_seo),
        ("Schema.org JSON-LD & FAQs", check_schema),
        ("Acessibilidade WCAG AA", check_a11y),
        ("Similaridade em Duas Passadas", check_similaridade),
        ("Bloqueio de Dados Pendentes", check_pendentes),
        ("Mínimos de Palavras por Template", check_palavras),
        ("Qualidade Editorial e Anti-Spinning", check_qualidade_texto),
        ("Dist Stale (dist em dia com content)", check_dist_stale),
        ("Fontes Factuais (linhas)", check_fontes_factuais_suite),
        ("Fontes Factuais (pontos turísticos)", check_pontos_factuais_suite),
        ("Fontes Factuais (bairros)", check_bairros_factuais_suite)
    ]

    for name, check_fn in checks:
        print(f"\n[*] Executando checagem: {name}...")
        try:
            fatals, avisos = check_fn()
            all_fatals.extend(fatals)
            all_avisos.extend(avisos)

            if fatals:
                print(f"  [X] {len(fatals)} erro(s) fatal(is) detectado(s).")
            elif avisos:
                print(f"  [!] Aprovado com {len(avisos)} aviso(s).")
            else:
                print("  [V] 100% aprovado.")
        except Exception as e:
            msg = f"Falha na execução de {name}: {e}"
            print(f"  [X] {msg}")
            all_fatals.append(f"[FATAL] {msg}")

    # Monta relatório
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = REPORTS_DIR / f"audit_{timestamp}.txt"
    latest_filename = REPORTS_DIR / "audit_latest.txt"

    lines = []
    lines.append(f"RELATÓRIO DE AUDITORIA AUTOMÁTICA INFOHAUS RP")
    lines.append(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Status Final: {'FALHOU (FATAL)' if all_fatals else 'APROVADO'}")
    lines.append("=" * 60)
    lines.append(f"Total de Erros Fatais: {len(all_fatals)}")
    lines.append(f"Total de Avisos: {len(all_avisos)}")
    lines.append("-" * 60)

    if all_fatals:
        lines.append("\n🔴 ERROS FATAIS (BLOQUEIAM COMMIT E PUBLICAÇÃO):")
        for f in all_fatals:
            lines.append(f"  - {f}")

    if all_avisos:
        lines.append("\n⚠️ AVISOS (REQUEREM REVISÃO HUMANA):")
        for a in all_avisos:
            lines.append(f"  - {a}")

    if not all_fatals and not all_avisos:
        lines.append("\n🟢 NENHUMA NÃO-CONFORMIDADE ENCONTRADA. TODAS AS PÁGINAS APROVADAS.")

    report_text = "\n".join(lines)

    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(report_text)
    with open(latest_filename, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print("\n" + "=" * 60)
    print(f"Relatório gravado em: {report_filename.relative_to(ROOT_DIR)}")
    print(f"Resultado: {'❌ STATUS: FALHOU' if all_fatals else '✅ STATUS: OK'}")
    print("=" * 60)

    return len(all_fatals) == 0

def main():
    success = run_full_audit()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
