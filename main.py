from toolsMCB.ferramentas.menu import *
from toolsMCB.ferramentas.install import *
from toolsMCB.scripts.admin import *


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
