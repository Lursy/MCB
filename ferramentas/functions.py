from pyfiglet import Figlet
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


figlet = Figlet()
