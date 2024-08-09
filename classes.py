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

    def editar_produto(self):
        new_nome = input("Digite o novo nome do produto: ")
        self.nome_produto = new_nome
        new_preco = float(input("Digite o novo preço do produto: "))
        self.preco = new_preco
    
    def lista_produtos(produtos):
        cod = 1
        print(50*'-')
        print('Código  Qt. Est.  Nome                  Preço')
        print(50*'-')
        for p in produtos:
            print(f'{cod:^7} {p.quantidade_estoque:^9} {p.nome_produto:<23} R$ {float(p.preco):.2f}')
            cod += 1

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
    
    

