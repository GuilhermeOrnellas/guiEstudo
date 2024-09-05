// 1 
// var a = 1
// while (a<=10){
//   document.write(`${a}`)
//a++
// }
// 2 
//var n = Number(prompt('digite um numero '))
// var a=1
// while(a<=n){
//   a++
//   var res=a+n
//   document.write(`o resultaddo é ${res}`)
// }
//3
// var a=20
// do{
//   document.write(`<br>${a}`)
//   a--
// }while(a >= 10)
//   document.write(`lançamento`)
//4
// var opção 
// do{
//   console.log ('menu de operações : 1loop-2responde e sai-3sair')
//   //opção= +(prompt('escolha uma opçao')) 
//     switch(opção){
//       case 1 :
//        //opção= +(prompt('escolha uma opçao'))
//         break
//           case 2:
//         document.write('saindo')
//         break
//       case 3 :
//         break
//     
//     }
//   }
// 5
// c = Math.floor(Math.random()* 11)
// var acerto = false
// var senhaacertada = 0
// do{
//   // j= + (prompt(`qual sua senha`))
//   if(j == c){
//     acerto = true
//   }
// }while (acerto == false)
// document.write(`palpites ${senhaacertada}`)
// document.write(`senha foi ${c}`)
//exercicio 6
// var nome = +(prompt('digite um nome )
// function saudacao(nome){
//   document.write(`oi!${nome}`)
// }
// 7 

// function potencia(base, expoente) {
//     var resultado = 1;
//     var contador = 0;

//     while (contador < expoente) {
//         resultado *= base;
//         contador++;
//     }

//     return resultado;
// }

// var base = +(prompt("Digite a base para a potência:"));
// var expoente = +(prompt("Digite o expoente para a potência:"));
// var resultadoPotencia = potencia(base, expoente);
// document.write("Resultado da potência: " + resultadoPotencia + "<br>");

// 8

// function ehPalindromo(texto) {
//     var textoInvertido = "";
//     var tamanho = texto.length;

//     for (var i = tamanho - 1; i >= 0; i--) {
//         textoInvertido += texto[i];
//     }

//     return texto === textoInvertido;
// }

// var texto = prompt("Digite uma palavra para verificar se é palíndromo:");
// var resultadoPalindromo = ehPalindromo(texto);
// document.write("É palíndromo a palavra '" + texto + "'? " + resultadoPalindromo + "<br>");

// 9

function calculadora(num1, num2, operacao) {
    switch (operacao) {
        case 'soma':
            return num1 + num2;
        case 'subtracao':
            return num1 - num2;
        case 'multiplicacao':
            return num1 * num2;
        case 'divisao':
            if (num2 !== 0) {
                return num1 / num2;
            } else {
                return "Erro: Divisão por zero";
            }
        default:
            return "Operação inválida";
    }
}

var num1 = +(prompt("Digite o primeiro número:"));
var operacao = prompt("Digite a operação (soma, subtracao, multiplicacao, divisao):");
var num2 = +(prompt("Digite o segundo número:"));

var resultadoCalculadora = calculadora(num1, num2, operacao);

document.write("Resultado da operação: " + resultadoCalculadora + "<br>");
