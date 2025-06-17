from os import system
from time import sleep
from random import uniform, randint
from sys import stdout
from string import *
from colorama import Fore, Back, Style, init

init(autoreset = True)



def main(): # Main Function
    mainScreen() # Main Menu
    choice = actionChoice() # Action Choice Input
    actionChecker(choice) # Action Choice Checker
    useAgain() # Use Program Again Prompt

def mainScreen(): # Main Menu
    startupScreen() # Startup Loading Screen

    system("cls")
    
    print(Fore.RESET + "-" * 30)
    print(Fore.MAGENTA + Style.BRIGHT + "\n     THE SORTING MACHINE\n") 
    print("-" * 30)
    sleep(0.25)
    print(Fore.RED + Style.BRIGHT + "\n1. Number Sorter (User Input)")
    sleep(0.1)
    print(Fore.YELLOW + Style.BRIGHT + "2. Number Sorter (Random Generated Numbers)")
    sleep(0.1)
    print(Fore.GREEN + Style.BRIGHT + "3. String Sorter (User Input)")
    sleep(0.1)
    print(Fore.BLUE + Style.BRIGHT + "4. Exit")
    sleep(0.25)
    print("\n" + "-" * 30, "\n")
    sleep(0.25)

def actionChoice(): # Action Choice
    while True: # Choice Input
        try:
            action = int(input(Fore.CYAN + Style.BRIGHT + "Pick an action [1-4]: "))
        
            if action < 1 or action > 4:
                errorScreen() # Error Message
            else:
                break
        except:
            errorScreen() # Error Message
    
    return action

def actionChecker(act): # Action Choice Checker
    loadingScreen() # Proceeding Loading Screen

    if act == 1:
        numberSorter() # Number Sorter (User Input) Main Machinery
    elif act == 2:
        randomNumberSorter() # Number Sorter (Random Input) Main Machinery
    elif act == 3:
        stringSorter() # String Sorter (User Input) Main Machinery
    elif act == 4:
        exitScreen() # Exit Program Screen

def numberSorter(): # Number Sorter (User Input) Main Machinery
    temp = 1
    listahan = []

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.RED + Style.BRIGHT + "\n       THE NUMBER SORTER\n")
    print("-" * 30 + "\n")
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "      Specify List Length\n")
    sleep(0.25)

    while True: # List Length Input
        try:
            list_range = int(input(Fore.CYAN + Style.DIM + "Enter the amount of numbers to be sorted: "))

            if list_range > 0:
                break
            else:
                errorScreen() # Error Message
        except:
            errorScreen() # Error Message

    sleep(0.5)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.RED + Style.BRIGHT + "\n       THE NUMBER SORTER\n")
    print("-" * 30 + "\n")
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "      Add Numbers to List\n")
    sleep(0.25)

    while temp <= list_range: # List Items Input
        try:
            num = float(input(Fore.CYAN + Style.DIM + f"[{temp}] Enter number: "))
            
            listahan.append(num)

            temp += 1
        except:
            errorScreen() # Error Message

    generatingScreen(list_range)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.RED + Style.BRIGHT + "\n       THE NUMBER SORTER\n") # Temporary Output Screen
    print("-" * 30, "\n")
    sleep(0.25)
    print(Fore.RED + " Generated List: ", listahan)
    sleep(0.25)
    print("\n" + "-" * 30 + "\n")

    sleep(0.5)

    for sec in reversed(range(1,6)):
        sleep(1)
        stdout.write(Fore.YELLOW + f"\r   PROCEEDING TO SORTER IN {sec}")

    sortingScreen(list_range) # Sorting Loading Screen

    sorted_list = sorted(listahan)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.RED + Style.BRIGHT + "\n       THE NUMBER SORTER\n") # Final Output Display
    print("-" * 30, "\n")
    sleep(0.25)
    print(Fore.RED + " Input List: ", listahan)
    sleep(0.1)
    print(Fore.RED + Style.DIM + "\n Sorted List (Ascending): ", sorted_list)
    print(Fore.RED + Style.DIM + " Sorted List (Descending): ", sorted_list[::-1])
    sleep(0.25)
    print("\n" + "-" * 30 + "\n")

    sleep(1)
    
    system("pause")

    sleep(0.5)

