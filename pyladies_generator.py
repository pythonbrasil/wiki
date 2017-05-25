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

import yaml
from slugify import slugify


# Diretório onde serão gerados os arquivos JSON
PAGE_PATH = 'content/pyladies/'

# Site oficial da Pyladies
PYLADIES_SITE = 'http://brasil.pyladies.com'

# Arquivo YML que será consumido para gerar os arquivos JSON
PYLADIES_YAML = 'https://raw.githubusercontent.com/pyladies-brazil/br-pyladies-pelican/master/data/locations.yml'


def scrapping_pyladies():
    """
    Chamado para analisar o YML e retornar uma lista de dicionários
    com os dados das sedes da Pyladies.
    """
    html = urlopen(PYLADIES_YAML).read()
    return yaml.load(html)


def get_filename(directory, locale):
    """
    Chamado para retornar o nome do JSON de cada Pyladies com base
    na sua cidade sede.
    """
    return '%spyladies-%s.json' % (directory, slugify(locale))


def list_pyladies():
    """
    Gera os arquivos JSON no diretório setado em PAGE_PATH.
    """

    if not os.path.exists(PAGE_PATH):
            os.makedirs(PAGE_PATH)

    for item in scrapping_pyladies():
        data = dict()

        data['nome'] = 'Pyladies %s' % item['city']
        data['links'] = list()

        if item.get('image'):
            data['imagem'] = '%s%s' % (PYLADIES_SITE, item['image'])

        if item.get('github'):
            data['links'].append(['Github', item['github']])

        if item.get('facebook'):
            data['links'].append(['Facebook', item['facebook']])

        if item.get('twitter'):
            data['links'].append(['Twitter', item['twitter']])

        if item.get('url'):
            data['links'].append(['Site', item['url']])

        if item.get('email'):
            data['links'].append(['Email', 'mailto:%s' % item['email']])

        if item.get('quitter'):
            data['links'].append(['Quitter', item['quitter']])

        if item.get('telegram'):
            data['links'].append(['Telegram', item['telegram']])

        filename = get_filename(PAGE_PATH, item['city'].lower())

        with open(filename, 'w') as f:
            json.dump(data, f)


if __name__ == '__main__':
    list_pyladies()
