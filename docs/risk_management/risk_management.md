# Plano de Gerenciamento de Riscos

## Histórico de versão

|   Data    | Versão | Descrição            | Autor(es)  |
|   :-:     |  :-:   |  :-:                 |  :-:       |
| 12/09/2020|  0.1   | Criação da estrutura do Documento | [Rafael Makaha](http://github.com/rafaelmakaha) |
| 12/09/2020|  0.2   | Criação do sumário | [Rafael Makaha](http://github.com/rafaelmakaha) |
| 13/09/2020| 1.0| Finalização do documento| [João Vítor](https://github.com/joaovitorml) e [Rafael Makaha](http://github.com/rafaelmakaha)| |

## Sumário

[1. Introdução](#1-introdução)

[2. Identificação](#2-identificação)

[3. Prevenção e Conteção](#3-prevenção-e-contenção)

## 1. Introdução

O Plano de Gerenciamento de Riscos visa realizar uma listagem dos possíveis riscos durante todas as fases do ciclo de vida do software, bem como as alternativas para contornar cada um destes riscos. Contornando estas situações adversas, pode-se manter o ritmo de trabalho da equipe de desenvolvimento.

O andamento contínuo dos riscos se encontra na documentação de cada _Sprint_, apresentando uma tabela e um gráfico indicativos da probabilidade dos riscos ocorrerem naquela _Sprint_.

## 2. Identificação 

| # | Descrição | Probabilidade do Risco |Tamanho da Perda (dias)|Exposição ao Risco|
| :--- | :------------- | :------------- | :------------- | :------------- |
| R01 | Membro faltar reunião  | -  | 1  | - |
| R02 | Features má pontuadas  | -  | 5 | - |
| R03 | Baixa produtividade da equipe  | -  | 7  | - |
| R04 | Mais pontos planejados do que o time é capaz de entregar  | -  | 5 | -  |
| R05 | Dificuldades com a tecnologia de desenvolvimento  | -  | 3  | - |
| R06 | Erros na implementação de Features  | -  | 7  |  - |
| R07 | Issues mal documentadas   |-  | 7  | -  |
| R08 | Quebra ou  furto de equipamentos da equipe   |-  | 7 | - |
| R09 | Desistência de algum membro       |- | 7 | - |
| R10 | Problemas na configuração do ambiente de desenvolvimento  | -  |  2 | - |
| R11 | Indisponibilidade dos membros de MDS  | - | 3 | - |
| R12 | Indisponibilidade dos membros de EPS  | - | 3 | - |
| R13 | Falta de comunicação | - | 3 | - |
|   |   |   | Exposição:  | -  |

## 3. Prevenção e Contenção

| # | Preveção | Contenção |
| :--- | :------------- | :------------- | 
| R01 | Notificar membros no dia de reunião e reforçar a importância da reunião | Repassar o que foi discutido para membros indisponíveis no horário da reunião  |
| R02 | Votação de pontos incluindo a equipe completa | Repontuar Issues |
| R03 | É responsabilidade de cada membro motivar e cooperar com o restante da equipe |  Acompanhamento por parte de EPS na resolução das issues de MDS |
| R04 | Realizar pontuação baseada no _Velocity_ da equipe | Deixar pontos como dívida técnica |
| R05 | Realizar treinamentos para a tecnologia em específico | Alterar a tecnologia |
| R06 | Realizar critérios de aceitação detalhadamente | Refatorar a feature realizada | 
| R07 | Documentar a Issue baseada nos critérios de aceitação da feature | Refatorar a documentação da feature em que a Issue está baseada | 
| R08 | Manter os equipamentos atualizados e seguros | Buscar equipamento emprestado ou auxílio de outros membros da equipe |
| R09 | Manter envolvimento e motivação dos membros no projeto | Repartir carga do membro desistente entre os membros restantes |
| R10 | Dockerização de ambiente | Configuração individualmente do ambiente com o membro |
| R11 | Planejar menos pontos para membros indisponíveis | Conversar com cada dupla para decidir horários de pareamento |
| R12 | Planejar menos pontos para membros indisponíveis | Conversar com cada dupla para decidir horários de pareamento |
| R13 | Realizar dailies e reuniões de review e planejamento | Reuniões extras para melhorar a comunicação entre os membros |