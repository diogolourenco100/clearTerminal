import os
import platform

def clear():
    operational_system = platform.system()

    if operational_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
