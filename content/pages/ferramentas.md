Title: Ferramentas de Desenvolvimento
Slug: ferramentas
Template: page

Escolher a ferramenta certa pode fazer toda a diferença na sua produtividade e aprendizado. Esta página reúne recomendações atualizadas de editores e IDEs para Python, organizadas por finalidade e perfil de uso.

## Recomendações Rápidas por Perfil

- **Iniciante geral**: VS Code ou PyCharm Community — interfaces intuitivas, bom suporte e comunidade ativa
- **Desenvolvimento web**: VS Code ou PyCharm — excelente suporte para Django, Flask e frameworks modernos
- **Ciência de dados e notebooks**: Positron (Python/R + IA), JupyterLab, VS Code com extensões Jupyter, ou PyCharm
- **Terminal e minimalistas**: Vim, Emacs, ou Neovim com configurações Python
- **Aprendizado Python básico**: IDLE (já vem com Python) ou VS Code

---

## IDEs e Editores — Principais Recomendações

### [Visual Studio Code](https://code.visualstudio.com/)

Editor gratuito e open source da Microsoft, com suporte excelente para Python através de extensões oficiais. Leve, extensível e muito popular. Suporta desenvolvimento web, ciência de dados (Jupyter integrado), debugging avançado e integração com Git. Ideal para quem quer um editor moderno e versátil.

### [PyCharm Community](https://www.jetbrains.com/pycharm/)

IDE gratuita e open source (licença Apache) desenvolvida pela JetBrains. Oferece análise de código inteligente, depurador gráfico, refatoração automática, testes integrados e suporte para frameworks web como Django e Flask. Multiplataforma e muito completa, ótima opção para projetos de médio a grande porte.

**PyCharm Professional** (pago): versão completa com suporte avançado para web (Django, Flask, FastAPI), bancos de dados, Jupyter Notebooks integrados, desenvolvimento remoto e mais. Possui licenças gratuitas para estudantes e projetos open source.

### [Positron](https://positron.posit.co/)

"The Data Science IDE" — IDE desenvolvida pela Posit (criadora do RStudio) para unificar trabalho exploratório e produtivo em ciência de dados. Suporta Python e R, com ferramentas de IA integradas, interface baseada no VS Code, notebooks Jupyter nativos, integração com Quarto, visualização de dados e exploração interativa de variáveis. Gratuita e com código-fonte disponível (Elastic License 2.0). Ideal para todo o ciclo de ciência de dados: desde análise exploratória até produção. Projeto ativo e funcional.

### [JupyterLab](https://jupyter.org/)

Ambiente interativo baseado em navegador para notebooks Jupyter. Excelente para análise de dados, prototipagem, ensino e documentação com código executável. Suporta visualizações inline, markdown, LaTeX e extensões. Fundamental para ciência de dados e pesquisa.

### [Spyder](https://www.spyder-ide.org/)

IDE open source voltada para cientistas, engenheiros e analistas de dados. Interface familiar para quem vem do MATLAB ou RStudio. Inclui editor com análise de código, console IPython integrado, explorador de variáveis e visualização de gráficos. Faz parte do ecossistema Anaconda.

---

## Editores de Texto Avançados

### [Vim](https://www.vim.org/)

