#ESSE ARQUIVO SERVE PARA COLORIR UM TEXTO

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
PURPLE = '\033[35m'
RESET = '\033[0m'


#COLOQUE O TEXTO NO ENTRE AS CONSTANTES PARA COLORIR

def red(txt):
    print(f'{RED}{txt}{RESET}')

def green(txt):
    print(f'{GREEN}{txt}{RESET}')

def blue(txt):
    print(f'{BLUE}{txt}{RESET}')

def yellow(txt):
    print(f'{YELLOW}{txt}{RESET}')

def cyan(txt):
    print(f'{CYAN}{txt}{RESET}')

def purple(txt):
    print(f'{PURPLE}{txt}{RESET}')