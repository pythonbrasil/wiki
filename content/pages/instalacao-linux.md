Title: Instalando o Python no Linux
Slug: instalacao-linux
Template: page

## Verifique se já tem o Python instalado

Se você usa GNU/Linux, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite em um terminal:

    $ which python

ou

    $ which python3

que deve retornar algo como `/usr/bin/python`. Isso significa que o Python está instalado nesse endereço.

Caso contrário, se retornar algo como `which: no python in (/usr/local/sbin:/usr/local/bin:/usr/bin:/usr...)` você precisa instalar pelos repositórios ou gerenciador de pacotes de sua distribuição.

## Instalação por Gerenciadores de Pacotes

Os gerenciadores de pacotes mais comuns são apt-get (Debian, Ubuntu) e yum
(RedHat, CentOS). Caso sua distribuição utilize um gerenciador de pacotes diferente, acesse a [página de downloads do Python](https://www.python.org/downloads/).

### Apt-get

Para instalar o Python 2.7, digite em um terminal:

    $ sudo apt-get install python2.7

Para instalar o Python 3.5, digite em um terminal:

    $ sudo apt-get install python3.5

(Opcional) Para instalar o gerenciador de pacotes pip, digite em um terminal:

    $ sudo apt-get install python-pip

### Yum

Para instalar o Python 2.7, digite em um terminal:

    $ sudo yum install python27

Para instalar o Python 3.5, digite em um terminal:

    $ sudo yum install python35

(Opcional) Para instalar o gerenciador de pacotes pip, digite em um terminal:

    $ yum -y install python-pip
