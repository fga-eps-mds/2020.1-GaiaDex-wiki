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

### US09 - Alterar os dados cadastrados na minha conta

- [ ] O usuário poderá alterar seu username
- [ ] O usuário poderá alterar seu email
- [ ] O usuário poderá alterar sua foto de perfil
- [ ] O usuário poderá alterar sua senha
- [ ] O sistema deve validar as modificações fornecidas pelo usuário

### US10 - Deletar minha conta

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar a conta ou não
- [ ] O sistema deve invalidar a sessão do usuário
- [ ] O sistema deve remover todos os dados pessoais do usuario do banco de dados

### US11 - Visualizar membros da comunidade

- [ ] Visualizar cargo de cada membro da comunidade

### US12 - Visualizar feed da comunidade

- [ ] Visualizar posts de amigos no feed
- [ ] Visualizar posts relacionados a uma planta favorita no feed

### US13 - Visualizar a privacidade (publica, privada) da comunidade

- [ ] criterio1
- [ ] criterio2

### US14 - Entrar em uma comunidade

- [ ] O usuário poderá apertar em um botão escrito "Entrar" no perfil da comunidade
- [ ] O sistema deve enviar uma mensagem para o dono da comunidade avisando do interesse do usuário de entrar na comunidade

### US15 - Sair de uma comunidade

- [ ] O usuário poderá apertar em um botão escrito "Sair" no perfil da comunidade
- [ ] O sistema deve enviar uma mensagem perguntando se o usuário quer mesmo sair da comunidade

### US16 - Criar comunidade

- [ ] O usuário que criar uma comunidade será o dono da mesma
- [ ] O usuário deverá definir a privacidade da comunidade
- [ ] O sistema deverá criar as abas de perfil, membros e configurações da comunidade

### US17 - Deletar comunidade

- [ ] O dono da comunidade poderá apertar um botão escrito "Deletar comunidade" nas configurações da comunidade para deletar a mesma
- [ ] O sistema deverá retirar todos os membros da comunidade deletada

### US18 - Alterar configurações da comunidade

- [ ] O dono da comunidade poderá alterar a privacidade da comunidade nas configurações da mesma

### US19 - Enviar convite para usuários ingressarem na comunidade

- [ ] O dono de comunidade pode enviar convite para membros ingressarem em sua comunidade
- [ ] Os membros convidados podem ingressar na comunidade apertando em um botão "Aceitar" localizado no convite

### US20 - Expulsar membro da comunidade

- [ ] O dono de comunidade pode remover um membro da mesma apertando um botão do lado do username do membro desejado
- [ ] O sistema deverá perguntar ao dono da comunidade se ele deseja realmente excluir o membro da mesma

### US21 - Criar tópico em um fórum de planta

- [ ] O usuário deve definir um titulo para o tópico
- [ ] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio
- [ ] O usuário poderá inserir uma descrição do tópico

### US22 - Editar tópico criado por mim

- [ ] O usuário poderá editar o nome do tópico
- [ ] O usuário poderá editar o conteúdo do tópico
- [ ] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio

### US23 - Deletar o tópico criado por mim

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o tópico ou não
- [ ] O sistema deve deletar o tópico e todos os comentários realizados dentro do mesmo

### US24 - Upvote e downvote em um tópico

- [ ] O usuário, excetuando-se o criador do próprio tópico, poderá dar uma avaliação positiva ou negativa por intermedio de dois botões auto-explicativos
- [ ] O usuário poderá desfazer qualquer uma das ações
- [ ] O sistema deve mostrar a diferença (subtração) entre upvotes e downvotes

### US25 - Criar comentário em um tópico

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio

### US26 - Editar comentário que fiz em um tópico

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio

### US27 - Remover um comentário que fiz em um tópico

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o comentário ou não
- [ ] O sistema deve trocar o conteudo da mensagem por algo explicativo (ex: "comentário removido pelo usuário")
- [ ] O sistema deve manter a existência dos comentários em resposta ao comentário removido

### US28 - Upvote e downvote em um comentário

- [ ] O usuário, excetuando-se o criador do próprio comentário, poderá dar uma avaliação positiva ou negativa por intermedio de dois botões auto-explicativos
- [ ] O usuário poderá desfazer qualquer uma das ações
- [ ] O sistema deve mostrar a diferença (subtração) entre upvotes e downvotes

### US29 - Visualizar informações sobre a planta

- [ ] O usuário poderá visualizar o nome da família desta planta
- [ ] O usuário poderá visualizar o nome do gênero desta planta
- [ ] O usuário poderá visualizar o nome da espécie desta planta
- [ ] O usuário poderá visualizar o nome comum da planta
- [ ] O usuário poderá visualizar uma imagem de “perfil” da planta

