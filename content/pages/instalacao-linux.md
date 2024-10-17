Title: Instalando o Python no Linux
Slug: instalacao-linux
Template: page

Os sistemas GNU/Linux mais recentes ja possuem uma versão do Python instalada junto com o sistema operacional. Podemos checar com o seguinte comando:

    $ which python3
    /usr/bin/python3

que nos mostra onde o Python padrão do sistema operacional está instalado.

A versão do Python na distribuição Linux Ubuntu 22.04.2 LTS é a 3.10.

    $ python3 --version
    Python 3.10.6

Para evitar conflitos com o Python do sistema operacional, sugere-se a instalação de um outro interpretador, que pode ser feita de 2 formas diferentes: através do  de gerenciador de pacotes ou de repositórios.

## Instalação por gerenciadores de pacotes

Os gerenciadores de pacotes mais comuns são `apt-get` (Debian, Ubuntu) e `yum`
(RedHat, CentOS). Caso sua distribuição utilize um gerenciador de pacotes diferente, acesse a [página de downloads do Python](https://www.python.org/downloads/).

### Debian e Ubuntu

Através do gerenciador de pacotes, é possível instalar versões específicas do Python.
No exemplo abaixo, é instalada a versão, por exemplo, 3.9 do Python

    sudo apt-get install python3.9

É possível instalar qualquer outra versão: `python3.8`, `python3.9`, `python.10`

Desta forma, a instalação desta versão específica do Python acima difere da versão padrão do sistema operacional.

    $ which python3.9
    /usr/bin/python3.9

    $ which python3
    /usr/bin/python3

### RedHat e CentOS

Assim como no tópico anterior, é possível instalar versões específicas do Python.
No comando abaixo, é instalada a versão, por exemplo, 3.9 do Python.

    sudo yum install python3.9

## Instalação por repositório

Os repositórios no GNU/Linux são chamados de PPAs (do inglês Personal Package Archives).

Para adicionar repositórios ao nosso sistema, precisamos de um software chamado `software-properties-common`, que pode ser instalado com o comando abaixo:

    sudo apt-get install software-properties-common

Habilitada a adição de repositórios ao nosso sitema operacional, podemos agora incluir o repositório que contém o Python. Este repositório é chamado de deadsnakes, cuja página oficial pode ser encontrada neste [link](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa).

    sudo add-apt-repository ppa:deadsnakes/ppa

Agora a instalação do Python pode ser feita a partir deste repositório com o comando

    sudo apt-get install python3.9

Da mesma forma, é possível instalar várias versões. Observem que a versão python correspondente à do sistema operacional padrão não está disponível no repositório deadsnakes.
