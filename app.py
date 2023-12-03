import mysql.connector

conexao = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='bdteste',
)

cursor = conexao.cursor()

# CRUD

#CREATE
#nome_produto = "RTX 4090"
#valor = "3500"
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#ursor.execute(comando)
#conexao.commit() #edita o banco de dados #

#READ
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#UPTADE
#nome_produto = "GTX 1060"
#valor = 950
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

#DELETE
#nome_produto = "GTX 1060"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

cursor.close()
conexao.close()