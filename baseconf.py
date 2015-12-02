#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### Base settings
SITEURL = ''
DEFAULT_LANG = u'pt'
DEFAULT_PAGINATION = False
TIMEZONE = 'America/Sao_Paulo'
SUMMARY_MAX_LENGTH = 35

### URL and Page generation settings
ARTICLE_URL = 'eventos/{slug}'
ARTICLE_SAVE_AS = 'eventos/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'eventos/categorias'
CATEGORIES_SAVE_AS = 'eventos/categorias/index.html'
CATEGORY_URL = 'eventos/categorias/{slug}'
CATEGORY_SAVE_AS = 'eventos/categorias/{slug}/index.html'

TAG_URL = 'eventos/tags/{slug}'
TAG_SAVE_AS = 'eventos/tags/{slug}/index.html'
TAGS_URL = 'eventos/tags'
TAGS_SAVE_AS = 'eventos/tags/index.html'

AUTHOR_URL = 'eventos/autores/{slug}'
AUTHOR_SAVE_AS = 'eventos/autores/{slug}/index.html'
AUTHORS_URL = 'eventos/autores'
AUTHORS_SAVE_AS = 'eventos/autores/index.html'

INDEX_SAVE_AS = "eventos/index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

### Feed settings
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

## Plugins
PLUGIN_PATHS = ['./.plugins']
PLUGINS = [
        'better_figures_and_images',
        'sitemap',
        'welcome-helpers',
        ]

# Plugins settings
RESPONSIVE_IMAGES = True
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    },
}
