Title: Contribua com este site
Slug: contribua
Template: page

Para contribuír com a melhoria do conteúdo deste site basta acessar alguma das páginas mapeadas abaixo, editar seu conteúdo e submeter sua alteração como um pull request.

### Páginas do Impressione-se

1. **Empresas** - Listagem das empresas que usam python

    O Conteúdo está em formato estruturado JSON. Para adicionar uma nova empresa basta criar um arquivo com extensão .json na pasta [content/empresas/](https://github.com/pythonbrasil/wiki/tree/pelican/content/empresas) seguindo o padrão dos demais arquivos desta pasta e caso queira adicionar o logo da empresa basta colocar o arquivo de extensão .png na pasta [content/images/empresas/](https://github.com/pythonbrasil/wiki/tree/pelican/content/images/empresas).

### Páginas do Inicie-se

1. **Qual python?** - Conteúdo em formato markdown no arquivo [content/pages/qual-python.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/qual-python.md).

2. **Instalação Linux** - Conteúdo em formato markdown no arquivo [content/pages/instalacao-linux.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/instalacao-linux.md).

3. **Instalação Mac** - Conteúdo em formato markdown no arquivo [content/pages/instalacao-mac.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/instalacao-mac.md).

4. **Instalação Windows** - Conteúdo em formato markdown no arquivo [content/pages/instalacao-windows.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/instalacao-windows.md).

5. **Introdução** - Conteúdo em formato markdown no arquivo [content/pages/introducao.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/introducao.md).

6. **Ferramentas** - Conteúdo em formato markdown no arquivo [content/pages/ferramentas.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/ferramentas.md)

### Páginas do Aprenda mais

1. **Web** - Conteúdo em formato markdown no arquivo [content/pages/web.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/web.md).

2. **Mobile** - Conteúdo em formato markdown no arquivo [content/pages/mobile.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/mobile.md).

3. **Games** - Conteúdo em formato markdown no arquivo [content/pages/games.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/games.md).

4. **Científico** - Conteúdo em formato markdown no arquivo [content/pages/cientifico.md](https://github.com/pythonbrasil/wiki/blob/pelican/content/pages/cientifico.md).

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

Crie um [virtualenv](https://virtualenv.readthedocs.org/en/latest/) com o nome que desejar, acesse a pasta e ative o virtualenv (Considerando os comandos em sistemas Linux e OS X):

```
$ virtualenv project-name
$ cd project-name
$ source bin/activate
```

Provavelmente irá aparecer em seu terminal algo como *(project-name)$*, agora vamos clonar o repositório do projeto:

```
$ git clone git@github.com:pythonbrasil/wiki.git
$ cd wiki
```

Pronto! Você já está na pasta do projeto! Agora vamos instalar os programas necessários (Certifique-se que o virtualenv está ativado):

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
