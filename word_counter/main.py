#Asher Wangia, Word Counter

from time_handling import time_set

def count_words():
    pass

def add_file():
    adding = input("What do you want to add to the file: ")
        
    with open("word_counter/file.txt", "a") as file:
        file.write(adding + "\n")


def remove_file():
    with open("word_counter/file.txt", "r+",) as file:
        
        print("""
        Remove Choices
        1. Remove
        2. Exit
        """)
        
        choice = input("Choose a Number: ")

        if choice == "1":
            removing = input("What do you want to remove from the file: ")

            
            for item in file:
                if removing in item:
                    with open("word_counter/file.txt", "r") as f:
                        lines = f.readlines()
                    with open("word_counter/file.txt", "w") as f:
                        for line in lines:
                            if line.strip("") != item:
                                f.write(line)
            
            print("\nRemoved Item")


        elif choice == "2":
            pass
        else:
            print("\nNot an Option")
            remove_file()

def reset_file():
    open("word_counter/file.txt", "w").close()

def main():
    print("""
    Choices
    1. Add to File
    2. Remove From File
    3. Reset File
    4. Exit
    """)

    choice = input("\nChoose a Number: ")

    if choice == "1":
        add_file()
        print(time_set())
        
    elif choice == "2":
        remove_file()
        print(time_set())
    elif choice == "3":
        reset_file()
        print(time_set())
    elif choice == "4":
        exit()
    else:
        print("Not an Option\n")
        pass



while True:
    main()