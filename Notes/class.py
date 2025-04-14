# Classes and Objects in Python


class subject:# Blueprint for an object
    def __init__(self, content, period, teacher, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Name: {self.content}\nTeacher: {self.teacher}\nRoom: {self.room}"

first = subject("CS Principles", 1, "LaRose", 200)
second = subject("CP2", 2, "LaRose", 200)

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"{self.name} is a {self.species} and they have {self.hp} HP and do {self.dmg} amount of damage in battle"
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} damage and {opponent.name} now has {opponent.hp}")

            if opponent.hp <= 0:
                print(f"{opponent.name}is knocked out {self.name} wins!")
            else:
                self.hp -= opponent.dmg
                print(f"{opponent.name} attacked {self.name} for {opponent.dmg} damage and {self.name} now has {self.hp}")
                if self.hp <= 0:
                    print(f"{self.name}is knocked out {opponent.name} wins!")

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spikey = pokemon("Spiky", "Jolteon", 150, 100)

fluffy.battle(spikey)


    


#1. What is a class in python?
    #Blueprint for an object

#2. What is an object in python?
    #An instance of a class

#3. How do python classes relate to python objects?
    #The object is based of the class

#4. How do you create a python class?
    # 'class_name:'

#5. What are methods?
    #A function that exists for a specific class

#6. How do you create a python object?
    # 'name_of_object = name_of_class(objects information)'


#7. How to call a method for an object?
    # 'name_of_object.name_of_methed'

#8. Why do we use python classes
    #Python classes provide all the standard features of Object Oriented Programming
