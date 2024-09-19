//função every()------------------

//função some()-------------------

//função filter()-----------------
/*
var frutas = ["banana", "uva", "jabuticaba", "goiaba", "kiwi"];
var esp = frutas.filter(function (frutas) {
  return frutas.indexOf("an") > 0;
});

document.write(`<br>${esp}`);
*/

//função map() ---------------

//função reduce() soma todos os elementos do Array--------
/*
numero3 = [10, 20, 30, 40, 50];
soma = 0;
soma = numero3.reduce(function (t, n) {
  return t + n;
});
document.write(`<br> A soma de todos os elementos do vetor 
    é ${soma}`);
*/
//--------------------Matéria da Av1-----------------------

var corpo = document.body;
corpo.style.background = "lightblue";

//Exemplo de seletor getElementsByTagName() ---------------

var a = document.getElementsByTagName("p")[1];
a.style.color = "red";
a.style.fontSize = "16pt";
a.style.background = "yellow";
a.style.fontFamily = "verdana";

//Exemplo de seletor getElementById() ---------------

var b = document.getElementById("a");
b.style.color = "red";
b.style.fontSize = "16pt";
b.style.background = "yellow";
b.style.fontFamily = "verdana";
b.innerText = "Alterando a palavra teste para Dom";

/*innerText/textContent - traz somente o texto
innerHTML - traz o texto e a sua formatação */
