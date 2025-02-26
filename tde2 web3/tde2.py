# 1

num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#2

nota1 = float(input("Digite a sua nota1 "))
nota2 = float(input("Digite a sua nota2 "))
nota3 = float(input("Digite a sua nota3 "))

media=nota1+nota2+nota3/3

if media>=7:
 print("aprovado")

if media<7 and media>=5:
   print("recuperação")

else:
   print("reprovado")

#3

num1 = int(input("Digite a sua num1 "))
num2 = int(input("Digite a sua num2 "))

if num1 % num2:
   print("Sim")
else:
   print("Não")

#4

num3 = int(input("Digite a sua num3 "))
num4 = int(input("Digite a sua num4 "))
num5 = int(input("Digite a sua num5 "))

if num3 <= num4 <= num5:
   print("Ordem crescente")

else:
   print("Não crescente")

#5

numero = int(input("digite um numero: "))

qtd_impar = (numero + 1) // 2

print(f"A quantidade de numeros impares é {qtd_impar} entre 1 e {numero}")

#6

numero1 = int(input("Digite um número positivo: "))

fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é {fatorial}.")

#7

numero2 = int(input("Digite um número: "))

qtd_digitos = len(str(abs(num)))

print(f"{qtd_digitos}")

#8

numero3 = int(input("Digite um número inteiro positivo: "))

if num <= 0:
    print("Digite um número inteiro e positivo.")
else:
    soma_divisores = sum(i for i in range(1, num) if num % i == 0)

    if soma_divisores == num:
        print(f"{num} é um número perfeito!")
    else:
        print(f"{num} não é um número perfeito.")

#9

n = int(input("Digite um número: "))

if n <= 0:
    print("Digite um número inteiro positivo maior que zero.")
else:
    fibonacci = [0, 1]

    for i in range(2, n):
        termo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(termo)

    print(fibonacci[:n])  

#10

numeroo=int(input("numero base: "))
numeroo2=int(input("numero limite: "))

for count in range(1, numeroo2 + 1):
    resultado= numeroo * count
    print(f"{numeroo}X{count}={resultado}")










