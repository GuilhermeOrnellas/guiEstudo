var slides = ["img1.png", "img2.png"];
var tam = slides.length;
var satual = 0;
var tpmslider;

function trocaAutomatica() {
  satual++;
  if (satual >= tam) {
    satual = 0;
  }

  document.querySelector(
    "#dvSlider"
  ).style.backgroundImage = `url("${slides[satual]}")`;
}

function iniciarSlider() {
  document.querySelector(
    "#dvSlider"
  ).style.backgroundImage = `url("${slides[satual]}")`;
  tpmslider = setInterval(trocaAutomatica, 2000);
}

function parar() {
  clearInterval(tpmslider);
}

function troca(dir) {
  satual += dir;
  if (satual < 0) {
    satual = 3;
  } else if (satual >= tam) {
    satual = 0;
  }
  document.querySelector(
    "#dvSlider"
  ).style.backgroundImage = `url("${slides[satual]}")`;
  clearInterval(tpmslider);
}
