from cor import *
from api import *
import os

class Itens:
    nome_produto: str
    quantidade_produto: str
    valor_produto: float

    def __init__(self,nome_produto,quantidade_produto,valor_produto):
        self.nome_produto = nome_produto   
        self.quantidade_produto = quantidade_produto 
        self.valor_produto = valor_produto

class Produtos:
    nome_produto:str
    preco: float
    quantidade_estoque: int
    id:str

    def __init__(self,nome_produto,preco,quantidade_estoque):
        self.nome_produto = nome_produto
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def editar_produto(p, produtos):
        os.system('cls')
        np = input(f"{CYAN}Produto:{RESET} {produtos[p].nome_produto}\nDigite um novo nome ou <ENTER> para manter: ")
        pp = input(f"{CYAN}\nPreço atual:{RESET} R$ {produtos[p].preco}\nDigite um novo preço ou <ENTER> para manter: ")
        qe = input(f"{CYAN}\nQuantidade em estoque:{RESET} {produtos[p].quantidade_estoque}\nDigite uma nova quantidade ou <ENTER> para manter: ")
        if np != '':
            produtos[p].nome_produto = np
        if pp != '':
            produtos[p].preco = float(pp)
        if qe != '':
            produtos[p].quantidade_estoque = int(qe)
        id = produtos[p].id
        produto_edit = {"produto":produtos[p].nome_produto, "preco":produtos[p].preco, "estoque":produtos[p].quantidade_estoque}
        editar_produto_db(id, produto_edit)

    def lista_produto(produtos):
        cod = 1
        green('CÓDIGO  QT. EST.  PRODUTO                 PREÇO')
        print(50*'-')
        for p in produtos:
            print(f'{BLUE}{cod:^7}{RESET} {p.quantidade_estoque:^9} {p.nome_produto:<23} R$ {float(p.preco):.2f}')
            cod += 1
        print('\n')

    def salva_produto(n,p,q):
        os.system('cls')
        blue(f'NOME: {RESET}{n}')
        blue(f'PREÇO: {RESET}R$ {p}')
        blue(f'QUANTIDADE: {RESET}{q}')
        green('\n> Produto adicionado com sucesso\n')
        # print(n, p, q)
        produto_atual = {"produto":n, "preco":p, "estoque":q}
        cria_produto(produto_atual)

    def delete_prod_lista(p, produtos):
        id = produtos[p].id
        produtos.pop(p)
        delete_prod_db(id)

class Cliente:
    id:str
    nome: str
    usuario: str
    senha: str
    tipo:str
    def __init__(self, nome, usuario, senha, tipo):
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.tipo = tipo

class Admin:
    id:str
    nome: str
    usuario: str
    senha: str
    tipo:str
    def __init__(self, nome, usuario, senha, tipo):
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.tipo = tipo

class Compra:
    itens: list
    valor:float
    cliente:Cliente
    def __init__(self, cliente, itens, valor):
        self.cliente = cliente
        self.itens = itens
        self.valor = valor
    
