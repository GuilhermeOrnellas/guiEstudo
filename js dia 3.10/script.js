//ex1 - captura das telas digitadas

//document.getElementById('input').addEventListener('keydown',function(event){
//    console.log('tecla precionada',event.key)
//})

//arrow function => ------------------

//document.getElementById('input1').addEventListener('keydown',(event)=>{
//    console.log('tecla precionada',event.key)
//})

//ex2 - prevenir a ação padrao do botão  -----------------

/*document.querySelector('#input2').addEventListener('keydown',function(event){
    if(event.key == 'Enter'){
        event.preventDefault() //previnir quebra de linha
        alert('tecla enter foi precionada, mas a ação foi previnida')
    }
})*/
//arrow function => ---------------------------
/*  document.querySelector('#input2').addEventListener('keydown',(event)=>{
    if(event.key == 'Enter'){
        event.preventDefault() //previnir quebra de linha
        alert('tecla enter foi precionada, mas a ação foi previnida')
    }
})*/

//ex3 - verificandio se as teclas são numericas ---------------------------

/*document.querySelector('#input3').addEventListener('keydown',function(event){
    if(isNaN(event.key)&& event.key != 'baskspace'){
        event.preventDefault() //impedir qualquer caractere que não seja numero 
    }
})*/

//ex4 - controle de volume ---------------------------------------------

var volume = 50
document.addEventListener('keydown',function(event){
    if(event.key =='ArrowUp'){
        volume = Math.min(100,volume + 5)
    }
    else if(event.key =='Arrowdown',volume-5){
        volume = Math.max(0,volume - 5)
    }
    document.getElementById('volume').textContent='volume:'+volume
})

//ex5 - Alterar a cor do fundo da tela ----------------------------------

/*function cor(event){
    var kc =event.which // obtem tecla precionada
    switch(kc){
        case 82: //corresponde a tecla r
            document.body.style.backgroundColor='red'
        break
        case 71: //corresponde a tecla g
            document.body.style.backgroundColor='green'
        break
        case 66: //corresponde a tecla b
            document.body.style.backgroundColor='blue'
        break
    }
}
document.addEventListener('keydown',cor)

*/

//ex6 - alterar a cor do elemento com a barra de espaço --------------------
/*
var elemento = document.getElementById('elemento')
function h(event){
    if(event.key == ' '){
        elemento.style.backgroundColor='lightgreen'
    }
}
function hh(event){
    if(event.key == ' '){
        elemento.style.backgroundColor='lightblue'
    }
}
document.addEventListener('keydown', h)
document.addEventListener('keyup', hh)
*/

//ex7 - inserir elementos na lista -----------------------------------------

var i = document.getElementById('input4')
var l = document.getElementById('lista')

function adicionar(event){
    if(event.key == 'Enter'){
        var novoItem = document.createElement('li')
        novoItem.innerText = i.value
        l.appendChild(novoItem)
        i.value = ''
    }
    else if(event.key =='Delete'){
        var ultimoL = l.lastChild
        if(ultimoL){
            l.removeChild(ultimoL)
        }
    }
}
i.addEventListener('keydown',adicionar)