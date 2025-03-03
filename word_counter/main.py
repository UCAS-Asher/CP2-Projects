#Asher Wangia, Word Counter

from time_handling import time_set

def count_words(user_file):
    try:
        with open(user_file, "r",) as file:
            words = 0
            file = file.read()

            rows = file.split()
            words += len(rows)
        if words > 1:  
            return"There are " + str(words) + " words"
        else:
            return"There is " + str(words) + " word"
    except:
        pass


def add_file(user_file):
    try:
        adding = input("What do you want to add to the file: ")
            
        with open(user_file, "a") as file:
            file.write(adding + "\n")
    except:
        print("Not a Valid Relative Path\n")


def remove_file(user_file):
    try:
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
    except:
        print("Not a Valid Relative Path\n")


def reset_file(user_file):
    try:
        open(user_file, "w").close()
    except:
        print("Not a Valid Relative Path\n")


def display_file(user_file):
    try:
        with open(user_file, "r",) as file:
            content = file.read()
            print("File:")
            print(content)
    except:
        print("Not a Valid Relative Path\n")


def main():
    
    user_file = input("Input a relative path for a text file: ")
    
    print("""
    Choices
    1. Add to File
    2. Remove From File
    3. Reset File
    4. Display File
    5. Exit
    """)

    choice = input("\nChoose a Number: ")

    if choice == "1":
        add_file(user_file)
        print("\n",count_words(user_file))
        print(time_set())
    elif choice == "2":
        remove_file(user_file)
        print("\n",count_words(user_file))
        print(time_set())
    elif choice == "3":
        reset_file(user_file)
        print("\n",count_words(user_file))
        print(time_set())
    elif choice == "4":
        display_file(user_file)
        print("\n",count_words(user_file))
        print(time_set())
    elif choice == "5":
        exit()
    else:
        print("Not an Option\n")


while True:
    main()