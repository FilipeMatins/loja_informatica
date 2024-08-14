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
        while True:
            Produtos.lista_produto(produtos)
            cyan('> Escolha seu produto na lista acima\n')
            cod_pro = int(input(f'Código do produto: {BLUE}'))
            if cod_pro > len(produtos) or cod_pro < 1:
                limpa_tela()
                red('> Código do Produto Inválido\n')
            else:
                break
        print(f'\n{BLUE}Produto Selecionado:{RESET} {produtos[cod_pro-1].nome_produto}')
        qtd = int(input(f'{RESET}Quantidade: {BLUE}'))
        while qtd <= -1 or qtd > int(produtos[cod_pro-1].quantidade_estoque):
            red('> Quantidade solicitada inválida!!')
            qtd = int(input(f'Por favor, redefina a quantidade: {BLUE}'))
        
        if qtd == 0:
            green('> Nenhum item adicionado')
        else: 
            prod = produtos[cod_pro-1].nome_produto
            valor_unit = produtos[cod_pro-1].preco
            item = Itens(prod, qtd, valor_unit)
            carrinho.append(item)
            q_est = int(produtos[cod_pro-1].quantidade_estoque)
            q_est -= qtd
            produtos[cod_pro-1].quantidade_estoque = q_est
            prod = {"estoque":produtos[cod_pro-1].quantidade_estoque}
            editar_produto_db(produtos[cod_pro-1].id, prod)
            limpa_tela()
            green('> Produto adicionado no carrinho\n')
            time.sleep(1.5)
        
        op = input(f'{RESET}Deseja continuar comprando (S/N): {BLUE}').lower()
        if op != 's':
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
        green("> Compra finalizada com sucesso!!!")
        
def ver_carrinho(carrinho):
    os.system("cls")
    if len(carrinho) == 0:
        green('> O carrinho ainda está vazio\n')
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
        green(f'VALOR TOTAL................................ R$ {total_carrinho:.2f}\n')

def deletar_item(carrinho, produtos):
    ver_carrinho(carrinho)
    if len(carrinho) != 0:
        while True:
            d = int(input('\nEscolha um item para deletar: '))
            if d > len(carrinho) or d <= 0:
                limpa_tela
                ver_carrinho(carrinho)
                red('\n> Item não encontrado no carrinho')
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
                print(f'{GREEN}> {BLUE}{carrinho[d-1].nome_produto} {GREEN}Deletado do carrinho\n{RESET}')
                p.quantidade_estoque = estoque
        carrinho.pop(d-1)

def relatorio_vendas():
    busca_vendas()
    stop = input("Tecle algo para sair!")
