lista_produto = []

from classes import *

def Adicionar_itens():
    _nome_produto = input("Informe o nome do produto: ")
    _quantidade = input("Informe quantidade:  ")
    _valor_produto = float(input("Digite o valor: "))
    add_item = Itens(_nome_produto,_quantidade,_valor_produto)
    lista_produto.append(add_item)

def listar():
    for index_item in range(len(lista_produto)):
        print(f"""{index_item}- Nome: {lista_produto[index_item].nome_produto}
Quantidade {lista_produto[index_item].quantidade_produto}""")

