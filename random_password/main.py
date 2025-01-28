#Asher Wangia, Random Password Generator
import random
import string

upper_char = (string.ascii_uppercase)
lower_char = (string.ascii_lowercase)
num_char = (string.digits)
special_char = (string.punctuation)

characters = []


password = []
password2 = []
password3 = []
password4 = []



#This function asks the user for the requirements
def main():
    

    while True:
        print("""
        Choose A Number for the Requirement
        1. Upper Case
        2. Lower Case
        3. Numbers
        4. Special Character
        5. Done""")
    
        req = input("What is your requirement: ")

        if req == "1":
            upper()
        elif req == "2":
            lower()
        elif req == "3":
            numbers()
        elif req == "4":
            special()
        else:
            pass_generator(int(input("How Many Characters In Length: ")))

            
            exit()



#This Function generates the random characters that will go in the password and combines them
def pass_generator(chars):
    
    characters_done = "".join(characters)
    
    for i in range(chars):
        random_char = random.choice(characters_done)
        password.append(random_char)
    print("Here is your password:", "".join(password))
        
    for i in range(chars):
        random_char = random.choice(characters_done)
        password2.append(random_char)
    print("Here is your password:", "".join(password2))
        
    for i in range(chars):
        random_char = random.choice(characters_done)
        password3.append(random_char)
    print("Here is your password:", "".join(password3))
    
    for i in range(chars):
        random_char = random.choice(characters_done)
        password4.append(random_char)
    print("Here is your password:", "".join(password4))
        
     
    

def upper():
    characters.append(upper_char)
    

def lower():
    characters.append(lower_char)
    

def numbers():
    characters.append(num_char)

def special():
    characters.append(special_char)

while True:
    main()