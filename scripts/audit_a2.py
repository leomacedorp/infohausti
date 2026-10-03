#!/usr/bin/env python3
"""
Auditoria do Bloco A2 - CSS e JS base
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def audit_a2():
    css_path = Path('assets/css/base.css')
    js_path = Path('assets/js/base.js')

    issues = []

    if not css_path.exists():
        issues.append("Arquivo assets/css/base.css não encontrado.")
    else:
        css = css_path.read_text(encoding='utf-8')
        required_css_tokens = [
            '--color-bg',
            '--color-text',
            '--color-primary',
            ':focus-visible',
            '.skip-link',
            'WCAG',
            '375px'
        ]
        for token in required_css_tokens:
            if token not in css:
                issues.append(f"Token/Regra '{token}' ausente em assets/css/base.css")

    if not js_path.exists():
        issues.append("Arquivo assets/js/base.js não encontrado.")
    else:
        js = js_path.read_text(encoding='utf-8')
        required_js_features = [
            'initMobileMenu',
            'initBackToTop',
            'initLgpdBanner',
            'aria-expanded'
        ]
        for feat in required_js_features:
            if feat not in js:
                issues.append(f"Função/Recurso '{feat}' ausente em assets/js/base.js")

    if issues:
        print("[ERRO] AUDITORIA A2 FALHOU:")
        for iss in issues:
            print(f"  - {iss}")
        return False

    print("[OK] AUDITORIA A2 APROVADA:")
    print("  - assets/css/base.css possui design tokens, contraste WCAG AA documentado e skip link")
    print("  - assets/js/base.js possui menu mobile acessivel, voltar ao topo e banner LGPD")
    return True

if __name__ == '__main__':
    ok = audit_a2()
    sys.exit(0 if ok else 1)
