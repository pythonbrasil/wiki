# Site estático APyB

[![Build Status](https://travis-ci.org/pythonbrasil/apyb.svg?branch=pelican)](https://travis-ci.org/pythonbrasil/apyb)

Pensando na possibilidade de mantermos um site para a comunidade de maneira mais colaborativa onde qualquer um possa contribuir com conteúdo de maneira rápida, surgiu a idéia de utilizarmos o GitHub Pages.

Site Live:  http://pythonbrasil.github.io/apyb/

Repo: https://github.com/pythonbrasil/apyb

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

## Mas se você for programador e tem conhecimentos mínimos de Python, saiba como rodar o projeto em sua máquina e colaborar conosco:

Se não sabe o que é o virtualenv e/ou pra que serve, sugiro que leia a página do projeto.

### Processo de instalação:

Crie um [virtualenv](https://virtualenv.readthedocs.org/en/latest/) com o nome que desejar, acesse a pasta e ative o virtualenv (Considerando os comandos em sistemas Linux e OS X):

> virtualenv project-name  

> cd project-name  

> source bin/activate

Provavelmente irá aparecer em seu terminal algo como *(project-name)$*, agora vamos clonar o repositório do projeto:

> git clone git@github.com:pythonbrasil/apyb.git

> cd apyb

Pronto! Você já está na pasta do projeto! Agora vamos instalar os programas necessários (Certifique-se que o virtualenv está ativado):

> pip install -r requirements.txt

Podem ocorrer problemas variados na instalação dos programas, se isso acontecer tente instalar as depêndencias do sistema operacional. No Ubuntu você pode usar o seguinte comando:

> sudo ./install_os_dependencies.sh install

Ou verifique pelo Stackoverflow e pelo Google quais as soluções possíveis. Se o problema persistir, nos informe nas issues.

Legal, agora já instalei todos os programas, vamos fazê-lo rodar em nosso computador?

> make html  

> make serve

O *make html* irá gerar o HTML e o *make serve* irá criar o servidor. Basta acessar *localhost:8000* e pronto! O site já está rodando em seu computador localmente!

Agora basta fazer as modificações na pasta *content/pages*, rodar os comandos *make html* e *make serve* e suas alterações já serão visíveis.

Resta então fazer o commit de suas alterações em seu repositório local e enviar-nos o Pull Request! o/

Mais informações sobre como funciona o Pelican, indicamos o artigo - [http://mindbending.org/pt/instalando-o-pelican](http://mindbending.org/pt/instalando-o-pelican).
