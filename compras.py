from menu import *
from classes import *
from time import sleep
carrinho = []
op = 's'
while op.upper() !='N':
    lista_produtos()
    print('Escolha seu produto:')
    cod_pro = int(input('Código do produto: '))
    qtd = int(input('Quantidade: '))
    prod = 
    item = Item(qtd, prod, valor_unit, valor_total)
    carrinho.append(item)
    op = input('Deseja continuar (s/n): ')
print(50*'-')
print('         Carrinho de compras:')
print(50*'-')
for item in carrinho:
    print(f'{item.quantidade} - {item.descricao}')


