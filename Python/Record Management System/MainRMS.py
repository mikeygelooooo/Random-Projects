from os import system
import ActionsRMS
import ScreensRMS



def main():
    ScreensRMS.mainScreen()

    while True:
        choice = input("\033[1A\033[K Choice: ")

        if choice.upper() in "AEVDX" and len(choice) == 1:
            break
        else:
            ScreensRMS.errorMessage()

    if choice in "aA":
        ActionsRMS.addRecord()
    elif choice in "eE":
        ActionsRMS.editRecord()
    elif choice in "vV":
        ActionsRMS.viewRecord()
    elif choice in "dD":
        ActionsRMS.deleteRecord()
    elif choice in "xX":
        exitProgram()

    main()



def exitProgram():
    system("cls")
    
    print("=" * 30)
    print("\n       EXITING PROGAM\n")
    print("=" * 30, "\n\n")
    
    while True:
        exit_prompt = input("\033[1A\033[K Are you sure? [Y/N]: ")

        if exit_prompt.upper() in "YN" and len(exit_prompt) == 1:
            break
        else:
            ScreensRMS.errorMessage()

    if exit_prompt in "yY":
        print("\n" + "=" * 30, "\n")
        quit("      THANK YOU FOR USING\n THE RECORD MANAGEMENT SYSTEM\n")
    elif exit_prompt in "nN":
        pass
    
    
    
main()