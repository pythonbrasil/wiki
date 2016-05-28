'''
bootstrapify
===================================
This pelican plugin adds css classes to nonstatic html output.

This is especially useful if you want to use bootstrap and want
to add its default classes to your tables and images.
'''

from bs4 import BeautifulSoup
from pelican import signals, contents


def set_default_config(settings, bootstrapify_default):
    settings.setdefault('BOOTSTRAPIFY', bootstrapify_default)


def init_default_config(pelican):
    from pelican.settings import DEFAULT_CONFIG
    bootstrapify_default = {
        'table': ['table', 'table-striped', 'table-hover'],
        'img': ['img-responsive']
    }

    set_default_config(DEFAULT_CONFIG, bootstrapify_default)
    if(pelican):
        set_default_config(pelican.settings, bootstrapify_default)


def replace_in_with(searchterm, soup, attributes):
    for item in soup.select(searchterm):
        attribute_set = set(item.attrs.get('class', []) + attributes)
        item.attrs['class'] = list(attribute_set)


def bootstrapify(content):
    if isinstance(content, contents.Static):
        return

    replacements = content.settings['BOOTSTRAPIFY']
    soup = BeautifulSoup(content._content, 'html.parser')

    for selector, classes in replacements.items():
        replace_in_with(selector, soup, classes)

    content._content = soup.decode()


def register():
    signals.initialized.connect(init_default_config)
    signals.content_object_init.connect(bootstrapify)
