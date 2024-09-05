//1

/*
var num = +prompt("Digite um valor")
var operador = prompt("Digite um operador (+,-,*,/)")
var num1 = +prompt("Digite outro valor")

switch (operador) {
  case "+":
    resultado = num + num1
    document.write(`resultado ${resultado}`)
    break
  case "-"
    resultado = num - num1
    document.write(`resultado ${resultado}`)
    break
  case "*":
    resultado = num * num1
    document.write(`resultado é ${resultado}`)
    break;
  case "/":
    resultado = num / num1
    document.write(`resultado ${resultado}`)
  default:
    document.write("Opções invalidas")
}*/

//2
/*
var valor = +(prompt("Digite o valor da compra"));
var desconto = prompt("(1)funcionário (2)vip ou (3)")

switch (desconto) {
  case "1":
    des = valor * 0.1
    valorFinal = valor - des
    document.write(`O valor final é ${valorFinal}`)
    break
  case "2":
    des = valor * 0.05
    valorFinal = valor - des
    document.write(`O valor final é ${valorFinal}`)
    break;
  case "3":
    document.write(`O valor final é ${valor}`)
    break;

  default:
    document.write("Opções invalidas")
}*/

//3


/*
var valor = +prompt("Digite o valor da compra");
var forma = prompt("Digite a forma de pagamento 1 (À vista) 2 (À prazo)");

switch (forma) {
  case "1":
    des = valor * 0.1
    valorFinal = valor - des
    document.write(`O desconto é de ${des} e o valor final é ${valorFinal}`)
    break;

  case "2":
    document.write(`O valor final é ${valor}`)
    break
  default:
    document.write("Opções invalidas")
}*/

//4

/*
var conceito = prompt("Digite o seu conceito na matéria Desenvolvimento Web2 (A,B,C,D,E,F)")
conceito = conceito.toLowerCase();

 switch(conceito){

  case 'a':
     document.write(`Excelente`)
    break
  case 'b':
     document.write(`Ótimo`)
    break
  case 'c':
     document.write(`Bom`)
    break
  case 'd':
      document.write(`Regular`)
    break
  case 'e':
     document.write(`Ruim`)
    break
  case 'f':
     document.write(`Nos vemos de novo ano que vem`)
    break
  default:
    document.write(`Erro`)
 }*/


// 5 
/*
var letra = prompt("Digite uma letra")

tem como simplificar com if massssss
switch(letra){
  case 'a':
  case 'e':
  case 'i':
  case 'o':
  case 'u':
    document.write(`Vogal`)
  break
  case 'b':
  case 'c':
  case 'd':
  case 'f':
  case 'g':
  case 'h':
  case 'j':
  case 'k':
  case 'l':
  case 'm':
  case 'n':
  case 'p':
  case 'q':
  case 'r':
  case 's':
  case 't':
  case 'v':
  case 'w':
  case 'x':
  case 'y':
  case 'z':
    document.write(`Consoante`)
      break
  default:
    document.write("Erro")
}
*/


// 6


// for (i = 1; i <= 9; i++) {
//   document.write(`<br>${i}`)
//   if (i % 2 == 0) {
//    console.log(`<br>${i}`);
//   }
//  }

// 7


// for (nota = -1; nota > 10 || nota < 0; ) {
 
//   var nota= +(prompt("Digite uma nota"))

//   if (nota <= 10 && nota >= 0){
    
//     document.write(`A nota digitada foi ${nota}`)
//   }
//   else {
//     alert (`Nota inválida`)
//  }
// }

// 8 dsadasd

// for (var i = 0; i<2; i++) {
//     var usuario= prompt("Digite o usuário")
//     var senha= prompt("Digite a senha")
  
//     if (usuario !== senha){
//       document.write(`concluido`)
//     break
//     }
//     else {
//       i--
//       alert (`erro`)
//    }
  
// }

// 9
//  var numeros = [15, 8, 22, 3, 11]
//   var menor = numeros[0]
//   var maior = numeros[0]
//   var soma = 0


// for (var i = 0; i < numeros.length; i++) {
//     soma += numeros[i]
    
//     if (numeros[i] < menor) {
//         menor = numeros[i]
//     }

//     if (numeros[i] > maior) {
//         maior = numeros[i]
//     }
// }

// document.write("<br>Menor valor:", menor);
// document.write("<br>Maior valor:", maior);
// document.write("<br>Soma dos valores:", soma);


// 10

// var quantidadeTurmas = parseInt(prompt("Informe a quantidade de turmas:"))
// var somaAlunos = 0


// for (var i = 1; i <= quantidadeTurmas; i++) {
//     var alunosNaTurma

//     do {
//         alunosNaTurma = parseInt(prompt("Informe a quantidade de alunos na turma " + i + " (máximo 40):"))
//         if (alunosNaTurma > 40) {
//             alert("O número máximo de alunos por turma é 40. Tente novamente.")
//         }
//     } while (alunosNaTurma > 40)

//     somaAlunos += alunosNaTurma
// }
// var mediaAlunosPorTurma = somaAlunos / quantidadeTurmas
// document.write(`A média de alunos por turma é: ${mediaAlunosPorTurma}`)

// 11
 
//  var num = +(prompt("Digite um numero"))
//  var por = +(prompt("Digite um numero de porcentagem"))

//   res = num * (por/100)
  
//   document.write(`${por}% de ${num} é ${res}`)

// 12

// var c = +(prompt("Quantos graus celsius está:"))

// f= (c*9/5) + 32

// document.write(`A temperatura em Fahrenheit é ${f}`)

// 13

// function fibonacci(n) {
//   if (n<= 1) {
//       return n
//   } else {
//       return fibonacci (n - 1) + fibonacci (n-2)
//   }
// }
//   function sequenciaFibonacci(n) {
//   let list = []
//   for (let i = 0; i <n; i++) {
//     list. push(fibonacci(i))
//   }
//   return list
//   }
//   document. write(sequenciaFibonacci(20))

// 14

// var numQ = +(prompt("Digite um numero para a raiz quadrada"))

// res = Math.sqrt(numQ)

// document.write(`${Math.round(res)}`)

// 15


  var num = +(prompt("Digite um número"))
  var num1 = +(prompt("Digite outro número"))

  if (num >= num1) {
    document.write(`O numero 1 é maior ou igual ao numero 2`)
    
  } else {
    document.write(`O numero 1 é menor do que o numero 2`)
  }


