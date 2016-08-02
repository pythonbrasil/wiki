
Como colaborar com a traduzição
-------------------------------

Para traduzir, faça o cadastro no transifex e entre nas urls:

https://www.transifex.com/django/django-docs/dashboard/

https://www.transifex.com/django/django-docs/language/pt_BR/


Você pode também participar da lista de e-mails para 
discussão sobre tradução do django:

https://groups.google.com/d/forum/django-i18n

https://docs.djangoproject.com/en/dev/internals/contributing/localizing/#documentation


o Luciano Ramalho e mais uma galera, criaram algumas dicas para quando eles estavam traduzindo o tutorial oficial do Python 2.7. Talvez algumas dessas dicas também sirvam para ajudar a traduzir a documentação do django.

http://turing.com.br/pydoc/2.7/glossary.html#glossary

http://turing.com.br/pydoc/2.7/tutorial/NOTAS.html#notas-para-os-tradutores-da-versao-pt-br

Se vc tem pouco tempo, alguns minutos, tente o tópico [faq]

[faq] https://www.transifex.com/django/django-docs/translate/#pt_BR/


Hoje algumas partes estão totalmente traduzidas. Mas toda vez que tem um release novo do Django, os textos ficam obsoletos, ao menos em parte, e tem que ser revistos. Então é um trabalho que nunca acaba.

O que traduzir
--------------

Ao ler a documentção do Django seria comum se confundisse

Model: Modelo -- Classe que representa uma tabela.
Module: Módulo -- Módulo Python, e dentro do Django ainda pode ser o nome de uma Django "app".


Atento aos nomes inerentes ao objeto da tradução
------------------------------------------------

A maioria dos termos de computação vem do inglês. E muitas vezes os temor em inglês ne não nos damos conta, ou pior, usamos uma tradução cujo o sentido da palbra em portuges é outro


Cuidado com os artigos
----------------------

Algumas vezes encontramos textos referenciando classe ou métodos por exemplo, onde descrevem o nome destes mas não explicitam que se referem a uma classe ou método. Como durante a traduçao temos as marcações de RestruturedText, temos uma ajuda para saber se por exemplo usamos um artigo feminino ou masculino. Como no texto abaixo.

    Or use a common ancestor to hold the :class:`~django.db.models.AutoField`::

alguém poderia traduzir como usando o artigo "o" referindo-se ao "autoField":

    Ou use um acestral comum para manter o :class:`~django.db.models.AutoField`::"

Mas não seria correto. Talvez para um leitor menos atento fique até estranho,
o que é bom pois o chamará atenção se usarmos um artigo feminino neste caso.

    Ou use um acestral comum para manter a :class:`~django.db.models.AutoField`::"

quer dizer, `ou use um acestral comum para a manter a classe `~django.db.models.AutoField``

Depois do texto renderizado, a  diretiva `\:class:\` não é mostrada, e usar o artigo correto ajuda a lembrar que referenciamos uma classe ou método por exemplo.


Não tente explicar mais que o Autor original
--------------------------------------------

Cuidado ao achar que um texto em inglês não está bem explicado, ou falta detalhes. Você pode ter razão, e a solução é sugerir melhorias no texto original.

Se ao invés disso,  tentar escrever um texto melhor na tradução,
além do problema raiz persistir, pode acontecer de estar sendo repetitivo.

O erro no texto original pode existir, mas antes de afirmá-lo, procure ler o contexto todo e entender se aquele detalhe ou explicaç ao deveria estar ali, ou já foi comentado emoutra seção,
ou se é realmente papel do texto explicar em detalhes tal condição.

---------------------------------

Notas do Cadu


Parser:
    Análisador sintática - é o processo de analisar uma sequência de entrada segundo uma grmática formal. 

auto-escaping : 
    auto substituição.

template: 
    modelo (mas dentro do contexto do django pode ser confundido como o modelo da classe Model.)

template tag:  
    tag de template - funções para serem usadas em templates

set the <var/attributo>: 
    defina a variaável ou atributo.



---------------------------------

topics[1355] - está confuso ao explicar que o modulo do modelo deve ser colocado no settings

    For example, if the models for your application live in the module ``myapp.models`` (the package structure that is created for an application by the :djadmin:`manage.py startapp <startapp>` script), :setting:`INSTALLED_APPS` should read, in part::


toics[1387]

sugestion: this fields **value** must be unique throughout the table.

    If ``True``, this field must be unique throughout the table.


Topics[1894]: referenciar a class como :class:`~django.db.models.query.QuerySet`

    For example, repeatedly getting a certain index in a queryset object will query the database each time::

topics[1906]

    Each lookup function that takes keyword-arguments (e.g. :meth:`~django.db.models.query.QuerySet.filter`, :meth:`~django.db.models.query.QuerySet.exclude`, :meth:`~django.db.models.query.QuerySet.get`) can also be passed one or more ``Q`` objects as positional (not-named) arguments. If you provide multiple ``Q`` object arguments to a lookup function, the arguments will be "AND"ed together. For example::


Mal escritos em inglês IMHO
---------------------------

[1355] do topics / models: está confuso ao explicar que o modulo do modelo deve ser colocado no settings

    For example, if the models for your application live in the module ``myapp.models`` (the package structure that is created for an application by the :djadmin:`manage.py startapp <startapp>` script), :setting:`INSTALLED_APPS` should read, in part::

[1387] doc/models:

    sugestion: this fields **value** must be unique throughout the table.
    If ``True``, this field must be unique throughout the table.



[1822] Topics/models: usou termos ruins pra traduzir até mesmo para a explicação em ingles. Ex.:"Field lookups are how you specify the meat of an SQL ``WHERE`` clause.""

     Field lookups are how you specify the meat of an SQL ``WHERE`` clause. They're specified as keyword arguments to the :class:`~django.db.models.query.QuerySet` methods :meth:`~django.db.models.query.QuerySet.filter`, :meth:`~django.db.models.query.QuerySet.exclude` and :meth:`~django.db.models.query.QuerySet.get`.


