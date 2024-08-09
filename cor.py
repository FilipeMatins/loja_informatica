#ESSE ARQUIVO SERVE PARA COLORIR UM TEXTO

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
RESET = '\033[0m'

#COLOQUE O TEXTO NO MEIO ENTRE AS VARIAVEIS PARA COLORIR

def red(txt):
    print(f'{RED} {txt} {RESET}')

def green(txt):
    print(f'{GREEN}{txt}{RESET}')

def blue(txt):
    print(f'{BLUE}{txt}{RESET}')

def blue(txt):
    print(f'{YELLOW}{txt}{RESET}')