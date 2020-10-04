# Node.js Style Guide

## Histórico de Versão
| Data | Versão | Descrição | Autor |
| :--- | :--- | :--- | :--- |
| 03/10/2020 | 0.1 | Created Document and added topic 1  | Vinícius |
| 04/10/2020 | 1.0 | Added topics 2. through 6. | Vinícius |

<!-- This is a guide for writing consistent and aesthetically pleasing node.js code.
It is inspired by what is popular within the community, and flavored with some
personal opinions.

There is a .jshintrc which enforces these rules as closely as possible. You can
either use that and adjust it, or use
[this script](https://gist.github.com/kentcdodds/11293570) to make your own.

This guide was created by [Felix Geisendörfer](http://felixge.de/) and is
licensed under the [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/)
license. You are encouraged to fork this repository and make adjustments
according to your preferences.

![Creative Commons License](http://i.creativecommons.org/l/by-sa/3.0/88x31.png) -->

## Sumário

### 1. Formatação
* [1.1. 2 espaços para identação](#11-2-espaços-para-identação)
* [1.2. Sem espaço em branco a direita](#12-Sem-espaço-em-branco-a-direita)
* [1.3. Ponto e Virgula](#13-Ponto-e-Vírgula)
* [1.4. 80 caracteres por linha](#14-80-caracteres-por-linha)
* [1.5. Use aspas simples](#15-Use-aspas-simples)
* [1.6. Abertura de chaves](#16-Abertura-de-chaves)
* [1.7. Declare uma variavel por declaração de var](#17-Declare-uma-variavel-por-declaração-de-var)

### 2. Convenção de Nomenclaturas
* [2.1 lowerCamelCase para variáveis, propriedades e nome de funções](#21-lowerCamelCase-para-variáveis,-propriedades-e-nome-de-funções)
* [2.2 UpperCamelCase para nome de classes](#22-UpperCamelCase-para-nome-de-classes)

### 3. Variaves
* [3.1 Objeto / Criação de Array](#31-Objeto--Criação-de-Array)

### 4. Condicionais
* [4.1 Use o operador ===](#41-Use-o-operador===)
* [4.2 Use condições descritivas](#42-Use-condições-descritivas)

### 5. Funções
* [5.1 Escreva funções pequenas](#51-Escreva-funções-pequenas)
* [5.2 Retorno cedo de funções](#52-Retorno-cedo-de-funções)
* [5.3 Nomeie seus fechamentos](#53-Nomeie-seus-fechamentos)
* [5.4 Sem fechamentos aninhados](#54-Sem-fechamentos-aninhados)
* [5.5 Aninhamento de Métodos](#55-Aninhamento-de-Métodos)

### 6. Comentários

* [6.1 Use o 'barras duplas' para comentarios](#61-Use-o-'barras-duplas'-para-comentarios)

## 1. Formatação

<!-- You may want to use [editorconfig.org](http://editorconfig.org/) to enforce the formatting settings in your editor. Use the [Node.js Style Guide .editorconfig file](.editorconfig) to have indentation, newslines and whitespace behavior automatically set to the rules set up below. -->


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

<!-- ### Use UPPERCASE for Constants

Constants should be declared as regular variables or static class properties,
using all uppercase letters.

*Right:*

```js
var SECOND = 1 * 1000;

function File() {
}
File.FULL_PERMISSIONS = 0777;
```

*Wrong:*

```js
const SECOND = 1 * 1000;

function File() {
}
File.fullPermissions = 0777;
```

[const]: https://developer.mozilla.org/en/JavaScript/Reference/Statements/const -->

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

*Right:*

```js
var a = 0;
if (a !== '') {
  console.log('vencendo');
}

```

*Wrong:*

```js
var a = 0;
if (a == '') {
  console.log('perdendo');
}
```

[operadorcomparar]: https://developer.mozilla.org/en/JavaScript/Reference/Operators/Comparison_Operators

<!-- ### Use multi-line ternary operator

The ternary operator should not be used on a single line. Split it up into multiple lines instead.

*Right:*

```js
var foo = (a === b)
  ? 1
  : 2;
```

*Wrong:*

```js
var foo = (a === b) ? 1 : 2;
``` -->

### 4.2 Use condições descritivas
Qualquer condição não trivial deve ser designada a uma variavel e função descritivamente nomeada

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
Utilize fechamentos, mas não aninhe-os. Caso contrário o seu codigo era se tornar uma bagunça.

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