from menu import *
from classes import *
from api import *
import time
import os

#           INICIAR COMPRA      #

def iniciar_compra(produtos, carrinho):
    op = 's'
    while op.upper() !='N':
        os.system("cls")
        Produtos.lista_produto(produtos)
        cyan('> Escolha seu produto na lista acima\n')
        while True:
            cod_pro = int(input(f'Código do produto: {BLUE}'))
            if cod_pro > len(produtos) or cod_pro < 1:
                limpa_tela()
                red('> Código do Produto Inválido\n')
                Produtos.lista_produto(produtos)
            else:
                break
        qtd = int(input(f'{RESET}Quantidade: {BLUE}'))
        while qtd > int(produtos[cod_pro-1].quantidade_estoque):
            red('> Quantidade solicitada não está disponível em estoque!!')
            qtd = int(input(f'Por favor, redefina a quantidade: {BLUE}'))
        prod = produtos[cod_pro-1].nome_produto
        valor_unit = produtos[cod_pro-1].preco
        item = Itens(prod, qtd, valor_unit)
        carrinho.append(item)
        q_est = int(produtos[cod_pro-1].quantidade_estoque)
        q_est -= qtd
        produtos[cod_pro-1].quantidade_estoque = q_est
        prod = {"estoque":produtos[cod_pro-1].quantidade_estoque}
        editar_produto_db(produtos[cod_pro-1].id, prod)
        op = input(f'{RESET}Deseja continuar (s/n): {BLUE}')
        if op != 'n':
            limpa_tela()
            green('> Produto adicionado no carrinho')
            time.sleep(1.5)
        
        else:
            limpa_tela()
            green('Carregando carrinho...')
            time.sleep(1)
        ver_carrinho(carrinho)

    return carrinho

            # FINALIZAR COMPRA #
def finalizar_compra(carrinho, nome):
    os.system("cls")
    if len(carrinho) == 0:
        green('> O carrinho ainda está vazio')
    else:
        total_carrinho = float(0)
        item_db = []
        for item in carrinho:
            n = item.nome_produto
            q = int(item.quantidade_produto)
            v = float(item.valor_produto)
            total_item = float(item.valor_produto)*float(item.quantidade_produto)
            item_db.append({"quantidade":q, "nome_produto":n, "valor":v})
            total_carrinho += total_item
        compra = {"tipo":"compra", "itens":item_db, "total":total_carrinho, "cliente":nome}
        salvar_compra(compra)
        
def ver_carrinho(carrinho):
    os.system("cls")
    if len(carrinho) == 0:
        green('> O carrinho ainda está vazio')
    else:
        print(f'{RESET}{50*'-'}')
        green('               CARRINHO DE COMPRAS:')
        print(50*'-')
        cyan('Item  Qtd. Produto                 Valor unit.  Valor Total')
        total_carrinho = float(0)
        i = 1
        for item in carrinho:
            total_item = float(item.valor_produto)*float(item.quantidade_produto)
            print(f'{i:<6}{item.quantidade_produto:<5}{item.nome_produto:<24} R$ {float(item.valor_produto):.2f}  R$ {total_item:.2f}')
            total_carrinho += total_item
            i +=1
        print(50*'-')
        green(f'VALOR TOTAL................................ R$ {total_carrinho:.2f}')

def deletar_item(carrinho, produtos):
    ver_carrinho(carrinho)
    if len(carrinho) != 0:
        while True:
            d = int(input('Escolha um item para deletar: '))
            if d > len(carrinho) or d <= -1:
                limpa_tela
                ver_carrinho(carrinho)
                red('\n> Item não encontrado no carrinho\n')
            else:
                break
        qtd = carrinho[d-1].quantidade_produto
        for p in produtos:
            if p.nome_produto == carrinho[d-1].nome_produto:
                estoque = int(p.quantidade_estoque)+int(qtd)
                id = p.id
                prod = {"estoque":estoque}
                editar_produto_db(id, prod)
                limpa_tela()
                green('\n> Produto Deletado')
                p.quantidade_estoque = estoque
        carrinho.pop(d-1)

def relatorio_vendas():
    busca_vendas()
    stop = input("Tecle algo para sair!")
