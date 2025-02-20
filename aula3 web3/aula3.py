'''
a= int(input("O valor de A: "))
b=int (input("O valor de B: "))

if a>b:
    print(f'O valor de {a} é maior')
else:
    print(f'O valor de {a} é menor')
print('Fim')

#---------------------------------------

nome = input('Digite seu nome: ')
if nome=='Isabel':
    print('Esse nome é bonito')

idade=int(input('Digite a sua idade: '))

if idade>=18:
    print(f'A idade da pessoa {idade} já pode votar')
else:
    print(f'A idade da pessoa {idade} não pode votar')

#-------------------------------------------------
if idade >= 0 and idade<3:
    print('bebe')
elif idade >= 3 and idade <10:
    print('criança')
elif idade >= 10 and idade <15:
    print('adolescente')
elif idade>=15 and idade < 60:
    print('adulto')
else:
    print('velho')

# condicionsl ternaria -------------------------------

nota = float(input('digite sua nota'))
print('Aprovado' if nota>=6 else 'reprovado')

# for ------------------------------------------------

g = 0 
h = 10
for i in range(h):
    print('olá')

# star, stop, step ----------------------------------

for num1 in range(1,20,2):
    print(num1) '''

t=int(input('digite um numero para saber a tabuada: '))
for tabuada in range(1,11):
    print(f'{t} x {tabuada} = {t*tabuada}')

