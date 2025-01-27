#Asher Wangia, Random Password Generator
import random
import string

upper_char = (string.ascii_uppercase).split()
lower_char = (string.ascii_lowercase).split()
num_char = (string.digits).split()
special_char = (string.punctuation).split()

characters = []


password = []

def main():
    
    chars = int(input("How Many Characters In Length: "))

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
            for x in range(chars): 
                pass_generator()

            print("Here is your password:", password)

            exit()



def pass_generator():
    password.append(random.choice(characters)) 
       

    

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