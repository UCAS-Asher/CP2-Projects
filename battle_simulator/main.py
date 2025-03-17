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
                3. Mage(Foccuses on Magic Strength)
                4. Tank(Foccuses on Both Defenses)
                5. Jack of All Trades(Stats are Balanced)
                """)
                
                char_class = input("Choose a Number for your Class")
                
                if char_class == "1":
                    health = 100
                    strength = 125
                    magic_strength = 100
                    defense = 75
                    magic_defense = 50
                    speed = 150
                    char_class = "Assasin"
                elif char_class == "2":
                    health = 125
                    strength = 175
                    magic_strength = 75
                    defense = 100
                    magic_defense = 50
                    speed = 75
                    char_class = "Warrior"
                elif char_class == "3":
                    health = 75
                    strength = 50
                    magic_strength = 225
                    defense = 25
                    magic_defense = 125
                    speed = 100
                    char_class = "Mage"
                elif char_class == "4":
                    health = 150
                    strength = 75
                    magic_strength = 50
                    defense = 150
                    magic_defense = 150
                    speed = 25
                    char_class = "Tank"
                elif char_class == "5":
                    health = 100
                    strength = 100
                    magic_strength = 100
                    defense = 100
                    magic_defense = 100
                    speed = 100
                    char_class = "Jack of All Trades"
                else:
                    print("Not a Valid Class!")

            return char_class, health, strength, magic_strength, defense, magic_defense, speed

    character_values = get_class()

    char_class = character_values[0]
    health = character_values[1]
    strength = character_values[2]
    magic_strength = character_values[3]
    defense = character_values[4]
    magic_defense = character_values[5]
    speed = character_values[6]

        
    
    
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