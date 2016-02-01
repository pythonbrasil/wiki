#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys
import glob
import json
import datetime

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
WELCOME_TEXT = 'A comunidade Python Brasil reune grupos de usuários em todo o Brasil interessados em difundir e divulgar a linguagem de programação.'
FOOTER_ABOUT = 'Este site busca reunir todo o conteúdo produzido e traduzido pela comunidade brasileira bem como informações relevantes em relação a mesma.'

# Tema do Syntax Hightlight
PYGMENTS_STYLE = 'perldoc'

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        'title': 'Impressione-se',
        'href': 'impressione-se',
        'desc': 'Descubra como Python está presente em seu dia-a-dia.',
    },
    {
        'title': 'Inicie-se',
        'href': 'inicie-se',
        'desc': 'Veja como é fácil começar a usar a linguagem.',
    },
    {
        'title': 'Aprenda mais',
        'href': 'aprenda-mais',
        'desc': 'Conheça mais sobre a linguagem e torne-se um verdadeiro pythonista.',
    },
    {
        'title': 'Participe',
        'href': '#',
        'desc': 'Encontre e participe da comunidade e compartilhe suas dúvidas e idéias.',
        'children': [
            {
                'title': 'Lista de Discussões',
                'href': 'lista-de-discussoes',
            },
            {
                'title': 'Comunidades Locais',
                'href': 'comunidades-locais',
            },
            {
                'title': 'Eventos',
                'href': 'eventos',
            },
            {
                'title': 'Conferência Python Brasil',
                'href': 'python-brasil',
            },
            {
                'title': 'A APyB',
                'href': 'apyb',
            },
        ]
    },
]

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        'href': 'https://github.com/pythonbrasil',
        'icon': 'fa-github',
        'text': 'GitHub',
    },
    {
        'href': 'https://twitter.com/pythonbrasil',
        'icon': 'fa-twitter',
        'text': 'Twitter',
    },
    {
        'href': 'https://www.facebook.com/groups/python.brasil',
        'icon': 'fa-facebook-official',
        'text': 'Facebook',
    },
    {
        'href': 'https://groups.google.com/forum/#!forum/python-brasil',
        'icon': 'fa-users',
        'text': 'Lista de Discussões',
    },
)

def date_hook(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = datetime.datetime.strptime(value, "%Y-%m-%d")
        except:
            pass
    return json_dict

EVENTOS = [json.load(open(fname, 'r'), object_hook=date_hook) for fname in glob.glob('content/eventos/*/*.json')]
COMUNIDADES_LOCAIS = [json.load(open(fname, 'r')) for fname in glob.glob('content/comunidades-locais/*.json')]
DEFAULT_COMMUNITY_IMAGE = "images/comunidades-locais/default.png"
