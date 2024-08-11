from menu import *
from compras import *
from classes import *
from adm import *
from api import *
import requests

#Busca de produtos no arquivo de texto
produtos = []
lista_prod = requests.get("https://loja-virtual-145-default-rtdb.firebaseio.com/.json")
lista_prod = lista_prod.json()
for k in lista_prod.keys():
    k
    n = lista_prod[k]["produto"]
    p = lista_prod[k]["preco"]
    e = lista_prod[k]["estoque"]
    prod_atual = Produtos(n,p,e)
    prod_atual.id = k
    produtos.append(prod_atual)
carrinho = []

limpa_tela()
while True:
    login()
    op = int(input(f'Escolha uma opção: {YELLOW}'))
    #FLUXO CLIENTE
    if op == 1:
        limpa_tela()
        while True:
            menu_loja()
            op_comprador = int(input(f'Escolha uma opção: {YELLOW}'))
            #LISTAR PRODUTOS
            if op_comprador == 1:
                limpa_tela()
                Produtos.lista_produtos(produtos)
            
            #ADICIONAR PRODUTOS
            elif op_comprador == 2:
                carrinho = iniciar_compra(produtos, carrinho)

            #DELETAR PRODUTO
            elif op_comprador == 3:
                deletar_item(carrinho, produtos)
                
            #VER CARRINHO
            elif op_comprador == 4:
                ver_carrinho(carrinho)

            #COMPRAR
            elif op_comprador == 5:
                pass

            elif op_comprador == 0:
                limpa_tela()
                cyan('Voltando...')
                time.sleep(1)
                limpa_tela()
                break

            else:
                limpa_tela()
                red('> Opção Inválida')

    #FLUXO ADM
    elif op == 2:
        limpa_tela()
        while True:
            menu_adm()
            op_adm= int(input(f'Escolha uma opção: {YELLOW}'))
            if op_adm == 1:
                limpa_tela()
                Produtos.lista_produtos(produtos)
            elif op_adm == 2:
                Adicionar_itens(produtos)
            elif op_adm == 3:
                editar_produto(produtos)
            elif op_adm == 4:
                pass
            elif op_adm == 0:
                limpa_tela()
                purple('Voltando...')
                time.sleep(1)
                limpa_tela()
                break

            else:
                limpa_tela()
                red('> Opção Inválida')

    elif op == 0:
        limpa_tela()
        green('Saindo...\nAté Breve')
        break
    
    else:
        limpa_tela()
        red('> Opção Inválida')

