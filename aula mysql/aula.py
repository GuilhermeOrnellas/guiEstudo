from mysql import connector
import mysql

conexao = mysql.connector.connect(
    host ='Localhost',
    user ='root',
    passwd = '',
    database = 'aula06'
)

x = conexao.cursor()

#criando a base de dados --------------------------

# x.execute('CREATE database if NOT EXISTS aula')

# x.execute('show databases')
# for i in x:
#     print(i)

# x.execute('use aula')

#criar tabela ----------------------------------------

# x.execute('''create table aluno(
#           matricula int primary key auto_increment,
#           nome varchar(30) NOT NULL,
#           idade int(3),
#           email varchar(40))''')


# mostrar a descrição da tabela -----------------------
'''
x.execute('desc aluno')
for i in x:
    print(i)
'''

#inserir dados na tabela - insert into nome da tabela (atributos) values(valores atribuidos)
'''
y = "insert into aluno(nome,idade,email) values('Gui',19,'quemedarabucetasopqeutodepistola@gmail.com')"
x.execute(y)
conexao.commit()
print(x.rowcount, 'Registro(s) inserido(s)')
'''
# ---------------------------------------------------------------------------------
"""
v = [
    ('Gui',19,'quemedarabucetasopqeutodepistola@gmail.com'),
    ('jorge',10,'quemedarabucetasopqeutodepistola@gmail.com'),
    ('lucas',12,'quemedarabucetasopqeutodepistola@gmail.com'),
    ('maria',20,'naooonaoooooooooo@gmail.com'),
    ('enzadas',28,'lapolicia@gmail.com'),
    ('natanzeira',21,'quemedarabucetasopqeutodepistola@gmail.com'),
    ('marcelao',18,'quemedarabucetasopqeutodepistola@gmail.com'),
    ('guilherme',19,'quemedarabucetasopqeutodepistola@gmail.com'),
]

x.executemany('insert into aluno(nome,idade,email) values(%s,%s,%s)',v)
conexao.commit()
print(x.rowcount, 'Registro(s) inserido(s)')

"""

#seleção simples -----------------------------------------------
"""
x.execute('Select * from aluno')
r = x.fetchall()   # se for fetchone() vai trazer so o primeiro dado da tabela 
print('Dados do aluno: ')

for i in r:
    print(i)
"""

"""
x.execute('Select nome from aluno where idade > 15')
r = x.fetchall()
print('Alunos com idade acima de 15 anos: ')

for i in r:
    print(i)

"""
"""
x.execute('Select nome from aluno order by nome')
r = x.fetchall()
print(' Dados do aluno ordenado de (A-Z): ')

for i in r:
    print(i)

#seleção condição - where  --------------------------------------

x.execute('select nome from aluno where idade > 15')
r = x.fetchall()
print('Alunos maiores de 15 anos: ')
for i in r:
    print(i)

#Ordenação asc/des - order by ------------------------------------

x.execute('Select * from aluno order by nome ')
r = x.fetchall()
print('Dados do aluno ordenado (A-Z)')
for i in r:
    print(i)
"""

#delete -- deletar apenas 1 registro 

# x.execute('delete from aluno where matricula=1')
# conexao.commit()
# print(x.rowcount,'Registro(s) deletado(s)')

# deletar multiplos registros ---------

# r = 'delete from aluno where matricula in (%s,%s)'
# x.execute(r,(2,4))
# conexao.commit()
# print(x.rowcount,'Registro(s) deletado(s)')

# deletar com intervalo - between ----------------

# r1='delete from aluno where matricula between %s and %s'
# x.execute(r1,(5,7))
# conexao.commit()
# print(x.rowcount,'Registro(s) deletado(s)')

# update ---------------------

# x.execute('update aluno set nome="Guilherme" where matricula=3')
# conexao.commit()
# print(x.rowcount,'Registro(s) deletado(s)')

#drop -- apaga tudo ------------------------------------------------

#x.execute('drop database aula06')
#x.execute('drop table aluno')

x.close()
conexao.close()
print('conexão incerrada')
