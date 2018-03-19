Title: Como colaborar com a tradução
Slug: traducao
Template: page

Uma excelênte forma de contribuir com a comunidade é através da tradução da documentação da linguagem, de bibliotecas e de ferramentas. Com isso você contribuí com o crescimento da comunidade aumentando o alcance da linguagem dentro dos falantes do Português Brasileiro.

Caso esteja interessado em contribuír, a comunidade possuí um grupo no telegram destinado a essa tarefa que pode ser acessado através do seguinte link:

[https://t.me/pybr_i18n](https://t.me/pybr_i18n)

As traduções estão sendo feitas através da plataforma [transifex](https://www.transifex.com/). Para ajudar com a tradução basta criar uma conta e seguir para um dos projetos em andamento abaixo:

### Tradução da documentação da linguagem Python

Para começar a traduzir faça sua requisição através de:

[https://www.transifex.com/python-doc/public/](https://www.transifex.com/python-doc/public/)

### Tradução da documentação do framework Django

Para começar a traduzir faça sua requisição através de:

[https://www.transifex.com/django/public/](https://www.transifex.com/django/public/)

Você pode também participar da lista de e-mails para
discussão sobre tradução do django:

[https://groups.google.com/d/forum/django-i18n](https://groups.google.com/d/forum/django-i18n)

E ler mais sobre a localização do projeto em:

[https://docs.djangoproject.com/en/dev/internals/contributing/localizing/#documentation](https://docs.djangoproject.com/en/dev/internals/contributing/localizing/#documentation)

## Referências de tradução

O Luciano Ramalho e mais uma galera, criaram algumas dicas para quando eles estavam traduzindo o tutorial oficial do Python 2.7 que podem ser usados como referência ao realizar as traduções:

[http://turing.com.br/pydoc/2.7/tutorial/NOTAS.html#notas-para-os-tradutores-da-versao-pt-br](http://turing.com.br/pydoc/2.7/tutorial/NOTAS.html#notas-para-os-tradutores-da-versao-pt-br)

## Tradução offline

Embora o processo de tradução possa ser feito diretamente pelo navegador web, também é possível gerar a documentação traduzida no computador. Isso pode facilitar o processo de revisão já que pelo browser fica mais difícil visualizar links quebrados e navegar pela documentação.

Para gerar a documentação em português siga os passos a seguir (usaremos o django como exemplo):

**1** - Conforme a [documentação do Transifex](http://docs.transifex.com/client/config/), será preciso criar um arquivo chamado `.transifexrc` na raiz do seu diretório pessoal (ex.: `/home/user/.transifexrc`) contendo seu login e senha no Transifex:

```
[https://www.transifex.com]
username = user
token =
password = passw0rd
hostname = https://www.transifex.com
```

**2** - Será preciso baixar os repositórios e instalar algumas bibliotecas, para isso é recomendado criar uma pasta de trabalho:

```
mkdir ~/traducoes/django-br && cd ~/traducoes/django-br
```

**3** - Faça o clone do repositório no GitHub:

```
git clone https://github.com/django/django.git
```

**4** - Faça também o clone do repositório contendo as traduções do Django (como as traduções consomem muito espaço, elas foram movidas para um repositório em separado):

```
git clone https://github.com/django/django-docs-translations.git
```

**5** - Para gerar a documentação em português, nós vamos trabalhar dentro do diretório `django-docs-translations`:

```
cd django-docs-translations/
```

**6** - Existem várias traduções disponíveis, uma para cada versão do Django, nesse exemplo nós vamos gerar a documentação para a versão 1.10.x:

```
git checkout stable/1.10.x
```

**7** - Para a instalação das bibliotecas, é recomendado também criar e ativar um virtualenv:

```
python -m venv .django-br
source .django-br/bin/activate
```

**6** - Para gerar a documentação, o Django utiliza uma biblioteca chamada Sphinx, você pode instalá-la rodando o comando abaixo:

```
pip install sphinx
```

**7** - Para baixar as últimas traduções do site Transifex, nós vamos precisar instalar também a biblioteca `Transifex-Client`:

```
pip install transifex-client
```

**8** - Com o `Transifex-Client` instalado e com o arquivo `.transifexrc` configurado na raiz do seu diretório pessoal, será possível executar o comando abaixo para baixar as traduções do Transifex:

```
tx pull -f -l pt_BR
```

**9** - Com o download das traduções concluído, agora é preciso executar o comando 'make translations' para compilá-las:

```
make translations
```

**10** - Também é necessário criar um link simbólico para que o Sphinx gere a documentação utilizando os arquivos baixados e compilados por você (ao invés dos arquivos padrão no repositório do Django):

```
ln -s ~/traducoes/django-br/django-docs-translations/translations/ ~/traducoes/django-br/django/docs/locale
```

**11** - Agora saia do repositório django-docs-translations e vá para o repositório django, onde vamos encontrar um diretório chamado `docs`. É dentro desse diretório que vamos poder gerar a documentação:

```
cd ../django/docs/
```

**12** - Dentro do diretório docs do repositório do Django, após executar os passos acima, rode o comando abaixo para que o Sphinx gere a documentação em português:

```
make html LANGUAGE=pt_BR
```

**13** - Como medida de segurança, eu sugiro excluir o arquivo `~/.transifexrc` do seu home ou apagar a senha contida dentro dele já que o Transifex não oferece autenticação via tokens (ainda):

```
rm ~/.transifexrc
```

**14** - Ao final do processo, um novo diretório `_build` é criado e dentro desse diretório é possível encontrar também o diretório `html` contendo os arquivos gerados pelo Sphinx. Para visualizar a documentação entre em `_build/html/`:

```
cd _build/html/
```

A página principal da documentação é a `index.html`, clique duas vezes nesse arquivo para que ele seja aberto no seu browser. Clique nos links para navegar pela documentação, embora sejam links html, todo o conteúdo está contido dentro da pasta `_build` e portanto disponível offline. O Sphinx permite ainda gerar a documentação em outros formatos como `.pdf`.

## Dicas de tradução

Nesta seção apresentamos agumas dicas de tradução.

### Atenção com palavras de grafía parecida

Model: Modelo -- Classe que representa uma tabela.
Module: Módulo -- Módulo Python, e dentro do Django ainda pode ser o nome de uma Django "app".


### Cudado com o neologismo

A maioria dos termos de computação vem do inglês. E muitas vezes usamos os termos em inglês sem nos dar conta, ou pior, usamos uma tradução cujo o sentido da palavra em português é outro.

### Cuidado com os artigos

Em inglês as palavras não possuem gênero, portando fique atento a concordancia dos artigos ao realizar a tradução:

**Or use a common ancestor to hold the :class:\`~django.db.models.AutoField\`**

alguém poderia traduzir como usando o artigo "o" referindo-se ao "autoField":

**Ou use um acestral comum para manter o :class:\`~django.db.models.AutoField\`**

Mas não seria correto. Talvez para um leitor menos atento fique até estranho, o que é bom pois o chamará atenção se usarmos um artigo feminino neste caso.

**Ou use um acestral comum para manter a :class:\`~django.db.models.AutoField\`**

quer dizer, "ou use um acestral comum para a manter a classe ~django.db.models.AutoField"

Depois do texto renderizado, a  diretiva `:class:` não é mostrada, e usar o artigo correto ajuda a lembrar que referenciamos uma classe ou método por exemplo.

### Não tente explicar mais que o Autor original

Cuidado ao achar que um texto em inglês não está bem explicado, ou falta detalhes. Você pode ter razão, e a solução é sugerir melhorias no texto original.

Se ao invés disso,  tentar escrever um texto melhor na tradução,
além do problema raiz persistir, pode acontecer de estar sendo repetitivo.

O erro no texto original pode existir, mas antes de afirmá-lo, procure ler o contexto todo e entender se aquele detalhe ou explicaç ao deveria estar ali, ou já foi comentado emoutra seção,
ou se é realmente papel do texto explicar em detalhes tal condição.

### Glossário de tradução

Este glossário tem como objetivo criar uma consistência de tradução entre os projetos:
