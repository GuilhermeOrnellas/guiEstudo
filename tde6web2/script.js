document.getElementById("btn").addEventListener("click",function(){
   var nome = document.getElementById("nome").value
   var resposta = document.getElementById("resposta")
   resposta.innerHTML=`Boas Vindas ${nome}`
}) 