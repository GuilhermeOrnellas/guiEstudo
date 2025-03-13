#1

dados = (2,10,'Gui',True)

print(dados[1:2])

del(dados[1:3])

a tupla não pode ser modificada entao vai dar erro

#2

a=(1,2,2,4,5)

print(f'O num 2 repete {h.count(2)} vezes')

#3

num=[2,10,50]

num.append(100)

num.(num[2])

num[0] = 500

print(num)

#4

notas = [7, 8, 10, 9, 6]

soma = sum(notas)
media = soma / len(notas)

print(f"Soma das notas: {soma}")
print(f"Média das notas: {media}")

#5

lista = [10,20,30,40]

lista.sort()
print(lista)

lista.sort(reverse=true)

if lista>10:
    print(lista)

#6

nota = [[7, 8, 9, 6], [6, 5, 8, 7], [10, 9, 8, 9]]

print(notas[1][2])
medias = []
for i in range(len(notas)):
    media = sum(notas[i]) / len(notas[i])
    medias.append(media)


maior_media = medias.index(maior_media) + 1

print(f"O aluno com a maior média é o Aluno {maior_media}, com a média de {maior_media:.2f}.")




