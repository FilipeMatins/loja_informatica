from cor import *
import os

def titulo(txt, cor):
    print(f'{RESET}-' * 42)
    print(f'{cor}{txt.center(42)}{RESET}')
    print('-' * 42)


def menu_principal():
    titulo('MENU PRINCIPAL', YELLOW)
    print(f'{YELLOW}1{RESET} - Cliente')
    print(f'{YELLOW}2{RESET} - ADM')
    print(f'{YELLOW}3{RESET} - LISTAR CLIENTES')
    print(f'{YELLOW}0{RESET} - SAIR')

def log_cliente():
    print(f'{YELLOW}1{RESET} - Login')
    print(f'{YELLOW}2{RESET} - Cadastro')

def menu_loja():
    cyan('\n>>> MENU DA LOJA <<<')
    print(f'{YELLOW}1{RESET} - Listar Produtos')
    print(f'{YELLOW}2{RESET} - Adicionar Produto')
    print(f'{YELLOW}3{RESET} - Remover Produto')
    print(f'{YELLOW}4{RESET} - Ver Carrinho')
    print(f'{YELLOW}5{RESET} - Confirmar Comprar')
    print(f'{YELLOW}0{RESET} - Voltar')

def menu_adm():
    titulo('MENU ADMINISTRADOR', PURPLE)
    print(f'{PURPLE}1{RESET} - Adicionar Produto')
    print(f'{PURPLE}2{RESET} - Listar Produtos')
    print(f'{PURPLE}3{RESET} - Editar Produto')
    print(f'{PURPLE}4{RESET} - Deletar Produto')
    print(f'{PURPLE}5{RESET} - Relatório de vendas')
    print(f'{PURPLE}0{RESET} - Voltar')

def menu_vendas():
    purple('\n>>> TIPO DE RELATÓRIO <<<')
    print(f'{YELLOW}1{RESET} - Por Vendas')
    print(f'{YELLOW}2{RESET} - Por Produtos')
def limpa_tela():
    os.system('cls')