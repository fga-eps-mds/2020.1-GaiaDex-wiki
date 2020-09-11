| versão |    data    |                                                autor(es)                                                |      descrição       |
| :----: | :--------: | :-----------------------------------------------------------------------------------------------------: | :------------------: |
|  0.1   | 11/09/2020 | [@guilhermedelyra](https://github.com/guilhermedelyra) e [@joaovitorml](https://github.com/joaovitorml) | Criação do documento |

# Critérios de Aceitação

Este artefato diz respeito a uma lista de critérios necessários para que as _histórias de usuário_ sejam consideradas concluídas.
[Clique aqui para visualizar as histórias de usuário.](./product_backlog.md)

### US01 - Scannear planta

- [ ] O usuário deve poder acessar a câmera do celular
- [ ] O usuário deve poder scannear a planta por meio da câmera do celular
- [ ] O sistema deve identificar a planta scanneada
- [ ] O sistema deve retornar ao usuário informações sobre a planta scanneada

### US07 - Cadastrar minha conta no aplicativo

- [ ] O usuário deve fornecer o username/apelido desejado
- [ ] O usuário deve fornecer o email
- [ ] O usuário deve fornecer a senha
- [ ] O usuário deve fornecer a confirmação de senha
- [ ] O sistema deve validar os dados fornecidos pelo usuário
- [ ] Em caso de invalidação, o sistema deve informar ao usuário quais dados não são válidos.
- [ ] Em caso de invalidação, o sistema deve informar ao usuário o motivo pelo qual aquele dado não é válido.

### US15 - Cadastrar com conta do Google

- [ ] O usuário deve poder realizar login com Google.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Google.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US16 - Cadastrar com conta do Facebook

- [ ] O usuário deve poder realizar login com Facebook.
- [ ] O sistema deve pedir permissão ao usuário para acessar as informações do Facebook.
- [ ] O sistema deve mostrar uma mensagem de erro caso o login não seja realizado.

### US51 - Visualizar posts de minhas conexões

- [ ] O usuário deve poder visualizar o nome de quem publicou
- [ ] O usuário deve poder visualizar a tag/username/apelido de quem publicou
- [ ] O usuário deve poder visualizar {há quantas horas/data de quando} o post foi publicado
- [ ] O usuário deve poder visualizar a foto publicada pelo usuário
- [ ] O usuário deve poder visualizar a legenda da foto publicada pelo usuário

### US08 - Fazer login no aplicativo

- [ ] O usuário deve poder logar no aplicativo
- [ ] O sistema deve válidar os dados utilizados pelo usuário no login.
- [ ] O usuário deve poder logar com o Facebook

### US09 - Fazer logout no aplicativo

- [ ] O usuário deve poder deslogar da conta
- [ ] O sistema deve pedir as informações do usuário novamente para ele poder fazer login

<!-- ```

### US003 - visualizar meu perfil

- [ ] O usuário deve poder visualizar seu nome de usuário.
- [ ] O usuário deve poder visualizar sua foto.
- [ ] O usuário deve poder visualizar a quantidade de Ribons que ele possui.
- [ ] O usuário deve poder visualizar a quantidade de Ribons doados.
- [ ] O usuário deve poder visualizar a quantidade de dias que ele ajudou cada causa.

### - visualizar trending posts das comunidades que participo
```

|  ID  |     Épico      |       eu como       |                                          quero                                           |          para          | Prioridade |
| :--: | :------------: | :-----------------: | :--------------------------------------------------------------------------------------: | :--------------------: | :--------: |
| US01 |     Perfil     |       Usuário       |                                Fazer login no aplicativo                                 |           -            |    Must    |
| US02 |     Perfil     |       Usuário       |                           Cadastrar minha conta no aplicativo                            |           -            |    Must    |
| US03 |     Perfil     |       Usuário       |                                Fazer logout no aplicativo                                |           -            |    Must    |
| US04 |     Perfil     |       Usuário       |                       Alterar os dados cadastrados na minha conta                        |           -            |    Must    |
| US05 |     Perfil     |       Usuário       |                                   Deletar minha conta                                    |           -            |    Must    |
| US06 |     Perfil     |       Usuário       |                                    Cadastrar meu nome                                    |           -            |    Must    |
| US07 |     Perfil     |       Usuário       |                                   Cadastrar meu e-mail                                   |           -            |    Must    |
| US08 |     Perfil     |       Usuário       |                             Cadastrar minha senha de acesso                              |           -            |    Must    |
| US09 |     Perfil     |       Usuário       |                              Cadastrar com conta da Google                               |           -            |    Want    |
| US10 |     Perfil     |       Usuário       |                             Cadastrar com conta do Facebook                              |           -            |    Want    |
| US11 |   Planta-dex   |       Usuário       |                                     Scannear planta                                      |           0            |    Must    |
| US12 |   Planta-dex   |       Usuário       |                                 Visualizar minha coleção                                 |           -            |    Must    |
| US13 |  Minha Planta  |       Usuário       |                             Adicionar apelido à minha planta                             |           q            |   Could    |
| US14 |  Minha Planta  |       Usuário       |                    Visualizar a data de quando a planta foi coletada                     |           -            |   Could    |
| US15 |  Minha Planta  |       Usuário       |               Visualizar, no mapa, onde a planta selecionada fora coletada               |           -            |   Could    |
| US16 |  Minha Planta  |       Usuário       |                           Definir configurações de notificação                           |           ta           |   Could    |
| US17 |   Comunidade   |       Usuário       |                             Visualizar membros da comunidade                             |           -            |   Could    |
| US18 |   Comunidade   |       Usuário       |                       Visualizar timeline (de posts) da comunidade                       |           -            |   Could    |
| US19 |   Comunidade   |       Usuário       |           Visualizar a privacidade (publica, privada ou secreta) da comunidade           |           -            |   Could    |
| US20 |   Comunidade   |       Usuário       |                                 Entrar em uma comunidade                                 |           -            |   Could    |
| US21 |   Comunidade   |       Usuário       |                                  Sair de uma comunidade                                  |           -            |   Could    |
| US22 |   Comunidade   |       Usuário       |                                     Criar comunidade                                     |           -            |   Could    |
| US23 |   Comunidade   | Dono de Comunidade  |                                    Deletar comunidade                                    |           -            |   Could    |
| US24 |   Comunidade   | Dono de Comunidade  |                           Alterar configurações da comunidade                            |           -            |   Could    |
| US25 |   Comunidade   | Dono de Comunidade  |                  Enviar convite para usuários ingressarem na comunidade                  |           -            |   Could    |
| US26 |   Comunidade   | Dono de Comunidade  |                              Expulsar membro da comunidade                               |           -            |   Could    |
| US27 |     Tópico     |       Usuário       |                            Criar tópico em um fórum de planta                            |           -            |    Must    |
| US28 |     Tópico     |       Usuário       |                               Editar tópico criado por mim                               |           -            |    Must    |
| US29 |     Tópico     |       Usuário       |                             Deletar o tópico criado por mim                              |           -            |    Must    |
| US30 |     Tópico     |       Usuário       |                              Criar comentário em um tópico                               |           -            |    Must    |
| US31 |     Tópico     |       Usuário       |                              Remover um comentário que fiz                               |           -            |    Must    |
| US32 |     Tópico     |       Usuário       |                           Upvote e downvote em uma comentário                            |           -            |    Must    |
| US33 | Card de Planta |       Usuário       |                   Visualizar a primeira pessoa no mundo que coletou-a                    |           -            |   Could    |
| US34 | Card de Planta |       Usuário       |                    Visualizar quantas vezes a planta ja fora coletada                    |           -            |   Could    |
| US35 | Card de Planta |       Usuário       |                         Visualizar instruções de como cultiva-la                         |           -            |    Must    |
| US36 | Card de Planta |       Usuário       |                        Visualizar o status de extinçao da planta                         |           -            |    Want    |
| US37 | Card de Planta |       Usuário       |           Visualizar potenciais usos culinários da planta (caso seja cabível)            |           -            |   Could    |
| US38 | Card de Planta |       Usuário       |                          Visualizar o nome científico da planta                          |           -            |    Must    |
| US39 | Card de Planta |       Usuário       |                            Visualizar o nome comum da planta                             |           -            |    Must    |
| US40 | Card de Planta |       Usuário       |                       Visualizar uma imagem de “perfil” da planta                        |           -            |    Must    |
| US41 | Card de Planta |       Usuário       | Visualizar ícone indicando quanta exposição à luz (pouca/média/muita) a planta necessita |           -            |    Must    |
| US42 | Card de Planta |       Usuário       |  Visualizar ícone indicando quantas vezes há de se regar a planta em média semanalmente  |           -            |    Must    |
| US43 | Card de Planta |       Usuário       |         Visualizar ícone indicando o tamanho/porte da planta (pequena...grande)          |           -            |    Must    |
| US44 |     Fórum      | Mantenedor de fórum |                                     Excluir tópicos                                      |           -            |    Must    |
| US45 |     Fórum      | Mantenedor de fórum |                                    Excluir comentário                                    |           -            |    Must    |
| US46 |     Fórum      | Mantenedor de fórum |                                  Banir usuário do fórum                                  |           -            |    Must    |
| US47 |   Favoritos    |       Usuário       |                           Adicionar planta aos meus Favoritos                            |           -            |   Could    |
| US48 |   Favoritos    |       Usuário       |                     Remover uma planta da minha coleção de favoritos                     |           -            |   Could    |
| US49 |   Favoritos    |       Usuário       |                          Visualizar minha coleção de favoritos                           |           -            |   Could    |
| US50 |      Feed      |       Usuário       |                                 Publicar fotos & textos                                  |           -            |    Want    |
| US51 |      Feed      |       Usuário       |                           Visualizar posts de minhas conexões                            |           -            |    Want    |
| US52 |      Feed      |       Usuário       |               Visualizar trending topics sobre minhas plantas favoritadas                |           -            |    Want    |
| US53 |      Feed      |       Usuário       |                  Curtir/descurtir posts que aparecem na minha timeline                   |           -            |    Want    |
| US54 |      Feed      |       Usuário       |                     Salvar um post na minha coleção de Posts Salvos                      |           -            |    Want    |
| US55 |      Feed      |       Usuário       |                          Comentar em um post na minha timeline                           |           -            |    Want    |
| US56 |      Feed      |       Usuário       |                       Remover um comentario que fiz em algum post                        |           -            |    Want    |
| US57 |       -        |    Desenvolvedor    |                                   Um ambiente estável                                    | desenvolver meu código |    Must    | -->
