var qtdT = 0
var reset=document.getElementById('button')


document.addEventListener('keydown', function(event){
    if(event.key = 'a'){
        qtdT+=1
        document.getElementById('res').innerHTML = `Tecla a digitada ${qtdT} vezes.`
    }
})

reset.addEventListener('click',function(){
    qtdT= 0
    document.getElementById('res').innerHTML = `Tecla a digitada ${qtdT} vezes`
})






