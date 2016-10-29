Title: Instalando o Python
Slug: instalacao
Template: page

Aprenda aqui como instalar o python para começar a trabalhar:

# GNU/Linux

Se você usa GNU/Linux, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite em um terminal:

    $ which python

ou

    $ which python3

que deve retornar algo como `/usr/bin/python`. Isso significa que o Python está instalado nesse endereço.

Caso contrário, se retornar algo como `which: no python in (/usr/local/sbin:/usr/local/bin:/usr/bin:/usr...)` você precisa instalar pelos repositórios de sua distribuição.

# Windows

Para instalar o Python em Windows, baixe o instalador do site oficial [neste link](https://www.python.org/downloads/). **Dê preferência ao Python 3**, já que a versão 2.x é mantida por compatibilidade com códigos antigos e será descontinuada em 2020.

**Importante:** Certifique-se de selecionar a opção "Adicionar python.exe ao Path" na etapa de Personalização da instalação. Isso garante que ao digitar "python" no prompt de comando, o Windows consiga encontrar o executável do programa e/ou iniciar no modo interativo pelo `cmd`.

# Mac OS X
Se você usa macOS 10.2 ou superior, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite em um terminal:

    $ which python

ou

    $ which python3

que deve retornar algo como `/usr/bin/python`. Isso significa que o Python está instalado nesse endereço.

Antes de fazer a instalação do Python, é preciso fazer a instalação do XCode, que pode ser baixado na [App Store](https://itunes.apple.com/br/app/xcode/id497799835), do pacote para desenvolvimento em linha de comando no macOS, command line tools e dos gerenciadores de pacotes pip e homebrew.

Instale o command line tools:
$ xcode-select --install

Instale o pip
$ sudo easy_install pip

Atualize o pip
$ sudo pip install --upgrade pip

Instale o homebrew
$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

Instale o Python 2
$ brew install python

Instale o Python 3
$ brew install python3
