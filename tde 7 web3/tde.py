import mysql.connector
from tkinter import *
from tkinter import messagebox

def conectar(): conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="livraria",
    )

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS livraria")
conexao.database = "livraria"

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Editora (
        codigo INT PRIMARY KEY AUTO_INCREMENT,
        nome_gerente VARCHAR(100),
        endereco VARCHAR(200),
        telefone VARCHAR(20)
    )
    """)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Livro (
        ISBN VARCHAR(20) PRIMARY KEY,
        nome VARCHAR(100),
        autor VARCHAR(100),
        assunto VARCHAR(100),
        quantidade_estoque INT,
        codigo_editora INT,
        FOREIGN KEY (codigo_editora) REFERENCES Editora(codigo)
    )
    """)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente (
        codigo INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100),
        telefone VARCHAR(20),
        endereco VARCHAR(200),
        documento VARCHAR(20),
        tipo ENUM('Física', 'Jurídica')
    )
    """)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Compra (
        id_compra INT PRIMARY KEY AUTO_INCREMENT,
        codigo_cliente INT,
        ISBN_livro VARCHAR(20),
        data DATE,
        FOREIGN KEY (codigo_cliente) REFERENCES Cliente(codigo),
        FOREIGN KEY (ISBN_livro) REFERENCES Livro(ISBN)
    )
    """)
conexao.commit()
cursor.close()
conexao.close()

def inserir_cliente(nome, telefone, endereco, documento, tipo):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Cliente (nome, telefone, endereco, documento, tipo) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, telefone, endereco, documento, tipo)
    cursor.execute(sql, valores)
    conn.commit()
    cursor.close()
    conn.close()

def atualizar_cliente(codigo, novo_nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Cliente SET nome = %s WHERE codigo = %s", (novo_nome, codigo))
    conn.commit()
    cursor.close()
    conn.close()


def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cliente")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)
    cursor.close()
    conn.close()


def interface():
    def enviar():
        nome = entry_nome.get()
        telefone = entry_tel.get()
        endereco = entry_end.get()
        documento = entry_doc.get()
        tipo = var_tipo.get()
        inserir_cliente(nome, telefone, endereco, documento, tipo)
        messagebox.showinfo("Sucesso", "Cliente cadastrado")

    janela = Tk()
    janela.title("Cadastro de Cliente")

    Label(janela, text="Nome").grid(row=0, column=0)
    entry_nome = Entry(janela)
    entry_nome.grid(row=0, column=1)

    Label(janela, text="Telefone").grid(row=1, column=0)
    entry_tel = Entry(janela)
    entry_tel.grid(row=1, column=1)

    Label(janela, text="Endereço").grid(row=2, column=0)
    entry_end = Entry(janela)
    entry_end.grid(row=2, column=1)

    Label(janela, text="CPF/CNPJ").grid(row=3, column=0)
    entry_doc = Entry(janela)
    entry_doc.grid(row=3, column=1)

    Label(janela, text="Tipo").grid(row=4, column=0)
    var_tipo = StringVar()
    OptionMenu(janela, var_tipo, "Física", "Jurídica").grid(row=4, column=1)

    Button(janela, text="Cadastrar", command=enviar).grid(row=5, column=1)
    janela.mainloop()


criar_banco_e_tabelas()
interface()
