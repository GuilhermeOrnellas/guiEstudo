/*1-mousedown: Crie um evento que registre no console quando o botão do mouse é pressionado sobre um elemento específico.*/
document.getElementById("botaopre").addEventListener("mousedown",function(){
    console.log("botao precionado no elemento")
  })
  
  /*2-mouseup: Faça um evento que altere o texto de um elemento quando o botão do mouse é solto.*/
  document.getElementById("botaosolto").addEventListener("mouseup",function(){
    this.innerText="botao solto no elemento";
  })
  
  /*3-click: Implemente um botão que, quando clicado, exibe um alerta com uma mensagem.*/
  document.getElementById("clickbutao").addEventListener("click",function(){
    alert("botao clickado")
  })
  
  /*4-dblclick: Adicione um evento que mude a cor de fundo de um elemento ao ser clicado duas vezes.*/
  document.getElementById("botaocor").addEventListener("dblclick",function(){
    this.style.backgroundcolor="blue";
  })
  
  /*5-mousemove: Crie um evento que atualize as coordenadas do mouse exibidas em um elemento sempre que o mouse se move sobre ele.*/
   const coordinates = document.getElementById("coordinates");
    document.getElementById("mousemoveArea").addEventListener("mousemove", function(event) {
      coordinates.innerText = "X: " + event.clientX + ", Y: " + event.clientY;
    });

  /*6-mouseenter: Adicione um evento que mude a cor de um elemento ao passar o mouse sobre ele.*/
  
    document.getElementById("botaoenter").addEventListener("mouseenter", function() {
      this.style.backgroundColor = "lightgreen"
    });
  /*7-Combinação de Eventos: Faça um exercício que combine mousedown, mousemove e mouseup para criar uma funcionalidade de arrastar um elemento.*/
  let isDragging = false;
   const moveable = document.getElementById("moveable");

    moveable.addEventListener("mousedown", function(event) {
      isDragging = true;
      offsetX = event.offsetX;
      offsetY = event.offsetY;
    });
    document.addEventListener("mousemove", function(event) {
      if (isDragging) {
        moveable.style.left = event.clientX - offsetX + "px";
        moveable.style.top = event.clientY - offsetY + "px";
      }
    });
    document.addEventListener("mouseup", function() {
      isDragging = false;
    });