# Documento de Arquitetura

## Histórico de Versão

| Data  | Versão | Descrição | Autor(es)                           |
| :-:   |  :-:   |    :-:    |    :-:                              |
| 12/09 |  0.1   |  Criação da estrutura do documento | João Vítor |
| 13/09 |  0.2   | Atualização do sumário |  João Vítor            |
| 13/09 |  0.3   |  | [Victor Hugo](http://github.com/V100K) e [Rafael Makaha](http://github.com/rafaelmakaha)

## Sumário

[1. Introdução](#1-introdução)

* [1.1 Finalidade](#11-finalidade)
* [1.2 Escopo](#12-escopo)
* [1.3 Referências](#13-referências)
* [1.4 Visão Geral](#14-visão-geral)


[2. Representação da Arquitetura](#2-representação-da-arquitetura)

* [2.1 Arquitetura Nodejs](#21-arquitetura-nodejs)
* [2.2 Arquitetura React Native](#22-arquitetura-react-native)

[3. Metas e Restrições de Arquitetura](#3-metas-e-restrições-de-arquitetura)

[4. Visão Lógica](#4-visão-lógica)

* [4.1 Diagrama de Classes](#41-diagrama-de-classes)
* [4.2 Diagrama de Pacotes](#42-diagrama-de-pacotes)

[5. Visão de Implementação](#5-visão-de-implementação)

[6. Qualidade](#6-qualidade)

## **1. Introdução**

### 1.1 Finalidade

Este documento tem por finalidade, demonstrar uma clara visão da arquitetura do projeto <nome_do_projeto>, a ser implementado, para todos os envolvidos no desenvolvimento; permitindo um entendimento em suas possíveis subdivisões, funções de componentes e reestruturações.

### 1.2 Escopo

Este documento descreve toda a arquitetura do projeto <nome_do_projeto>, explicando as soluções arquiteturais estabelecidas para o projeto. Com isso, possibilita-se a compreensão e o entendimento da base do projeto.

### 1.3 Referências

MODELO EM TRÊS CAMADAS. Disponível em [Wikipedia](https://pt.wikipedia.org/wiki/Modelo_em_tr%C3%AAs_camadas).Acesso em 13 de Setembro de 2020.

MERN STACK. Disponível em [MongoDB](https://www.mongodb.com/mern-stack). Acesso em 13 de Setembro de 2020.

### 1.4 Visão Geral

O documento fornece detalhadamente, a nível de compreensão, a arquitetura do projeto. Escolhas de padrões arquiteturais, linguagens, frameworks foram tomadas com base num senso de opinião do grupo a fim de facilitar o trabalho e desenvolvimento com tais tecnologias: Nodejs e React Native.

## **2. Representação da Arquitetura**

O desenho arquitetural do projeto <nome_do_projeto> se faz pelo uso do modelo em três camadas, utilizando-se a _MERN Stack_ - MongoDB, Express, React e NodeJS.

O modelo em três camandas promove o desacoplamento das partes do projeto nas seguies camadas: camada de apresentação - onde há a interação com o usuário -; camada de negócio - onde há as funções e regras de todo o negócio, não havendo uma interface para o usuário -; e a camada de dados - responsável por armazenar as informações e dados a serem manipulados.

A _MERN Stack_ é a solução completa em _Javascript_ para o desenvolvimento de aplicações no modelo de três camadas, proporcionando ferramentas para desenvolvimento e evolução de todas as três camadas.

### 2.1 Arquitetura Nodejs

**Node.js** é um ambiente de desenvolvimento (framework) JavaScript de código aberto, multiplataforma, que executa o código JavaScript fora de um navegador web. Ele permite aos desenvolvedores usarem da linguagem para escrever scripts e automação com servidores, para produzir conteúdo dinâmico de páginas web antes da mesma ser enviada para o navegador do usuário.

O framework permite o uso da arquitetura MC proveniente da arquitetura MVC, deixando de fora a parte que lida com a interface do usuário, a qual será função de outra tecnologia: ReactNative.

Também conta com um outro framework para seus aplicativos web, o **Express**, que fornece um conjunto de recursos e ferramentas mais robustas, minimalista e flexível.



### 2.2 Arquitetura React Native



## **3. Metas e Restrições de Arquitetura**



## **4. Visão Lógica**

### 4.1 Diagrama de Classes

### 4.2 Diagrama de Pacotes

## **5. Visão de Implementação**

## **6. Qualidade**
