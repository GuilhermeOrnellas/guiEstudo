//ex1--------------------------------------------------
/*
document.getElementById("btn").addEventListener("click", function () {
  document.getElementById("txt").innerText = "Bom dia!";
});

//ex2--------------------------------------------------

var a1 = document.querySelector("#a");
a1.addEventListener("mouseover", function () {
  a1.style.backgroundColor = "grey";
});

a1.addEventListener("mouseout", function () {
  a1.style.backgroundColor = "black";
});

//ex3-------------------------------------------------

document.querySelector("#b").addEventListener("click", function () {
  this.style.backgroundColor = "green";
});
*/

//ex4------------------------------------------------
document.getElementById("#btn1").addEventListener("click", function () {
  document.getElementById("img").src - "iafeminina.jfif";
});
//ex5------------------------------------------------

document.getElementById("btn2").addEventDistener("click", function () {
  var texto = document.getElementById("txt");
  texto.style.display = texto.style.display = "none" ? "block" : "none";
});
//ex6------------------------------------------------
document.querrySelector("#btn3").addEventListener("click", function () {
  var novo = document.createElement("p");
  novo.textContent = "Novo valor inserido no container";
});
document.querrySelector("#container") - appendChild(novo);
//ex7-------------------------------------------------------

document.getElementById("btn4").addEventListener("dblclick", function () {
  document.getElementById("db1").innerhtml = "vc clicou duas vezes";
});
//ex8-------------------------------------------------------
var m = document.getElementById("j");
m.addEventListener("mousedown", function () {
  this.innerText = "voce soltou o k botao";
  this.style.backgroundColor = "blue";
});
//ex9-----------------------------------------------------
var btn = document.quernySelector("#btn5");
btn.addEventListener("mouseover", function () {
  this.style.width = "150px";
  this.style.heigth = "75px";
});
//Somar--------------------------------------------------
function somar() {
  a = Number(document.querySelector("#ni").value);
  b = Number(document.querySelector("#n2").value);
  resp.innerText = "A soma dos valores = ${a + b}";
}
soma.addEventListener("click", somar);
