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


vsql= """CREATE TABLE tb_alunos(
            N_MATRICULA INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOME VARCHAR(100) NOT NULL,
            T_CPF INT(11) NOT NULL UNIQUE,
            T_AVALIACAO INT(10) NOT NULL
    );"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print(ex)

def dql(query):
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query):
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)



criarTabela(vcon,vsql)

vcon.close()