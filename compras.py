from menu import *
from classes import *
from time import sleep
import os
def iniciar_compra(produtos):
    carrinho = []
    op = 's'
    while op.upper() !='N':
        os.system("cls")
        Produtos.lista_produtos(produtos)
        print('Escolha seu produto na lista acima')
        cod_pro = int(input('Código do produto: '))
        qtd = int(input('Quantidade: '))
        while qtd > int(produtos[cod_pro-1].quantidade_estoque):
            print('Quantidade solicitada não está disponível em estoque!!')
            qtd = int(input('Por favor, redefina a quantidade: '))
        prod = produtos[cod_pro-1].nome_produto
        valor_unit = produtos[cod_pro-1].preco
        item = Itens(prod, qtd, valor_unit)
        carrinho.append(item)
        q_est = int(produtos[cod_pro-1].quantidade_estoque)
        q_est -= qtd #Baixar a quantidade em estoque
        produtos[cod_pro-1].quantidade_estoque = q_est
        op = input('Deseja continuar (s/n): ')
    os.system("cls")
    print(50*'-')
    print('               Carrinho de Compras:')
    print(50*'-')
    print('Qtd. Produto                 Valor unit.  Valor Total')
    total_carrinho = float(0)
    for item in carrinho:
        total_item = float(item.valor_produto)*float(item.quantidade_produto)
        print(f'{item.quantidade_produto:<5}{item.nome_produto:<24} R$ {float(item.valor_produto):.2f}  R$ {total_item:.2f}')
        total_carrinho += total_item
    print(50*'-')
    print(f'Valor total................................ R$ {total_carrinho:.2f}')
