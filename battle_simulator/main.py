#Asher Wangia, Battle Simulator
import csv

def display_characters():
    pass

def create():
    with open("battle_simulator/characters.csv") as file:
        characters = csv.reader(file)
        next(characters)
        
        def get_name():
            name = input("What is your characters name: ")

            if name in characters:
                print("There is already a character with that name!\n")
                get_name()
                
            return name
        
        name = get_name()
    
        
    def get_class(): 
        print("""
        Classes
        1. Assasin(Focusses on Speed)
        2. Warrior(Foccuses on Strength)
        3. Mage(Foccuses on Magic Strength)
        4. Tank(Foccuses on Both Defenses)
        5. Jack of All Trades(Stats are Balanced)
        """)
                
        char_class = input("Choose a Number for your Class: ")
                
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
            get_class()

        return char_class, health, strength, magic_strength, defense, magic_defense, speed

    character_values = get_class()

    char_class = character_values[0]
    health = character_values[1]
    strength = character_values[2]
    magic_strength = character_values[3]
    defense = character_values[4]
    magic_defense = character_values[5]
    speed = character_values[6]

        
    
    with open("battle_simulator/characters.csv", "a") as file:
        file.write("\n"+ str(name) +", " + str(char_class) + ", " + str(health) + ", " + str(strength) + ", " + str(magic_strength) + ", "  + str(defense) + ", " + str(magic_defense) + ", " + str(speed) + ", " + "0, " + "0")


def save():
    pass


def load():
    with open("battle_simulator/characters.csv") as file:
        characters = csv.reader(file)
        next(characters)

        char_name = input("What Character do you want to load")

        for character in characters:
            if char_name in character[1]:
                char_name = character[1]
                char_class = character[2]
                health = character[3]
                strength = character[4]
                magic_strength = character[5]
                defense = character[6]
                magic_defense = character[7]
                speed = character[8]
                level = character[9]
                experience = character[10]

    return char_name, char_class, health, strength, magic_strength, defense, magic_defense, speed, level, experience
def main():
    print("""
    Choices
    1. Create A Character
    2. Save A Character
    3. Load a Character
    4. Display a Character
""")

    choice = input("Choose a Number: ")

    if choice == "1":
        create()
    elif choice == "2":
        save()
    elif choice == "3":
        load()
    elif choice == "4":
        display_characters()

while True:
    main()