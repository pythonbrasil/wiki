
# Site estático python.org.br (Teste)

[![Build Status](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/<WORKFLOW_FILE>/badge.svg)](https://github.com/pythonbrasil/wiki/actions/workflows/build.yml)

Site Live: [http://python.org.br/](http://python.org.br/)

Repositório: [https://github.com/pythonbrasil/wiki](https://github.com/pythonbrasil/wiki)

Para contribuír com a melhoria do conteúdo deste site basta acessar alguma das páginas mapeadas abaixo, editar seu conteúdo e submeter sua alteração como um pull request.

### Páginas do Impressione-se

1. **Empresas** - O conteúdo em formato JSON criado através de uma importação do
conteúdo encontrado em
[pyBusinesses-BR](https://github.com/pythonbrasil/pyBusinesses-BR).
Essa importação é feita quando *make html* é executado (ver abaixo), pelo
arquivo [empresas_generator.py](empresas_generator.py) e os arquivos são salvos
em content/empresas.
1. **Projetos Brasileiros** - Conteúdo em formato markdown no arquivo
[content/pages/projetos.md](content/pages/projetos.md)

### Páginas do Inicie-se

1. **Introdução** - Conteúdo em formato markdown no arquivo
[content/pages/introducao.md](content/pages/qual-python.md).

1. **Qual python?** - Conteúdo em formato markdown no arquivo
[content/pages/qual-python.md](content/pages/qual-python.md).

1. **Download do Python** - Apenas um link para [página de download do Python]
(https://www.python.org/downloads/). Esse link, assim como todos os itens do
menu principal, são definidos na arquivo [pelicanconf.py](pelicanconf.py) na
variável *NAVBAR_HOME_LINKS*.

1. **Instalação Linux** - Conteúdo em formato markdown no arquivo
[content/pages/instalacao-linux.md](content/pages/instalacao-linux.md).

1. **Instalação Mac** - Conteúdo em formato markdown no arquivo
[content/pages/instalacao-mac.md](content/pages/instalacao-mac.md).

1. **Instalação Windows** - Conteúdo em formato markdown no arquivo
[content/pages/instalacao-windows.md](content/pages/instalacao-windows.md).

1. **Ferramentas** - Conteúdo em formato markdown no arquivo [content/pages/ferramentas.md](content/pages/ferramentas.md)

### Páginas do Aprenda mais

1. **Web** - Conteúdo em formato markdown no arquivo
[content/pages/web.md](content/pages/web.md).

1. **Mobile** - Conteúdo em formato markdown no arquivo
[content/pages/mobile.md](content/pages/mobile.md).

1. **Games** - Conteúdo em formato markdown no arquivo
[content/pages/games.md](content/pages/games.md).

1. **Científico** - Conteúdo em formato markdown no arquivo
[content/pages/cientifico.md](content/pages/cientifico.md).

1. **Wiki** - Apenas um link para o [wiki antigo](https://wiki.python.org.br)
da comunidade Python Brasil.

### Páginas do Participe

1. **Comunidades Locais** - O Conteúdo está em formato estruturado JSON. Para adicionar uma nova comunidade basta criar um arquivo com extensão .json na pasta [content/comunidades-locais/](https://github.com/pythonbrasil/wiki/tree/pelican/content/comunidades-locais) seguindo o padrão dos demais arquivos desta pasta e caso queira adicionar o logo da comunidade basta colocar o arquivo de extensão .png de tamanho 400X400 na pasta [content/images/comunidades-locais/](https://github.com/pythonbrasil/wiki/tree/pelican/content/images/comunidades-locais).

2. **Pyladies** - O Conteúdo das pyladies é uma importação do conteúdo encontrado em [https://github.com/pyladies-brazil/br-pyladies-pelican/blob/master/data/ladies.yml](https://github.com/pyladies-brazil/br-pyladies-pelican/blob/master/data/ladies.yml).

3. **Eventos** - O Conteúdo está em formato estruturado JSON. Para adicionar um novo evento basta criar um arquivo com extensão .json na pasta [content/eventos/YYYY/](https://github.com/pythonbrasil/wiki/tree/pelican/content/eventos).

4. **Contribua** - Conteúdo em formato markdown no arquivo [content/pages/contribua.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/contribua.md).

5. **Tradução** - Conteúdo em formato markdown no arquivo [content/pages/traducao.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/traducao.md).

### Páginas da APyB

1. **Python Brasil** - Conteúdo em formato markdown no arquivo [content/pages/python-brasil.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/python-brasil.md).

2. **A APyB** - Conteúdo em formato markdown no arquivo [content/pages/apyb.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/apyb.md).

3. **Premio Dorneles Tremea** - Conteúdo em formato markdown no arquivo [content/pages/premio-dorneles-tremea.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/premio-dorneles-tremea.md).

### Para contribuir com desenvolvimento
*(ao contribuir com o Repositório utilizar a branch 'pelican')*

Clone o repositório do projeto para o seu computador e depois navegue para o
diretório criado:

```
$ git clone git@github.com:pythonbrasil/wiki.git

$ cd wiki
```

Crie um [virtualenv](https://virtualenv.readthedocs.org/en/latest/) com o nome que desejar, acesse a pasta e ative o virtualenv (Considerando os comandos em sistemas Linux e OS X):

```
$ virtualenv -p python3 .venv

$ source .venv/bin/activate
```

Provavelmente irá aparecer em seu terminal algo como *(.venv)$*:


Pronto! Você já está na pasta do projeto e com o virtualenv ativado!
Certifique-se disso. Agora vamos instalar os programas necessários:

```
$ pip install -r requirements.txt
```

Podem ocorrer problemas variados na instalação dos programas, se isso acontecer tente instalar as depêndencias do sistema operacional. No Ubuntu você pode usar o seguinte comando:

```
$ sudo ./install_os_dependencies.sh install
```

No Mac OS X Yosemite, use o seguinte comando para instalar ferramentas e utilitários como (libtool, lxml, cpp, etc...)que já é default em distros Linux:

```
$ x-code-select --install
```

Se der erro de locale, tente comando abaixo, o ideal é colocar no ~/.bash_profile

```
$ export LC_ALL=en_US.UTF-8

$ export LANG=en_US.UTF-8
```

Se der erro de pycripto instale:

```
$ sudo apt install python3-dev
```


Ou verifique pelo Stackoverflow e pelo Google quais as soluções possíveis. Se o problema persistir, nos informe nas issues.

Legal, agora já instalei todos os programas, vamos fazê-lo rodar em nosso computador?

```
$ make html

$ make serve
```

O *make html* irá gerar o HTML e o *make serve* irá criar o servidor. Basta acessar *localhost:8000* e pronto! O site já está rodando em seu computador localmente!

Agora basta fazer as modificações na pasta *content/pages*, rodar os comandos *make html* e *make serve* e suas alterações já serão visíveis.

Resta então fazer o commit de suas alterações em seu repositório local e enviar-nos o Pull Request! o/

Mais informações sobre como funciona o Pelican, indicamos o artigo - [http://mindbending.org/pt/instalando-o-pelican](http://mindbending.org/pt/instalando-o-pelican).

Caso queira contribuir com o tema é preciso ter o node instalado em sua máquina. Sua instalação é bem direta e pode ser obtida em:

[https://nodejs.org/en/download/](https://nodejs.org/en/download/)

Após a instalação do node você pode instalar as dependências do tema indo a seu diretório e rodando o npm:

```
$ cd themes/pybr
$ npm install
```

Com as dependências instaladas para rodar a montagem do css com live reload basta rodar:

```
$ npm run gulp
```

E caso queira rodar sem o live reload, somente para gerar o css para publicação rode:

```
$ npm run gulp build
```
