from menu import *
from classes import *
from time import sleep
import os
def iniciar_compra():
    carrinho = []
    op = 's'
    while op.upper() !='N':
        os.system("cls")
        lista_produtos()
        print('Escolha seu produto na lista acima')
        cod_pro = int(input('Código do produto: '))
        qtd = int(input('Quantidade: '))
        while qtd > produtos[cod_pro-1].quantidade_estoque:
            print('Quantidade solicitada não está disponível em estoque!!')
            qtd = int(input('Por favor, redefina a quantidade: '))
        prod = produtos[cod_pro-1].nome_produto
        valor_unit = produtos[cod_pro-1].preco
        item = Itens(prod, qtd, valor_unit)
        carrinho.append(item)
        produtos[cod_pro-1].quantidade_estoque = produtos[cod_pro-1].quantidade_estoque - qtd #Baixar a quantidade em estoque
        op = input('Deseja continuar (s/n): ')
    os.system("cls")
    print(50*'-')
    print('         Carrinho de compras:')
    print(50*'-')
    print('Qtd. Produto                 Valor unit.      Valor Total')
    total_carrinho = float(0)
    for item in carrinho:
        print(f'{item.quantidade} - {item.nome} - R$ {item.preco}  R$ {item.preco*item.quantidade}')
        total_carrinho += item.preco*item.quantidade
    print(50*'-')
    print(f'Valor total........................... R$ {total_carrinho:.2f}')
