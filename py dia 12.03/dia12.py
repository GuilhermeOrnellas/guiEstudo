'''
#len() - mostra a qtd de elementos ---

aluno = ('Paulo','Julia','Isabel','Marcelo')
    print(f'A qtd de elementos na tupla : {len(aluno)}')

#------------------------------------------------------------

for i in range(0, len(aluno)):
    print(f'Oi!{aluno[i]}')
print('Boa noite')

#del() - deletar a tupla--------------------------------------

del(aluno)
print(aluno)


#count() mostra a qtd de elementos repetidos ----------------

f=(1,2,3,4,5,1)
g(1,4,5)
h= f + g

print(f'O num 1 repete {h.count(1)} vezes')

# index() mostra a primeira posição da repetição do elemeto --

print(f'O indice da primeira repetição é : {h.index(1)}')


#lista() a lista é mutavel, representada [] ---------------

a = [1,2,3,4.5,'Marcelo',True]

a[4]= 'Tereza' #alterou o nome na lista não pode fazer isso na tupla pq a tupla é imutável

b=[1,[true,'luiz',0],5,6,8,9[0,1,2]]

print(b[5][1])


#append() - add novos elemtos no final da lista -----------

x.append('web 3')
print(x)

#recendo valores externos ---------------------------------

pessoas = [] #ou list()

nome1 =input('insira um nome')
nome2 =input('insira um nome')
nome3 =input('insira um nome')

pessoas.append(nome1)
pessoas.append(nome2)
pessoas.append(nome3)
print(pesssoas)

'''
#-------------------------------------------------------------

num = list()
for i in range(3,15,2)
    num.append(i)
    print(i)

#insert() - add novos elelmtos na posição desejada ----------

num1=[1,2,3]
num1.insert(1,'Tereza')
print(num1)

#remove() - remover elementos ------------------------

num1.remove(2)
print(num1)

#min() - busca o menor valor da lista ----------------

l = [10,20,50,40,80,0]
print(f'O menor valor da lista é {min(l)}')

#max() busca o maior valor da lista ----------------

print(f'O maior valor da lista é {max(l)}')

#-----------------------------------------------------

r = [10,20,30,40,50]
r.reverse()
print(r)

#sum() - soma todos os elementos da lista --------------

print(f'A soma dos elementos é : {sum(r)}')

#pop() - apaga o ultimo elemento da lista --------------

r1 = [10,20,30,40,50]
r1.pop()
print(f'O ultimo elemento a ser apagado {r1}')
 
r1.pop(2) # forcei a apagar o elemeto na posição 2
print(f'O ultimo elemento a ser apagado {r1}')

