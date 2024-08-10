lista_produto = []

from classes import *

def Adicionar_itens(produtos):
    _nome_produto = input("Informe o nome do produto: ")
    _quantidade = input("Informe quantidade:  ")
    _valor_produto = float(input("Digite o valor: "))
    add_item = Produtos(_nome_produto,_valor_produto, _quantidade)
    produtos.append(add_item)

# def listar():
#     for index_item in range(len(lista_produto)):
#         print(f"""{index_item}- Nome: {lista_produto[index_item].nome_produto}
# Quantidade {lista_produto[index_item].quantidade_produto}""")

