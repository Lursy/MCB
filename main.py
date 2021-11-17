from ferramentas.menu import *
from ferramentas.install import *
from scripts.admin import *


while True:
    install()
    clear()
    menu()
    option = str(input(f'{am}//: '))
    if option == '1':
        adminf()
    elif option == '5':
        break
    else:
        print('Em manutenção')
