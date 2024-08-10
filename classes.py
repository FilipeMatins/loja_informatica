from cor import *

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

    def editar_produto(self,new_nome,new_preco,new_quantidade,):
        self.nome_produto = new_nome
        self.preco = new_preco
        self.quantidade_estoque = new_quantidade
            
    def lista_produtos(produtos):
        cod = 1
        green('CÓDIGO  QT. EST.  PRODUTO                 PREÇO')
        print(50*'-')
        for p in produtos:
            print(f'{BLUE}{cod:^7}{RESET} {p.quantidade_estoque:^9} {p.nome_produto:<23} R$ {float(p.preco):.2f}')
            cod += 1
        print('\n')

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
    
    

