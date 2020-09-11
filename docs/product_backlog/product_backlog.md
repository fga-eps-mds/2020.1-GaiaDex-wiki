# 1. Épicos

| ID   | Épico          | Descrição                                                                                                                                    | Prioridade |
| ---- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| EP01 | Planta-dex     | Inventário, estilo Pokedex, indicando quais plantas o usuário já coletou                                                                     | Must       |
| EP02 | Perfil         | Informações relativas ao usuário                                                                                                             | Must       |
| EP03 | Card de Planta | Informações relativas à planta                                                                                                               | Must       |
| EP04 | Fórum          | Threads que um usuário pode abrir dentro do fórum (único) de cada planta, onde haverá interações (comentários, respostas etc) entre usuários | Must       |
| EP05 | Favoritos      | Coleção de plantas favoritadas                                                                                                               | Should     |
| EP06 | Feed           | Feed de notícia onde o usuário visualizará os trending topics das plantas favoritadas, além de visualizar posts de suas conexões             | Could      |
| EP07 | Comunidade     | Grupos criados e gerenciados por usuários                                                                                                    | Could      |
| EP08 | Meta           | Metas estabelecidas (e intrinsecas) aos grupos, orientadas, por exemplo, à revitalização urbana                                              | Could      |
| EP09 | Histórico/Log  | Listar todas as atividades que um usuário fez (comentarios em posts, scans etc)                                                              | Want-      |
| EP10 | Minha Planta   | Planta que fora adicionada à coleção do usuário e está sendo cultivada pelo mesmo                                                            | Should     |
| EP11 | Marketplace    | Espaço onde o usuário pode comprar/vender produtos orgânicos                                                                                 | Want+      |

# 2. User Stories

