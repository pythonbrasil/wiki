# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive

class WelcomeButton(Directive):
    """ Include a Button

    Usage:
    .. welcome-button:: Title
        :color: css-color
        :target: URL
    """

    required_arguments = 1
    optional_arguments = 3
    option_spec = {
            'color': str,
            'target': str,
            }

    final_argument_whitespace = False
    has_content = True

    def run(self):
        html = '<a class="{} wave-effect waves-light btn" href="{}">{}</a>'
        if 'color' in self.options:
            color = self.options['color']
        else:
            color = 'blue-grey'

        if 'target' in self.options:
            target = self.options['target']
        else:
            target = '#'

        if self.arguments:
            title = ' '.join(self.arguments)
        else:
            title = 'Mais...'

        html = html.format(color, target, title)
        return [nodes.raw('', html, format='html')]

class WelcomeIcon(Directive):
    """ Include a Welcome Icon

    Usage:
    .. welcome-icon:: Title
        :icon: icon-name
        :class: class

        Body text
    """

    required_arguments = 0
    optional_arguments = 2
    option_spec = {
            'icon': str,
            'class': str,
            }

    final_argument_whitespace = False
    has_content = True
    node_class = nodes.TextElement

    def run(self):
        html_class = self.options.get('class', '')
        html = ['<div class="col s12 m4 icon-block {}">'.format(html_class)]
        if 'icon' in self.options:
            icon = '<h3 class="center blue-grey-text text-lighten-1">\n' +\
                   '    <i class="fa {} fa-2x"></i>\n' +\
                   '</h3>'
            html.append(icon.format(self.options['icon']))

        if self.arguments:
            title = ' '.join(self.arguments)
            title = '<h5 class="center">{}</h5>'.format(title)
            html.append(title)

        if self.content:
            text = '\n'.join(self.content)
            body = self.node_class(rawsource=text)
            self.state.nested_parse(self.content, self.content_offset, body)

            if isinstance(body[0], nodes.paragraph):
                html.append('<p class="light">{}</p>'.format(body[0].astext()))
                buttons = body[1:]
            else:
                buttons = body

            if buttons:
                pre_html = ['<div class="center">']
                for button in buttons:
                    pre_html.append(button.astext())
                pre_html.append("</div>")
                pre_html = "\n".join(pre_html)
                html.append(pre_html)

        html.append("</div>")
        html = "\n".join(html)
        return [nodes.raw('', html, format='html')]

class WelcomeSection(Directive):
    """ Include a Welcome Section

    Usage:
    .. welcome-section:: Title
        :color: css color

        Body text including home icons
    """

    required_arguments = 0
    optional_arguments = 20
    option_spec = {
            'color': str,
            }

    final_argument_whitespace = False
    has_content = True
    node_class = nodes.TextElement

    def run(self):
        html = []
        if 'color' in self.options:
            color_class = self.options['color']
            html.append('<div class="{}">'.format(color_class))
        else:
            html.append('<div class="white">')

        html.append('<div class="container content-container ">')
        html.append('<div class="section">')

        if self.arguments:
            title = ' '.join(self.arguments)
            title = '<h2 class="center">{}</h2>'.format(title)
            html.append(title)

        html.append('<div class="row">')

        if self.content:
            text = '\n'.join(self.content)
            body = self.node_class(rawsource=text)
            self.state.nested_parse(self.content, self.content_offset, body)
            html.append(body.astext())

        html.append("</div>")
        html.append("</div>")
        html.append("</div>")
        html.append("</div>")
        html = "\n".join(html)
        return [nodes.raw('', html, format='html')]


def register():
    directives.register_directive('welcome-icon', WelcomeIcon)
    directives.register_directive('welcome-section', WelcomeSection)
    directives.register_directive('welcome-button', WelcomeButton)
