#1
'''
from tkinter import *

def impar_par():
    num = int(entry_num.get())
    if num %2 ==0:
        result= 'par'
    else:
        result= 'impar'

    r_Label.config(text=result)

num = Tk()

label = Label(num, text='digite um numero')
label.grid(row=0,column=0,padx=10,pady=10)

entry_num = Entry(num)
entry_num.grid(row=1,column=0,padx=10,pady=10)

btn = Button(num, text ='impar ou par ?' , command =impar_par)
btn.grid(row=2,column=0,padx=10,pady=10)

r_Label = Label(num)
r_Label.grid(row =3 , column =0, columnspan =2)


num.mainloop()
'''

#2
'''
from tkinter import*

def limite_obter():

    lista_numeros = list(map(int, entry_lista.get().split(',')))
    limite = int(entry_limite.get())

    result = '-1'

    for i, num in enumerate(lista_numeros):
        if num > limite:
            result = f"numero maior que {limite} no inice {i}: {num}"
            break

    r_Label.config(text=result)

limite = Tk()

label = Label(limite,text='digite um num limite')
label.grid(row=0,column=0,padx=10,pady=10)

entry_limite = Entry(limite)
entry_limite.grid(row=1, column = 0,padx = 10,pady = 10)

label_lista = Label(limite, text='Digite números separados por vírgula :')
label_lista.grid(row=2, column=0, padx=10, pady=10)

entry_lista = Entry(limite)
entry_lista.grid(row=3, column=0, padx=10, pady=10)


botao = Button(limite, text="Verificar", command=limite_obter)
botao.grid(row=4, column=0, padx=10, pady=10)

r_Label = Label(limite, text="")
r_Label.grid(row =5 , column =0, columnspan =2)

limite.mainloop()

'''

#3
'''
from tkinter import*

def anos():
    anos = int(entry_bissexto.get())
    if (anos % 4 == 0 and anos % 100 != 0) or (anos % 400 == 0):
        result = "Ano Bissexto"

    else:
        result = "Não é bissexto"

    r_label.config(text=result)

bissexto = Tk()

label = Label(bissexto, text='Digite um ano')
label.grid(row=0,column=0,padx=10,pady=10)

entry_bissexto= Entry(bissexto)
entry_bissexto.grid(row=1,column=0,padx=10,pady=10)

botao=Button(bissexto,text='Ano Bissexto ?',command=anos)
botao.grid(row=2,column=0,padx=10,pady=10)

r_label = Label(bissexto,text="")
r_label.grid(row =5 , column =0, columnspan =2)

bissexto.mainloop()

'''

#4
'''
from tkinter import *


def soma():
    number1 = int(entry_num1.get())
    number2 = int(entry_num2.get())
    resultado.config(text=number1 + number2)


def subtracao():
    number1 = int(entry_num1.get())
    number2 = int(entry_num2.get())
    resultado.config(text=number1 - number2)


def multiplicacao():
    number1 = int(entry_num1.get())
    number2 = int(entry_num2.get())
    resultado.config(text=number1 * number2)


def divisao():
    number1 = int(entry_num1.get())
    number2 = int(entry_num2.get())

    if number1 == 0 or number2 == 0:
        resultado.config(text="Não pode dividir com 0")
        return
    resultado.config(text=number1 / number2)


calculo = Tk()


label = Label(calculo, text="Digite dois números e depois selecione a operação que deseja")
label.grid(row=0,column=0,padx=1,pady=10)


entry_num1 = Entry(calculo)
entry_num1.grid(row=1,column=0,padx=1,pady=10)

entry_num2 = Entry(calculo)
entry_num2.grid(row=1,column=1,padx=1,pady=10)


oper_soma = Button(calculo, text="+", command=soma)
oper_soma.grid(row=2,column=0,padx=1,pady=10)

oper_subtracao = Button(calculo, text="-", command=subtracao)
oper_subtracao.grid(row=2,column=1,padx=1,pady=10)

oper_multiplicacao = Button(calculo, text="*", command=multiplicacao)
oper_multiplicacao.grid(row=2,column=2,padx=1,pady=10)

oper_divisao = Button(calculo, text="/", command=divisao)
oper_divisao.grid(row=2,column=3,padx=1,pady=10)


resultado = Label(calculo, text="resultado")
resultado.grid(row=3,column=0,padx=1,pady=10)

calculo.mainloop()
'''

#5

from tkinter import *


def info_lista():
    lista = entry_num.get().split(",")
    lista = [int(n) for n in lista]
    pares = [
        n for n in lista
        if n % 2 == 0
    ]

    if 3 in lista:
        index_3 = lista.index(3)
    else:
        index_3 = -1

    resultado.config(text=f"""\
O número 9 apareceu {lista.count(9)} vezes.
O número 3 apareceu a primeira vez no índice {index_3}.
Os números pares são: {pares}""", justify="left"
                     )

lista = Tk()

label = Label(lista, text='Digite uma lista de números, separados por ",".')
label.place(x=5, y=5)

entry_num = Entry(lista)
entry_num.place(x=5, y=30)

btn = Button(lista, text="Clique aqui", command=info_lista)
btn.place(x=5, y=55)

resultado = Label(lista, text="O resultado sairá aqui", anchor='w')
resultado.place(x=5, y=85)

lista.mainloop()