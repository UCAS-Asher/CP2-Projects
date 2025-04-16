#Asher Wangia, Random Password Generator
import random
import string

def pass_gen():
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
    def get_req():
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
            get_req()
        elif req == "2":
            lower()
            get_req()
        elif req == "3":
            numbers()
            get_req()
        elif req == "4":
            special()
            get_req()
        else:
            generator(length())
            pass_gen()
    def length():
        try:
            chars = int(input("How Many Characters In Length: "))
        except:
            print("Not a Number")
            length()

        return chars


    #This Function generates the random characters that will go in the password and combines them
    def generator(chars):
        
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

    print("""
    Password Genrator Choices
    1. Generate a Password
    2. Exit Program
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        get_req()
    elif choice == "2":
        print("Program End!")
    else:
        print("Not an Option!")
        pass_gen()