def randomNumberSorter(): # Number Sorter (Random Input) Main Machinery
    choiceA = "Aa"
    choiceB = "Bb"
    rand_list = []

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.YELLOW + Style.BRIGHT + "\n     RANDOM NUMBER SORTER\n")
    print("-" * 30)
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "\n         Types of RNG\n")
    sleep(0.25)
    print(Fore.BLUE + "A. Integer Generator")
    sleep(0.1)
    print(Fore.MAGENTA + "B. Float Generator")
    sleep(0.25)
    print("\n" + "-" * 30 + "\n")
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "       Specify RNG Type\n")
    sleep(0.25)

    while True: # List Type Input
        rng_type = input(Fore.CYAN + Style.DIM + "Enter type choice [A/B]: ")

        if rng_type in choiceA or rng_type in choiceB:
            break
        else:
            errorScreen() # Error Message

    sleep(0.5)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.YELLOW + Style.BRIGHT + "\n     RANDOM NUMBER SORTER\n")
    print("-" * 30 + "\n")
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "      Specify List Length\n")
    sleep(0.25)

    while True: # List Length Input
        try:
            list_range = int(input(Fore.CYAN + Style.DIM + "Enter the amount of numbers to be sorted: "))

            if list_range > 0:
                break
            else:
                errorScreen() # Error Message
        except:
            errorScreen() # Error Message

    sleep(0.5)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.YELLOW + Style.BRIGHT + "\n     RANDOM NUMBER SORTER\n")
    sleep(0.25)
    print("-" * 30)
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "\n       Specify RNG Range\n")
    sleep(0.25)

    if rng_type in choiceA: 
        rand_list = randomIntGenerator(list_range) # Random Integer Generator

    elif rng_type in choiceB:
        rand_list_temp = randomFloatGenerator(list_range) # Random Float Generator
        rand_list = [round(rand_float, 2) for rand_float in rand_list_temp]

    generatingScreen(list_range)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.YELLOW + Style.BRIGHT + "\n     RANDOM NUMBER SORTER\n") # Temporary Output Screen
    print("-" * 30, "\n")
    sleep(0.25)
    print(Fore.YELLOW + " Generated List: ", rand_list)
    sleep(0.25)
    print("\n" + "-" * 30 + "\n")

    sleep(0.5)

    for sec in reversed(range(1,6)):
        sleep(1)
        stdout.write(Fore.YELLOW + f"\r   PROCEEDING TO SORTER IN {sec}")

    sortingScreen(list_range)

    sorted_list = sorted(rand_list)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.YELLOW + Style.BRIGHT + "\n     RANDOM NUMBER SORTER\n") # Final Output Screen
    print("-" * 30, "\n")
    sleep(0.25)
    print(Fore.YELLOW + " Generated List: ", rand_list)
    sleep(0.1)
    print(Fore.YELLOW + Style.DIM + "\n Sorted List (Ascending): ", sorted_list)
    print(Fore.YELLOW + Style.DIM + " Sorted List (Descending): ", sorted_list[::-1])
    sleep(0.25)
    print("\n" + "-" * 30 + "\n")

    sleep(1)
    
    system("pause")

    sleep(0.5)

