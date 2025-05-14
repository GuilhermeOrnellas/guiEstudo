from tkinter import *

# r= Tk()
# r.geometry('500x500')
# r.title('Aula 10')

# x = Menu(r)

# arquivo_menu= Menu(x, tearoff=0)
# arquivo_menu.add_command(label='Novo')
# arquivo_menu.add_command(label='Salvar')
# arquivo_menu.add_command(label='Salvar como')
# arquivo_menu.add_command(label='Imprimir')
# arquivo_menu.add_command(label='Sair')
# x.add_cascade(label ='Arquivo', menu=arquivo_menu)
# r.config(menu=x)

# editar_menu = Menu(x,tearoff=0)
# editar_menu.add_command(label='Copiar')
# editar_menu.add_command(label='Colar')
# editar_menu.add_command(label='Voltar')
# editar_menu.add_command(label='Sair')
# x.add_cascade(label ='Editar', menu=editar_menu)
# r.config(menu=x)


#r.mainloop()
#------------------------------------------------------------

r = Tk()
r.geometry('500x500')
r.title('Janela Principal')

# def abrir_arquivo():
#     nova_janela = Toplevel(r)   #toplevel abre uma nova janela secundaria atravez de um botao
#     nova_janela.geometry('500x500')
#     nova_janela.title('Janela Secundaria')
#     l = Label(nova_janela, text='Esta é uma nova janela')
#     l.pack()
    
# btn = Button(r,text='Abrir Nova Janela',command=abrir_arquivo).pack()


#---------------------------------------------------------------------

# menu_bar =Menu(r)
# r.config(menu=menu_bar)

# def abrir_arquivo():
#     nova_janela = Toplevel(r) 
#     nova_janela.geometry('500x500')
#     nova_janela.title('Janela Secundaria')
#     l = Label(nova_janela, text='Esta é uma nova janela')
    
# novo_menu = Menu(r,tearoff=0)
# novo_menu.add_command(label='Abrir Nova Janela',command=abrir_arquivo)
# menu_bar.add_cascade(label='Arquivo',menu = novo_menu)

#------------------------------------------------------------------------

# f  = Frame(r)
# f.pack()

# s = IntVar()

# def abrir_arquivo():
    
#     nova_janela = Toplevel(r) 
#     nova_janela.geometry('500x500')
#     nova_janela.title('Janela Secundaria')
#     l = Label(nova_janela, text='Esta é uma nova janela')
#     l.pack()
    
# r1 = Radiobutton(f,text='Abrir Nova Janela', variable=s,value=1, command=abrir_arquivo).pack()
# r2 = Radiobutton(f,text='Abrir Arquivo', variable=s,value=2).pack()
# r3 = Radiobutton(f,text='Fechar janela', variable=s,value=3).pack()

#--------------------- exemplo de site ---------------------------------

# div_cabecalho = Frame(r,bg='gray', width=500 , height=80)
# div_cabecalho.pack()

# div_conteudo = Frame(r,bg='black', width=500 , height=300)
# div_conteudo.pack()

# div_rodape = Frame(r,bg='dark gray', width=500 , height=100)
# div_rodape.pack()


r.mainloop()
