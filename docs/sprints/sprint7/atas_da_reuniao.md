# Atas da Reunião 15/10

- [Atas da Reunião 15/10](#atas-da-reunião-1510)
  - [Links/ferramentas a serem utilizados](#linksferramentas-a-serem-utilizados)
  - [1 - discussão geral](#1---discussão-geral)
  - [2 - review e retrospectiva](#2---review-e-retrospectiva)
    - [2.1 - Atualização do quadro de conhecimentos](#21---atualização-do-quadro-de-conhecimentos)
    - [2.2 - "o que eu fiz"](#22---o-que-eu-fiz)
    - [2.3 - estado das issues](#23---estado-das-issues)
    - [2.4.1 - Quais problemas houveram (no contexto do projeto)?](#241---quais-problemas-houveram-no-contexto-do-projeto)
    - [2.4.2 - Pontos positivos, negativos e a melhorar, em geral](#242---pontos-positivos-negativos-e-a-melhorar-em-geral)
  - [3 - planejamento](#3---planejamento)
    - [3.1 - De acordo com o Roadmap:](#31---de-acordo-com-o-roadmap)
    - [3.2 - Antecipando problemas](#32---antecipando-problemas)
    - [3.3 - O que mais pode ser adicionado](#33---o-que-mais-pode-ser-adicionado)
    - [3.4 - Geração dos pareamentos](#34---geração-dos-pareamentos)
    - [3.5 - Votação de riscos](#35---votação-de-riscos)
    - [3.6 - Considerações finais sobre a reunião](#36---considerações-finais-sobre-a-reunião)

## Links/ferramentas a serem utilizados

[Gerador de pareamentos](https://www.randomlists.com/team-generator?grp=2&items=felipe%0Aruan%0Asamuel%0Avinicius%0Agabriel%0A)
[Quadro de conhecimentos](https://docs.google.com/spreadsheets/d/1jK_06zaBXD485tWDkwCnQ6xhP0_jICVg1GNkNt1AgUw/edit#gid=0)
[Votação de riscos](https://docs.google.com/spreadsheets/d/1vfmnsztDCSwHpmeRw8vGGG4ExzWC-EdefWPhXHg358I/edit#gid=0)
[Visualizador de markdown online](https://jbt.github.io/markdown-editor/)

## 1 - discussão geral

Pontos a serem discutidos na reunião:

1. inclusão de documento de atas da reuniao [como este]
1. mudança de nome dos repositorios
    `git remote set-url origin https://github.com/fga-eps-mds/2020.1-GaiaDex-wiki`
1. automatizar mkdocs
1. adicionar codacy (junto com codeclimate)
1. começar doc de post mortem
1. padrao de pull request -> descrever melhor no pull request quais alteraçoes foram feitas, como testa-las etc, adicionar prints de como está
1. refatorar estrutura do backend (routes = handlers, refatoração por metodos?)
1. não planejar sprints em horário que não foram determinados com o grupo todo
1. reconfiguração de horarios de alerta não foi feito pois depende de uma issue que não começou a ser desenvolvida
1. como vai ficar a questão 'estética' do app (em relação ao prototipo)

## 2 - review e retrospectiva

### 2.1 - Atualização do quadro de conhecimentos

`autodescritivo` - [link](https://docs.google.com/spreadsheets/d/1jK_06zaBXD485tWDkwCnQ6xhP0_jICVg1GNkNt1AgUw/edit#gid=0)

### 2.2 - "o que eu fiz"

`passaremos a fala pra cada membro fazer um resumo de como foi a experiencia durante essa sprint [quase uma 'super daily']`

### 2.3 - estado das issues

checar nos repositorios quais tasks foram realizadas ou não

por ora, eis o estado:

| estado atual (14h 15/10) | issue |
| ------------------------ | ----- |
| feito          | [Guia de Estilo](https://github.com/fga-eps-mds/2020.1-Grupo2-wiki/issues/59) |
| feito          | [Issue 97 - US15 - Criar tópico em um fórum de planta (Backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/97) |
| feito          | [Issue US16 - Editar tópico criado por mim (Backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/98) |
| feito          | [US17 - Deletar o tópico criado por mim (Backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/99) |
| feito          | [US18 - Upvote e downvote em um tópico (Backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/100) |
| feito          | [US19 - Criar comentário em um tópico (Backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/101) |
| feito          | [US20 - Editar comentário que fiz em um tópico (Backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/102) |
| feito          | [US21 - Remover um comentário que fiz em um tópico (Backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/103) |
| iniciado       | [Issue 04 (frontend) - US04 - Cadastrar minha conta no aplicativo (FrontEnd)](https://github.com/fga-eps-mds/2020.1-Grupo2-FrontEnd/issues/4) |
| iniciado       | [Issue 05 (frontend) - US07 - Fazer login no aplicativo (Frontend)](https://github.com/fga-eps-mds/2020.1-Grupo2-FrontEnd/issues/5) |
| iniciado       | [Issue 06 (frontend) - US08 - Fazer logout no aplicativo (FrontEnd)](https://github.com/fga-eps-mds/2020.1-Grupo2-FrontEnd/issues/6) |
| iniciado       | [Issue 09 (frontend) - US11 - Alterar os dados cadastrados na minha conta (FrontEnd)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/9) |
| iniciado       | [Issue 07 (frontend) - US12 - Deletar minha conta (FrontEnd)](https://github.com/fga-eps-mds/2020.1-Grupo2-FrontEnd/issues/7) |
| feito          | [Issue 08 (frontend) - US23 - Visualizar informações sobre a planta (Frontend)](https://github.com/fga-eps-mds/2020.1-Grupo2-FrontEnd/issues/8) |
| feito          | [Plano de GCS](https://github.com/fga-eps-mds/2020.1-Grupo2-wiki/issues/94) |
| feito          | [Refatorar arquitetura](https://github.com/fga-eps-mds/2020.1-Grupo2-wiki/issues/95) |
| nao iniciado   | [Refatorar critérios de aceitação](https://github.com/fga-eps-mds/2020.1-Grupo2-wiki/issues/96) |
| feito          | [Refatorar o roadmap](https://github.com/fga-eps-mds/2020.1-Grupo2-wiki/issues/97) |
| nao iniciado   | [US01 - Scannear planta (backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/83) |
| nao iniciado   | [US02 - Visualizar minha coleção (backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/84) |
| iniciado       | [US03 - Visualizar informações da Minha Planta (backend)](https://github.com/fga-eps-mds/2020.1-Grupo2-BackEnd/issues/85) |

### 2.4.1 - Quais problemas houveram (no contexto do projeto)?
`perdeu o notebook? teve 3 provas em um dia só?`

### 2.4.2 - Pontos positivos, negativos e a melhorar, em geral
`pontos positivos = o que foi de bom | pontos negativos = ruim, não da mais pra mudar | pontos a melhorar = ruim mas circunstancial |`

## 3 - planejamento

### 3.1 - De acordo com o Roadmap:

- Testes nas histórias já feitas no backend (Jest)
  - sugestão de materiais:
    - Documentação oficial
      - 1. [Getting Started](https://jestjs.io/docs/en/getting-started)
      - 1. [Jest com MongoDB](https://jestjs.io/docs/en/mongodb)
      - 1. [Jest com React Native](https://jestjs.io/docs/en/tutorial-react-native)
    - Outros
      - 1. [(FreeCodeCamp) How to set up Jest and Enzyme to test React Native apps](https://medium.com/free-code-camp/setting-up-jest-enzyme-for-testing-react-native-40393ca04145)
      - 1. [How to test Express.js with Jest and Supertest](https://www.albertgao.xyz/2017/05/24/how-to-test-expressjs-with-jest-and-supertest/)
- Cobertura de Testes Code Climate
- Configurar Lint com Guia de Estilo

Frontend:

- US15 - Criar tópico em um fórum de planta (frontend)
- US16 - Editar tópico criado por mim (frontend)
- US17 - Deletar o tópico criado por mim (frontend)
- US18 - Upvote e downvote em um tópico (frontend)
  
### 3.2 - Antecipando problemas

`como está a disponibilidade dos membros nesta sprint? muita prova?`

### 3.3 - O que mais pode ser adicionado

`quais dividas tecnicas? o que foi discutido que pode ser incluido nesta sprint?`

### 3.4 - Geração dos pareamentos

`autoexplicativo` [link](https://www.randomlists.com/team-generator?grp=2&items=felipe%0Aruan%0Asamuel%0Avinicius%0Agabriel%0A)

### 3.5 - Votação de riscos

`autoexplicativo` [link](https://docs.google.com/spreadsheets/d/1vfmnsztDCSwHpmeRw8vGGG4ExzWC-EdefWPhXHg358I/edit#gid=0)

### 3.6 - Considerações finais sobre a reunião

`o que houve de positivo? o que pode melhorar? algo passou batido?`
