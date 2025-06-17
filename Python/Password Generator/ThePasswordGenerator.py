from os import system
from time import sleep
from sys import stdout
from string import *
from random import choice
from colorama import Fore, Back, Style, init

init(autoreset = True)



def compile(): # Function Compilation
    mainScreen()
    action_choice = actionChoice()
    actionChecker(action_choice)
    


def mainScreen(): # Main Menu Screen
    startupScreen() # Startup Loading Screen
    
    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "\n    THE PASSWORD GENERATOR\n")
    print("-" * 30 + "\n ")
    sleep(0.25)
    print(Fore.GREEN + Style.BRIGHT + " 1. Create a Password")
    sleep(0.1)
    print(Fore.YELLOW + Style.BRIGHT + " 2. Password Creation Info")
    sleep(0.1)
    print(Fore.RED + Style.BRIGHT + " 3. Exit\n")
    sleep(0.1)
    print("-" * 30)
    sleep(0.25)



def actionChoice(): # Action Choice
    while True: # Choice Input
        try:
            action = int(input(Fore.CYAN + Style.BRIGHT + "\nPick an action [1-3]: "))
        
            if action < 1 or action > 3:
                errorScreen() # Error Message
            else:
                break
        except:
            errorScreen() # Error Message
    
    return action



def actionChecker(act): # Action Choice Checker
    loadingScreen() # Proceeding Loading Screen

    if act == 1:
        passwordMachinery() # Password Generator Machinery
        useAgain() # Use Program Again Prompt
    elif act == 2:
        passwordCreationInfo() # Password Creation Info
    elif act == 3:
        exitScreen() # Exit Program Screen



def passwordMachinery(): # Password Generator Machinery
    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "\n    THE PASSWORD GENERATOR\n")
    print("-" * 30)
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "\n   Password Specifications")

    password_length = passwordLengthQuery() # Password Length Input Prompt
    with_numbers = withNumbersQuery() # Use Numbers Input Prompt
    with_punctuations = withPunctuationsQuery() # Use Punctuations Input Prompt
    
    loadingScreen() # Proceeding Loading Screen

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "\n    THE PASSWORD GENERATOR\n") # Temporary Input Display
    print("-" * 30)
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "\n   Password Specifications")
    sleep(0.1)
    print(Fore.CYAN + "\n Password Length: " + Fore.YELLOW + f"{password_length} characters")
    sleep(0.1)
    print(Fore.CYAN + "\n Numbers in Password: ", end = "")

    if with_numbers:
        print(Fore.GREEN + f"{with_numbers}")
    else:
        print(Fore.RED + f"{with_numbers}")

    sleep(0.1)
    print(Fore.CYAN + "\n Special Characters in Password: ", end = "")

    if with_punctuations:
        print(Fore.GREEN + f"{with_punctuations}")
    else:
        print(Fore.RED + f"{with_punctuations}")

    sleep(0.25)
    print("\n" + "-" * 30 + "\n")

    for sec in reversed(range(1,4)): # Proceeding Loading Prompt
        sleep(1)
        stdout.write(Fore.YELLOW + f"\r PROCEEDING TO GENERATOR IN {sec}")

    generatingScreen(password_length) # Generating Password Loading Screen

    generated_password = passwordGenerator(password_length, with_numbers, with_punctuations) # Password Generator Function

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "\n    THE PASSWORD GENERATOR\n") # Final Output Display
    print("-" * 30)
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "\n   Password Specifications")
    sleep(0.1)
    print(Fore.CYAN + "\n Password Length: " + Fore.YELLOW + f"{password_length} characters")
    sleep(0.1)
    print(Fore.CYAN + "\n Numbers in Password: ", end = "")

    if with_numbers:
        print(Fore.GREEN + f"{with_numbers}")
    else:
        print(Fore.RED + f"{with_numbers}")

    sleep(0.1)
    print(Fore.CYAN + "\n Special Characters in Password: ", end = "")

    if with_punctuations:
        print(Fore.GREEN + f"{with_punctuations}")
    else:
        print(Fore.RED + f"{with_punctuations}")

    sleep(0.25)
    print("\n" + "-" * 30 + "\n")
    sleep(0.25)
    print(Fore.MAGENTA + Style.DIM + " Generated Password: " + Fore.MAGENTA + Style.BRIGHT +  f"{generated_password}")
    sleep(0.25)
    print("\n" + "-" * 30 + "\n")

    sleep(1)
    
    system("pause")

    sleep(0.5)

    

def passwordLengthQuery(): # Password Length Input Prompt
    while True:
        try:
            length_input = int(input(Fore.CYAN + Style.NORMAL + "\nEnter Password Length: "))

            if length_input < 8:
                print(Fore.RED + "\nPASSWORD SHOULD BE MORE THAN 8 CHARACTERS!")
                errorScreen()
            elif length_input > 128:
                print(Fore.RED + "\nPASSWORD SHOULD BE LESS THAN 128 CHARACTERS!")
                errorScreen()
            else:
                break
        except:
            errorScreen() # Error Message

    return length_input



def withNumbersQuery(): # Use Numbers Input Prompt
    yes = "Yy"
    no = "Nn"

    while True:
        use_numbers = input(Fore.CYAN + Style.NORMAL + "\nUse Numbers in Password? [Y/N]: ") # Input

        if use_numbers in yes or use_numbers in no:
            break
        else:
            errorScreen() # Error Message

    if use_numbers in yes:
        return True
    else:
        return False



