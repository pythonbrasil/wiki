Title: Instalando o Python no Windows
Slug: instalacao-windows
Template: page

Para instalar o Python em Windows, baixe o instalador do site oficial [neste link](https://www.python.org/downloads/). **Dê preferência ao Python 3**, já que a versão 2.x é mantida por compatibilidade com códigos antigos e será descontinuada em 2020.

Rode o instalador baixado para instalar o python no sistema e ao finalizar a instalação siga os passos para adicionar o python no path do sistema, ou ignore esta etapa caso a versão do instalador que você baixou possua a opção de configurar o path para você.

## Adicionando o python no path

Para que você consiga rodar o python pela linha de comando é necessário adiciona-lo no path do sistema que pode ser feito seguindo os passos a seguir:

![passos]({filename}/images/instalacao-windows/add-python-to-path.png)

1. Abra o painel de controle e navegue até as configurações de sistema
2. Selecione as configurações avançadas do sistema
3. Clique em variáveis de ambiente
4. Procure nas variáveis do sistema pela variável `Path`
5. Clique em editar
6. Verifique se os valores `C:\Python34` e `C:\Python34\Scripts` existem no campo de valor da variável, caso não exista adicione ao final dos valores separando cada valor com `;`. O `Python34` neste exemplo é referente a pasta onde o python foi instalado no seu sistema, este valor pode ser diferente caso esteja instalando outra versão do python por exemplo se for a versão 2.7 o valor será `Python27`. Verifique o destino da sua instalação e subistitua por este valor.
7. Clique em OK


## Instalando o pip

Para que você consiga instalar os pacotes do python é necessário que você tenha o `pip` instalado no sistema. Este procedimento funciona com python 2.7.9 ou versões superiores e python 3.x.

Clique com o botão direito no icone do windows e selecione **executar**:

![executar]({filename}/images/instalacao-windows/windows-run.png)

Digite `cmd` e clique em ok:

![cmd]({filename}/images/instalacao-windows/cmd.png)

Na linha de comando rode `python -m ensurepip`:

![ensurepip]({filename}/images/instalacao-windows/ensurepip.png)

Se o comando retornar dizendo que os requisitos já estão satisfeitos rode `python -m ensurepip --upgrade`:


![ensurepip-upgrade]({filename}/images/instalacao-windows/ensurepip-upgrade.png)
