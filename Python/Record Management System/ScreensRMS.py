from os import system
from time import sleep



def mainScreen():
    system("cls")
    
    print("=" * 30)
    print("\n   RECORD MANAGEMENT SYSTEM\n")
    print("=" * 30)
    print("\n [ A ] - Add Record")
    print(" [ E ] - Edit Record")
    print(" [ V ] - View Record")
    print(" [ D ] - Delete Record")
    print(" [ X ] - Exit\n")
    print("=" * 30 + "\n\n")
    
    
    
def errorMessage():
    sleep(0.5)
    print("\033[1A\033[K        INVALID INPUT")
    sleep(1.25)