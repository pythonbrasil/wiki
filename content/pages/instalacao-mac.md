Title: Instalando o Python no Mac OS X
Slug: instalacao-mac
Template: page

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

