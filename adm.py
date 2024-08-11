from classes import *
import os

def Adicionar_itens(produtos):
    _nome_produto = input("Informe o nome do produto: ")
    _quantidade = input("Informe quantidade:  ")
    _valor_produto = float(input("Digite o valor: "))
    add_item = Produtos(_nome_produto,_valor_produto, _quantidade)
    produtos.append(add_item)
    Produtos.salva_produto(_nome_produto,_valor_produto, _quantidade)
def editar_produto(produtos):
    os.system("cls")
    Produtos.lista_produtos(produtos)
    p = int(input('Digite o código do produto para editar -->'))-1
    Produtos.editar_produto(p, produtos)
    os.system("cls")
# def listar():
#     for index_item in range(len(lista_produto)):
#         print(f"""{index_item}- Nome: {lista_produto[index_item].nome_produto}
# Quantidade {lista_produto[index_item].quantidade_produto}""")

