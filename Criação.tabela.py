import sqlite3
from sqlite3 import Error




def ConexaoBanco():
    caminho= "C:/BZ_bzu/Bz_BzU.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

nome=input("Digite o nome: ")
cpf=input("Digite o cpf: ")
avaliacao=input("Digite a avaliacao: ")

vsql="INSERT INTO tb_alunos (T_NOME, T_CPF, T_AVALIACAO) VALUES('"+nome+"', '"+cpf+"','"+avaliacao+"')"
def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)
inserir(vcon,vsql)

#deletar
def deletar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido")
vsql="DELETE FROM tb_alunos WHERE N_MATRICULA=12"
deletar(vcon,vsql)

#up
def atualizar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")
vsql="UPDATE tb_alunos SET T_NOME='Breno',T_CPF='70026404290', T_AVALIACAO='7' WHERE N_MATRICULA="
atualizar(vcon,vsql)

#select
def consulta(conexao, sql):
        c=conexao.cursor()
        c.execute(sql)
        resultado=c.fetchall()
        return resultado

vsql="SELECT * FROM tb_alunos"
res=consulta(vcon,vsql)
for r in res:
    print(r)