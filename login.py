from classes import *
from api import *
from menu import *

def login_cliente(clientes):
    limpa_tela()
    titulo('LOGIN', CYAN)
    u = input(f'Usuário: {CYAN}')
    s = input(f'{RESET}Senha: {CYAN}')
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
    titulo('CLIENTES CADASTRADOS', CYAN)
    cont = 1
    for c in clientes:
        print(f'{BLUE}{cont}°{RESET} - {c.nome}')
        cont += 1
    flag = input("\nTecle algo para sair-->")