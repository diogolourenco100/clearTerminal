import os
import platform

def clear():
    sistema_operacional = platform.system()

    if sistema_operacional == 'Windows':
        os.system('cls')
    elif sistema_operacional == 'Linux':
        os.system('clear')
