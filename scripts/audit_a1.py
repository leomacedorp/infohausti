#!/usr/bin/env python3
"""
Auditoria mínima do Bloco A1 - Verificação da estrutura básica
"""

import os
import sys
import json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def check_structure():
    """Verifica se a estrutura básica foi criada corretamente"""
    root = Path('.')
    required_paths = [
        'content',
        'content/paginas', 
        'content/dados-fonte',
        'templates',
        'partials',
        'assets',
        'assets/css',
        'assets/js',
        'assets/img',
        'scripts',
        'reports'
    ]
    
    missing = []
    for path in required_paths:
        if not (root / path).exists():
            missing.append(path)
    
    return missing

def check_files():
    """Verifica se os arquivos obrigatórios foram criados"""
    root = Path('.')
    required_files = [
        'README.md',
        'PENDENCIAS.md', 
        'LOG.md',
        '.gitignore',
        'content/status.json'
    ]
    
    missing = []
    for file in required_files:
        if not (root / file).exists():
            missing.append(file)
    
    return missing

def check_gitignore():
    """Verifica se o .gitignore contém os padrões necessários"""
    gitignore_path = Path('.gitignore')
    if not gitignore_path.exists():
        return ['.gitignore ausente']
    
    content = gitignore_path.read_text()
    required_patterns = ['dist/', '*.log', '.DS_Store', 'Thumbs.db']
    
    missing = []
    for pattern in required_patterns:
        if pattern not in content:
            missing.append(pattern)
    
    return missing

def check_status_json():
    """Verifica se o content/status.json é válido JSON e vazio"""
    try:
        with open('content/status.json', 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return ['content/status.json não é um objeto JSON válido']
            return []
    except json.JSONDecodeError:
        return ['content/status.json contém JSON inválido']
    except FileNotFoundError:
        return ['content/status.json não existe']

def main():
    print("🔍 [AUDITORIA A1] Verificando estrutura básica...\n")
    
    all_issues = []
    
    # Verificar estrutura
    structure_issues = check_structure()
    if structure_issues:
        all_issues.append(f"📁 Pastas faltantes: {', '.join(structure_issues)}")
    
    # Verificar arquivos
    file_issues = check_files()
    if file_issues:
        all_issues.append(f"📄 Arquivos faltantes: {', '.join(file_issues)}")
    
    # Verificar gitignore
    gitignore_issues = check_gitignore()
    if gitignore_issues:
        all_issues.append(f"⚠️  Padrões .gitignore faltantes: {', '.join(gitignore_issues)}")
    
    # Verificar status.json
    status_issues = check_status_json()
    if status_issues:
        all_issues.extend(status_issues)
    
    if all_issues:
        print("❌ AUDITORIA FALHOU:")
        for issue in all_issues:
            print(f"  {issue}")
        return False
    else:
        print("✅ AUDITORIA A1 APROVADA:")
        print("  - Toda a estrutura básica foi criada corretamente")
        print("  - Todos os arquivos obrigatórios estão presentes")
        print("  - O .gitignore contém os padrões necessários")
        print("  - O content/status.json é válido JSON")
        return True

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)