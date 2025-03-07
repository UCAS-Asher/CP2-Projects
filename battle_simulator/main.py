#Asher Wangia, Battle Simulator
import csv

def display_characters():
    pass

def create():
    with open("battle_simulator/characters.csv", "a") as file:
        characters = csv.reader(file)
        next(characters)
        
        def get_name():
            name_valid = True
            
            while name_valid == False:
                name = input("What is your characters name")

                if name not in characters:
                    name_valid = True
            
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
                    health = 100
                    strength = 20
                    defense = 10
                    speed = 20
                    magic_power = 10
                    char_class = "Assasin"
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

            return char_class, health, strength, defense, speed, magic_power

        character_values = get_class()

        char_class = character_values[0]

        health = character_values[1]
        
    
    
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