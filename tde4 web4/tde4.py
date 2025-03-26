#1
'''
contagem = ('zero','um','dois','três','Quatro',
            'Cinco', 'Seis', 'Sete','Oito',
            'Nove','Dez','Onze','Doze',
            'Treze','Quatorze','Quinze','Dezesseis',
            'Dezessete','Dezoito','Dezenove','Vinte')

while True:
    num = int(input('digite um numero de 0 a 20: '))
    if 0 <= num <=20:
        break
print(f'{contagem[num]}')
'''

#2



#3
'''
num = [2,9,8,7]

qtd_nove = num.count(9)

print(f"valor 9 apareceu {qtd_nove} vezes.")

if 3 in num:
    posicao_tres = num.index(3) + 1
    print(f"O primeiro valor 3 foi digitado na posição {posicao_tres}.")
else:
    print("O valor 3 não foi digitado.")


numeros_pares = [num for num in num if num % 2 == 0]
print(f"Os números pares digitados foram: {numeros_pares}")
'''
#4
'''
import random
lista = []

for i in range(50):
    lista.append(random.randint(1, 6))              # esse randint gera valor aleatorio
conta = lista.count(6)
porcentagem = conta /50 *100
print(f"{porcentagem}%")

'''
#5
'''
palavras = {
   'olá' : 'hello',
   'amigo': 'friend',
    'gelo': 'ice',
    'avião': 'plane',
    'espelho': 'mirror',
    'rapido' : 'fast',
    'sonho': 'dream',
    'travesseiro': 'pillow'
}

palavra = input("Digite uma palavra em português para traduzir para inglês: ").strip().lower()

traduçao = palavras.get(palavra,'palavra não encontrada')
print(f"Tradução: {traduçao}")

'''
#6
'''
import os

estoque = dict()

print("Seja bem vindo ao cadastro de produtos!\n")

opcao = 0
while True:
    opcao = int(input("O que deseja realizar?\n1 - Cadastrar produto\n2 - Ver estoque\n3 - Sair\n>>> "))
    if opcao == 1:
        os.system('cls')
        produto = str(input("Qual produto deseja cadastrar? (sair para encerrar) ")).lower()
        qtd = int(input("Digite a quantidade do produto: "))
        estoque[produto] = qtd
        print(f"{produto.capitalize()} cadastrado com sucesso!\n")
    elif opcao == 2:
        os.system('cls')
        for key, values in estoque.items():
            print(f"Produto: {key} | Quantidade: {values}")
        print()
    elif opcao == 3:
        break
print("Sistema encerrado")

'''
#7
'''

idades = []
 alturas = []
 
 for i in range(5):
     idades.append(int(input(f"Digite a idade da {i+1} pessoa: ")))
     alturas.append(float(input(f"Digite a altura da {i+1} pessoa: ")))
 
 for i in range(4, -1, -1):
     print(f"\n{i+1} pessoa:")
     print(f"Idade: {idades[i]}")
     print(f"Altura: {alturas[i]}")
 
 
 '''
#8
'''
qtd_letras = {}
 
string = str(input("Digite algo: ")).lower()
for letra in string:
    qtd_letras[letra] = string.count(letra)
 
for key, values in qtd_letras.items():
    print(f"Letra: {key} | Qtd: {values}")
 
 
 '''
#9
'''
def calcular_media(alunos):
    medias = {}
    soma = 0
    i = 1
    for key, values in alunos.items():
        medias[f'media_{key}'] = sum(values) / len(values)
        soma += sum(values)
        i += 1
    medias['media_geral'] = (soma / 3) / 3
    return medias
 
alunos = {
    "Kate": (8, 7, 6),
    "Nellie": (10, 6, 8),
    "Stephen": (5, 4, 6),
}
 
medias = calcular_media(alunos)
alunos.update(medias)
 
for k, v in alunos.items():
    print(k,v)
 
 
'''
#10
'''
string = input("Digite uma frase: ")
 
string = string.split(" ")
palavras = {}
for palavra in string:
    palavras[palavra] = string.count(palavra)
for k, v in palavras.items():
    print(f"Palavra: {k} | Qtd: {v}")
 
 
'''
#11
'''
def is_positive(n):
    return 'Positivo' if n > 0 else 'Negativo'
 
print(is_positive(5))
print(is_positive(-5))
print(is_positive(.4053))
 
 
'''
#12
'''
def valor_absoluto(n):
    return abs(n)

print(valor_absoluto(5))


'''
#13
'''
def soma(n1, n2, limite=100):
    return True if n1 + n2 <= limite else False

print(soma(50,49))
print(soma(50,100))
print(soma(10,24))


'''
#14
'''
def somaImposto(custo, taxaImposto):
    imposto = custo * taxaImposto / 100
    return custo + imposto
print(somaImposto(100,10))


'''
#15

def qtd_digitos(num):
    num_string = str(num)
    return len(num_string)
print(qtd_digitos(10))






