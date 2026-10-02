import sqlite3

with sqlite3.connect('meu_banco.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM authors WHERE id=1")
    autores = cursor.fetchone()
    print(autores)