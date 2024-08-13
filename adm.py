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
    while True:
        Produtos.lista_produtos(produtos)
        p = int(input(f'Digite o código do produto para editar: {BLUE}'))-1
        if p >= len(produtos) or p <= -1:
            os.system("cls")
            red('> Produto não encontrado\n')
        else:
            break
    Produtos.editar_produto(p, produtos)
    os.system("cls")
    green('> Produto alterado com sucesso\n') 
# def listar():
#     for index_item in range(len(lista_produto)):
#         print(f"""{index_item}- Nome: {lista_produto[index_item].nome_produto}
# Quantidade {lista_produto[index_item].quantidade_produto}""")



# if cod_pro > 7 or cod_pro < 1:
# if d > len(carrinho) or d <= -1: