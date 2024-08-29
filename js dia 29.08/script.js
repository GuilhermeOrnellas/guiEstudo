//contagem dos numeros pares entre 0 e 20 -------------

//for (i = 0; i <= 20; i++) {
//if (i % 2 == 0) {
//document.write(`<br>${i}`);
//}
//}

//inverter uma string---------------------------------

/*palavra = prompt("Digite uma palavra");
palavraInvertida = "";

for (i = palavra.length - 1; i >= 0; i--) {
  palavraInvertida += palavra[i];
}
document.write(`${palavra} invertida: ${palavraInvertida}`);*/

//.toLowerCase() para colocar as letras em minusculo -------------

/*var nomes = ["Maria", "Paulo", "Lucas"];
for (i = 0; i < nomes.length; i++) {
  nomes[i] = nomes[i].toLowerCase();
}
document.write(`<br> ${nomes}`);*/

// -----------------------------------------------------------------

/*var nota = +prompt("Digite a nota do aluno");

var conceito =nota >= 9 ? "A" : 
              nota >= 8 ? "B" : 
              nota >= 7 ? "C" : 
              nota >= 6 ? "D" : "E";
document.write(`<br> ${conceito}`);*/

//-------------------------------------------------------------

/*var tem = +prompt("Digite a temperaturada pessoa");
var saude =
  tem < 35
    ? "Hiportemia"
    : tem >= 35 && tem < 37.5
    ? "Normal"
    : tem >= 37.5 && tem < 39
    ? "Febre"
    : "Tá morrendo";

document.write(`<br> ${saude}`);*/

//- switch()-------------------------------------------------

sexo = prompt("Digite F(feminino), M(masculino) e O (outros)");
sexo = sexo.toLowerCase();
switch (sexo) {
  case "m":
    document.write("Masculino");
    break;
  case "f":
    document.write("Feminino");
    break;
  case "o":
    document.write("Outros");
    break;
  default:
    document.write("Opções invalidas");
}