### US30 - Adicionar planta aos meus Favoritos

- [ ] O usuário deverá apertar em um botão no card de planta para adicionar a mesma aos favoritos
- [ ] O sistema deverá enviar a referida planta a coleção de favoritos

### US31 - Remover uma planta da minha coleção de favoritos

- [ ] O botão de enviar aos favoritos irá se transformar em botão de remover dos favoritos se a referida planta já estiver na coleção de favoritos
- [ ] O sistema deverá remover a referida planta da coleção de favoritos

### US32 - Visualizar minha coleção de favoritos

- [ ] O usuário poderá abrir os cards de planta diretamente da aba de favoritos

### US33 - Publicar fotos & textos

- [ ] O usuário poderá publicar fotos e textos apertando em um botão na timeline

### US34 - Visualizar posts de minhas conexões

- [ ] O usuário poderá visualizar o nome de quem publicou o post
- [ ] O usuário poderá visualizar a tag/username/apelido de quem publicou
- [ ] O usuário poderá visualizar {há quantas horas/data de quando} o post foi publicado
- [ ] O usuário poderá visualizar a foto publicada pelo usuário
- [ ] O usuário poderá visualizar a legenda da foto publicada pelo usuário

### US35 - Visualizar trending topics sobre minhas plantas favoritadas

- [ ] O usuário poderá ver no seu feed os trending topics sobre as plantas favoritadas

### US36 - Curtir/descurtir posts que aparecem na minha timeline

- [ ] O usuário poderá apertar em um botão curtir ou em um botão descutir nos posts que aparecem na timeline do mesmo

### US37 - Salvar um post na minha coleção de Posts Salvos

- [ ] O usuário poderá apertar em um botão nas opções do post para adicioná-lo a coleção de posts salvos
- [ ] O usuário poderá remover um post de sua coleção de posts salvos

### US38 - Comentar em um post na minha timeline

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio
- [ ] Outro usuário poderá responder ao seu comentário, que por sua vez poderá ser respondido também

### US39 - Editar um comentário que fiz em algum post

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio

### US40 - Remover um comentario que fiz em algum post

- [ ] O sistema deverá remover todas as respostas a um comentário que foi removido de um post

### US41 - Adicionar apelido à minha planta

- [ ] criterio1
- [ ] criterio2

### US42 - Definir configurações de notificação

- [ ] O usuário deverá receber notificação quando um amigo publicar um post
- [ ] O usuário deverá receber notificação quando um amigo comentar em um posto do mesmo
- [ ] O usuário poderá escolher se deseja receber ou não notificações

### US43 - que o usuário seja obrigado a definir uma meta na criação de uma comunidade

- [ ] criterio1
- [ ] criterio2

### US44 - que o usuário seja obrigado a definir o local onde dever-se-a realizar a tal meta

- [ ] criterio1
- [ ] criterio2

### US45 - visualizar comunidades que possuam metas definidas em locais próximos ao que me localizo

- [ ] criterio1
- [ ] criterio2

### US46 - ser informado, no ato de criação de uma comunidade, caso haja outras comunidades com metas orientadas àquele local

- [ ] criterio1
- [ ] criterio2

### US47 - visualizar produtos por categorias (vegetais, ervas, etc)

- [ ] criterio1
- [ ] criterio2

### US48 - pesquisar produtos por nome

- [ ] O usuário poderá digitar o nome do produto que está procurando
- [ ] Se o produto não existe, o sistema deverá exibir uma mensagem: "Desculpe, mas não existem produtos com este nome"

### US49 - filtrar produtos por avaliação, preço, categoria etc

- [ ] O usuário poderá utilizar filtros localizados no topo do marketplace
- [ ] Quando pelo menos um filtro estiver selecionado, aparecerá um botão próximo aos filtros que permite ao usuário limpar todos os filtros

### US50 - comprar produto pelo aplicativo (com cartão, por exemplo)

- [ ] O usuário poderá escolher entre compar com o aplicativo ou não durante o processo da compra

### US51 - avaliar minha ultima compra

- [ ] Após finalizada a compra, deverá aparecer ao usuário uma mensagem pedindo que o mesmo avalie o produto quando ele chegar

### US52 - fazer um anúncio

- [ ] O vendedor poderá anunciar um produto por meio de um botão no marketplace
- [ ] O vendedor deverá definir o nome, o preço e mais algumas informações acerca do produto

### US53 - remover um anúncio

- [ ] O vendedor poderá retirar um anúncio feito anteriormente por ele a qualquer momento por meio de outro botão no marketplace

### US54 - pausar um anúncio

- [ ] O usuário poderá esconder/pausar um anúncio feito por ele anteiormente por meio de outro botão no marketplace

