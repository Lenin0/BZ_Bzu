import os
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

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operacao Realizada com sucesso")
        #conexao.close()

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    #conexao.close()
    return res

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por Matricula")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def menuInserir():
    os.system("cls")
    vnome=input("Digite o nome: ")
    vcpf=input("Digite o cpf: ")
    vavaliacao=input("Digite a avaliacao: ")
    vsql="INSERT INTO tb_alunos (T_NOME, T_CPF, T_AVALIACAO) VALUES ('"+vnome+"','"+vcpf+"','"+vavaliacao+"')"
    query(vcon,vsql)

def menuDeletar():
    os.system("cls")
    vid=input("Digite a Matricula do registo a ser deletado: ")
    vsql="DELETE FROM tb_alunos WHERE N_MATRICULA="+vid
    query(vcon, vsql)

def menuAtualizar():
    os.system("cls")
    vid=input("Digite a Matricula do registro a ser alterado: ")
    r=consultar(vcon, "SELECT * FROM tb_alunos WHERE N_MATRICULA="+vid)
    rnome=r[0][1]
    rcpf=[0][2]
    ravaliacao=[0][3]
    vnome=input("Digite o nome: ")
    vcpf=input("Digite o cpf: ")
    vavaliacao=input("Digite a avaliacao:")
    if(len(vnome)==0):
        vnome=rnome
    if(len(vcpf)==0):
        vcpf=rcpf
    if(len(vavaliacao)==0):
        vavaliacao=ravaliacao
    vsql="UPDATE tb_alunos SET T_NOME='"+vnome+"', T_CPF='"+vcpf+"', T_AVALIACAO='"+vavaliacao+"' WHERE N_MATRICULA="+vid
    query(vcon,vsql)

def menuConsultar():
    vsql="SELECT * FROM tb_alunos"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:
        print("Matricula:{0:_<3} Nome:{1:_<40} Cpf:{2:_<11} Avaliacao:{3:_<10}". format(r[0], r[1], r[2], r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont=0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("Pause")

def menuConsultarNomes():
    vnome=input("Digite o nome: ")
    vsql = "SELECT * FROM tb_alunos WHERE T_NOME LIKE '%"+vnome+"%'"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print("Matricula:{0:_<3} Nome:{1:_<40} Cpf:{2:_<11} Avaliacao:{3:_<10}".format(r[0], r[1], r[2], r[3]))
        vcont += 1
        if (vcont >= vlim):
            vcont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("Pause")

opc=0
while opc !=6:
    menuPrincipal()
    opc=int(input("Digite uma opcao: "))
    if  opc==1:
        menuInserir()
    elif opc==2:
        menuDeletar()
    elif opc==3:
        menuAtualizar()
    elif opc==4:
        menuConsultar()
    elif opc==5:
        menuConsultarNomes()
    elif opc==6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("opcao invalida")
        os.system("pause")

vcon.close()
os.system("pause")