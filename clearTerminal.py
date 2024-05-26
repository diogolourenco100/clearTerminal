import os
import platform

def clear():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    except Exception as e:
        pass
        try:
            if os_name == "Windows":
                os.system('clear')
            else:
                os.system('cls')
        except Exception as e:
            print(f'ERROR: {e}')
