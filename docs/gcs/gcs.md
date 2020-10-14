# Plano de Gerenciamento de Configuração de Software (GCS)


## Histórico de Versão
| Data | Versão | Descrição | Autor |
| :--- | :--- | :--- | :--- |
| 26/08/2020 | 1.0 | Criação e Formatação do tópico 1  | [Rafael Makaha](http://github.com/rafaelmakaha) |
| 14/10/2020 | 2.0 | Criação e Formatação do tópico 2 | [Rafael Makaha](http://github.com/rafaelmakaha) e [João Vítor](http://github.com/joaovitorml) |



## Sumário
- [Plano de Gerenciamento de Configuração de Software (GCS)](#plano-de-gerenciamento-de-configuração-de-software-gcs)
  - [Histórico de Versão](#histórico-de-versão)
  - [Sumário](#sumário)
  - [1. Políticas de Repositório](#1-políticas-de-repositório)
    - [1.1 Política de Commits](#11-política-de-commits)
    - [1.2 Política de Branches](#12-política-de-branches)
    - [1.3 Padrão para criação e uso das branches](#13-padrão-para-criação-e-uso-das-branches)
    - [1.4 Automatização de Fechamento de Issue](#14-automatização-de-fechamento-de-issue)
    - [1.5 Pull Requests tempestivos e permanentes](#15-pull-requests-tempestivos-e-permanentes)
    - [1.6 Conflitos nos Pull Requests](#16-conflitos-nos-pull-requests)
    - [1.7 Validações de produto](#17-validações-de-produto)
  - [2. Integração Contínua e Entrega Contínua](#2-integração-contínua-e-entrega-contínua)
    - [2.1. Integração Contínua](#21-integração-contínua)
    - [2.2. Entrega Contínua](#22-entrega-contínua)
    - [2.3. Pipeline](#23-pipeline)


## 1. Políticas de Repositório

### 1.1 Política de Commits
Adota-se para este projeto padrões para o comentário e execução dos commits. O idioma padrão para efetuar commits neste repositório é o inglês. As mensagens devem ser sucintas e expressarem de forma clara e objetiva a ação do commit.

Como exemplo, considere o trabalho da construção de uma tela inicial da aplicação. O commit deverá ser efetuado como segue:
```
git commit -m "Create new home Screen"
```

Atente ainda para os seguintes aspectos:
* O commit deve iniciar com letras maiúsculas.
* O commit deve iniciar com verbo no infinitivo.
Exemplos:  
-"Fix login auth error"  
-"Create User model"  
-"Refactor profile View"  
-"Translate flat pages"

### 1.2 Política de Branches
O repositório possui uma branch `master`, que possui objetivo de manter a versão estável do projeto.
Possui também uma branch para desenvolvimento chamada `devel`, cujo objetivo é manter-se atualizada.
Desta forma nenhum commit deve ser efetuado diretamente nestas branchs. As alterações devem ser criadas inicialmente em branchs de funcionalidades ou de configuração e correção, toda branch de funcionalidade deve ser criada a partir da branch devel. 

A imagem a seguir, ilustra como deve ser a organização das branchs e os eventos de criação e merge de acordo com o [Git Flow](https://leanpub.com/git-flow/read).
![](https://leanpub.com/site_images/git-flow/git-workflow-release-cycle-2feature.png)

Como pode ser visto, após a etapa de desenvolvimento em uma branch de funcionalidade ser concluída, deve ser submetido um pull request em caso de alguma revisão ou merge da mesma. O pull request deve ser conferido por um membro da equipe e se estiver em conformidade, então o pull request é aceito. 

### 1.3 Padrão para criação e uso das branches
Deve-se criar novas branches para trabalho seguindo padrão [GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html). Estas devem ser criadas a partir da branch __develop__, e devem seguir a nomenclatura padrão abaixo, redigidas no idioma inglês. 

O código das branchs deve estar sincronizado com alguma Issue do repositório, sendo então o nome padrão para as branchs no formato:  
__i401_validate_username__  
__i397_create_cluster_group__

### 1.4 Automatização de Fechamento de Issue
Caso termine sua funcionalidade e deseje fechar a Issue automaticamente é possivel através das palavras chaves na descrição do commit ou pull request:  
`resolves: #numeroDaIssue`  
Em caso de múltiplas issues é necessário replicar o comando:  
`resolves: #numeroDaIssue`  
`resolves: #numeroDaIssue2`  
`resolves: #numeroDaIssue3`  

### 1.5 Pull Requests tempestivos e permanentes

Nesse projeto adotamos a política dos pull requests tempestivos e permanentes, ou seja, a partir do primeiro commit deve ser criado o pull request de merge da branch da issue com a develop. Esse pull request é, portanto, tempestivo - criado no primeiro commit - e permanente - permanece aberto enquanto o trabalho da issue estiver sendo executado. Além disso, sugere-se, para alterações no frontend, o envio também de prints ou gifs que ajudem a entender o trabalho realizado.

O autor do pull request deve assignar o grupo de revisão: https://github.com/orgs/ejplatform/teams/revision

### 1.6 Conflitos nos Pull Requests

A branch do PR deve estar sempre atualizado com a branch de desenvolvimento (develop) em caso de conflitos, deve-se realizar um rebase na branch com a develop

* Exceções: commits que podem ser feitos diretamente na devel
  - Fix de conteúdo e css (não arquiteturais)
  - Tradução
  - Cobertura de teste
  - Atualizar assets
  - Commits de melhoramentos/bugfix de pipeline (que precisam ser commitados na branch do pipeline)

### 1.7 Validações de produto

As validações de produto acontecem motivadas pelos PRs do develop para a master. Sempre que um revisor fizer o merge dos PRs vindos das branches de issue pra develop, gera um PR correspondente pra master, acionando a validação de produto, focada na release.

## 2. Integração Contínua e Entrega Contínua

### 2.1. Integração Contínua

O projeto é composto por dois repositórios de códigos e um de documentação. Os repositórios de código são um backend - referente a API do projeto - e um frontend mobile.

Ambos respositórios utilizam a linguagem JavaScript para desenvolvimento. Mas se diferem nos frameworks utilizados, onde o backend utiliza NodeJS em conjunto com as bibliotecas de testes Jest e Supertest; e o frontend utiliza React Native em conjunto com as bibliotecas de testes Jest e Enzyme.

Será utilizado o Github Actions para a realização da Integração Contínua por meio do workflow disponível na ferramenta e sua facilidade de utilização.

### 2.2. Entrega Contínua

A Entrega Contínua é realizada, também, por meio do Github Actions. As alterações realizadas nas branches Develop e Master seguirão um fluxo de trabalho para a realização de uma Build de homologação e uma Build de Produção, respectivamente.

### 2.3. Pipeline

<!-- Adicionar pipelines -->
![](#)