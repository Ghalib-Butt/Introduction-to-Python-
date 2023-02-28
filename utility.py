from time import sleep
from os import system
from keyboard import read_key

def clearTerminal():
    sleep(1)
    print("Thanks for using our services. Press any key to exit.")
    if read_key():
        system('clear')