# Critérios de Aceitação

| versão |    data    |                                                                         autor(es)                                                                         |                                     descrição                                      |
| :----: | :--------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: |
|  0.1   | 11/09/2020 |                          [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml)                          |                                Criação do documento                                |
|  0.2   | 13/09/2020 |                          [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml)                          | Adição dos critérios das issues das sprints 2 e 3 (us01, us05, us08..11, us22..30) |
|  0.3   | 15/09/2020 | [@rafaelmakaha](https://github.com/rafaelmakaha), [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml) |                     Remoção de [critérios extras](./extras.md)                     |

Este artefato diz respeito a uma lista de critérios necessários para que as _histórias de usuário_ sejam consideradas concluídas.
[Clique aqui para visualizar as histórias de usuário.](./product_backlog.md)

### US01 - Scannear planta

- [ ] O usuário deve poder acessar a câmera do celular
- [ ] O usuário deve poder scannear a planta por meio da câmera do celular
- [ ] O sistema deve identificar a planta scanneada
- [ ] O sistema deve retornar ao usuário informações sobre a planta scanneada
  <!-- - [ ] O usuário deve poder decidir se deseja compartilhar com o app a foto que scanneou ou não (de forma que esta figuraria no Card daquela Planta) -->
  <!-- - [ ] O usuário deve poder compartilhar a foto tirada em suas comunidades e linha do tempo -->

### US02 - Visualizar minha coleção

- [ ] criterio 1
- [ ] criterio 2

### US03 - Visualizar a data de quando a planta foi coletada

- [ ] criterio 1
- [ ] criterio 2

### US04 - Visualizar, no mapa, onde a planta selecionada fora coletada

- [ ] criterio 1
- [ ] criterio 2

### US05 - Cadastrar minha conta no aplicativo

- [ ] O usuário deve fornecer o username/apelido desejado
- [ ] O usuário deve fornecer o email
- [ ] O usuário deve fornecer a senha
- [ ] O usuário deve fornecer a confirmação de senha
- [ ] O sistema deve validar os dados fornecidos pelo usuário
- [ ] Em caso de invalidação, o sistema deve informar ao usuário quais dados não são válidos.
- [ ] Em caso de invalidação, o sistema deve informar ao usuário o motivo pelo qual aquele dado não é válido.

### US06 - Cadastrar/fazer login com conta Facebook

- [ ] O usuário deve poder realizar login com Facebook.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Facebook.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US07 - Cadastrar/fazer login com conta Google

- [ ] O usuário deve poder realizar login com Google.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Google.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US08 - Fazer login no aplicativo

- [ ] O sistema deve válidar os dados utilizados pelo usuário no login.
- [ ] Em caso de falha de login por dados invalidos, o sistema deve informar que há dados invalidos (sem explicitar quais são).
- [ ] Em caso de login valido, o sistema deve redirecionar o usuário à tela principal.
- [ ] O sistema deve manter a sessão do usuário válida, até que ele decida deslogar.

### US09 - Fazer logout no aplicativo

- [ ] O sistema deve invalidar a sessão do usuário
- [ ] O sistema deve redirecionar o usuário à tela de login

### US10 - Alterar os dados cadastrados na minha conta

- [ ] O usuário deve poder alterar seu username
- [ ] O usuário deve poder alterar seu email
- [ ] O usuário deve poder alterar sua foto de perfil
- [ ] O usuário deve poder alterar sua senha
- [ ] O sistema deve validar as modificações fornecidas pelo usuário

### US11 - Deletar minha conta

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar a conta ou não
- [ ] O sistema deve invalidar a sessão do usuário
- [ ] O sistema deve remover todos os dados pessoais do usuario do banco de dados
  <!-- - [ ] O sistema deve manter os tópicos e comentários nos fóruns (com a tag "usuario removido") -->
  <!-- - [ ] O sistema deve remover os posts, comentários em posts (tanto em comunidades como no próprio feed) -->

### US12 - Visualizar membros da comunidade

- [ ] criterio 1
- [ ] criterio 2

### US13 - Visualizar feed da comunidade

- [ ] criterio 1
- [ ] criterio 2

### US14 - Visualizar a privacidade (publica, privada) da comunidade

- [ ] criterio 1
- [ ] criterio 2

### US15 - Entrar em uma comunidade

- [ ] criterio 1
- [ ] criterio 2

### US16 - Sair de uma comunidade

- [ ] criterio 1
- [ ] criterio 2

### US17 - Criar comunidade

- [ ] criterio 1
- [ ] criterio 2

### US18 - Deletar comunidade

- [ ] criterio 1
- [ ] criterio 2

### US19 - Alterar configurações da comunidade

- [ ] criterio 1
- [ ] criterio 2

### US20 - Enviar convite para usuários ingressarem na comunidade

- [ ] criterio 1
- [ ] criterio 2

### US21 - Expulsar membro da comunidade

- [ ] criterio 1
- [ ] criterio 2

### US22 - Criar tópico em um fórum de planta

- [ ] O usuário deve definir um titulo para o tópico
- [ ] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio
- [ ] O usuário deve poder inserir uma descrição do tópico
  <!-- - [ ] O usuário deve poder editar o estilo da descrição (tipo de fonte (título, subtitulo ou normal), negrito, sublinhado, tachado, mono-espaçado, centralizado, justificado e/ou alinhado à esquerda) -->
  <!-- - [ ] O usuário deve poder adicionar imagens à descrição -->
  <!-- - [ ] O usuário deve poder adicionar hyperlinks à descrição -->

### US23 - Editar tópico criado por mim

- [ ] O usuário deve poder editar o nome do tópico
- [ ] O usuário deve poder editar o conteúdo do tópico
- [ ] O sistema deve validar o titulo do tópico, de forma a garantir que este não está vazio
<!-- - [ ] O sistema deve explicitar que aquele tópico foi editado (com tag '[editado]' por exemplo) -->

### US24 - Deletar o tópico criado por mim

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o tópico ou não
- [ ] O sistema deve deletar o tópico e todos os comentários realizados dentro do mesmo

### US25 - Upvote e downvote em um tópico

- [ ] O usuário, excetuando-se o criador do próprio tópico, deve poder dar uma avaliação positiva ou negativa por intermedio de dois botões auto-explicativos
- [ ] O usuário deve poder desfazer qualquer uma das ações
- [ ] O sistema deve mostrar a diferença (subtração) entre upvotes e downvotes

### US26 - Criar comentário em um tópico

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio
  <!-- - [ ] O usuário deve poder adicionar hyperlinks ao comentário -->
  <!-- - [ ] O usuário deve poder adicionar imagens ao comentário -->
  <!-- - [ ] O usuário deve poder editar o estilo da descrição (negrito, sublinhado, tachado, mono-espaçado) -->

### US27 - Editar comentário que fiz em um tópico

- [ ] O sistema deve validar o conteúdo do comentario, de forma a garantir que este não está vazio
<!-- - [ ] O sistema deve explicitar que aquele comentário foi editado (com tag '[editado]' por exemplo) -->

### US28 - Remover um comentário que fiz em um tópico

- [ ] O sistema deve perguntar ao usuário se ele _realmente_ gostaria de deletar o comentário ou não
- [ ] O sistema deve trocar o conteudo da mensagem por algo explicativo (ex: "comentário removido pelo usuário")
- [ ] O sistema deve manter a existência dos comentários em resposta ao comentário removido

### US29 - Upvote e downvote em um comentário

- [ ] O usuário, excetuando-se o criador do próprio comentário, deve poder dar uma avaliação positiva ou negativa por intermedio de dois botões auto-explicativos
- [ ] O usuário deve poder desfazer qualquer uma das ações
- [ ] O sistema deve mostrar a diferença (subtração) entre upvotes e downvotes

### US30 - Visualizar informações sobre a planta

- [ ] O usuário deve poder visualizar o nome da família desta planta
- [ ] O usuário deve poder visualizar o nome do gênero desta planta
- [ ] O usuário deve poder visualizar o nome da espécie desta planta
- [ ] O usuário deve poder visualizar o nome comum da planta
- [ ] O usuário deve poder visualizar uma imagem de “perfil” da planta
  <!-- - [ ] O usuário deve poder acessar links com informações complementares -->
  <!-- - [ ] O usuário deve poder visualizar os casos comuns de uso desta planta -->
  <!-- - [ ] O usuário deve poder visualizar a primeira pessoa no mundo que coletou-a -->
  <!-- - [ ] O usuário deve poder visualizar quantas vezes a planta ja fora "coletada" (no mundo, pelo app) -->
  <!-- - [ ] O usuário deve poder visualizar o status de extinçao da planta (possíveis referencias: https://www.iucnredlist.org/, https://explorer.natureserve.org) -->
  <!-- - [ ] O usuário deve poder visualizar potenciais usos culinários da planta (receitas), caso seja cabível -->
  <!-- - [ ] O usuário deve poder visualizar instruções de como cultiva-la -->
  <!-- - [ ] O usuário deve poder visualizar ícone indicando quanta exposição à luz (pouca/média/muita) a planta necessita -->
  <!-- - [ ] O usuário deve poder visualizar ícone indicando quantas vezes há de se regar a planta em média semanalmente -->
  <!-- - [ ] O usuário deve poder visualizar ícone indicando o tamanho/porte da planta (pequena...grande) -->
  <!-- - [ ] O usuário deve poder visualizar fotos de outros usuários desta mesma planta -->

### US31 - Adicionar planta aos meus Favoritos

- [ ] criterio 1
- [ ] criterio 2

### US32 - Remover uma planta da minha coleção de favoritos

- [ ] criterio 1
- [ ] criterio 2

### US33 - Visualizar minha coleção de favoritos

- [ ] criterio 1
- [ ] criterio 2

### US34 - Publicar fotos & textos

- [ ] criterio 1
- [ ] criterio 2

### US35 - Visualizar posts de minhas conexões

- [ ] O usuário deve poder visualizar o nome de quem publicou
- [ ] O usuário deve poder visualizar a tag/username/apelido de quem publicou
- [ ] O usuário deve poder visualizar {há quantas horas/data de quando} o post foi publicado
- [ ] O usuário deve poder visualizar a foto publicada pelo usuário
- [ ] O usuário deve poder visualizar a legenda da foto publicada pelo usuário

### US36 - Visualizar trending topics sobre minhas plantas favoritadas

- [ ] criterio 1
- [ ] criterio 2

### US37 - Curtir/descurtir posts que aparecem na minha timeline

- [ ] criterio 1
- [ ] criterio 2

### US38 - Salvar um post na minha coleção de Posts Salvos

- [ ] criterio 1
- [ ] criterio 2

### US39 - Comentar em um post na minha timeline

- [ ] criterio 1
- [ ] criterio 2

### US40 - Editar um comentário que fiz em algum post

- [ ] criterio 1
- [ ] criterio 2

### US41 - Remover um comentario que fiz em algum post

- [ ] criterio 1
- [ ] criterio 2

### US42 - Adicionar apelido à minha planta

- [ ] criterio 1
- [ ] criterio 2

### US43 - Definir configurações de notificação

- [ ] criterio 1
- [ ] criterio 2

### US44 - que o usuário seja obrigado a definir uma meta na criação de uma comunidade

- [ ] criterio 1
- [ ] criterio 2

### US45 - que o usuário seja obrigado a definir o local onde dever-se-a realizar a tal meta

- [ ] criterio 1
- [ ] criterio 2

### US46 - visualizar comunidades que possuam metas definidas em locais próximos ao que me localizo

- [ ] criterio 1
- [ ] criterio 2

### US47 - ser informado, no ato de criação de uma comunidade, caso haja outras comunidades com metas orientadas àquele local

- [ ] criterio 1
- [ ] criterio 2

### US48 - visualizar produtos por categorias (vegetais, ervas, etc)

- [ ] criterio 1
- [ ] criterio 2

### US49 - pesquisar produtos por nome

- [ ] criterio 1
- [ ] criterio 2

### US50 - filtrar produtos por avaliação, preço, categoria etc

- [ ] criterio 1
- [ ] criterio 2

### US51 - comprar produto pelo aplicativo (com cartão, por exemplo)

- [ ] criterio 1
- [ ] criterio 2

### US52 - avaliar minha ultima compra

- [ ] criterio 1
- [ ] criterio 2

### US53 - fazer um anúncio

- [ ] criterio 1
- [ ] criterio 2

### US54 - remover um anúncio

- [ ] criterio 1
- [ ] criterio 2

### US55 - pausar um anúncio

- [ ] criterio 1
- [ ] criterio 2
