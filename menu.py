from cor import *

def login():
    blue('>>> MENU PRINCIPAL <<<')
    print(f'{YELLOW}1{RESET} - Cliente')
    print(f'{YELLOW}2{RESET} - ADM')
    print(f'{YELLOW}0{RESET} - SAIR')

def menu_loja():
    print(f'{YELLOW}1{RESET} - Listar Produtos')
    print(f'{YELLOW}2{RESET} - Adicionar Produto')
    print(f'{YELLOW}3{RESET} - Remover Produto')
    print(f'{YELLOW}4{RESET} - Ver Carrinho')
    print(f'{YELLOW}5{RESET} - Confirmar Comprar')