import sqlite3

conexao = sqlite3.connect("teste_banco.db")

def init_db(conexao): 
    with open("arquivo.sql", "r", encoding="utf-8") as arquivo:
        sql_script = arquivo.read()

    cursor = conexao.cursor()
    cursor.executescript(sql_script)    

def add_dados(conexao, nome, email):
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO Teste (nome, email) VALUES (?, ?)", (nome, email,)
    )

    conexao.commit()
    conexao.close()

def ver_dados(conexao): 
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Teste")
    dados = cursor.fetchall()

    for linha in dados:
        print(f"{linha[0]}, {linha[1]}, {linha[2]}")

    conexao.close()


# nome = input("Digite o seu nome: ")
# email = input("Digite o seu email: ")

init_db(conexao)
# add_dados(conexao, nome, email)
ver_dados(conexao)
