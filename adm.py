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
    p = int(input('Digite o código do produto para editar -->'))-1
    Produtos.editar_produto(p, produtos)
    os.system("cls")

def deletar_produto(produtos):
    os.system("cls")
    Produtos.lista_produto(produtos)
    p = int(input('Digite o código do produto para deletar -->'))-1
    Produtos.delete_prod_lista(p, produtos)
    print("Produto deletado com sucesso!")
