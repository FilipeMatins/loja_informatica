from cor import *
import os

def login():
    yellow('\n>>> MENU PRINCIPAL <<<')
    print(f'{YELLOW}1{RESET} - Cliente')
    print(f'{YELLOW}2{RESET} - ADM')
    print(f'{YELLOW}0{RESET} - SAIR\n')

def menu_loja():
    cyan('>>> MENU DA LOJA <<<')
    print(f'{YELLOW}1{RESET} - Listar Produtos')
    print(f'{YELLOW}2{RESET} - Adicionar Produto')
    print(f'{YELLOW}3{RESET} - Remover Produto')
    print(f'{YELLOW}4{RESET} - Ver Carrinho\n')
    print(f'{YELLOW}5{RESET} - Confirmar Comprar')
    print(f'{YELLOW}0{RESET} - Voltar\n')

def menu_adm():
    purple('>>> MENU ADMINISTRADOR <<<')
    print(f'{YELLOW}1{RESET} - Listar Produtos')
    print(f'{YELLOW}2{RESET} - Adicionar Produto')
    print(f'{YELLOW}3{RESET} - Editar Produto')
    print(f'{YELLOW}4{RESET} - Deletar Produto')
    print(f'{YELLOW}0{RESET} - Voltar\n')

def limpa_tela():
    os.system('cls')