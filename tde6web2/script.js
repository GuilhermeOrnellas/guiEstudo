// 1

// document.getElementById("btn").addEventListener("click",function(){
//    var nome = document.getElementById("nome").value
//    var resposta = document.getElementById("resposta")
//    resposta.innerHTML=`Boas Vindas ${nome}`
// }) 

// 2

// function calcular() {
//    let valor1 = parseFloat(document.getElementById('valor1').value);
//    let valor2 = parseFloat(document.getElementById('valor2').value);

//    if (isNaN(valor1) || isNaN(valor2)) {
//        alert("Por favor, insira números válidos!");
//        return;
//    }

//    let soma = valor1 + valor2;
//    let produto = valor1 * valor2;
//    let quociente = valor1 / valor2;
//    let diferenca = valor1 - valor2;

//    document.getElementById('soma').innerHTML = "Soma: " + soma;
//    document.getElementById('produto').innerHTML = "Produto: " + produto;
//    document.getElementById('quociente').innerHTML = "Quociente: " + quociente;
//    document.getElementById('diferenca').innerHTML = "Diferença: " + diferenca;
// }

// 3

// function calcularMedia() {

//    let nota1 = parseFloat(document.getElementById('nota1').value);
//    let nota2 = parseFloat(document.getElementById('nota2').value);
//    let nota3 = parseFloat(document.getElementById('nota3').value);

//    if (isNaN(nota1) || isNaN(nota2) || isNaN(nota3)) {
//        alert("Por favor, insira notas válidas!");
//        return;
//    }

//    let media = (nota1 + nota2 + nota3) / 3;
//    document.getElementById('mediaResultado').innerHTML = "Média: " + media.toFixed(2);
// }
// document.getElementById('calcularBtn').addEventListener('click', calcularMedia);

// 4

// function calcularSubtracao() {
//    let var1 = parseFloat(document.getElementById('valor1').value);
//    let var2 = parseFloat(document.getElementById('valor2').value);

//    if (isNaN(var1) || isNaN(var2)) {
//        alert("Por favor, insira números válidos!");
//        return;
//    }

//    let var3 = var1 - var2;
//    document.getElementById('resultadoSubtracao').innerHTML = `Resultado da subtração é: ${var3}`;
// }
// document.getElementById('calcularBtn').addEventListener('click', calcularSubtracao);

// 5

// function gerarTabuada() {

//    let numero = parseInt(document.getElementById('numero').value);

//    let tabuadaResultado = document.getElementById('tabuadaResultado');
//    tabuadaResultado.innerHTML = '';

//    if (isNaN(numero)) {
//        tabuadaResultado.innerHTML = '<li>Por favor, insira um número válido.</li>';
//        return;
//    }
//    for (let i = 1; i <= 10; i++) {
//        let resultado = numero * i;
//        let item = document.createElement('li');
//        item.textContent = `${numero} x ${i} = ${resultado}`;
//        tabuadaResultado.appendChild(item);
//    }
// }
// document.getElementById('numero').addEventListener('input', gerarTabuada);

// 6

function calcularFatorial() {
   let numero = parseInt(document.getElementById('numero').value);

   if (isNaN(numero) || numero < 0) {
       document.getElementById('resultadoFatorial').innerHTML = 'Por favor, insira um número válido (>= 0).';
       return;
   }

   let fatorial = 1;
   for (let i = 1; i <= numero; i++) {
       fatorial *= i;
   }
   document.getElementById('resultadoFatorial').innerHTML = `O fatorial de ${numero} é: ${fatorial}`;
}
document.getElementById('calcularBtn').addEventListener('click', calcularFatorial);