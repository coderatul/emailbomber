import os


def clear():
    """
    If the operating system is Windows, clear the screen using the cls command, otherwise clear the screen using the clear
    command
    """
    os.system('cls' if os.name == 'nt' else 'clear')