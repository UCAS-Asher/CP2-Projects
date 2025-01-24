#Asher Wangia, Random Password Generator
import random
import string

upper = (string.ascii_uppercase).split()
lower = (string.ascii_lowercase).split()
num = (string.digits).split()



password = ""

def main():
    
    chars = int(input("How Many Characters In Length: "))
    
    print("""
    Choose A Number for the Requirement
    1. Upper Case
    2. Lower Case
    3. Numbers
    4. Special Character
    5. Done""")
    
    req = input("What are your requirements: ")

    if req == "1":
        upper()
    elif req == "2":
        lower()
    elif req == "3":
        numbers()
    elif req == "4":
        special_char()
    else:
        print("Here is your Password: ",password)
        exit()


def upper():
    pass

def lower():
    pass

def numbers():
    pass

def special_char():
    pass

while True:
    main()