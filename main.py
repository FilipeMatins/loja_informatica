
#import *
from menu import *

# fluxo_principal()
while True:
    login()
    op = int(input('Escolha uma opção: '))
    if op == 1:
        limpa_tela()
        while True:
            menu_loja()
            op_comprador = int(input('Escolha uma opção: '))
            if op_comprador == 1:
                #função
                pass
            elif op_comprador == 2:
                #função
                pass
            elif op_comprador == 99:
                break
            else:
                print ('Opção Inválida')

    elif op == 2:
        while True:
            #menu_adm()
            op_adm= int(input('Escolha uma opção: '))
            if op_adm == 1:
                #função
                pass
            elif op_adm == 2:
                #função
                pass
            elif op_adm == 99:
                break
            else:
                print ('opção Inválida')
    
    else:
        break

