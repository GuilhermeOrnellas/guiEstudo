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
/*
var h = [10,20,30,40]
h.push(50)
document.write(`<br>${h}`)

//pop- remove o utimo elemento da Array --------------

h.pop()
document.write(`<br>${h}`)

//unshift - adiciona um novo elemento no inicio da Array -----------

h.unshift(0)
document.write(`<br>${h}`)

//shift() - remove o primeiro elemento na Array

h.shift()
document.write(`<br>${h}`)
*/
//slice()- fatia a Array sem alterar o Array original ------
/*
aluno='Maria Da Silva Xavier'
a=aluno.slice(5)
document.write(`<br>${a}`)
a=aluno.slice(5,14)
document.write(`<br>${a}`)

email = 'exemplo@gmail.com'
e=email.slice(email.indexOf('a')+1)
document.write(`<br>${e}`)
*/

/*splice() - 1º valor: posição 
             2º valor: quantidade de elementos excluidos
             3º valor: novos elementos */
/*
d=['Sedunda','Terça','Quarta']
d1=d.splice(1,1)
document.write(`<br> A ${d1} foi deletada`)
document.write(`<br> Sobram - ${d} `)

d2= d.splice(1,1,'Quinta','Sexta')
document.write(`<br> A ${d2} foi deletada`)
document.write(`<br>${d}`)

d3= d.splice(1,0,'Quinta','Sexta')
document.write(`<br> A ${d3} foi deletada`)
document.write(`<br>${d}`)*/
/*
nome = []
for(i=0;i<5;i++){
    nome[i]=prompt('Digite o seu nome')
}
document.write(`<br>Nome: ${nome}`)
n=nome.splice(2,0,1)
document.write(`<br>Nome: ${nome}`)*/

//Função anonima - não possui nome, atribui-se a função a uma variável
/*
var msg=function(){
    return 'Olá,bom dia'
}
document.write(`<br>${msg()}`)
// ---------------------------------
var msg1=function(){
    return `Olá ${nome}, bom dia`
}
nome=prompt('Digite o seu nome')
document.write(`<br>${msg1()}`)
// ---------------------------------
var numero=function(num){
    return num**2
}
num=+(prompt('Digite um numero'))
document.write(`<br>${numero(num)}`)
*/
