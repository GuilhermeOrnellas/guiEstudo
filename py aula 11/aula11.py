import tkinter as tk
from tkinter import messagebox

''' 
class Aluno:
    def __init__(self,nome,idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso=curso
      
    def apresentar(self):
        print(f'Olá! Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}')
        
    def MaiorIdade(self):
        if self.idade>=18:
            print(f'{self.nome} é maior de idade')
        else:
            print(f'{self.nome} é menor de idade')
        
aluno1 = Aluno('Guilherme',19,'TI')
aluno1.apresentar()
aluno1.MaiorIdade() '''

#------------------------------------------------------------
'''
class Aluno:
    def __init__(self,nome,idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso=curso
        self.notas = []
    
    def apresentar(self):
        print(f'Olá! Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}')
        
    def addNota(self, nota):
        if 0<= nota <=10:
            self.notas.append(nota)
        else:
            print('Nota inválida, add uma not entre 0 e 10')
    
    def calcularMedia(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def aprovacao(self):
        media = self.calcularMedia()
        print(f'A media do {self.nome}: {media:.2f}')
        if media>=7:
            print(f'Aluno {self.nome} foi aprovado')
        else:
            print(f'Aluno {self.nome} foi reprovado')
            
      
aluno1 = Aluno('Guilherme',19,'TI')
aluno1.apresentar()
aluno1.addNota(8.9)
aluno1.addNota(7.0)
aluno1.addNota(6.5)
aluno1.calcularMedia()
aluno1.aprovacao()
'''
#--------------------------------------------------------------

class Aluno:
    def __init__(self,nome,idade,curso):
        self.nome = nome
        self.idade = idade
        self.curso=curso
        self.notas = []
    
    def apresentar(self):
        print(f'Olá! Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}')
        
    def addNota(self, nota):
        if 0<= nota <=10:
            self.notas.append(nota)
        else:
            print('Nota inválida, add uma not entre 0 e 10')
    
    def calcularMedia(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def aprovacao(self):
        media = self.calcularMedia()
        print(f'A media do {self.nome}: {media:.2f}')
        if media>=7:
            print(f'Aluno {self.nome} foi aprovado')
        else:
            print(f'Aluno {self.nome} foi reprovado')
'''
    def menu():
        aluno = None
        
        while True:
            print('\n===== Menu =====')
            print('1- Cadastrar Aluno')
            print('2- Adicionar nota do aluno')
            print('3- Média/aprovação')
            print('4- Mostrar dados do aluno')
            print('5- Sair')

            opcao = input('Escolha a opção desejada (1-5): ').strip()

            if not opcao:
                print('Entrada vazia. Digite uma opção.')
                continue
            
            if opcao == '1':
                nome = input('Digite o nome do aluno: ')
                idade = int(input('Digite a idade do aluno: '))
                curso = input('Digite o curso do aluno: ')
                aluno = Aluno(nome, idade, curso)
                print('Aluno cadastrado com sucesso.')
                
            elif opcao == '2':
                if aluno:
                    try:
                        nota= float(input('Digite a nota do aluno'))
                        aluno.addNota(nota)
                    except ValueError:
                        print('Nota invalida, insira uma nota de 0 a 10')
                else:
                    print('Cadastre um aluno primeiro( opção 1 )')
                 
            elif opcao == '3': 
                if aluno:
                    aluno.verificar_aprovacao()
                else:
                    print('Nenhum aluno cadastrado.')

            elif opcao == '4': 
                if aluno:
                    aluno.apresentar()
                    print(f'Média atual: {aluno.calcular_media():.2f}')
                else:
                    print('Nenhum aluno cadastrado.')

            elif opcao == '5':  
                print('Saindo...')
                break
            else:
                print('Opção inválida. Tente novamente.')   
            
Aluno.menu() '''

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Gerenciador de Aluno')
        self.aluno = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text='Nome').grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(self.root, text='Idade').grid(row=1, column=0)
        self.idade_entry = tk.Entry(self.root)
        self.idade_entry.grid(row=1, column=1)

        tk.Label(self.root, text='Curso').grid(row=2, column=0)
        self.curso_entry = tk.Entry(self.root)
        self.curso_entry.grid(row=2, column=1)

        tk.Button(self.root, text='Cadastrar Aluno', command=self.cadastrar_aluno).grid(row=3, columnspan=2, pady=10)

        tk.Label(self.root, text='Nota').grid(row=4, column=0)
        self.nota_entry = tk.Entry(self.root)
        self.nota_entry.grid(row=4, column=1)

        tk.Button(self.root, text='Adicionar Nota', command=self.adicionar_nota).grid(row=5, columnspan=2, pady=10)

        tk.Button(self.root, text='Media/Situação', command=self.mostrar_media_situacao).grid(row=6, columnspan=2, pady=10)
        tk.Button(self.root, text='Mostrar Dados', command=self.mostrar_dados).grid(row=7, columnspan=2, pady=10)

    def cadastrar_aluno(self):
        nome = self.nome_entry.get().strip()
        idade = self.idade_entry.get().strip()
        curso = self.curso_entry.get().strip()

        if nome and idade.isdigit() and curso:
            self.aluno = Aluno(nome, idade, curso)
            messagebox.showinfo('Cadastro Aluno', 'Aluno cadastrado com sucesso.')
        else:
            messagebox.showwarning('Erro', 'Erro! Preencha todos os campos corretamente.')

    def adicionar_nota(self):
        if not self.aluno:
            messagebox.showwarning('Erro', 'Erro! Cadastre um aluno primeiro.')
            return

        nota = self.nota_entry.get().strip()
        try:
            nota = float(nota)
            if self.aluno.addNota(nota):
                messagebox.showinfo('Nota', 'Nota cadastrada com sucesso.')
            else:
                messagebox.showwarning('Erro', 'Nota deve estar entre 0 e 10.')
        except ValueError:
            messagebox.showwarning('Erro', 'Digite um número válido para a nota.')

    def mostrar_media_situacao(self):
        if not self.aluno:
            messagebox.showwarning('Erro', 'Erro! Cadastre um aluno primeiro.')
            return
        
        resultado = self.aluno.verificar_aprovacao()
        messagebox.showinfo('Situação', resultado)

    def mostrar_dados(self):
        if not self.aluno:
            messagebox.showwarning('Erro', 'Erro! Cadastre um aluno primeiro.')
            return
        
        dados = self.aluno.apresentar() + "\n" + self.aluno.maior_idade()
        messagebox.showinfo('Dados do Aluno', dados)


root = tk.Tk()
app = App(root)
root.mainloop()