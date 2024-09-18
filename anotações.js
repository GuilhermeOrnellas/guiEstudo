Arrays

var familia = [true,26,40,50,18, 'gui']
document.write(familia.length)   para saber o tamanho da Array
document.write(familia[3])

var nomeAmigo = ['Kleber', 'niteroi', 18]

a variável + .push() add um item no final da Array

a variável + .pop() remove um item no final da Array

var variavelEscolhida = variavelEscolhida.pop()
          se fizer isso, você poderá
           mostar a Array removida

a variável + .shift() remove o primeiro item da Array
a variável + .unshift() add um item no início da Array


--------------------------------------------------
var frutas = ['maçã', 'banana']  
var vegetais = ['cenoura', 'batata']

var alimentos = frutas.concat(vegetais)

aqui eu criei duas variáveis (Array) e juntei elas com 
o  -  variavel.concat(outraVariavel)  -
 e exibi o resultado com a variável alimentos
-------------------------------------------------

a variável + .slice(colocar o indice) cria uma Array só com os numeros dos indices (posição) escolhidos

a variável + .splice(posição da Array , numero de arrays apagadas , novos elementos)

a Variavel + Map() nesse caso o map vai analizar todos os numeros 
da Array sem altera-la, mas se usar o -- a Variavel + map(function(variável){ return ... }) tudo que pedir no function vai mudar

a variavel + .filter() -> funciona igual ao map() encima , mas o filter() filtra

