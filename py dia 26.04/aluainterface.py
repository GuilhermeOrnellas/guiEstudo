from tkinter import *

i = Tk()  # Cria uma instância da janela
'''
i.title('Primeira Janela')  # Inserir título na janela
i.geometry('600x300')  # Define o tamanho da janela
# i.resizable(False, False)  # Restringir o redimensionamento da janela
# i.state('zoomed')  # Abre em full screen
# i.state('iconic')  # Abre no ícone da barra de atalho da área de trabalho
# i.maxsize(900, 500)  # Máximo que a página vai
# i.minsize(300, 150)  # Mínimo que a página vai
i['bg'] = 'darkblue'  # Define a cor do background da janela

# Descomente esta linha para definir o ícone, certificando-se de ter o arquivo 'opa.ico' no mesmo diretório
# i.wm_iconbitmap('opa.ico')

# Entry() - Cria uma caixa de entrada de dados
e = Entry(i)
e.pack()

# Função do botão
def botao_clicado():
    label.config(text='Olá, você clicou no botão')  # Correção aqui, 'config' agora altera o texto do label

# Button() - Inserir um botão na janela
btn = Button(i, text='Inserir', font='Verdana 12 bold')
btn.pack()

btn1 = Button(
    i,
    text='Clique aqui',
    font='Arial 12 bold',
    fg='white',  # Cor da fonte
    bg='#4CAF50',  # Cor de fundo
    relief='raised',  # Para inserir uma borda
    bd=5,  # Ajusta o tamanho da borda
    padx=20,  # Espaço entre o conteúdo e a borda na horizontal
    pady=10,  # Espaço entre o conteúdo e a borda na vertical
    activebackground='#45A049',  # Altera a cor de fundo ao clicar no botão
    activeforeground='#CECECE',  # Altera a cor da fonte ao clicar no botão
    command=botao_clicado  # Ação a ser exercida pelo botão
)
btn1.pack(pady=20)

# Label() - Rótulo
label = Label(i, bg='darkblue', fg='white')  # Modificado para ter a cor preta na fonte
label.pack()


#sistema grid(linha e coluna) ---------------------
x1 = Label(i,text='Teste1',bg='black',fg='white')
x2 = Label(i,text='Teste2',bg='gray',fg='white')
x3 = Label(i,text='Teste3',bg='darkgray',fg='white')

x1.grid(row=0,column=0, padx=10)
x2.grid(row=0,column=1, padx=10)
x3.grid(row=0,column=2, padx=10)
'''
#-------------------------------------------
'''
label_nome = Label(i,text='Nome: ', font = 'Arial 10',bg='white')
label_nome.grid(row=0,column=0,padx=10,pady=10)

entry_nome = Entry(i)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_idade = Label(i,text='Idade: ', font = 'Arial 10',bg='white')
entry_idade.grid(row=1, column=0, padx=10, pady=10)

entry_idade = Entry(i)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

def informaçoes():
    nome = entry_nome.get()
    idade = entry_idade.get()
    r_Label.config(text =f'Nome: {nome}\n idade: {idade}')

btn2 = Button(i, text = 'Cadastrar', command = informaçoes)
btn2.grid(row = 2, column = 0, columnspan = 2 , pady = 20)

r_Label = Label(i, bg='pink')
r_Label.grid(row =3 , column =0, columnspan =2)
'''
#Checkbutton() - seleção multipla --------------------------------------------------
'''
t = Label(i, text='Qual o seu esporte favorito')
a1 = Checkbutton(i,text='Futebol')
a2 = Checkbutton(i,text='tennis')
a3 = Checkbutton(i,text='Natação')
a4 = Checkbutton(i,text='Basquete')

t.grid(row = 0 , column = 0, padx = 10)
a1.grid(row = 1 , column = 0, padx = 10)
a2.grid(row = 2 , column = 0, padx = 10)
a3.grid(row = 3 , column = 0, padx = 10)
a4.grid(row = 4 , column = 0, padx = 10)'

t.place(x=10, y=10)
a1.place(x = 10 , y = 40)
a2.place(x = 10 , y = 80)
a3.place(x = 10 , y = 120)
a4.place(x = 10 , y = 160)
''' '''
def mostrar_selecionados():
    selecionados = []
    if futebol_var.get():
        selecionados.append('Futebol')
    if  tennis_var.get():
        selecionados.append('tennis')
    if natacao_var.get():
        selecionados.append('Natação')
    if basquete_var.get():
        selecionados.append('Basquete') 

    r_Label.config(text='Esporte selecionado(): '+' ☻' .join(selecionados))
    
futebol_var = IntVar()
tennis_var = IntVar()
natacao_var = IntVar()
basquete_var = IntVar()

t = Label(i, text='Qual o seu esporte favorito')
t.place(x=10,y=0)
a1 = Checkbutton(i,text='Futebol', variable =futebol_var)
a2 = Checkbutton(i,text='tennis', variable=tennis_var)
a3 = Checkbutton(i,text='Natação', variable=natacao_var)
a4 = Checkbutton(i,text='Basquete', variable=basquete_var)

t.place(x=10, y=10)
a1.place(x = 10 , y = 40)
a2.place(x = 10 , y = 80)
a3.place(x = 10 , y = 120)
a4.place(x = 10 , y = 160)

btn3 = Button(i, text = 'clique aqui', command = mostrar_selecionados)
btn3.place(x=10,y=200)

r_Label = Label(i,text='Esportes selecionados: Nenhum', bg='pink')
r_Label.place(x=10,y=100)

'''
#Listbox() - cria uma lista --------------------------------------------

lista = Listbox(i, selectmode=MULTIPLE)
lista.insert(0,'AC')
lista.insert(1,'AM')
lista.insert(2,'AL')
lista.insert(3,'MG')
lista.insert(END,'TO')
lista.pack()

estado=['a','b','c']
for u in estado:
    lista.insert(END, u)


i.mainloop()
