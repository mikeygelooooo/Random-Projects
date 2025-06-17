import ScreensRMS



class Person:
    def __init__(self, name, age, gender, address):
        self.name = {'Name': name}
        self.age = {'Age': age}
        self.gender = {'Gender': gender}
        self.address = {'Address': address}
        


record_list = []



def mainInput():
    name_input = nameInput()
    age_input = ageInput()
    gender_input = genderInput()
    address_input = addressInput()
    
    new_person = Person(name_input, age_input, gender_input, address_input)
    new_record = new_person.name | new_person.age | new_person.gender | new_person.address
    
    return new_record



def nameInput():
    name_input = input(" Enter name: ")

    return name_input.title()



def ageInput():
    print()
    
    while True:
        try:
            age_input = int(input("\033[1A\033[K Enter age: "))

            if age_input < 0:
                ScreensRMS.errorMessage()
            else:
                break
        except:
            ScreensRMS.errorMessage()
            
    return age_input



def genderInput():
    choices = ['m', 'male', 'f', 'female']
    male_choice = ['m', 'male']
    
    print()
    
    while True:
        gender_input = input("\033[1A\033[K Enter gender: ")

        if gender_input.lower() in choices:
            break
        else:
            ScreensRMS.errorMessage()

    if gender_input.lower() in male_choice:
        student_gender_input = 'Male'
    else:
        student_gender_input = 'Female'

    return student_gender_input



def addressInput():
    address_input = input(" Enter address: ")

    return address_input.title()