def stringSorter(): # String Sorter (User Input) Main Machinery
    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.GREEN + Style.BRIGHT + "\n       THE STRING SORTER\n")
    print("-" * 30)
    sleep(0.25)
    print(Fore.CYAN + Style.BRIGHT + "\n     String to be Sorted\n")
    sleep(0.25)
    string_input = input(Fore.CYAN + Style.DIM + "Enter string: ")

    string_length = len(string_input)

    sortingScreen(string_length)

    remove_punctuations = string_input.translate(str.maketrans('', '', punctuation))
    string_to_list = remove_punctuations.split()
    word_list = [word for word in string_to_list if word.isalnum()]
    words_case_sensitive = sorted(word_list)
    words_case_insensitive = sorted(word_list, key=str.casefold)
    words_by_length = sorted(word_list, key=len)

    system("cls")

    print(Fore.RESET + "-" * 30)
    print(Fore.GREEN + Style.BRIGHT + "\n       THE STRING SORTER\n") # Final Output Display
    print("-" * 30, "\n")
    sleep(0.25)
    print(Fore.RED + Style.BRIGHT + "       Sorting By Words\n")
    sleep(0.25)
    print(Fore.RED + f" String Input: {string_input}\n")
    sleep(0.1)
    print(Fore.RED + f" Total Words Used: {len(word_list)}")
    print(Fore.RED + f" Words Used: {word_list}\n")
    sleep(0.1)
    print(Fore.RED + "     Sorting Alphabetically")
    print(Fore.RED + Style.DIM + "     Case-sensitive")
    print(Fore.RED + Style.DIM + f" Ascending: {words_case_sensitive}")
    print(Fore.RED + Style.DIM + f" Descending: {words_case_sensitive[::-1]}\n")
    sleep(0.1)
    print(Fore.RED + Style.DIM + "     Case-insensitive")
    print(Fore.RED + Style.DIM + f" Ascending: {words_case_insensitive}")
    print(Fore.RED + Style.DIM + f" Descending: {words_case_insensitive[::-1]}\n")
    sleep(0.1)
    print(Fore.RED + "        Sorting by Length")
    print(Fore.RED + Style.DIM + f" Ascending: {words_by_length}")
    print(Fore.RED + Style.DIM + f" Descending: {words_by_length[::-1]}")
    sleep(0.25)

    string_to_letters = [letter for letter in string_input if letter.isalpha()]
    total_letters = len(string_to_letters)
    lower_case = dict(zip(ascii_lowercase, [0]*26))
    upper_case = dict(zip(ascii_uppercase, [0]*26))

    for letter in string_to_letters:
        for item in lower_case:
            if letter == item:
                lower_case[item] += 1

        for item in upper_case:
            if letter == item:
                upper_case[item] += 1

    string_to_numbers = [letter for letter in string_input if letter.isnumeric()]
    total_numbers = len(string_to_numbers)
    number_list = dict(zip(digits, [0]*10))

    for number in string_to_numbers:
        for item in number_list:
            if number == item:
                number_list[item] += 1

    print("\n" + "-" * 30 + "\n")
    sleep(0.25)
    print(Fore.YELLOW + Style.BRIGHT + "       Letter & Numbers\n")
    sleep(0.25)
    print(Fore.YELLOW + f" Total Letters Used: {total_letters}\n")
    
    for (ucl, ucv), (lcl, lcv) in zip(upper_case.items(), lower_case.items()):
        if (ucv + lcv) != 0:
            sleep(0.1)
            print(Fore.YELLOW + Style.DIM + f"      {ucl}:{ucv}   {lcl}:{lcv}   Total:{ucv + lcv}")

    sleep(0.25)
    print(Fore.YELLOW + f"\n Total Numbers Used: {total_numbers}\n")

    for (nu, nv) in number_list.items():
        sleep(0.1)

        if nv != 0:
            print(Fore.YELLOW + Style.DIM + f"\t{nu} : {nv}")

    string_to_punctuations = [mark for mark in string_input if not mark.isalnum()]
    total_punctuation = len(string_to_punctuations)
    punctuation_list = dict(zip(punctuation, [0]*32))
    punctuation_list[" "] = 0

    for mark in string_to_punctuations:
        for item in punctuation_list:
            if mark == item:
                punctuation_list[item] += 1

    sleep(0.25)
    print("\n" + "-" * 30 + "\n")
    sleep(0.25)
    print(Fore.BLUE + Style.BRIGHT + "Punctuations & Special Characters\n")
    sleep(0.25)
    print(Fore.BLUE + f" Total Punctuations Used: {total_punctuation}\n")

    for (pm, pv) in punctuation_list.items():
        sleep(0.1)

        if pv != 0:
            if pm == " ":    
                print(Fore.BLUE + Style.DIM + f"\t[space] : {pv}")
            else:
                print(Fore.BLUE + Style.DIM + f"\t{pm} : {pv}")
    
    sleep(0.25)
    print("\n" + "-" * 30 + "\n")

    sleep(1)
    
    system("pause")

    sleep(0.5)

