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
                4. Tank(Foccuses on Defense)
                5. Jack of All Trades(Stats are Balanced)
                """)
                
                char_class = input("Choose a Number for your Class")
                
                if char_class == "1":
                    health = 100
                    strength = 25
                    defense = 5
                    speed = 20
                    magic_power = 10
                    char_class = "Assasin"
                elif char_class == "2":
                    health = 100
                    strength = 40
                    defense = 10
                    speed = 10
                    magic_power = 1
                    char_class = "Warrior"
                elif char_class == "3":
                    health = 100
                    strength = 10
                    defense = 1
                    speed = 5
                    magic_power = 45
                    char_class = "Mage"
                elif char_class == "4":
                    health = 100
                    strength = 25
                    defense = 35
                    speed = 1
                    magic_power = 1
                    char_class = "Tank"
                elif char_class == "5":
                    health = 100
                    strength = 15
                    defense = 15
                    speed = 15
                    magic_power = 15
                    char_class = "Jack of All Trades"
                else:
                    print("Not a Valid Class!")

            return char_class, health, strength, defense, speed, magic_power

    character_values = get_class()

    char_class = character_values[0]
    health = character_values[1]
    strength = character_values[2]
    defense = character_values[3]
    speed = character_values[4]
    magic_power = character_values[5]

        
    
    
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