|  ID  |      Épico      |       eu como       |                                                       quero                                                        |                                                para                                                | Prioridade (em relação ao épico) |
| :--: | :-------------: | :-----------------: | :----------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------: | -------------------------------- |
| US01 |   Planta-dex    |       Usuário       |                                                  Scannear planta                                                   |                                     adicionar à minha coleção                                      | Must                             |
| US02 |   Planta-dex    |       Usuário       |                                              Visualizar minha coleção                                              |                           saber quais plantas eu possuo na minha coleção                           | Must                             |
| US03 |   Planta-dex    |       Usuário       |                                 Visualizar a data de quando a planta foi coletada                                  |                                lembrar do dia que coletei a planta                                 | Could                            |
| US04 |   Planta-dex    |       Usuário       |                            Visualizar, no mapa, onde a planta selecionada fora coletada                            |                                  lembrar onde encontrei a planta                                   | Want                             |
| US05 |     Perfil      |       Usuário       |                                        Cadastrar minha conta no aplicativo                                         |                                poder informar meus dados ao sistema                                | Must                             |
| US06 |     Perfil      |       Usuário       |                                             Fazer login no aplicativo                                              |                             acessar as demais funcionalidades do mesmo                             | Must                             |
| US07 |     Perfil      |       Usuário       |                                             Fazer logout no aplicativo                                             |                                        sair da minha conta                                         | Must                             |
| US08 |     Perfil      |       Usuário       |                                    Alterar os dados cadastrados na minha conta                                     |                                       mantê-los atualizados                                        | Should                           |
| US09 |     Perfil      |       Usuário       |                                                Deletar minha conta                                                 |                              impedir o acesso a mesma permanentemente                              | Should                           |
| US10 |   Comunidade    |       Usuário       |                                          Visualizar membros da comunidade                                          |                                      procurar novas amizades                                       | Should+                          |
| US11 |   Comunidade    |       Usuário       |                                           Visualizar feed da comunidade                                            |                                me manter atualizado acerca da mesma                                | Must                             |
| US12 |   Comunidade    |       Usuário       |                             Visualizar a privacidade (publica, privada) da comunidade                              |                                 saber das intenções da comunidade                                  | Could-                           |
| US13 |   Comunidade    |       Usuário       |                                              Entrar em uma comunidade                                              |                                        fazer parte da mesma                                        | Must                             |
| US14 |   Comunidade    |       Usuário       |                                               Sair de uma comunidade                                               |                                   não fazer mais parte da mesma                                    | Must                             |
| US15 |   Comunidade    | Dono de Comunidade  |                                                  Criar comunidade                                                  |                               juntar pessoas com interesses em comum                               | Must                             |
| US16 |   Comunidade    | Dono de Comunidade  |                                                 Deletar comunidade                                                 |                              desfazer o que não quero mais que exista                              | Must                             |
| US17 |   Comunidade    | Dono de Comunidade  |                                        Alterar configurações da comunidade                                         |                          ajustar a comunidade com o formato que eu desejo                          | Must                             |
| US18 |   Comunidade    | Dono de Comunidade  |                               Enviar convite para usuários ingressarem na comunidade                               |                          dar permissão para o usuário ingressar na mesma                           | Must-                            |
| US19 |   Comunidade    | Dono de Comunidade  |                                           Expulsar membro da comunidade                                            |                         remover quem não atende aos padrões da comunidade                          | Must                             |
| US20 |      Fórum      |       Usuário       |                                         Criar tópico em um fórum de planta                                         |                        obter informações relativas a algo do meu interesse                         | Must                             |
| US21 |      Fórum      |       Usuário       |                                            Editar tópico criado por mim                                            |                              modificar um erro que eu tenha cometido                               | Should                           |
| US22 |      Fórum      |       Usuário       |                                          Deletar o tópico criado por mim                                           |                          remover um tópico que me arrependo de ter criado                          | Must                             |
| US23 |      Fórum      |       Usuário       |                                           Upvote e downvote em um tópico                                           |                         julgar um tópico segundo meus padrões de qualidade                         | Should                           |
| US24 |      Fórum      |       Usuário       |                                           Criar comentário em um tópico                                            |                          responder ao questionamento levantado pelo mesmo                          | Must                             |
| US25 |      Fórum      |       Usuário       |                                       Editar comentário que fiz em um tópico                                       |                              modificar um erro que eu tenha cometido                               | Could                            |
| US26 |      Fórum      |       Usuário       |                                     Remover um comentário que fiz em um tópico                                     |                        remover um comentário que me arrependo de ter feito                         | Must                             |
| US27 |      Fórum      |       Usuário       |                                         Upvote e downvote em um comentário                                         |                       julgar um comentário segundo meus padrões de qualidade                       | Should                           |
| US28 | Card de Plantas |       Usuário       |                                       Visualizar informações sobre a planta                                        |                              aumentar meu conhecimento sobre a mesma                               | Must                             |
| US29 | Card de Plantas |       Usuário       |                                        Adicionar planta aos meus Favoritos                                         |                           adicionar um atalho para utilizá-lo mais tarde                           | Could                            |
| US30 |    Favoritos    |       Usuário       |                                  Remover uma planta da minha coleção de favoritos                                  |                                 remover um atalho que não uso mais                                 | Must                             |
| US31 |    Favoritos    |       Usuário       |                                       Visualizar minha coleção de favoritos                                        |                  facilitar o processo de navegação pelas páginas que mais visito                   | Must                             |
| US32 |      Feed       |       Usuário       |                                              Publicar fotos & textos                                               |                            compartilhar momentos da minha vida botânica                            | Must                             |
| US33 |      Feed       |       Usuário       |                                        Visualizar posts de minhas conexões                                         |                    me manter informado acerca das atividades de minhs conexões                     | Must                             |
| US34 |      Feed       |       Usuário       |                            Visualizar trending topics sobre minhas plantas favoritadas                             |                         me manter atualizado sobre minha planta favoritada                         | Could                            |
| US35 |      Feed       |       Usuário       |                               Curtir/descurtir posts que aparecem na minha timeline                                |                      julgar minha timeline segundo meus padrões de qualidade                       | Should                           |
| US36 |      Feed       |       Usuário       |                                  Salvar um post na minha coleção de Posts Salvos                                   |                          acessar meus posts favoritos com mais facilidade                          | Want                             |
| US37 |      Feed       |       Usuário       |                                       Comentar em um post na minha timeline                                        |                         compartilhar minha visão acerca do que foi postado                         | Should                           |
| US38 |      Feed       |       Usuário       |                                     Editar um comentário que fiz em algum post                                     |                         compartilhar minha visão acerca do que foi postado                         | Could                            |
| US39 |      Feed       |       Usuário       |                                    Remover um comentario que fiz em algum post                                     |                      remover um comentário meu que me arrependo de ter feito                       | Should                           |
| US40 |  Minha Planta   |       Usuário       |                                          Adicionar apelido à minha planta                                          |        que eu possa distinguir uma planta de outra (caso tenha multiplas da mesma especie)         | Must                             |
| US41 |  Minha Planta   |       Usuário       |                                        Definir configurações de notificação                                        |                             que eu me lembre de cultivar minha planta                              | Must                             |
| US42 |      Meta       |     Aplicativo      |                    que o usuário seja obrigado a definir uma meta na criação de uma comunidade                     |                                   que esta tenha algum propósito                                   | Must                             |
| US43 |      Meta       |     Aplicativo      |                 que o usuário seja obrigado a definir o local onde dever-se-a realizar a tal meta                  |                             que o escopo de intervenção seja limitado                              | Should                           |
| US44 |      Meta       |       Usuário       |              visualizar comunidades que possuam metas definidas em locais próximos ao que me localizo              |                         que eu possa me integrar a comunidades relevantes                          | Could                            |
| US45 |      Meta       |       Usuário       | ser informado, no ato de criação de uma comunidade, caso haja outras comunidades com metas orientadas àquele local | que eu possa ter uma decisão mais consciente acerca da necessidade de criar esta comunidade ou não | Want                             |
| US46 |      Meta       |       Usuário       |                                       definir informações relevantes a meta                                        |                                      que esta seja mensurável                                      | Should                           |
| US47 |   Marketplace   |       Usuário       |                               navegar produtos por categorias (vegetais, ervas, etc)                               |                                                                                                    | Should                           |
| US48 |   Marketplace   |       Usuário       |                                            pesquisar produtos por nome                                             |                                                                                                    | Must                             |
| US49 |   Marketplace   |       Usuário       |                                filtrar produtos por avaliação, preço, categoria etc                                |                                                                                                    | Should                           |
| US50 |   Marketplace   |       Usuário       |                             comprar produto pelo aplicativo (com cartão, por exemplo)                              |                                                                                                    | Want                             |
| US51 |   Marketplace   |      Comprador      |                                            avaliar minha ultima compra                                             |                                                                                                    | Must                             |
| US52 |   Marketplace   | Vendedor Individual |                                                  criar uma venda                                                   |                                                                                                    | Must                             |
| US53 |   Marketplace   | Vendedor Individual |                                                 remover uma venda                                                  |                                                                                                    | Must                             |

 <!-- criterios |
 - |
 [→](./acceptance_criteria.md#US09---Fazer-logout-no-aplicativo) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) |
 [→](./acceptance_criteria.md) | -->
