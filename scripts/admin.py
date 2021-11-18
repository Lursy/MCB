from ferramentas.functions import *
from ferramentas.menu import *
from threading import Thread
from requests import get
from time import sleep
from tqdm import tqdm

# definindo uma função para chamar no arquivo MCB.py como admin finder
def adminf():
    while True:
        # definindo variaveis globais por conta do comando exec()
        global url
        global headers
        global redirecionando
        global encontrados

        # Tratamento de url
        url = str(input(f'{az}URL: {ve}'))
        if 'http' not in url:
            url = 'http://' + url
        if '/' not in url[-1]:
            url = url + '/'
        headers = {'User-Agent': 'None'}
        verify = get(url, headers=headers).status_code
        if verify != 200:
            print(f'{ve}A url digitada não existe.')
            sleep(2)
            break

        # Definindo threads para deixar a "pesquisa" mais rápida
        threads()
        thrd = str(input(f'{am}//: {ve}')).casefold()
        if thrd == 's':
            break
        elif thrd == 'i':
            break
        elif thrd in '1^2^4^6^8^16':

            # configurando tamanho de cada laço para se ajustar a wordlist
            lista = lista2 = 887 // int(thrd)
            tamanho = {}
            encontrados = []
            redirecionando = []

            for c in range(0, int(thrd)):
                if c == 0:
                    tamanho[c] = [0, lista]
                else:
                    tamanho[c] = [lista, lista + lista2]
                    lista += lista2

            # Criando as funções deacordo com a quantidade de threads
            def busca(n):
                wordlist = open('wordlist.MCB', 'r').readlines()
                num = tamanho[n]
                for palavra in tqdm(wordlist[num[0]:num[1]]):
                    admin = url + palavra.rstrip().lstrip()
                    response = get(admin, headers=headers).status_code
                    if response == 200:
                        print(vd)
                        encontrados.append(admin)
                        with open('admin.txt', 'w') as file:
                            file.write(admin + '\n')
                    if response == 302:
                        redirecionando.append(admin)

            # Executando as funções com thread
            for c in range(0, int(thrd)):
                exec(f'''function{c} = Thread(target=busca, args=[c])
function{c}.start()''')

            # Esperando os threads acabarem para executar o resto do script
            for c in range(0, int(thrd)):
                exec(f'function{c}.join()')

            # mostrando resultados
            clear()
            print('Encontrado:')
            for site in encontrados:
                print(f'{vd}{site} > admin.txt')
                sleep(2)
            for site in redirecionando:
                print(f'{az}{site}')
                sleep(2)
            break
