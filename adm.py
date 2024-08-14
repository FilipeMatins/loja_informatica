from classes import *
from cor import *
import os

def Adicionar_itens(produtos):
    _nome_produto = input(f"{RESET}Informe o nome do produto: ")
    _quantidade = input("Informe quantidade:  ")
    _valor_produto = float(input("Digite o valor: "))
    add_item = Produtos(_nome_produto,_valor_produto, _quantidade)
    produtos.append(add_item)
    Produtos.salva_produto(_nome_produto,_valor_produto, _quantidade)
    
def editar_produto(produtos):
    os.system("cls")
    Produtos.lista_produto(produtos)
    while True:
        p = int(input('Digite o código do produto para editar: '))-1
        if p >= len(produtos) or p <= -1:
            os.system("cls")
            Produtos.lista_produto(produtos)
            red('> Código do produto inválido\n')
        else:
            break
    Produtos.editar_produto(p, produtos)

def deletar_produto(produtos):
    os.system("cls")
    Produtos.lista_produto(produtos)
    while True:
        p = int(input('Digite o código do produto para deletar: '))-1
        if p >= len(produtos) or p <= -1:
            os.system("cls")
            Produtos.lista_produto(produtos)
            red('> Código do produto inválido\n')
        else:
            break
    os.system('cls')
    green(f"> Produto {BLUE}{produtos[p].nome_produto}{GREEN} deletado com sucesso!")
    Produtos.delete_prod_lista(p, produtos)
