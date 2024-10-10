var distancia = +(prompt('Digite a distancia percorrida em km:'))
var q = 0
switch(true){
	case(distancia<=100):
		q=distancia*10
	break
case(distancia>=101 && distancia<=300):
		q=distancia*8
	break
case(distancia<=100):
		q=distancia*6    
	break
default:
	document.write(`invalido`)
}
document.write(`distancia percorrida ${distancia}km<br>`)
document.write(`Custo de : R$${q.toFixed(2)}`)

