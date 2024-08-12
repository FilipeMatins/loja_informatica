from classes import *
from api import *

def login_cliente(clientes):
    u = input('Usuário: ')
    s = input('Senha: ')
    flag = False
    n = ''
    for c in clientes:
        if u == c.usuario and s == c.senha:
            flag = True
            n = c.nome
    return [flag, n]
def cad_cliente():
    print("Dados para cadastro: ")
    n = input('Nome: ')
    u = input('Usuário: ')
    s = input('Senha: ')
    dados = {"nome":n, "usuario":u, "senha":s, "tipo":"c"}
    cad_cli_db(dados)
    
def listar_clientes(clientes):
    for c in clientes:
        print(c.nome)
    flag = input("Tecle algo para sair-->")