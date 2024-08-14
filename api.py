from classes import *
import requests
url = "https://loja-virtual-145-default-rtdb.firebaseio.com/"
url_users = "https://loja-senac-users-op-default-rtdb.firebaseio.com/"

def cria_produto(p):
    url1 = url+'.json'
    requests.post(url1, json=p)

def editar_produto_db(id, prod):
    url1 = url+id+'.json'
    requests.patch(url1, json=prod)

def delete_prod_db(id):
    url1 = url+id+'.json'
    requests.delete(url1)

def cad_cli_db(dados):
    url1 = url_users+'.json'
    requests.post(url1, json=dados)
    
def salvar_compra(compra):
    url1 = url_users+'.json'
    requests.post(url1, json=compra)

def busca_vendas():
    url1 = url_users+'.json'
    dbusers = requests.get(url1)
    dbusers = dbusers.json()
    tot_relat = float(0)
    for k in dbusers.keys():
        if dbusers[k]["tipo"] == "compra":
            print(f'Cliente: {dbusers[k]["cliente"]}')
            print('Qtd. Produto                 Vl. Unit.   Vl. Total')
            print(50*'-')
            tot_compra = float(0)
            for item in dbusers[k]["itens"]:
                tot_item = float(item["quantidade"])*float(item["valor"])
                print(f'{item["quantidade"]:^2} {item["nome_produto"]:<24} R$ {item["valor"]:.2f} R$ {tot_item:.2f}')
                tot_compra += float(tot_item)
            print(f'Total desta venda: R$ {tot_compra:.2f}')
            print(40*'-=')
            print()
            tot_relat = tot_relat + tot_compra
    print(50*'-')
    print(f'Total deste relatório........................ R$ {tot_relat:.2f}')
    print(50*'-')
