from menu import *
from compras import *
from classes import *
from adm import *
from api import *
from login import *
from time import sleep
import requests

#Busca de produtos banco de dados Firebase
produtos = []
carrinho = []
clientes = []
lista_prod = requests.get("https://loja-virtual-145-default-rtdb.firebaseio.com/.json")
lista_prod = lista_prod.json()
for k in lista_prod.keys():
    n = lista_prod[k]["produto"]
    p = lista_prod[k]["preco"]
    e = lista_prod[k]["estoque"]
    prod_atual = Produtos(n,p,e)
    prod_atual.id = k
    produtos.append(prod_atual)

def carregar_usuarios():
    url_users = "https://loja-senac-users-op-default-rtdb.firebaseio.com/.json"
    dbusers = requests.get(url_users)
    dbusers = dbusers.json()
    for k in dbusers.keys():
        if dbusers[k]["tipo"] == "c":
            n = dbusers[k]["nome"]
            u = dbusers[k]["usuario"]
            s = dbusers[k]["senha"]
            t = dbusers[k]["tipo"]
            cliente_atual = Cliente(n,u,s,t)
            cliente_atual.id = k
            clientes.append(cliente_atual)
    return clientes

clientes = carregar_usuarios()

os.system("cls")
while True:
    menu_principal()
    op = int(input(f'Escolha uma opção: {YELLOW}'))
    #FLUXO CLIENTE
    if op == 1:
        os.system("cls")
        log_cliente()
        esc = int(input(f'Escolha uma opção: {YELLOW}'))
        if esc == 1:
            resp = login_cliente(clientes)
            nome = resp[1]
            if resp[0] == False and nome == '':
                limpa_tela()
                red("> Usuário não cadastrado!")
                sleep(2)
                os.system("cls")
            while resp[0]:
                limpa_tela()
                while resp[0]:
                    menu_loja()
                    op_comprador = int(input(f'Escolha uma opção: {YELLOW}'))
                    #LISTAR PRODUTOS
                    if op_comprador == 1:
                        limpa_tela()
                        Produtos.lista_produto(produtos)
                    
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
                        finalizar_compra(carrinho, nome)
                        sleep(1)
                        os.system("cls")
                        carrinho.clear()

                    elif op_comprador == 0:
                        limpa_tela()
                        cyan('Voltando...')
                        time.sleep(1)
                        limpa_tela()
                        resp[0] = False
                        op = 99
                        break

                    else:
                        limpa_tela()
                        red('> Opção Inválida\n')
            if resp[0] == False:
                limpa_tela()
                red('> Usuário não cadastrado!!')


        elif esc == 2:
            cad_cliente()
            clientes.clear()
            clientes = carregar_usuarios()
            limpa_tela()
            green('> Conta criada com sucesso!')
            sleep(2)
            os.system("cls")

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
                Adicionar_itens(produtos)

            elif op_adm == 2:
                Produtos.lista_produto(produtos)

            elif op_adm == 3:
                editar_produto(produtos)

            elif op_adm == 4:
                deletar_produto(produtos)
                sleep(1)
                os.system("cls")
                Produtos.lista_produto(produtos)

            elif op_adm == 5:
                os.system("cls")
                relatorio_vendas()
                os.system("cls")

            elif op_adm == 6:
                os.system("cls")
                listar_clientes(clientes)
                os.system("cls")

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

