#Asher Wangia, Battle Simulator
import csv

def display_characters():
    pass

def create():
    with open("battle_simulator/characters.csv") as file:
        characters = csv.reader(file)
        
        def get_name():
            name_valid = True
            
            while name_valid == False:
                name = input("What is your characters name")

                for character in characters:
                    if name in character[0]:
                        name_valid = False
            
                if name_valid == False:
                    print("There is already a character with that name!\n")
                
            return name
        
        name = get_name()
    
        
        def get_class():
            class_valid = False
            
            while class_valid == False:
                print("""
                Classes
                1. Assasin(Focusses on Speed)
                2. Warrior(Foccuses on Strength)
                3. Mage(Foccuses on Magic Power)
                5. Tank(Foccuses on Defense)
                6. No Class(Stats are Balanced)
                """)
                
                char_class = input("Choose a Number for your Class")
                
                if char_class == "1":
                    pass
                elif char_class == "2":
                    pass
                elif char_class == "3":
                    pass
                elif char_class == "4":
                    pass
                elif char_class == "5":
                    pass
                elif char_class == "6":
                    pass
                else:
                    print("Not a Valid Class!")

            return char_class

        char_class = get_class()

    
    
    
    with open("battle_simulator/characters.csv") as file:
        characters = csv.reader(file)


def save():
    pass


def load():
    pass


def main():
    pass


while True:
    main()