from menu import *
from compras import *
from classes import *

#Busca de produtos no arquivo de texto
produtos = []
with open('lista_produtos.txt', 'r', encoding='utf-8') as list_prod:
    dados = list_prod.readlines()
    for i in range(0, len(dados), 3):
        n = dados[i].rstrip('\n')
        p = dados[i+1].rstrip('\n')
        q = dados[i+2].rstrip('\n')
        prod_atual = Produtos(n,p,q)
        produtos.append(prod_atual)
carrinho = []
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
            op_adm= int(input('Escolha uma opção: '))
            if op_adm == 1:
                #função
                pass
            elif op_adm == 2:
                #função
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

