# Critérios de Aceitação

| versão |    data    |                                                                         autor(es)                                                                         |                                     descrição                                      |
| :----: | :--------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: |
|  0.1   | 11/09/2020 |                          [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml)                          |                                Criação do documento                                |
|  0.2   | 13/09/2020 |                          [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml)                          | Adição dos critérios das issues das sprints 2 e 3 (us01, us05, us08..11, us22..30) |
|  0.3   | 15/09/2020 | [@rafaelmakaha](https://github.com/rafaelmakaha), [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml) |                     Remoção de [critérios extras](./extras.md)                     |

Este artefato diz respeito a uma lista de critérios necessários para que as _histórias de usuário_ sejam consideradas concluídas.
[Clique aqui para visualizar as histórias de usuário.](./product_backlog.md)

### US01 - Scannear planta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/83) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/71) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/117) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/106) |

- [x] O usuário poderá acessar a câmera do celular
- [x] O usuário poderá scannear a planta por meio da câmera do celular
- [x] O sistema deve identificar a planta scanneada
- [x] O sistema deve retornar ao usuário informações sobre a planta scanneada

### US02 - Visualizar minha coleção

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/84) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/72) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/118) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/123) |

- [x] Visualizar widgets de todas as plantas coletadas
- [x] O widget deve mostrar o apelido da planta
- [ ] O widget deve redirecionar para a tela de Minha Planta caso seja tocado
- [ ] Visualizar mensagem de nenhuma planta coletada caso não existam plantas coletadas

### US03 - Visualizar informações da Minha Planta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/85) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/73) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/114) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/99) |

- [x] Visualizar nome dado pelo usuário a essa planta
- [ ] Visualizar data de quando ela foi adicionada a coleção
- [x] O usuário deve poder alterar o apelido da planta
- [ ] O usuário deve poder re-configurar regras de notificação para lembrá-lo de regar/fertilizar a planta
- [x] O usuário deve poder excluir a mesma

### US04 - Cadastrar minha conta no aplicativo

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/5) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/4) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/14) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/111) |

- [x] O usuário deve fornecer o username/apelido desejado
- [x] O usuário deve fornecer o email
- [x] O usuário deve fornecer a senha
- [x] O usuário deve fornecer a confirmação de senha
- [x] O sistema deve validar os dados fornecidos pelo usuário
- [x] Em caso de invalidação, o sistema deve informar ao usuário quais dados não são válidos.
- [ ] Em caso de invalidação, o sistema deve informar ao usuário o motivo pelo qual aquele dado não é válido.

### US05 - Cadastrar/fazer login com conta Facebook

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/87) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/75) |
| ![Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pulls?q=is%3Apr+is%3Aclosed+87) | [![Pull request] |

- [ ] O usuário poderá realizar login com Facebook.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Facebook.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US06 - Cadastrar/fazer login com conta Google

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/88) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/76) |
| ![Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pulls?q=is%3Apr+is%3Aclosed+88) | [![Pull request] |

- [ ] O usuário poderá realizar login com Google.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Google.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US07 - Fazer login no aplicativo

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/89) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/5) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/18) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/111) |

- [x] O sistema deve válidar os dados utilizados pelo usuário no login.
- [x] Em caso de falha de login por dados invalidos, o sistema deve informar que há dados invalidos (sem explicitar quais são).
- [x] Em caso de login valido, o sistema deve redirecionar o usuário à tela principal.
- [ ] O sistema deve manter a sessão do usuário válida, até que ele decida deslogar.

### US08 - Fazer logout no aplicativo

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/90) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/6) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/18) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/111) |

- [x] O sistema deve invalidar a sessão do usuário
- [x] O sistema deve redirecionar o usuário à tela de login

### US09 - Visualizar minha conta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/91) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/79) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/129) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/117) |

- [x] O usuário poderá visualizar o nome cadastrado
- [x] O usuário poderá visualizar o email cadastrado
- [x] O usuário poderá visualizar a foto de perfil utilizada
- [x] O usuário poderá visualizar o menu de configurações

