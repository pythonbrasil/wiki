# Site estático python.org.br

[![Build Status](https://travis-ci.org/pythonbrasil/wiki.svg?branch=pelican)](https://travis-ci.org/pythonbrasil/wiki)

Pensando na possibilidade de mantermos um site para a comunidade de maneira mais colaborativa onde qualquer um possa contribuir com conteúdo de maneira rápida, surgiu a idéia de utilizarmos o GitHub Pages.

Site Live:  http://pythonbrasil.github.io/wiki

Repo: https://github.com/pythonbrasil/wiki

Este projeto utiliza [Pelican](http://blog.getpelican.com/) como gerador de páginas estáticas e [Travis-CI](https://travis-ci.org/) para realizar a integração contínua.

## Porque usar isso?

1. Basta ter uma conta no GitHub.
2. Consigo editar via web.
3. O site não tem senha, mas é automaticamente versionado.

## Porque não usar um framework web?

Porque a tecnologia não pode estar entre o voluntário que deseja colaborar e a publicação do conteúdo.

## Mas somos todos programadores...

Não, não somos.

Mas mesmo entre os dev temos conhecimentos distintos, muitos da comunidade não tem interesse em programação web.

Independente de ser ou não programador, ou conhecer ou não **python**, podemos tentar criar um site em que **qualquer um** com o mínimo de boa vontade consiga contribuir.

*O mínimo de boa vontade é ter uma conta no GitHub*

## Mapeamento do Conteúdo

Veja como está organizado o conteúdo e como contribuir:

### Páginas do Impressione-se

1. Empresas: Listagem das empresas que usam python

O Conteúdo está em formato estruturado JSON. Para adicionar uma nova empresa basta criar um arquivo com extensão .json na pasta [content/empresas/](https://github.com/pythonbrasil/wiki/tree/pelican/content/empresas) seguindo o padrão dos demais arquivos desta pasta e caso queira adicionar o logo da empresa basta colocar o arquivo de extensão .png na pasta [content/images/empresas/](https://github.com/pythonbrasil/wiki/tree/pelican/content/images/empresas).

### Páginas do Inicie-se

1. Instalação

Conteúdo em formato markdown no arquivo [content/pages/instalacao.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/instalacao.md).

2. Ferramentas

Conteúdo em formato markdown no arquivo [content/pages/ferramentas.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/ferramentas.md)

### Páginas do Aprenda mais

1. Introdução

Conteúdo em formato markdown no arquivo [content/pages/introducao.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/introducao.md).

2. Web

Conteúdo em formato markdown no arquivo [content/pages/web.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/web.md).

3. Mobile

Conteúdo em formato markdown no arquivo [content/pages/mobile.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/mobile.md).

4. Games

Conteúdo em formato markdown no arquivo [content/pages/games.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/games.md).

5. Científico

Conteúdo em formato markdown no arquivo [content/pages/cientifico.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/cientifico.md).

### Páginas do Participe

1. Comunidades Locais

O Conteúdo está em formato estruturado JSON. Para adicionar uma nova comunidade basta criar um arquivo com extensão .json na pasta [content/comunidades-locais/](https://github.com/pythonbrasil/wiki/tree/pelican/content/comunidades-locais) seguindo o padrão dos demais arquivos desta pasta e caso queira adicionar o logo da comunidade basta colocar o arquivo de extensão .png na pasta [content/images/comunidades-locais/](https://github.com/pythonbrasil/wiki/tree/pelican/content/images/comunidades-locais).

2. Eventos

O Conteúdo está em formato estruturado JSON. Para adicionar um novo evento basta criar um arquivo com extensão .json na pasta [content/eventos/<ano>/](https://github.com/pythonbrasil/wiki/tree/pelican/content/eventos).

3. Python Brasil

Conteúdo em formato markdown no arquivo [content/pages/python-brasil.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/python-brasil.md).

4. A APyB

Conteúdo em formato markdown no arquivo [content/pages/apyb.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/apyb.md).

## Mas se você for programador e tem conhecimentos mínimos de Python, saiba como rodar o projeto em sua máquina e colaborar conosco:

Se não sabe o que é o virtualenv e/ou pra que serve, sugiro que leia a página do projeto.

### Processo de instalação:

Crie um [virtualenv](https://virtualenv.readthedocs.org/en/latest/) com o nome que desejar, acesse a pasta e ative o virtualenv (Considerando os comandos em sistemas Linux e OS X):

> virtualenv project-name  

> cd project-name  

> source bin/activate

Provavelmente irá aparecer em seu terminal algo como *(project-name)$*, agora vamos clonar o repositório do projeto:

> git clone git@github.com:pythonbrasil/wiki.git

> cd wiki

Pronto! Você já está na pasta do projeto! Agora vamos instalar os programas necessários (Certifique-se que o virtualenv está ativado):

> pip install -r requirements.txt

Podem ocorrer problemas variados na instalação dos programas, se isso acontecer tente instalar as depêndencias do sistema operacional. No Ubuntu você pode usar o seguinte comando:

> sudo ./install_os_dependencies.sh install

No Mac OS X Yosemite, use o seguinte comando para instalar ferramentas e utilitários como (libtool, lxml, cpp, etc...)que já é default em distros Linux:

> x-code-select --install

Se der erro de locale, tente comando abaixo, o ideal é colocar no ~/.bash_profile

> export LC_ALL=en_US.UTF-8

> export LANG=en_US.UTF-8

Ou verifique pelo Stackoverflow e pelo Google quais as soluções possíveis. Se o problema persistir, nos informe nas issues.

Legal, agora já instalei todos os programas, vamos fazê-lo rodar em nosso computador?

> make html  

> make serve

O *make html* irá gerar o HTML e o *make serve* irá criar o servidor. Basta acessar *localhost:8000* e pronto! O site já está rodando em seu computador localmente!

Agora basta fazer as modificações na pasta *content/pages*, rodar os comandos *make html* e *make serve* e suas alterações já serão visíveis.

Resta então fazer o commit de suas alterações em seu repositório local e enviar-nos o Pull Request! o/

Mais informações sobre como funciona o Pelican, indicamos o artigo - [http://mindbending.org/pt/instalando-o-pelican](http://mindbending.org/pt/instalando-o-pelican).
