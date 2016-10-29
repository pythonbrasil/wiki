Title: Instalando o Python
Slug: instalacao
Template: page

Aprenda aqui como instalar o python para começar a trabalhar:

# GNU/Linux

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

# Windows

Para instalar o Python em Windows, baixe o instalador do site oficial [neste link](https://www.python.org/downloads/). **Dê preferência ao Python 3**, já que a versão 2.x é mantida por compatibilidade com códigos antigos e será descontinuada em 2020.

**Importante:** Certifique-se de selecionar a opção "Adicionar python.exe ao Path" na etapa de Personalização da instalação. Isso garante que ao digitar "python" no prompt de comando, o Windows consiga encontrar o executável do programa e/ou iniciar no modo interativo pelo `cmd`.

# Mac OS X

## Verifique se já tem o Python instalado
Se você usa macOS 10.2 ou superior, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite em um terminal:

    $ which python

ou

    $ which python3

que deve retornar algo como `/usr/bin/python`. Isso significa que o Python está instalado nesse endereço.

## Instalação
Antes de fazer a instalação do Python, é preciso fazer a instalação do XCode, que pode ser baixado na [App Store](https://itunes.apple.com/br/app/xcode/id497799835), do pacote para desenvolvimento em linha de comando no macOS, command line tools e dos gerenciadores de pacotes pip e homebrew.

Para instalar o command line tools, digite em um terminal:

    $ xcode-select --install

Para instalar o pip, digite em um terminal:

    $ sudo easy_install pip

Para atualizar o pip, digite em um terminal:

    $ sudo pip install --upgrade pip

Para instalar o homebrew, digite em um terminal:

    $ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

Para instalar o Python 2, digite em um terminal:

    $ brew install python

Para instalar o Python 3, digite em um terminal:

    $ brew install python3

