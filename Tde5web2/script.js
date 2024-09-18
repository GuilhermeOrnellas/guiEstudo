// 1
/*
var animais = ['cachorro','gato','pássaro']
animais.push('leão')

console.log(`${animais}`)

*/

// 2
/*
var fruta = ['maçã', 'banana', 'laranja']
var frutaRemovida = fruta.pop()

document.write(`A fruta removida foi a ${frutaRemovida}`)
document.write(`<br>Ficaram as frutas: ${fruta}`)
*/

// 3
/*
var cores =['vermelho','azul','verde']

cores.shift()
cores.unshift('roxo')
document.write(`${cores}`)
*/

// 4
/*
var frutas = ['maçã', 'banana']  
var vegetais = ['cenoura', 'batata']

var alimentos = frutas.concat(vegetais)

console.log(`${alimentos}`)
*/

// 5
/*
var numeros = [1,2,3,4,5,6]
 var final = numeros.slice(2,5)  //duvida aqui

document.write(`${final}`)
*/

// 6
/*
var linguagens = ['JavaScript', 'Python', 'C++','Java']

linguagens.splice(1,2,'ruby','Go')

document.write(`${linguagens}`)
*/

// 7
/*
var numeros = [1,2,3,4,5]

var dobro = numeros.map(function(numero){
    return numero *2
})

console.log(`${dobro}`)
*/

// 8
/*
var idades = [10, 15, 20, 25, 30]

var idadeGrande = idades.filter(function(idades){
    return idades>=18
})

document.write(`${idadeGrande}`)
*/

// 9
/*
var precos = [10, 20, 30, 40];

var precosAumento = precos.map(function(precos) {
    return precos * 1.1;
});

console.log(precosAumento);
*/

// 10

var numeros = [5, 12, 8, 130, 44]

var numeroMaior = numeros.filter(function(numeros){
    return numeros>10
})

 document.write(`${numeroMaior[0]}`) // o [0] serve para mostrar o primerio da ordem 