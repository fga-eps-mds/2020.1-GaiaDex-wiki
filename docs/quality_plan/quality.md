# Plano de Qualidade do Projeto

## Histórico de Revisões

|    Data    |  Versão  |        Descrição       |          Autor(es)          |
|:----------:|:--------:|:----------------------:|:---------------------------:|
| 04/10/2020 |   0.1    | Criação do Documento |   [Rafael Makaha](http://github.com/rafaelmakaha), [Arthur Sena](http://github.com/)  |

## Introdução

Este documento apresentará o Plano de Qualidade do Projeto, englobando os métodos e métricas a serem adotadas pelo time para realizar medições de qualidade do produto, bem como a definição de qualidade para este projeto.

## Monitoramento da Qualidade

Em busca de garantir que os procedimentos de qualidade estão sendo realizados como ditos neste documento, sabe-se da necessidade do monitoramento dos mesmos, o que será abordado neste tópico. Dividindo-se em etapas, o monitoramento se dará por duas diferentes formas, uma delas sendo automatizada, onde o software do projeto será analisado por ferramentas, e a outra manual, onde a equipe de gerência ficará responsável por verificar periodicamente se o código e a documentação estão de acordo com os padrões previamente discutidos.

## Métricas a Monitorar

Para a análise das métricas foram estabelecidos alguns critérios a serem seguidos. Quanto mais próximo do bom melhor.

|                    Métrica                    | Bom          | Regular      | Crítico       |
| :-------------------------------------------: | ------------ | ------------ | ------------- |
|            Complexidade ciclomática           | 0 a 20       | 21 a 60      | acima de 60   |
|              Duplicação de código             | 0% a 1.5%    | 1.6% a 2.9%  | acima de 3%   |
| Quebras no padrão de código/Flake8/ESLint ES6 | 0 a 5        | 6 a 10       | acima de 11   |
|              Cobertura de código              | acima de 90% | acima de 80% | abaixo de 80% |

## Ferramentas Utilizadas para o Monitoramento das Métricas

### [Code Climate](https://codeclimate.com/)

O Code Climate é uma ferramenta de análise estática de qualidade do código, praticamente um revisador de código, se assegura de avisar os desenvolvedores de diversos tipos de problemas, como duplicações, code smells e más práticas em geral.

### [Jest](https://jestjs.io/)

Focado na linguagem JavaScript, o jest é um framework que busca simplificar ao máximo o desenvolvimento de testes, permitindo que sejam escritos através de uma API.

### [ES Lint](https://eslint.org/)

ESLint é uma ferramenta para identificar e reportar padrões encontrados no código com o objetivo de gerar um código mais consistente e evitar problemas.

## Referências

* PLANO DE GERENCIAMENTO DE QUALIDADE. Laços da Alegria. Disponível em: [Laços Da Alegria](https://github.com/fga-eps-mds/2018.1-Lacos-da-Alegria/blob/develop/docs/code_quality_plan.md). Acesso em: 04/10/2020.