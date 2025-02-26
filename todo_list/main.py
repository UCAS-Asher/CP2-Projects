#Asher Wangia, To Do List


def add_list():
    with open("todo_list/list.txt", "a",) as file:
        print("""
        Add To List Choices
        1. Add
        2. Exit
        """)
        
        choice = input("Choose a Number: ")

        if choice == "1":
            file.write(input("What do you want to add to the to do list: ") + "\n")
        elif choice == "2":
            pass
        else:
            print("Not an Option")
            add_list()
        


def remove_list():
    
    with open("todo_list/list.txt", "r",) as toDoList:
        content = toDoList.read()
        
        print("""
        Remove To List Choices
        1. Remove
        2. Exit
        """)
        
        choice = input("Choose a Number: ")

        if choice == "1":
            removing = input("What do you want to remove from the to do list: ")

            for item in content:
                if removing in item:
                    with open("todo_list/list.txt", "r") as file:
                        lines = file.readlines()
                    with open("todo_list/list.txt", "w") as file:
                        for line in lines:
                            if line.strip("") != line:
                                file.write(line)
            
            print("Removed Item")


        elif choice == "2":
            pass
        else:
            print("Not an Option")
            remove_list()


def display_list():
    with open("todo_list/list.txt", "r",) as file:
        content = file.read()
        print(" ")
        print("To Do List:")
        print(content)

def main():
    print("""
    Choices
    1. Add To The To Do List
    2. Mark Items as Complete
    3. Delete Items From The List
    4. Display To Do List
    5. Exit
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        add_list()
    elif choice == "2":
        pass
    elif choice == "3":
        remove_list()
    elif choice == "4":
        display_list()
    elif choice == "5":
        exit()
    else:
        print("Not an Option")


while True:
    main()