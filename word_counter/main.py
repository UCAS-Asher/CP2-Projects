#Asher Wangia, Word Counter
import os


from time_handling import time_set

def check_file(user_file):
    exists = os.path.isfile(user_file)

    if exists == True:
        pass
    else:
        print("Not a File Path... Try Again")
        user_file = input("Input a relative path for a text file: ")
        check_file(user_file)

def count_words():
    with open(user_file, "r",) as file:
        words = 0
        file = file.read()

        rows = file.split()
        words += len(rows)
    if words > 1:  
        return"There are " + str(words) + " words"
    else:
        return"There is " + str(words) + " word"



def add_file():
    adding = input("What do you want to add to the file: ")
            
    with open(user_file, "a") as file:
        file.write(adding + "\n")


def remove_file():
    with open(user_file, "r+",) as file:
        removing = input("What do you want to remove from the file: ")

                
        for item in file:
            if removing in item:
                with open(user_file, "r") as f:
                    lines = f.readlines()
                with open(user_file, "w") as f:
                    for line in lines:
                        if line.strip("") != item:
                            f.write(line)
                
            print("\nRemoved Item")


def reset_file():
    open(user_file, "w").close()


def display_file():
    with open(user_file, "r",) as file:
        content = file.read()
        print("File:")
        print(content)


def main():
    
    print("""
    Choices
    1. Add to File
    2. Remove From File
    3. Reset File
    4. Display File
    5. Use A Diffrent File
    6. Exit
    """)

    choice = input("\nChoose a Number: ")

    if choice == "1":
        add_file()
        print("\n",count_words())
        print(time_set())
    elif choice == "2":
        remove_file()
        print("\n",count_words())
        print(time_set())
    elif choice == "3":
        reset_file()
        print("\n",count_words())
        print(time_set())
    elif choice == "4":
        display_file()
        print("\n",count_words())
        print(time_set())
    elif choice == "5":
        user_file = input("Input a relative path for a text file: ")
        check_file(user_file)
    elif choice == "6":
        exit()
    else:
        print("Not an Option\n")


user_file = input("Input a relative path for a text file: ")
check_file(user_file)

while True:
    main()