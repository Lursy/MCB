import os


def install():
    null = '&>/dev/null'
    os.system(f'python3 -m pip install --upgrade pip {null}')
    try:
        import pyfiglet
    except ModuleNotFoundError:
        os.system(f'pip install pyfiglet {null}')
    try:
        import requests
    except ModuleNotFoundError:
        os.system(f'pip install requests {null}')