def randomIntGenerator(length): # Random Integer Generator
    temp_list = []

    while True: # RNG Range Starting Point Input
        try:
            range1 = int(input(Fore.CYAN + Style.DIM + "Enter starting point: "))

            break
        except:
            errorScreen() # Error Message

    while True: # RNG Range Stopping Point Input
        try:
            range2 = int(input(Fore.CYAN + Style.DIM + "Enter stopping point: "))

            if range2 <= range1:
                errorScreen() # Error Message
            else:
                break
        except:
            errorScreen() # Error Message

    for n in range(0, length): # List Items Input
        rand_int = randint(range1, range2)
        temp_list.append(rand_int)

    return temp_list

def randomFloatGenerator(length): # Random Integer Generator
    temp_list = []

    while True: # RNG Range Starting Point Input
        try:
            range1 = float(input(Fore.CYAN + Style.DIM + "Enter starting point: "))

            break
        except:
            errorScreen() # Error Message

    while True: # RNG Range Stopping Point Input
        try:
            range2 = float(input(Fore.CYAN + Style.DIM + "Enter stopping point: "))

            if range2 <= range1:
                errorScreen() # Error Message
            else:
                break
        except:
            errorScreen() # Error Message

    for n in range(0, length): # List Items Input
        rand_float = uniform(range1, range2)
        temp_list.append(rand_float)

    return temp_list

def useAgain(): # Use Program Again Prompt
    again_flag = 0

    system("cls")

    print(Fore.RESET + "-" * 30 + "\n")
    print(Fore.MAGENTA + Style.BRIGHT + "Use THE SORTING MACHINE Again?")
    print("\n" + "-" * 30 + "\n")
    
    while again_flag == 0: # Choice Input
        again = input(Fore.CYAN + Style.BRIGHT + "Enter Choice [Y/N]: ")

        if again == "y" or again == "Y":
            again_flag = 1

            main() # Main Function
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
        sleep(0.0375)
        stdout.write(Fore.YELLOW + f"\r\tPREPARING SORTING PROGRAMS [{percent}%]")
    
    sleep(0.5)

def loadingScreen(): # Proceeding Loading Screen
    sleep(0.5)

    system("cls")

    print("\n\n")

    for sec in reversed(range(1,4)):
        sleep(1)
        stdout.write(Fore.YELLOW + f"\r\tPROCEEDING IN {sec}")

    sleep(0.5)

def sortingScreen(items): # Sorting Loading Screen
    sleep(0.5)

    system("cls")

    print("\n\n")

    for sec in range(0, items + 1):
        sleep(0.075)
        stdout.write(Fore.YELLOW + f"\r\tSORTING ITEMS [{sec}/{items}]")

    sleep(0.5)

def generatingScreen(items): # list Generating Loading Screen
    sleep(0.5)

    system("cls")

    print("\n\n")

    for sec in range(0, items + 1):
        sleep(0.075)
        stdout.write(Fore.YELLOW + f"\r\tGENERATING LIST OF ITEMS [{sec}/{items}]")

    sleep(0.5)

def exitScreen(): # Exit Program Screen
    system("cls")

    print(Fore.RESET + "-" * 30 + "\n")
    print(Fore.MAGENTA + Style.BRIGHT + "     THE SORTING MACHINE\n")
    print("-" * 30 + "\n")
    sleep(0.5)
    print(Fore.MAGENTA + " By: The Bocchinator\n")
    sleep(0.5)
    print("-" * 30 + "\n")
    sleep(0.5)
    print(Fore.CYAN + "Thank You For Using THE SORTING MACHINE\n")
    sleep(0.5)
    print("-" * 30 + "\n")
    sleep(1)
    system("pause")

    quit()

def errorScreen(): # Error Message
    print(Fore.RESET + "\n" + "-" * 30)
    print(Fore.RED + Style.BRIGHT + "\n\tINVALID INPUT!\n")
    print("-" * 30 + "\n")

    sleep(0.25)



main() # Call to Run Program