def withPunctuationsQuery(): # Use Punctuations Input Prompt
    yes = "Yy"
    no = "Nn"

    while True:
        use_punctuation = input(Fore.CYAN + Style.NORMAL + "\nUse Special Characters in Password? [Y/N]: ") # Input

        if use_punctuation in yes or use_punctuation in no:
            break
        else:
            errorScreen() # Error Message

    if use_punctuation in yes:
        return True
    else:
        return False



def passwordGenerator(length, numbers_bool, punctuations_bool): # Password Generator Function
    letters_list = ascii_letters
    numbers_list = digits
    punctuations_list = punctuation

    compilation = ""

    final_password = ""

    compilation += letters_list

    if numbers_bool:
        compilation += numbers_list

    if punctuations_bool:
        compilation += punctuations_list

    final_password += choice(letters_list)

    for item in range(1, length):
        final_password += choice(compilation)

    return final_password



def passwordCreationInfo(): # Password Creation Info
    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "\n    PASSWORD CREATION INFO\n")
    print("-" * 30)
    sleep(0.25)
    print(Fore.MAGENTA + Style.NORMAL + "\n - Passwords must be longer than 8 characters")
    sleep(0.1)
    print(Fore.RED + Style.NORMAL + "\n - Passwords have a 128-character limit")
    sleep(0.1)
    print(Fore.YELLOW + Style.NORMAL + "\n - Passwords must always start with a letter")
    sleep(0.1)
    print(Fore.GREEN + Style.NORMAL + "\n - Passwords should not include spaces")
    sleep(0.1)
    print(Fore. CYAN + Style.NORMAL + "\n - Passwords are a combination of:")
    sleep(0.1)
    print(Fore.CYAN + Style.DIM + "       > Uppercase & Lowercase Letters")
    sleep(0.05)
    print(Fore.CYAN + Style.DIM + "       > Numbers")
    sleep(0.05)
    print(Fore.CYAN + Style.DIM + "       > Special Characters / Punctuations")
    sleep(0.05)
    print(Fore.BLUE + Style.NORMAL + "\n - You have the option to include or not include the following:")
    sleep(0.1)
    print(Fore.BLUE + Style.DIM + "       > Numbers")
    sleep(0.05)
    print(Fore.BLUE + Style.DIM + "       > Special Characters / Punctuations\n")
    sleep(0.05)
    print("-" * 30 + "\n")
    
    sleep(0.25)

    system("pause")

    compile() # Call Program


def useAgain(): # Use Program Again Prompt
    again_flag = 0

    system("cls")

    print(Fore.RESET + "-" * 30 + "\n")
    print(Fore.MAGENTA + Style.BRIGHT + "Use THE PASSWORD GENERATOR Again?")
    print("\n" + "-" * 30 + "\n")
    sleep(0.25)
    
    while again_flag == 0: # Choice Input
        again = input(Fore.CYAN + Style.BRIGHT + "Enter Choice [Y/N]: ")

        if again == "y" or again == "Y":
            again_flag = 1

            compile() # Main Function
        elif again == "n" or again == "N":
            again_flag = 1

            loadingScreen() # Proceeding Loading Screen

            exitScreen() # Exit Program Screen
        else:
            errorScreen() # Error Message



def startupScreen(): # Startup Loading Screen
    sleep(0.5)

    system("cls")

    print("\n\n")

    for percent in range(0,101):
        sleep(0.00000001)
        stdout.write(Fore.YELLOW + f"\r\tPREPARING STRINGS [{percent}%]")

    system("cls")

    print("\n\n")

    for percent in range(0,101):
        sleep(0.00000001)
        stdout.write(Fore.YELLOW + f"\r\tPREPARING PASSWORD GENERATOR [{percent}%]")

    sleep(0.5)



def loadingScreen(): # Proceeding Loading Screen
    sleep(0.5)

    system("cls")

    print("\n\n")

    for sec in reversed(range(1,4)):
        sleep(1)
        stdout.write(Fore.YELLOW + f"\r\tPROCEEDING IN {sec}")

    sleep(0.5)



def generatingScreen(items): # Generating Password Loading Screen
    sleep(0.5)

    system("cls")

    print("\n\n")

    for sec in range(0, items + 1):
        sleep(0.05)
        stdout.write(Fore.YELLOW + f"\r\tGENERATING PASSWORD [{sec}/{items}]")

    sleep(0.5)



def exitScreen(): # Exit Program Screen
    system("cls")

    print(Fore.RESET + "-" * 30 + "\n")
    print(Fore.MAGENTA + Style.BRIGHT + "    THE PASSWORD GENERATOR\n")
    print("-" * 30 + "\n")
    sleep(0.5)
    print(Fore.MAGENTA + " By: The Bocchinator\n")
    sleep(0.5)
    print("-" * 30 + "\n")
    sleep(0.5)
    print(Fore.CYAN + "Thank You For Using THE PASSWORD GENERATOR\n")
    sleep(0.5)
    print("-" * 30 + "\n")
    sleep(1)
    system("pause")

    quit()



def errorScreen(): # Error Message
    print(Fore.RESET + "\n" + "-" * 30)
    print(Fore.RED + Style.BRIGHT + "\n\tINVALID INPUT!\n")
    print("-" * 30)

    sleep(0.25)

compile() # Call Program