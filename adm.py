lista_produto = []

from classes import *

def Adicionar_produto():
    _nome_produto = input("Informe o nome do produto: ")
    _quantidade = input("Informe ")
    _valor_produto = float(input("Digite o valor: "))
    add_item = Itens(_nome_produto,_quantidade,_valor_produto)
    lista_produto.append(add_item)

