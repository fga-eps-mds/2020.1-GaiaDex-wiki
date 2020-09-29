# Critérios de Aceitação

| versão |    data    |                                                                         autor(es)                                                                         |                                     descrição                                      |
| :----: | :--------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: |
|  0.1   | 11/09/2020 |                          [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml)                          |                                Criação do documento                                |
|  0.2   | 13/09/2020 |                          [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml)                          | Adição dos critérios das issues das sprints 2 e 3 (us01, us05, us08..11, us22..30) |
|  0.3   | 15/09/2020 | [@rafaelmakaha](https://github.com/rafaelmakaha), [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml) |                     Remoção de [critérios extras](./extras.md)                     |

Este artefato diz respeito a uma lista de critérios necessários para que as _histórias de usuário_ sejam consideradas concluídas.
[Clique aqui para visualizar as histórias de usuário.](./product_backlog.md)

### US01 - Scannear planta

- [ ] O usuário poderá acessar a câmera do celular
- [ ] O usuário poderá scannear a planta por meio da câmera do celular
- [ ] O sistema deve identificar a planta scanneada
- [ ] O sistema deve retornar ao usuário informações sobre a planta scanneada

### US02 - Visualizar minha coleção

- [ ] Visualizar todas as plantas coletadas
- [ ] Visualizar mensagem de nenhuma planta coletada caso não existam plantas coletadas

### US03 - Visualizar informações da Minha Planta

- [ ] Visualizar nome dado pelo usuário a essa planta
- [ ] Visualizar data de quando ela foi adicionada a coleção

### US04 - Cadastrar minha conta no aplicativo

- [ ] O usuário deve fornecer o username/apelido desejado
- [ ] O usuário deve fornecer o email
- [ ] O usuário deve fornecer a senha
- [ ] O usuário deve fornecer a confirmação de senha
- [ ] O sistema deve validar os dados fornecidos pelo usuário
- [ ] Em caso de invalidação, o sistema deve informar ao usuário quais dados não são válidos.
- [ ] Em caso de invalidação, o sistema deve informar ao usuário o motivo pelo qual aquele dado não é válido.

### US05 - Cadastrar/fazer login com conta Facebook

- [ ] O usuário poderá realizar login com Facebook.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Facebook.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US06 - Cadastrar/fazer login com conta Google

- [ ] O usuário poderá realizar login com Google.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Google.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US07 - Fazer login no aplicativo

- [ ] O sistema deve válidar os dados utilizados pelo usuário no login.
- [ ] Em caso de falha de login por dados invalidos, o sistema deve informar que há dados invalidos (sem explicitar quais são).
- [ ] Em caso de login valido, o sistema deve redirecionar o usuário à tela principal.
- [ ] O sistema deve manter a sessão do usuário válida, até que ele decida deslogar.

### US08 - Fazer logout no aplicativo

- [ ] O sistema deve invalidar a sessão do usuário
- [ ] O sistema deve redirecionar o usuário à tela de login

### US09 - Visualizar minha conta

- [ ] O usuário poderá visualizar o nome cadastrado
- [ ] O usuário poderá visualizar o email cadastrado
- [ ] O usuário poderá visualizar a foto de perfil utilizada
- [ ] O usuário poderá visualizar o menu de configurações

### US10 - Visualizar configurações da conta

- [ ] O usuário poderá visualizar as Politicas de Privacidade do aplicativo
- [ ] O usuário poderá visualizar os Termos de Uso
- [ ] O usuário poderá visualizar botão de Ajuda
- [ ] O usuário poderá visualizar o botão de Privacidade

### US11 - Alterar os dados cadastrados na minha conta

- [ ] O usuário poderá alterar seu username
- [ ] O usuário poderá alterar seu email
- [ ] O usuário poderá alterar sua foto de perfil
- [ ] O usuário poderá alterar sua senha
- [ ] O sistema deve validar as modificações fornecidas pelo usuário

### US12 - Deletar minha conta

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar a conta ou não
- [ ] O sistema deve invalidar a sessão do usuário
- [ ] O sistema deve remover todos os dados pessoais do usuario do banco de dados

### US13 - Visualizar perfil de outro usuário

- [ ] O usuário poderá visualizar o nome do outro usuário
- [ ] O usuário poderá visualizar a foto de perfil do outro usuário
- [ ] O usuário poderá, de acordo com as configurações de privacidade do outro usuário, visualizar a lista de amigos do outro usuário
- [ ] O usuário poderá, de acordo com as configurações de privacidade do outro usuário, visualizar as publicações deste usuário

### US14 - Bloquear outro usuário

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de bloquear o outro usuário
- [ ] O sistema deverá adicionar o outro usuário à lista de bloqueio deste usuário
- [ ] O sistema deverá garantir que o usuário nunca verá nada que dê indicios da existencia do outro usuário (perfil, comentarios, posts...), e vice-versa

### US15 - Adicionar amizade

- [ ] O sistema deverá notificar o usuário solicitado sobre o pedido.
- [ ] O usuário poderá aceitar ou recusar uma solicitação de amizade.
- [ ] O usuário poderá enviar uma solicitação de amizade à qualquer usuário.

### US16 - Remover amizade

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de remover a amizade ou não
- [ ] O sistema deverá encerrar a conexão entre os dois usuários

### US17 - Criar tópico em um fórum de planta

- [ ] O usuário deve definir um titulo para o tópico
- [ ] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio
- [ ] O usuário poderá inserir uma descrição do tópico

### US18 - Editar tópico criado por mim

- [ ] O usuário poderá editar o nome do tópico
- [ ] O usuário poderá editar o conteúdo do tópico
- [ ] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio

### US19 - Deletar o tópico criado por mim

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o tópico ou não
- [ ] O sistema deve deletar o tópico e todos os comentários realizados dentro do mesmo

### US20 - Upvote e downvote em um tópico

- [ ] O usuário, excetuando-se o criador do próprio tópico, poderá dar uma avaliação positiva ou negativa por intermedio de dois botões auto-explicativos
- [ ] O usuário poderá desfazer qualquer uma das ações
- [ ] O sistema deve mostrar a diferença (subtração) entre upvotes e downvotes

### US21 - Criar comentário em um tópico

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio

### US22 - Editar comentário que fiz em um tópico

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio

### US23 - Remover um comentário que fiz em um tópico

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o comentário ou não
- [ ] O sistema deve trocar o conteudo da mensagem por algo explicativo (ex: "comentário removido pelo usuário")
- [ ] O sistema deve manter a existência dos comentários em resposta ao comentário removido

### US24 - Upvote e downvote em um comentário

- [ ] O usuário, excetuando-se o criador do próprio comentário, poderá dar uma avaliação positiva ou negativa por intermedio de dois botões auto-explicativos
- [ ] O usuário poderá desfazer qualquer uma das ações
- [ ] O sistema deve mostrar a diferença (subtração) entre upvotes e downvotes

### US25 - Visualizar informações sobre a planta

- [ ] O usuário poderá visualizar o nome da família desta planta
- [ ] O usuário poderá visualizar o nome do gênero desta planta
- [ ] O usuário poderá visualizar o nome da espécie desta planta
- [ ] O usuário poderá visualizar o nome comum da planta
- [ ] O usuário poderá visualizar uma imagem de “perfil” da planta

### US26 - Adicionar planta aos meus Favoritos

- [ ] O usuário deverá apertar em um botão no card de planta para adicionar a mesma aos favoritos
- [ ] O sistema deverá enviar a referida planta a coleção de favoritos

### US27 - Remover uma planta da minha coleção de favoritos

- [ ] O botão de enviar aos favoritos irá se transformar em botão de remover dos favoritos se a referida planta já estiver na coleção de favoritos
- [ ] O sistema deverá remover a referida planta da coleção de favoritos

### US28 - Visualizar minha coleção de favoritos

- [ ] O usuário poderá abrir os cards de planta diretamente da aba de favoritos

### US29 - Adicionar apelido à minha planta

- [ ] O usuário deverá adicionar um apelido a sua planta após o processo de scanneamento da mesma
- [ ] O usuário poderá alterar o apelido da planta a qualquer momento em sua coleção

### US30 - Definir configurações de notificação

- [ ] O usuário deverá receber notificação quando um amigo publicar um post
- [ ] O usuário deverá receber notificação quando um amigo comentar em um posto do mesmo
- [ ] O usuário poderá escolher se deseja receber ou não notificações

