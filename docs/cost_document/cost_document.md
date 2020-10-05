# Gerenciamento de Plano de Custo

## Histórico de Versão
| Data | Versão | Descrição | Autor |
| :--- | :--- | :--- | :--- |
| 04/10/2020 | 1.0 | Criação do Documento e adição de tópicos 1 à 7 | Victor Samuel, Marcos Felipe e Guilherme Lira |

## Sumário

[1. Introdução](#1-introdução)

[2. Estimação de Custos](#2-estimação-de-custos)

[3. Recursos Humanos](#3-recursos-humanos)

[4. Custos Operacionais](#4-custos-operacionais)

[5. Custos das Ferramentas](#5-custos-das-ferramentas)

[6. Custo Final](#6-custo-final)

[7. Referências](#7-referências)

## **1. Introdução**
Segundo o Guia de conhecimento PMBOK, o processo de Gerenciamento de Custos envolve a definição e o destino dos recursos disponíveis, além de, explicitar os critérios do planejamento, estruturação e controle de gastos para a confecção do projeto. Logo, este documento tem como principal objetivo, apresentar uma visão geral sobre o desenvolvimento de gastos e garantir que o projeto seja concretizado dentro das margens orçamentais. 

## **2. Estimação de Custos**
O Guia de conhecimento PMBOK afirma que, o ato de estimar custos de um projeto é um processo baseado na elaboração de uma análise crítica. Essa análise visa identificar quais serão as necessidades dentro da estimação monetária, cujo a qual é necessária para executar as atividades do projeto.

Para fazer a análise de custo, o nosso projeto usará a estimativa de Program Evaluation and Review Technique também conhecida como PERT. Essa técnica tem o intuito de ajudar a diminuir os erros provocados pela estimativa relacionados ao levantamento dos custos.

Para fazer o cálculo de estimativa, o PERT usa três cenários, sendo eles: estimativa Otimista (O), Pessimista (P) e Mais Provável (M). Logo o PERT é calculada pela formula:

<p align="center">
  <img src="img/pert.jpeg" />
</p>

## **3. Recursos Humanos**
As estimativas de custos relacionadas a Recursos Humanos levarão em consideração a carga horária de 8 diárias e a média de 22 dias úteis para estimar um valor-hora de um profissional. Os valores relativos as médias saláriais foram retirados do site [GlassDoor](https://www.glassdoor.com.br/index.htm).

A média de horas trabalhada por cada integrante foi feita por meio da plataforma de gerenciamento [TopTracker](https://www.toptal.com/tracker) e pode ser acesssada nas pastas relativas a cada sprint. 

| Profissional | Quantidade de Profissionais | Salário Médio | Valor por Hora |
| :----------: | :----------: | :----------: | :----------: |
| Product Owner | 1 | R$ 9500,00| R$ 53,98
| Scrum Master	| 1 | R$ 7830,00 | R$ 44,49
| DevOps | 1 | R$ 6015,00 | R$ 34,18
| Desenvolvedor Júnior | 7 | R$ 2926,00 | R$ 16,62

Logo após o levantamento da média de horas junto ao grupo, se faz necessário realizar uma estimativa Pessimista, para tal, cada integrante trabalhou 15 horas por semana, na Mais Provável, 10 horas e, na Otimista 8 horas. É necessário ressaltar que essas médias podem váriar para cada integrante da equipe e para cada semana de trabalho, de acordo com a demanda e dificuldade da sprint. 

* Estimativa Pessimista 

| Profissional | Quantidade de Profissionais | Média de Horas Trabalhada | Preço da Hora | Custo Semanal |
| :----------: | :----------: | :----------: | :----------: | :----------: |
| Product Owner | 1 | 15h | R$ 53,98 | R$ 809,70 |
| Scrum Master	| 1 | 15h | R$ 44,49 | R$ 667,35 |
| DevOps | 1 | 15h | R$ 34,18 | R$ 512,70 |
| Desenvolvedor Júnior | 7 | 15h | R$ 16,62 | R$ 249,30 |
| **Total** | 10 | 150h | R$ 149,27| R$ 2239,05


* Estimativa Mais Provável 

| Profissional | Quantidade de Profissionais | Média de Horas Trabalhada | Preço da Hora | Custo Semanal |
| :----------: | :----------: | :----------: | :----------: | :----------: |
| Product Owner | 1 | 10h | R$ 53,98 | R$ 539,80 |
| Scrum Master	| 1 | 10h | R$ 44,49 | R$ 444,90 |
| DevOps | 1 | 10h | R$ 34,18 | R$ 341,8 |
| Desenvolvedor Júnior | 7 | 10h | R$ 16,62 | R$ 166,20 |
| **Total** | 10 | 100h | R$ 149,27| R$ 1492,70

* Estimativa Otimista

| Profissional | Quantidade de Profissionais | Média de Horas Trabalhada | Preço da Hora | Custo Semanal |
| :----------: | :----------: | :----------: | :----------: | :----------: |
| Product Owner | 1 | 8h | R$ 53,98 | R$ 431,84 |
| Scrum Master	| 1 | 8h | R$ 44,49 | R$ 355,92 |
| DevOps | 1 | 8h | R$ 34,18 | R$ 273,44 |
| Desenvolvedor Júnior | 7 | 8h | R$ 16,62 | R$ 132,96 |
| **Total** | 10 | 80h | R$ 149,27| R$ 1194,16


## **4. Custos Operacionais**
Devido a pandemia, os custos operacionais consistem em gastos com o ambiente de desenvolvimento, energia, internet, computadores e periféricos da equipe. 

Foi calculado que o valor médio dos computadores e dos periféricos da nossa equipe é de R$ 3287,5 e de R$ 277,64 respectivamente, e sabendo que nossa equipe é composta por 10 integrantes o valor total em equipamentos soma R$ 34263,32. Podemos calcular os custos operacionais somando o custo com internet ao custo padrão de alimentação das fontes de computadores/desktop, que em sua média consomem 250W e multiplicando pelas horas gastas semanalmente. 

Custo = Pot. x Dias x Horas x Tarifa 

Pot = 0,25kW = (250W / 1000) 

Custo = 0,250kW x 5 x 2.06x 0,4863109 (tarifa local) = R$1,25.

Para o cálculo final da internet será considerado um preço base de R$ 86,17, que foi calculado utilizando 24.7MBs como internet media contratada e um valor de R$ 3,50 por MB, onde possivelmente, suprirá todas as atividades do time. 

| Item | Quantidade | Valor por Semana |
| :----------: | :----------: | :----------: | 
| Notebook | 10 | R$ 2054, 68 |
| Periférico | Variável | R$ 87,77 |
| Energia | 10 | R$ 12,5 |
| Internet | 10 | R$ 53,85 |
| Total |  | R$ 2208,80 |

## **5. Custos das Ferramentas**
Como todas as ferramentas usadas contém plano gratuito, ou o e-mail da [UnB](https://www.unb.br/) disponibiliza algum recurso gratuito para uso, o custo de ferramentas será nulo. 

| Ferramenta | Objetivo | Preço |
| :----------: | :----------: | :----------: | 
| Discord | Responsável pela comunicação via áudio em tempo real da Equipe | R$ 0,00 |
| Telegram | Responsável pela comunicação instantânea da Equipe | R$ 0,00 |
| GitHub | Mecanismo de versionamento do produto | R$ 0,00 |
| Servidor | *Ainda será definido* | R$ 0,00 |
| TopTracker | Ferramenta para o Gerenciamento das horas trabalhadas pela equipe | R$ 0,00 |
| Scrum Poker | Responsável por estimar o esforço ou o tamanho relativo para um determinado desenvolvimento | R$ 0,00 |
| Insomnia | Ferramenta para teste de Rotas | R$ 0,00 |
| **Total** | | R$ 0,00 |

## **6. Custo Final**

O calculo realizado somente nos entrega uma estimativa do valor final do projeto, ele será atualizado durante as semanas com base na carga horária dos integrantes da equipe ou ajustado se ouver algum incidente. O calculo é realizado levando em consideração as 16 sprintes que seram utilizadas para desenvolvimento.

| Ferramenta | Custo (R$) |
| :---------- | :--------- |
| Custo de Pessoal | R$ 105084,00 |
| Custo Operacional | R$ 35346,80 |
| Custo de Ferramentas | R$ 0,00 |
| Total | R$ 140424,80 |

## **7. Referências**
1. DevMedia. PMBOK: Trabalhando com Gerenciamento de Custos. - Disponível em: [DevMedia PMBOK](https://www.devmedia.com.br/pmbok-trabalhando-com-gerenciamento-de-custos/31158). Acessado em 04/10/2020.

2. eSaude. ROGERS, Joberth. Disponível em: [eSaude Documento de Custo](https://github.com/fga-eps-mds/2020.1-eSaudeUnB-Wiki/blob/develop/docs/plano_gerenciamento_custo.md).Acessado em 04/10/2020 