### US10 - Visualizar configurações da conta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/92) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/80) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pulls?q=is%3Apr+is%3Aclosed+92) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/118) |

- [x] Notificação de novo topico, like e comentario

### US12 - Deletar minha conta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/10) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/7) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/14) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/111) |

- [x] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar a conta ou não
- [x] O sistema deve invalidar a sessão do usuário
- [x] O sistema deve remover todos os dados pessoais do usuario do banco de dados

### US15 - Criar tópico em um fórum de planta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/97) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/85) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [x] O usuário deve definir um titulo para o tópico
- [x] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio
- [x] O usuário poderá inserir uma descrição do tópico

### US16 - Editar tópico criado por mim

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/98) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/86) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [x] O usuário poderá editar o nome do tópico
- [x] O usuário poderá editar o conteúdo do tópico
- [x] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio

### US17 - Deletar o tópico criado por mim

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/99) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/87) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [x] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o tópico ou não
- [x] O sistema deve substituir o tópico por alguma mensagem explicativo (ex: "topico deletado") e manter os comentarios criados dentro do topico

### US18 - Upvote e downvote em um tópico

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/100) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/88) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [x] O usuário poderá dar uma avaliação positiva por intermedio de um botao auto-explicativo
- [x] O usuário poderá desfazer a ação
- [x] O sistema deve mostrar a quantidade de upvotes

### US19 - Criar comentário em um tópico

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/101) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/89) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [x] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio

### US20 - Editar comentário que fiz em um tópico

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/102) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/90) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [x] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio

### US21 - Remover um comentário que fiz em um tópico

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/103) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/91) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o comentário ou não

### US22 - Upvote e downvote em um comentário

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/104) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/92) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/82) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/103) |

- [x] O usuário, excetuando-se o criador do próprio comentário, poderá dar uma avaliação positiva
- [x] O usuário poderá desfazer a ação
- [x] O sistema deve mostrar a quantidade de upvotes

### US23 - Visualizar informações sobre a planta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/85) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/93) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/114) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/99) |

- [x] O usuário poderá visualizar o nome da família desta planta
- [x] O usuário poderá visualizar o nome do gênero desta planta
- [x] O usuário poderá visualizar o nome da espécie desta planta
- [x] O usuário poderá visualizar o nome comum da planta
- [x] O usuário poderá visualizar uma imagem de “perfil” da planta

### US24 - Adicionar planta aos meus Favoritos

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/106) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/94) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/124) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/116) |

<adicionar>

### US25 - Remover uma planta da minha coleção de favoritos

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/107) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/95) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/124) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/116) |

- [x] O sistema deverá remover a referida planta da coleção de favoritos

### US26 - Visualizar minha coleção de favoritos

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/108) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/96) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/106) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/116) |

- [x] O usuário poderá abrir os cards de planta diretamente da aba de favoritos
- [x] Cada widget das plantas adicionadas à coleção de favoritos deverá mostrar seu Nome Comum
- [x] Cada widget das plantas adicionadas à coleção de favoritos deverá mostrar seu nome científico
- [x] Cada widget das plantas adicionadas à coleção de favoritos deverá mostrar um botão que redireciona, também, ao card de planta

### US27 - Adicionar apelido à minha planta

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/109) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/97) |
| [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pull/114) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/99) |

- [x] O usuário deverá adicionar um apelido a sua planta após o processo de scanneamento da mesma
- [x] O usuário poderá alterar o apelido da planta a qualquer momento em sua coleção
- [x] O sistema deverá garantir que o apelido é válido

### US28 - Definir configurações de notificação

| Backend | Frontend |
| ------- | -------- |
| [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/issues/110) | [Issue](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/issues/98) |
| ![Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-BackEnd/pulls?q=is%3Apr+is%3Aclosed+110) | [Pull request](https://github.com/fga-eps-mds/2020.1-GaiaDex-FrontEnd/pull/118) |

- [ ] O usuário deve poder configurar regras de notificação para lembrá-lo de regar/fertilizar a planta

