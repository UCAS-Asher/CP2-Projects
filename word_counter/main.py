#Asher Wangia, Word Counter

def add_file():
    adding = input("What do you want to add to the to do list: ")
        
    with open("todo_list/list.txt", "a") as file:
        file.write(adding + "\n")


def remove_file():
    pass

def reset_file():
    pass

def main():
    print("""
    Choices
    1. Add to File
    2. Remove From File
    3. Reset File
    4. Exit
    """)

    choice = input("\nChoose a Number: ")

    if choice == 1:
        add_file()
    elif choice == 2:
        remove_file()
    elif choice == 3:
        reset_file()
    elif choice == 4:
        exit()
    else:
        print("Not an Option\n")
        pass



while True:
    main()