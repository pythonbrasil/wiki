#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de teste simples para validar o site antes de aceitar PRs.

Validações:
- Verifica presença de JSON na página (indicando erro de parser)
- Valida estrutura básica do HTML
- Opcionalmente verifica links 404 com requests

Uso: python test_site.py
"""

import sys
import re
from pathlib import Path


def check_json_in_html(filepath):
    """Verifica se há JSON exposto no HTML (indicando erro de parser)."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

        # Procura padrões de JSON fora de tags script
        if re.search(r'(?<!<script[^>]*>)\{["\'][a-z_]+["\']\s*:\s*["\']', content):
            return ["JSON exposto detectado"]
    return []


def check_html_structure(filepath):
    """Valida estrutura básica do HTML."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read().lower()

        # Ignora redirects
        if 'http-equiv="refresh"' in content:
            return []

        issues = []
        if '<html' not in content:
            issues.append("Tag <html> ausente")
        if '<body' not in content:
            issues.append("Tag <body> ausente")
        return issues


def check_links_404():
    """Verifica links 404 (requer requests)."""
    try:
        import requests
    except ImportError:
        print("Instale 'requests' para verificar links: pip install requests")
        return True

    try:
        r = requests.get('http://localhost:8000', timeout=5)
        # Extrai links básicos com regex
        links = re.findall(r'href=["\']([^"\']+)["\']', r.text)

        errors = []
        for link in set(links[:20]):  # Limita a 20
            if link.startswith(('http', '/', '#')) and not link.startswith('#'):
                url = link if link.startswith('http') else f'http://localhost:8000{link}'
                try:
                    resp = requests.head(url, timeout=3, allow_redirects=True)
                    if resp.status_code == 404:
                        errors.append(f"404: {url}")
                except:
                    pass

        if errors:
            print("\nLinks 404 encontrados:")
            for e in errors:
                print(f"  {e}")
            return False
        print("\nLinks verificados OK")
        return True
    except:
        print("\nServidor nao disponivel. Execute 'make serve' primeiro.")
        return True


def main():
    print("=" * 50)
    print("Teste do Site - Python Brasil")
    print("=" * 50)

    output_dir = Path('output')
    if not output_dir.exists():
        print("\nDiretorio 'output' nao existe. Execute 'make html'")
        sys.exit(1)

    html_files = list(output_dir.rglob('*.html'))
    print(f"\n{len(html_files)} arquivos HTML encontrados\n")

    errors, warnings = [], []

    for html_file in html_files:
        path = html_file.relative_to(output_dir)

        # Verifica JSON exposto
        json_issues = check_json_in_html(html_file)
        for issue in json_issues:
            warnings.append(f"AVISO: {path}: {issue}")

        # Verifica estrutura
        html_issues = check_html_structure(html_file)
        for issue in html_issues:
            errors.append(f"ERRO: {path}: {issue}")

    if errors:
        print("ERROS:")
        for e in errors[:10]:
            print(f"  {e}")
        if len(errors) > 10:
            print(f"  ... +{len(errors)-10} erros")

    if warnings:
        print("\nAVISOS:")
        for w in warnings[:5]:
            print(f"  {w}")
        if len(warnings) > 5:
            print(f"  ... +{len(warnings)-5} avisos")

    if not errors and not warnings:
        print("Nenhum problema encontrado!")

    # Verifica links se --check-links
    links_ok = True
    if '--check-links' in sys.argv:
        links_ok = check_links_404()

    print("\n" + "=" * 50)
    if not errors and links_ok:
        print("TESTES OK")
        print("=" * 50)
        sys.exit(0)
    else:
        print("TESTES FALHARAM")
        print("=" * 50)
        sys.exit(1)


if __name__ == '__main__':
    main()
