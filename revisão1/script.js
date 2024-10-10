// 1
// var altura = 1.70
// var peso = 70
// var imc = 0

// imc = peso/(altura*altura)

// document.write(`O IMC medio é de ${imc}`)

// 2

// var ano = +(prompt("Quantos anos nessam vida:"))
// var nCigarros = +(prompt("Quantos cigarros por dia:"))
// var preco=+(prompt("Quanto você paga por cartela:"))
// var din=0
// var cigarro=0
// var qtdDia = 0
// qtdDia=nCigarros*365*ano
// cigarro=preco/20
// din = qtdDia*cigarro
// document.write(`Voce gastou R$ ${din} de cigarro`)

// 3

// var amalia=+(prompt("Quantos anos você tem Amalia:"))
// var joaquim=+(prompt("Quantos anos você tem Joaquim:"))
// var maisVelho = 0
// if(amalia>joaquim){
// document.write(`O mais velho é  a Amalia de ${amalia}`)
// }
// else if(joaquim>amalia){
//     document.write(`O mais velho é o Joaquim de ${joaquim}`)
//     }
// else{
//     document.write(`idades iguais`)
// }

// 4

// function vida(saude,dano){
//     if(saude<=dano){
//         return true
//     }
//     else{
//         return false
//     }
// }
// var saude=+(prompt("Qual é a sua saude no jogo(0 a 100)"))
// var dano=+(prompt("Quanto de dano você tomou: "))

// document.write(vida(saude,dano))

// 5
sorteado=[]
for(var i=0;i<6;i++){
    sorteado[i]=Math.floor(Math.random()*60)
}
tentativa=[]
for(var i=0;i<6;i++){
    tentativa[i]=+(prompt(`digite um numero: `))
}
acerto=0
for(var i=0;i<6;i++){
    if(tentativa[i].include(sorteado)){
        acertos++
    }
}
document.write(`${sorteado} , qtd ${acerto} e a ${tentativa} `)






