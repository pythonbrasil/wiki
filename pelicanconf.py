#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import datetime
import glob
import json
import os
import sys

sys.path.append(os.curdir)

from collections import OrderedDict

from baseconf import *

# Configurações Base
SITENAME = 'Python Brasil'
AUTHOR = 'Python Brasil'
THEME = 'themes/pybr'

# Referências à Github
GITHUB_REPO = 'https://github.com/pythonbrasil/wiki'
GITHUB_BRANCH = 'pelican'

# Referencia ao Google Groups
GOOGLE_GROUPS_MAIL_LIST_NAME = 'python-brasil'

# GOOGLE_ANALYTICS
GOOGLE_ANALYTICS_CODE = None

# https://www.google.com/webmasters/tools/
# https://support.google.com/webmasters/answer/35659?hl=pt&ref_topic=4564314
GOOGLE_SITE_VERIFICATION_METATAG_CODE = None

# Imagens
ARTICLE_BANNERS_FOLDER = 'images/banners'

# Home settings
WELCOME_TITLE = 'Python Brasil'
WELCOME_TEXT = (
    'A comunidade Python Brasil reune grupos de usuários em todo '
    'o Brasil interessados em difundir e divulgar a linguagem de programação.'
)
FOOTER_ABOUT = (
    'Este site busca reunir todo o conteúdo produzido e traduzido pela '
    'comunidade brasileira bem como informações relevantes em relação a mesma.'
)

# Statics
STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/pages',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/pages/denuncia.html': {'path': 'denuncia/index.html'},
}

PAGE_EXCLUDES = ARTICLE_EXCLUDES = [
    'extra/pages',
]

# Tema do Syntax Hightlight
PYGMENTS_STYLE = 'monokai'

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        "title": "Impressione-se",
        "href": "#",
        "desc": "Descubra como Python está presente em seu dia-a-dia.",
        "children": [
            {
                "title": "Empresas",
                "href": "empresas",
            },
            {
                "title": "Projetos Brasileiros",
                "href": "projetos",
            },
        ],
    },
    {
        "title": "Inicie-se",
        "href": "#",
        "desc": "Veja como é fácil começar a usar a linguagem.",
        "children": [
            {
                "title": "Introdução",
                "href": "introducao",
            },
            {
                "title": "Qual Python?",
                "href": "qual-python",
            },
            {
                "title": "Download do python",
                "href": "https://www.python.org/downloads/",
            },
            {
                "title": "Instalação Linux",
                "href": "instalacao-linux",
            },
            {
                "title": "Instalação Mac",
                "href": "instalacao-mac",
            },
            {
                "title": "Instalação Windows",
                "href": "instalacao-windows",
            },
            {
                "title": "Ferramentas",
                "href": "ferramentas",
            },
        ],
    },
    {
        "title": "Aprenda mais",
        "href": "#",
        "desc": (
            "Conheça mais sobre a linguagem e torne-se um " "verdadeiro pythonista."
        ),
        "children": [
            {
                "title": "Web",
                "href": "web",
            },
            {
                "title": "Mobile",
                "href": "mobile",
            },
            {
                "title": "Games",
                "href": "games",
            },
            {
                "title": "Científico",
                "href": "cientifico",
            },
            {
                "title": "Wiki",
                "href": "wiki",
            },
        ],
    },
    {
        "title": "Participe",
        "href": "#",
        "desc": (
            "Encontre e participe da comunidade e compartilhe " "suas dúvidas e idéias."
        ),
        "children": [
            {
                "title": "Lista de Discussões",
                "href": "lista-de-discussoes",
            },
            {
                "title": "Comunidades Locais",
                "href": "comunidades-locais",
            },
            {
                "title": "Pyladies",
                "href": "pyladies",
            },
            {
                "title": "Eventos",
                "href": "https://eventos.python.org.br",
            },
            {
                "title": "Contribua",
                "href": "contribua",
            },
            {
                "title": "Tradução",
                "href": "traducao",
            },
        ],
    },
    {
        "title": "APyB",
        "href": "https://apyb.python.org.br/",
        "desc": "Conheça a Associação Python Brasil.",
    },
]

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        "href": "https://github.com/pythonbrasil",
        "icon": "fa-github",
        "text": "GitHub",
    },
    {
        "href": "https://twitter.com/pythonbrasil",
        "icon": "fa-twitter",
        "text": "Twitter",
    },
    {
        "href": "https://www.instagram.com/pythonbrasil/",
        "icon": "fa-instagram",
        "text": "Instagram",
    },
    {
        "href": "https://www.facebook.com/groups/python.brasil",
        "icon": "fa-facebook-official",
        "text": "Facebook",
    },
    {
        "href": "https://groups.google.com/forum/#!forum/python-brasil",
        "icon": "fa-users",
        "text": "Lista de Discussões",
    },
    {"href": "https://t.me/pythonbrasil", "icon": "fa-paper-plane", "text": "Telegram"},
    {
        "href": "https://planet.python.org.br/",
        "icon": "fa-globe",
        "text": "Planet Python",
    },
)


def date_hook(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = datetime.datetime.strptime(
                value, "%Y-%m-%d").date()
        except:
            pass
    return json_dict


def ordena_por_regiao(empresas):
    por_regiao = {}
    for empresa in empresas:
        regiao = empresa['regiao']
        estado = empresa['estado']

        por_estado = por_regiao.get(regiao, {})
        no_estado = por_estado.get(estado, [])

        no_estado.append(empresa)
        por_estado[estado] = no_estado
        por_regiao[regiao] = por_estado

    empresas_ordenadas = OrderedDict()
    for regiao in sorted(por_regiao):
        empresas_ordenadas[regiao] = OrderedDict()
        for estado in sorted(por_regiao[regiao]):
            no_estado = por_regiao[regiao][estado]
            no_estado.sort(key=lambda x: x['nome'])
            no_estado.sort(key=lambda x: x['cidade'])
            empresas_ordenadas[regiao][estado] = no_estado
    return empresas_ordenadas


# Configurações da página de comunidades locais
COMUNIDADES_LOCAIS = [
    json.load(open(fname, 'r'))
    for fname in glob.glob('content/comunidades-locais/*.json')
]
DEFAULT_COMMUNITY_IMAGE = "images/comunidades-locais/default.png"

# Configurações da página de empresas
# EMPRESAS = import_empresas('content/empresas/*.json')
EMPRESAS = [
    json.load(open(fname, 'r'))
    for fname in glob.glob('content/empresas/*.json')
]
EMPRESAS = ordena_por_regiao(EMPRESAS)
DEFAULT_EMPRESA_IMAGE = "images/empresas/default.png"

# Configurações da página das pyladies
PYLADIES = [
    json.load(open(fname, 'r'))
    for fname in glob.glob('content/pyladies/*.json')
]
DEFAULT_PYLADIES_IMAGE = "images/pyladies/default.png"
