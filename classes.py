class Itens:
    nome_produto = ''
    quantidade_produto = ''
    valor_produto = float

    def __init__(self,nome_produto,quantidade_produto,valor_produto):
        self.nome_produto = nome_produto   
        self.quantidade_produto = quantidade_produto 
        self.valor_produto = valor_produto

class Produtos:
    nome_produto = ''
    preco = float
    quantidade_estoque = int

    def __init__(self,nome_produto,preco,quantidade_estoque):
        self.nome_produto = nome_produto
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

class Cliente:
    nome = ''

    def __init__(self,nome):
        self.nome = nome

class Admin:
    nome = ''
    codigo_adm = int

    def __init__(self,nome,codigo_adm):
        self.nome = nome
        self.codigo_adm = codigo_adm
    