Editor clássico de terminal, altamente configurável e presente em praticamente todo sistema Unix/Linux. Curva de aprendizado íngreme, mas extremamente poderoso e eficiente para quem domina. Pode ser transformado em IDE Python completa com plugins modernos como `coc.nvim`, `vim-lsp` e `ALE`. Veja também [Neovim](https://neovim.io/) (fork moderno do Vim).

### [Emacs](https://www.gnu.org/software/emacs/)

Editor (ou "sistema operacional com capacidades de edição") extremamente poderoso e extensível via Emacs Lisp. Suporta Python através de pacotes como `elpy`, `python-mode` e `lsp-mode`. Curva de aprendizado considerada difícil, mas oferece produtividade excepcional após domínio. Ideal para quem gosta de personalização profunda.

### [Sublime Text](https://www.sublimetext.com/)

Editor proprietário rápido e elegante, com versão de avaliação gratuita (sem limite de tempo). Interface limpa, múltiplos cursores, busca poderosa e sistema de plugins. Popular entre desenvolvedores que valorizam desempenho e minimalismo.

---

## Ferramentas Específicas por Contexto

### Para Notebooks e Análise Interativa

- **[JupyterLab](https://jupyter.org/)**: ambiente padrão da comunidade científica
- **[Positron](https://positron.posit.co/)**: IDE completa para ciência de dados com notebooks nativos (Python e R)
- **[VS Code](https://code.visualstudio.com/)**: com extensão oficial Jupyter
- **[Google Colab](https://colab.research.google.com/)**: notebooks na nuvem, gratuito, com GPU

### Para Ciência de Dados

- **Positron**: IDE completa com IA integrada, suporte a Python e R, notebooks nativos
- **Spyder**: interface familiar, explorador de variáveis
- **PyCharm Professional**: suporte completo para Jupyter, DataFrames, SQL
- **VS Code**: com extensões Python, Jupyter e Data Wrangler

### Para Desenvolvimento Web

- **PyCharm**: excelente suporte para Django, Flask, FastAPI, templates
- **VS Code**: leve, extensível, ótimo para frameworks modernos

### Para Terminal e Servidores

- **Vim/Neovim**: ubíquo, eficiente, ideal para SSH
- **Emacs**: poderoso e programável
- **Micro**: editor de terminal moderno e amigável ([https://micro-editor.github.io/](https://micro-editor.github.io/))

---

## IDEs Complementares e Alternativas

### [IDLE](https://docs.python.org/3/library/idle.html)

IDE que acompanha a instalação padrão do Python. Feita com Tkinter, é simples e adequada para iniciantes absolutos ou para testes rápidos. Inclui shell interativo e editor básico.

### [Thonny](https://thonny.org/)

IDE gratuita voltada para iniciantes. Interface simples, depurador visual passo a passo, visualização de variáveis e indicação clara de erros. Excelente para aprendizado e ensino de Python.

### [Eclipse + PyDev](https://www.pydev.org/)

Plugin Python para o Eclipse IDE. Opção robusta para quem já usa Eclipse em outros projetos (ex.: Java). Oferece análise de código, debugging, refatoração e integração com ferramentas.

### [Neovim](https://neovim.io/)

Fork moderno do Vim com foco em extensibilidade e desempenho. Suporta LSP (Language Server Protocol) nativamente, interface gráfica via plugins e configuração em Lua. Comunidade ativa e plugins modernos.

---

## Refatoração e Ferramentas de Código

### [Rope](https://github.com/python-rope/rope)

Biblioteca Python para refatoração automática. Integra-se a várias IDEs e editores. Suporta renomeação, extração de métodos, reorganização de imports e mais.

---

## Outras Opções (Verifique Status Atual)

Ferramentas abaixo podem estar descontinuadas ou com manutenção irregular. Recomendamos verificar repositórios e comunidades antes de adotar:

- **Komodo Edit/IDE**: editor/IDE da ActiveState (verifique se ainda é mantido)
- **Eric**: IDE baseada em Qt, projeto de longa data
- **NINJA-IDE**: IDE multiplataforma (verifique atividade do projeto)
- **Wing IDE**: IDE comercial com versão educacional gratuita

---

## Dicas para Escolher

1. **Iniciantes**: prefira ferramentas com boa documentação em português, comunidade ativa e curva de aprendizado suave (VS Code, PyCharm Community, Thonny).
2. **Ciência de dados**: priorize suporte a notebooks, visualização de dados e exploração interativa (Positron, JupyterLab, Spyder).
3. **Desenvolvimento profissional**: invista em IDEs completas com refatoração, debugging avançado e integração com ferramentas de deploy (PyCharm, VS Code).
4. **Performance e minimalismo**: editores leves e configuráveis como Vim, Neovim ou Sublime Text podem ser mais produtivos após configuração inicial.

---

*Conteúdo original baseado em http://wiki.python.org.br/IdesPython, atualizado pela comunidade Python Brasil.*
