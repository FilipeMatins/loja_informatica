from cor import *
from api import *

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
        np = input(f"Produto: {produtos[p].nome_produto}\nDigite um novo nome ou <ENTER> para manter -->")
        pp = input(f"Preço atual R$ {produtos[p].preco}\nDigite um novo preço ou <ENTER> para manter -->")
        qe = input(f"Quantidade em estoque: {produtos[p].quantidade_estoque}\nDigite uma nova quantidade ou <ENTER> para manter -->")
        if np != '':
            produtos[p].nome_produto = np
        if pp != '':
            produtos[p].preco = float(pp)
        if qe != '':
            produtos[p].quantidade_estoque = int(qe)
        id = produtos[p].id
        produto_edit = {"produto":produtos[p].nome_produto, "preco":produtos[p].preco, "estoque":produtos[p].quantidade_estoque}
        editar_produto_db(id, produto_edit)             
    def lista_produtos(produtos):
        cod = 1
        green('CÓDIGO  QT. EST.  PRODUTO                 PREÇO')
        print(50*'-')
        for p in produtos:
            print(f'{BLUE}{cod:^7}{RESET} {p.quantidade_estoque:^9} {p.nome_produto:<23} R$ {float(p.preco):.2f}')
            cod += 1
        print('\n')

    def salva_produto(n,p,q):
        print(n, p, q)
        produto_atual = {"produto":n, "preco":p, "estoque":q}
        cria_produto(produto_atual)

class Cliente:
    nome: str
    usuario: str
    senha: str
    def __init__(self,nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha = senha

class Admin:
    nome: str
    usuario: str
    senha: str
    def __init__(self,nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha = senha

class Compra:
    itens: list
    valor:float
    cliente:Cliente
    def __init__(self, cliente, itens, valor):
        self.cliente = cliente
        self.itens = itens
        self.valor = valor
    
