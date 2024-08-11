from classes import *
import requests
url = "https://loja-virtual-145-default-rtdb.firebaseio.com/"
def cria_produto(p):
    url1 = url+'.json'
    requests.post(url1, json=p)

def editar_produto_db(id, prod):
    url1 = url+id+'.json'
    requests.patch(url1, json=prod)
#Testar push