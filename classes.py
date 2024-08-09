class Itens:
    nome_produto = ''
    quantidade_produto = ''
    valor_produto = float

    def __init__(self,nome_produto,quantidade_produto,valor_produto):
        nome_produto = nome_produto   
        quantidade_produto = quantidade_produto 
        valor_produto = valor_produto

class Produtos:
    nome_produto = ''
    preco = float
    quantidade_estoque = int

    def __init__(self,nome_produto,preco,quantidade_estoque):
        nome_produto = nome_produto
        preco = preco
        quantidade_estoque = quantidade_estoque

class Cliente:
    nome = ''

    def __init__(self,nome):
        nome = nome

class Admin:
    nome = ''
    codigo_adm = int

    def __init__(self,nome,codigo_adm):
        nome = nome
        codigo_adm = codigo_adm

