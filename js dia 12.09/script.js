/*
// Metodo construtor() - new Array()--------

var a = new Array()
document.write(`<br> ${a}`)

var b = new Array(true,1,2,3,4,new Array(1,2,3),'a')
document.write(`<br> ${b}`)

//length - verificar o tamanho da Array---------------------

document.write(`<br>O tamanho da Array é ${b.length}`)

// indexOf() - identifica a posição do elemmento no Array ----------

document.write(`<br>A posição: ${b.indexOf('a')}`)*/

/*
//Metodo literal - [] ------------------------------------

var c = []

document.write(`<br>${c}`)
document.write(`<br>O tamanho da Array é ${c.length}`)

var d = [true,1,2,3,4[1,2,3],2,'a']
document.write(`<br>${d}`)
document.write(`<br>${d[0]}`)
document.write(`<br>${d[5][0]}`)*/

/*
//Valores externos-----------------------------------

nota=[]
for(i=0;i<3;i++){
    nota[i]=+(prompt('Digite a sua nota'))
}
document.write(`<br>As notas são: ${nota}`)
*/
/*
//string---------------------------------------------

nome='Thereza'
document.write(`<br>O tamanho da Array é ${nome.length}`)
document.write(`<br>A posição do elemento na Array é ${nome.lastIndexOf}`)*/

/*
//Inserir novos elementos no Array-----------------------

var e = [1,2,3,4]
e[4] ='Novo Valor'
document.write(`<br>${e}`)

//ou

e[e.length] ='Novo Valor'
document.write(`<br>${e}`)*/

//--------------------------------------------------------
/*
pessoa = ['Ana','Liz','Eva']

for(i=0;i<pessoa.length;i++){
    document.write(`<br>Nome: ${pessoa[i]}`)
}
*/

/*Função de ordenação-----------------------------------------
reverse() - le o Array de forma invertida --------------------*/

/*

pessoa = ['Ana','Liz','Eva']

document.write(`<br>${pessoa}`)
document.write(`<br>A ordem invertida do Array é: ${pessoa.reverse()}`)

//sort()- coloca em ordem alfabética --------------------------

document.write(`<br>A ordem alfabética do Array é: ${pessoa.sort()}`)



// coloca em ordem alfabética e inverte a ordem -------------------------

document.write(`<br>A ordem alfabética do Array é: ${pessoa.sort().reverse}`)

*/
//concat () - concatenar vetores ----------------------------------------
/*
var f = [1,2,3,4,5]
var g = [6,7,8]

document.write(`<br>O valor concatenado é: ${f.concat(g)}`)
//e ao contrario

document.write(`<br>O valor concatenado é: ${g.concat(f)}`)

//includes()- verifica se um detrminado elemento encontra-se no Array--------------------

document.write(`<br>O numero 2 encontra-se na Array? ${f.includes(2)}`)
document.write(`<br>O numero 12 encontra-se na Array? ${f.includes(12)}`)
*/

//push()- adiciona um novo elemento no final do Array -------------------------

var h = [10,20,30,40]
h.push(50)
document.write(`<br>${h}`)