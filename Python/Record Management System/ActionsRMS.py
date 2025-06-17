from os import system
import InputRMS
import ScreensRMS



def addRecord():
    system("cls")
    
    print("=" * 30)
    print("\n       ADDING RECORD/S\n")
    print("=" * 30, "\n\n")
    
    while True:
        try:
            no_of_inputs = int(input("\033[1A\033[K Enter input amount: "))

            if no_of_inputs <= 0:
                ScreensRMS.errorMessage()
            else:
                break
        except:
            ScreensRMS.errorMessage()

    for i in range(1, no_of_inputs + 1):
        system("cls")
        
        print("=" * 30)
        print("\n       ADDING RECORD/S\n")
        print("=" * 30)
        print(f"\n         INPUT {i} of {no_of_inputs}\n")
        print("=" * 30, "\n")
        
        new_record = InputRMS.mainInput()
        
        InputRMS.record_list.append(new_record)
    
    system("cls")
    
    print("=" * 30)
    print("\n  SUCCESSFULLY ADDED RECORD\n")
    print("=" * 30, "\n\n")
    
    while True:
        view_prompt = input("\033[1A\033[K View the records? [Y/N]: ")
        
        if view_prompt.upper() in "YN" and len(view_prompt) == 1:
            break
        else:
            ScreensRMS.errorMessage()
            
    if view_prompt in "Yy":
        viewRecord()



def editRecord():
    viewRecord()

    if len(InputRMS.record_list) != 0:
        system("cls")
    
        print("=" * 30)
        print("\n       EDITING A RECORD\n")
        print("=" * 30, "\n\n")
        
        while True:
            try:
                rec_num = int(input("\033[1A\033[K Enter record number: "))

                if rec_num > len(InputRMS.record_list) or rec_num <= 0:
                    ScreensRMS.errorMessage()
                else:
                    break
                
            except:
                ScreensRMS.errorMessage()

        print("\n" + "=" * 30, "\n")
        
        new_record = InputRMS.mainInput()
        
        InputRMS.record_list[rec_num - 1] = new_record

        system("cls")
    
        print("=" * 30)
        print("\n SUCCESSFULLY EDITED RECORD\n")
        print("=" * 30, "\n\n")
        
        while True:
            view_prompt = input("\033[1A\033[K View the records? [Y/N]: ")
            
            if view_prompt.upper() in "YN" and len(view_prompt) == 1:
                break
            else:
                ScreensRMS.errorMessage()
                
        if view_prompt in "Yy":
            viewRecord()
            
            

def viewRecord():
    system("cls")
    
    print("=" * 30)
    print("\n        RECORD DATABASE\n")
    print("=" * 30)

    if len(InputRMS.record_list) == 0:
        print("\n        WOW SUCH EMPTY\n")
        print("=" * 30, "\n")
    else:
        for rec in InputRMS.record_list:
            print(f"\n          RECORD # {InputRMS.record_list.index(rec) + 1}")
            
            for data in rec:
                print(f" {data}: {rec[data]}")
                
            if InputRMS.record_list.index(rec) != len(InputRMS.record_list) - 1:
                print("\n" + "-" * 30)
            
        print("\n" + "=" * 30, "\n")

    system("pause")



def deleteRecord():
    viewRecord()

    if len(InputRMS.record_list) != 0:
        system("cls")
    
        print("=" * 30)
        print("\n       DELETING A RECORD\n")
        print("=" * 30, "\n\n")
        
        while True:
            try:
                rec_num = int(input("\033[1A\033[K Enter record number: "))

                if rec_num > len(InputRMS.record_list) or rec_num <= 0:
                    ScreensRMS.errorMessage()
                else:
                    break
                
            except:
                ScreensRMS.errorMessage()

        del InputRMS.record_list[rec_num - 1]

        system("cls")
    
        print("=" * 30)
        print("\n SUCCESSFULLY DELETED RECORD\n")
        print("=" * 30, "\n\n")
        
        while True:
            view_prompt = input("\033[1A\033[K View the records? [Y/N]: ")
            
            if view_prompt.upper() in "YN" and len(view_prompt) == 1:
                break
            else:
                ScreensRMS.errorMessage()
                
        if view_prompt in "Yy":
            viewRecord()