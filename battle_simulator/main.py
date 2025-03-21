#Asher Wangia, Battle Simulator
import csv

characters = []

def display_characters():
    with open("battle_simulator/characters.csv") as file:
        characters = csv.reader(file)
        next(characters)
        
        print("""
        Display Choices
        1. SImple Display(Names)
        Detailed Display(Stats)
        """)

        display_choice = input("Choose a Number")

        if display_choice == "1":
            char_names = []
            for character in characters:
                char_names.append(character[0])
            print("Characters:")
            print(char_names)
        elif display_choice == "2":
            print("Characters:")
            for character in characters:
                print("Character Name:", character[0])
                print("Character Class:", character[1])
                print("Health:", character[2])
                print("Strength:", character[3])
                print("Magic Strength:", character[4])
                print("Defense:", character[5])
                print("Magic Defense:", character[6])
                print("Speed:", character[7])
                print("Level:", character[8])
                print("EXP:", character[9])
                print("\n")

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


def save(player_character):
    pass


def load():
    with open("battle_simulator/characters.csv") as file:
        characters = csv.reader(file)
        next(characters)

        char_name = input("What Character do you want to load")

        for character in characters:
            if char_name in character[0]:
                char_name = character[0]
                char_class = character[1]
                health = character[2]
                strength = character[3]
                magic_strength = character[4]
                defense = character[5]
                magic_defense = character[6]
                speed = character[7]
                level = character[8]
                experience = character[9]

        

        player_character = {
            "Character Name": char_name,
            "Character Class": char_class,
            "Health": health,
            "Strength": strength,
            "Magic Strength": magic_strength,
            "Defense": defense,
            "Magic Defense": magic_defense,
            "Speed": speed,
            "Level": level,
            "Experience Points": experience
        }

        
    return player_character
        

def main():
    print("""
    Choices
    1. Create A Character
    2. Save A Character
    3. Load a Character
    4. Display a Character
    5. Battle a 
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        create()
    elif choice == "2":
        save(player_character)
    elif choice == "3":
        player_character = load()
    elif choice == "4":
        display_characters()

while True:
    main()