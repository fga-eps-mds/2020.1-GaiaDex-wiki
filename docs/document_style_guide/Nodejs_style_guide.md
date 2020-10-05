# Guia de estilo

## Histórico de Versão
| Data | Versão | Descrição | Autor |
| :--- | :--- | :--- | :--- |
| 03/10/2020 | 0.1 | Created Document and added topic 1  | Vinícius |
| 04/10/2020 | 1.0 | Added topics 2. through 6 | Vinícius |
| 05/10/2020 | 1.1 | Added references, note and updated document | Vinícius |
|  |  |  |  |

> **Nota**: Este Guia contém algumas das normas de programação que acreditamos que devem ser levadas em
consideração para a escrita de um código adequado. A criação deste Guia foi realizada usando como base
[este repositorio](https://github.com/felixge/node-style-guide), criado por [Felix Geisendörfer](http://felixge.de/)
e está licenciado sob [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/). Também vale salientar que outro material que consideramos de extrema importância é o [guia de estilos javascript Airbnb](https://github.com/armoucar/javascript-style-guide). Este último se tornou um material de referência frequente
para nós pois ao contrário do guia utilizado como base. O guia disponibilizado no repositório Airbnb tem recebido suporte contínuo, inclusive durante o ano de criação deste documento. Por esse motivo incentivamos a todos que façam uso de ambos os materiais citados como referências.

## Sumário

[1. Formatação](#1-Formatação)
* [1.1. 2 espaços para identação](#11-2-espaços-para-identação)
* [1.2. Sem espaço em branco a direita](#12-Sem-espaço-em-branco-a-direita)
* [1.3. Ponto e Virgula](#13-Ponto-e-Vírgula)
* [1.4. 80 caracteres por linha](#14-80-caracteres-por-linha)
* [1.5. Use aspas simples](#15-Use-aspas-simples)
* [1.6. Abertura de chaves](#16-Abertura-de-chaves)
* [1.7. Declare uma variavel por declaração de var](#17-Declare-uma-variavel-por-declaração-de-var)

[2. Convenção de Nomenclaturas](#2-Convenção-de-Nomenclaturas)
* [2.1 lowerCamelCase para variáveis, propriedades e nome de funções](#21-lowerCamelCase-para-variáveis,-propriedades-e-nome-de-funções)
* [2.2 UpperCamelCase para nome de classes](#22-UpperCamelCase-para-nome-de-classes)
* [2.3. MAIÚSCULO para constantes](#23-MAIÚSCULO-para-constantes)

[3. Variáves](#3-Variáveis)
* [3.1 Objeto / Criação de Array](#31-Objeto--Criação-de-Array)

[4. Condicionais](#4-Condicionais)
* [4.1 Use o operador ===](#41-Use-o-operador===)
* [4.2 Use condições descritivas](#42-Use-condições-descritivas)
* [4.3. Uso do operado ternario de multiplas linhas](#43-Uso-do-operado-ternario-de-multiplas-linhas)

[5. Funções](#5-Funções)
* [5.1 Escreva funções pequenas](#51-Escreva-funções-pequenas)
* [5.2 Retorno cedo de funções](#52-Retorno-cedo-de-funções)
* [5.3 Nomeie seus fechamentos](#53-Nomeie-seus-fechamentos)
* [5.4 Sem fechamentos aninhados](#54-Sem-fechamentos-aninhados)
* [5.5 Aninhamento de Métodos](#55-Aninhamento-de-Métodos)
* [5.6 Evite o Callback Hell ou Inferno de Callback.](#56-Evite-o-Callback-Hell-ou-Inferno-de-Callback.)
  * [5.6.1. Mantenha seu código raso.](#561-Mantenha-seu-código-raso.)
  * [5.6.2. Modularize.](#562-Modularize.)
  * [5.6.3 Trate cada um dos erros os erros.](#563-Trate-cada-um-dos-erros-os-erros.)

[6. Comentários](#6-Comentários)
* [6.1 Use o 'barras duplas' para comentarios](#61-Use-o-'barras-duplas'-para-comentarios)

[7. Referências.](#7-Referências.)

## 1. Formatação

### 1.1. 2 espaços para identação
Utilize 2 espaços para a identação do seu código e jure nunca confundir a tabulação e espaços -  Caso contrario você ira sofrer as consequencias.

### 1.2 Sem espaço em branco a direita
Antes de realizar o commit sempre lembre de limpar os espaços em branco a direira dos arquivos .js

### 1.3 Ponto e Vírgula
De acordo com [pesquisas][ponto_virgula], o uso de ponto e virgula é um valor importante em nossa comunidade. Considere os pontos da [oposição][], mas seja tradicionalista quando se trata de abusar dos mecanismos de correção de erros para praseres sintáticos leves

[oposição]: http://blog.izs.me/post/2353458699/an-open-letter-to-javascript-leaders-regarding
[ponto_virgula]: http://news.ycombinator.com/item?id=1547647


### 1.4 80 caracteres por linha
Limite sua linha em 80 caracteres. Use o espaço adicional para split screen. Se seu editor for capaz de fazer isso, é claro.

### 1.5 Use aspas simples
Faça uso das aspas simples, a menos que esteja escrevendo JSON.

*Certo:*
```js
  var foo = 'bar'; 
```

*Errado:*
```js
  var foo = "bar";
```

### 1.6 Abertura de chaves
A abertura de chaves ocorre na mesma linha que a declaração.

*Certo:*
```js
if (true) {
  console.log('Hello World');
}
```

*Errado:*
```js
if (true) 
{
  console.log('Hello World');
}
```
Note também, o uso do espaço em branco antes e depois da declaração

### 1.7 Declare uma variavel por declaração de var
Declare somente uma variavel por declaração de var, isso facilita a reorganização das linhas. No entanto, ignore [Crockford][crockfordconvention] quando se trata de variáveis mais internas da função, apenas coloque as declarações onde fizer sentido.

*Certo:*

```js
var keys   = ['foo', 'bar'];
var values = [23, 42];

var object = {};
while (keys.length) {
  var key = keys.pop();
  object[key] = values.pop();
}
```

*Errado:*

```js
var keys = ['foo', 'bar'],
    values = [23, 42],
    object = {},
    key;

while (keys.length) {
  key = keys.pop();
  object[key] = values.pop();
}
```

[crockfordconvention]: http://javascript.crockford.com/code.html 

## 2. Convenção de Nomenclaturas

### 2.1 lowerCamelCase para variáveis, propriedades e nome de funções
Variáveis, propriedades e nomenclatura de funções usam 'lowerCamelCase'. Elas também devem ser descritivas. Variáveis de caracteres únicos e abreviações incomuns devem ser geralmente evitadas.

*Certo:*

```js
var adminUser = db.query('SELECT * FROM users ...');
```
*Errado:*

```js
var admin_user = db.query('SELECT * FROM users ...');
```
### 2.2 UpperCamelCase para nome de classes
Nome de classes devem ser capitalizadas usando o formato 'UpperCamelCase'.

*Certo:*

```js
function ContaBancaria() {
}
```

*Errado:*

```js
function conta_Bancaria() {
}
```

### 2.3. MAIÚSCULO para constantes
Constantes deveriam ser declaradas como varáveis regulares ou propriedades de classes estáticas, usando todas as letras maiúsculas.

*Certo:*

```js
var SECOND = 1 * 1000;

function File() {
}
File.FULL_PERMISSIONS = 0777;
```

*Errado:*

```js
const SECOND = 1 * 1000;

function File() {
}
File.fullPermissions = 0777;
```

[const]: https://developer.mozilla.org/en/JavaScript/Reference/Statements/const

## 3. Variáveis

### 3.1 Objeto / Criação de Array
Coloque declarações *curtas* em uma única linha. Apenas cite chaves quando seu interprete reclamar:

*Certo:*

```js
var a = ['hello', 'world'];
var b = {
  good: 'code',
  'is generally': 'pretty',
};
```

*Errado:*

```js
var a = [
  'hello', 'world'
];
var b = {good: 'code'
        ,' is generally': 'pretty'
        };
``` 

## 4. Condicionais
### 4.1 Use o operador ===
Quando se trata de programação não se preocupe com [regras bobas][operadorcomparar]. Use o operador de tripla igualdade que ele irá funcionar como o esperado.

*Certo:*

```js
var a = 0;
if (a !== '') {
  console.log('vencendo');
}

```

*Errado:*

```js
var a = 0;
if (a == '') {
  console.log('perdendo');
}
```

[operadorcomparar]: https://developer.mozilla.org/en/JavaScript/Reference/Operators/Comparison_Operators

### 4.2 Use condições descritivas
Qualquer condição não trivial deve ser designada a uma variavel e função descritivamente nomeada.

*Certo:*

```js
var isValidPassword = password.length >= 4 && /^(?=.*\d).{4,}$/.test(password);

if (isValidPassword) {
  console.log('vencendo');
}
```

*Errado:*

```js
if (password.length >= 4 && /^(?=.*\d).{4,}$/.test(password)) {
  console.log('perdendo');
}
```
### 4.3. Uso do operado ternario de multiplas linhas
O operador não deve ser utilizado em uma única linha. Divida-o em múltiplas linhas.

*Certo:*

```js
var foo = (a === b)
  ? 1
  : 2;
```

*Errado:*

```js
var foo = (a === b) ? 1 : 2;
``` 

## 5. Funções

### 5.1 Escreva funções pequenas
Mantenha suas funções curtas. Uma boa função é visível por pessoas da última fileira de uma sala grande. Então não conte para que elas tenham uma visão de perfeita. Tente se limitar a 15 linhas.

### 5.2 Retorno cedo de funções
Para evitar aninhamento de condicionais IF, sempre retorne o valor de uma função o quanto antes.

*Certo:*

```js
function isPercentage(val) {
  if (val < 0) {
    return false;
  }

  if (val > 100) {
    return false;
  }

  return true;
}
```

*Errado:*

```js
function isPercentage(val) {
  if (val >= 0) {
    if (val < 100) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}
```

Ou, nesse exemplo em particular é possível encurtar mais ainda:

```js
function isPercentage(val) {
  var isInRange = (val >= 0 && val <= 100);
  return isInRange;
}
```

### 5.3 Nomeie seus fechamentos
Sinta-se a vontade para dar nome aos fechamentos. Isso mostra que você se importa com eles e irá produzir melhores rastreamentos de pilha, heap e perfís de cpu.

*Certo:*

```js
req.on('end', function onEnd() {
  console.log('winning');
});
```

*Errado:*

```js
req.on('end', function() {
  console.log('losing');
});
``` 

### 5.4 Sem fechamentos aninhados
Utilize fechamentos, mas não aninhe-os. Caso contrário o seu codigo irá se tornar uma bagunça.

*Certo:*

```js
setTimeout(function() {
  client.connect(afterConnect);
}, 1000);

function afterConnect() {
  console.log('winning');
}
```

*Errado:*

```js
setTimeout(function() {
  client.connect(function() {
    console.log('losing');
  });
}, 1000);
```

### 5.5 Aninhamento de Métodos
Um método por linha deve ser usado se você quer aninhar metodos.
Você também deve identar esses metodos para tornar fácil a identificação daqueles que fazem parte da mesma cadeia.

*Certo:*

```js
User
  .findOne({ name: 'foo' })
  .populate('bar')
  .exec(function(err, user) {
    return true;
  });
```

*Errado:*

```js
User
.findOne({ name: 'foo' })
.populate('bar')
.exec(function(err, user) {
  return true;
});

User.findOne({ name: 'foo' })
  .populate('bar')
  .exec(function(err, user) {
    return true;
  });

User.findOne({ name: 'foo' }).populate('bar')
.exec(function(err, user) {
  return true;
});

User.findOne({ name: 'foo' }).populate('bar')
  .exec(function(err, user) {
    return true;
  });
```

### 5.6 Evite o Callback Hell ou Inferno de Callback.
Ao utilizar funções de callbacks tenha muito cuidado como você as implementa pois seu código pode se tornar algo grotesco e gigante. Aqui vai algumas dicas para se evitar isso: 

#### 5.6.1. Mantenha seu código raso.
Nomear funções torna seu código mais legível. Quando ocorrer excessôes você obterá rastreadores de pilhas referenciando aos nomes das funções, e além disso, você mesmo poderá mover e referenciá-las muito mais facilmente.

#### 5.6.2. Modularize.
Siga as palavras de [Isaac Schlueter][]: "*Escreva pequenos modulos que fazem cada um uma coisa, e então junte-os em outros modulos que fazem algo maior. Você não vai entrar num Callbak Hell se você não ir para um*"

#### 5.6.3 Trate cada um dos erros os erros.
Erros acontecem, e você nunca sabe quando podem acontecer por isso esteja sempre preparado.
Para isso deixe o primeiro argumento da função reservado para o erro. Dessa forma você se lembra de tratá-lo mais tarde.

Exemplo:
```js
var fs = require('fs')

 fs.readFile('/Does/not/exist', handleFile)

 function handleFile (error, file) {
   if (error) return console.error('Uhoh, there was an error', error)
   // Ao contrário continue e use o 'file' no seu codigo.
 }
```

[Isaac Schlueter]: http://twitter.com/izs

## 6. Comentários

### 6.1 Use o 'barras duplas' para comentarios
Utilize ambos para comentários de uma linha ou múltiplas. Tente escrever comentários que explicam mecanismos de alto nível ou deixam claros a dificuldade de elementos do código.

Não use comentários em coisas triviais.

*Certo:*

```js
// 'ID_SOMETHING=VALUE' -> ['ID_SOMETHING=VALUE', 'SOMETHING', 'VALUE']
var matches = item.match(/ID_([^\n]+)=([^\n]+)/));

// Esta Função tem um efeito colateral esquisito onde a falha em incrementar  um
//contador redis utilizado para estatísticas ira causar uma exceção. Isto precisa
// ser concertado em uma iteração futura.
function loadUser(id, cb) {
  // ...
}

var isSessionValid = (session.expires < Date.now());
if (isSessionValid) {
  // ...
}
```

*Errado:*

```js
// Execute a regex
var matches = item.match(/ID_([^\n]+)=([^\n]+)/);

// Usage: loadUser(5, function() { ... })
function loadUser(id, cb) {
  // ...
}

// Verifica se a sessão é válida
var isSessionValid = (session.expires < Date.now());
// Se a sessão não for válida
if (isSessionValid) {
  // ...
}
```

## 7. Referências.

### 1.Airbnb. Javascript Style Guide - Disponível em: https://github.com/armoucar/javascript-style-guide. Acessado: 05/10/2020.

### 2. Hacker News. Poll: Semicolons in Javascript - Disponível em: https://news.ycombinator.com/item?id=1547647. Acessado: 03/10/2020.

### 3. SCHLUETER, Isaac. An Open Letter to JavaScript Leaders Regarding Semicolons. - Disponível em: https://blog.izs.me/2010/12/an-open-letter-to-javascript-leaders-regarding. Acessado: 03/10/2020

### 4. CROCKFORD, Douglas: Code Conventions for the JavaScript Programming Language - Disponível em:  http://javascript.crockford.com/code.html.  Acessado em 04/10/2020.

### 5. MDN Web Docs. Expression and Operators. - Disponível em: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators. Acessado em 04/10/2020.
