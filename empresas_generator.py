#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json
import os

try:
    # python 2
    from urllib2 import urlopen
except ImportError:
    # python 3
    from urllib.request import urlopen

from slugify import slugify


# Diretório onde serão gerados os arquivos JSON
PAGE_PATH = 'content/empresas/'

# Arquivo que será consumido para gerar os arquivos JSON
EMPRESAS_FILE = 'https://raw.githubusercontent.com/pythonbrasil/pyBusinesses-BR/master/README.md'
EMPRESAS_LOGO_PATH = 'https://raw.githubusercontent.com/pythonbrasil/pyBusinesses-BR/master/'

def scrapping_empresas():
    file = urlopen(EMPRESAS_FILE)
    file = file.read().decode()
    region = state = city = ''
    empresas = []

    for line in file.split('\n'):
        if line.startswith('## '):
            region = line[2:].strip()
        elif line.startswith('### '):
            state =  line[3:].strip()
        elif line.startswith('#### '):
            city =  line[4:].strip()
        elif line.startswith('!') and region and state and city:
            parts = line.split('|')
            site = parts[2].split('(')[1].strip().strip(')')
            name = parts[1].strip()
            logo = EMPRESAS_LOGO_PATH + parts[0].split(
                '(')[1].strip().strip(')')

            empresas.append({
                'nome': name,
                'regiao': region,
                'estado': state,
                'cidade': city,
                'site': site,
                'logo': logo,
            })

    return empresas


if __name__ == '__main__':
    for empresa in scrapping_empresas():
        filename = '{0}-{1}.json'.format(
            slugify(empresa['nome']), slugify(empresa['cidade']))

        if not os.path.exists(PAGE_PATH):
            os.makedirs(PAGE_PATH)

        with open(os.path.join(PAGE_PATH, filename), 'w') as file:
            json.dump(empresa, file)
