from cor import *
import os

def login():
    yellow('>>> MENU PRINCIPAL <<<')
    print(f'{YELLOW}1{RESET} - Cliente')
    print(f'{YELLOW}2{RESET} - ADM')
    print(f'{YELLOW}0{RESET} - SAIR')

def menu_loja():
    yellow('>>> MENU PRODUTOS <<<')
    print(f'{YELLOW}1{RESET} - Listar Produtos')
    print(f'{YELLOW}2{RESET} - Adicionar Produto')
    print(f'{YELLOW}3{RESET} - Remover Produto')
    print(f'{YELLOW}4{RESET} - Ver Carrinho\n')
    print(f'{YELLOW}5{RESET} - Confirmar Comprar')
    print(f'{YELLOW}0{RESET} - Voltar')

def limpa_tela():
    os.system('cls')