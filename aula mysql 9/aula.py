from mysql import connector
import mysql
from tkinter import*
import tkinter.messagebox as MessageBox

def inserir():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade= e_qtd.get()
    
    if(codigo=='' or nome=='' or preco=='' or quantidade==''):
        MessageBox.showerror('Inserir', 'Todos os campos são obrigatórios')
    else:
        cursor.execute('insert into produto(codigo,nome,preco,quantidade)values(%s,%s,%s,%s)', 
                        (codigo, nome, preco, quantidade))
        conexao.commit()
        MessageBox.showinfo('Inserir', 'Produto inserido com sucesso')
        
        e_codigo.delete(0,END)
        e_nome.delete(0,END)
        e_preco.delete(0,END)
        e_qtd.delete(0,END)
        
def excluir():
    codigo = e_codigo.get()
    if codigo =='':
        MessageBox.showerror('Excluir', 'Informe o codigo do produto')
    else:
        cursor.execute('delete from produto where codigo = %s', (codigo,))
        conexao.commit()
        MessageBox.showinfo('Excluir', 'produto excluido com sucesso')
        
        e_codigo.delete(0,END)

def atualizar():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade= e_qtd.get()
    if (codigo=='' or nome=='' or preco=='' or quantidade==''):
        MessageBox.showerror('Inserir', 'Inserir campos são obrigatorios ')
    else:
        cursor.execute('update produto set nome=%s, preco=%s, quantidade=%s where codigo = %s', (nome,preco,quantidade,codigo))
        conexao.commit()
        MessageBox.showinfo('Atualizar', 'produto atualizado com sucesso')
  
def selecionar():
    codigo=e_codigo.get()
    if codigo=="":
        MessageBox.showerror('Selecionar','Todos os campos são obrigatórios.')
    else:
        cursor.execute('select * from produto where cod=%s',(codigo,))
        r=cursor.fetchall()
        if r:
            for r1 in r:
                e_nome.delete(0, END)
                e_preco.delete(0, END)
                e_qtd.delete(0, END)
                            
                e_nome.insert(0, r1[1])
                e_preco.insert(0, r1[2])
                e_qtd.insert(0, r1[3])
                            
                MessageBox.showinfo('Selecionar', f'Selecionado com sucesso!\n\nCódigo: {r1[0]}\nNome: {r1[1]}\nPreço: {r1[2]}\nQuantidade: {r1[3]}')
        else:
            MessageBox.showerror('Selecionar', 'produto nao encontrado!')
      
conexao = mysql.connector.connect(
    host ='Localhost',
    user ='root',
    passwd = '',
    database = 'loja',
)

cursor = conexao.cursor()

#cursor.execute("create database if not exists loja")
cursor.execute('use loja')
"""
cursor.execute('''create table produto(
                codigo int primary key,
                nome varchar(20) not null,
                preco decimal(10,2) not null,
                quantidade int not null)''')
"""

root=Tk()
root.geometry('237x170')
root.title('Loja')
Label(root,text='Código:').grid(row=0,column=0,padx=5,pady=5)
e_codigo=Entry(root)
e_codigo.grid(row=0,column=1,padx=5,pady=5)
Label(root,text='Nome:').grid(row=1,column=0,padx=5,pady=5)
e_nome=Entry(root)
e_nome.grid(row=1,column=1,padx=5,pady=5)
Label(root,text='Preço:').grid(row=2,column=0,padx=5,pady=5)
e_preco=Entry(root)
e_preco.grid(row=2,column=1,padx=5,pady=5)
Label(root,text='Quantidade:').grid(row=3,column=0,padx=5,pady=5)
e_qtd=Entry(root)
e_qtd.grid(row=3,column=1,padx=5,pady=5)

frame_botoes = Frame(root)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=10)

Button(frame_botoes, text='Consultar', command= selecionar).pack(side=LEFT, padx=5)
Button(frame_botoes, text='Inserir', command = inserir).pack(side=LEFT, padx=5)
Button(frame_botoes, text='Alterar', command = atualizar).pack(side=LEFT, padx=5)
Button(frame_botoes, text='Excluir', command = excluir).pack(side=LEFT, padx=5)

root.mainloop()
