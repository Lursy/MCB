from ferramentas.cores import *
from ferramentas.functions import *


def menu():
    clear()
    options = ['Admin Finder', 'DoS', 'Exploit', 'Criador', 'Sair']
    print(az + figlet.renderText('Menu'))
    for c, item in enumerate(options):
        print(f'{vd}[ {c+1} ] {br}-{cy} {item}')


def threads():
    clear()
    print(rx + figlet.renderText('Threads'))
    print(f'{pt}{fbr}[i]{pb} Use deacordo com os núcleos do aparelho!\nUso não compativel pode causar travamentos no processo')
    options = {f'{cy}[ 1  ]': f'{br}-{vd}', f'{cy}[ 2  ]': f'{br}-{vd}',
               f'{cy}[ 4  ]': f'{br}-{am}', f'{cy}[ 6  ]': f'{br}-{am}',
               f'{cy}[ 8  ]': f'{br}-{ve}', f'{cy}[ 16 ]': f'{br}-{ve}',
               f'{cy}[ i  ]': f'{br}- informações', f'{cy}[ s  ]': f'{br}- Sair'}
    for key, value in options.items():
        print(f'{key} {value} Thread' if not 'i' in key and not 's' in key
              else f'{key} {value}')
