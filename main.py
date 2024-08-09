<<<<<<< HEAD
#import *

=======
from menu import *
>>>>>>> 1820e7113986ec64a941ef3055440a35d4eae5f8
# fluxo_principal()
while True:
    login()
    op = int(input('Escolha uma opção: '))
    if op == 1:
        while True:
            #menu_adm()
            op_adm = int(input('Escolha uma opção: '))
            if op_adm == 1:
                #função
                pass
            elif op_adm == 2:
                #função
                pass
            elif op_adm == 99:
                break
            else:
                print ('Opção Inválida')

    elif op == 2:
        while True:
            #menu_comprador()
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

