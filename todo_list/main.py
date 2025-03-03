#Asher Wangia, To Do List

def mark_done():
    print("""
    Mark Done To List Choices
    1. Mark Done
    2. Exit
    """)
        
    choice = input("Choose a Number: ")


    
    if choice == "1":
        marking = input("What do you want to mark in the to do list as done: ")
        
        with open("todo_list/list.txt", "r+",) as toDoList: #Checks every line in the text file to see if it contains what the user wants to mark done and rewrites the file marking what user wants as done
            for item in toDoList:
                if marking in item:
                    with open("todo_list/list.txt", "r") as file:
                        lines = file.readlines()
                    with open("todo_list/list.txt", "w") as file:
                        for line in lines:
                            if line.strip("") != item:
                                file.write(line)
                            elif line.strip("") == item:
                                file.write("Done: "+ line)
        print("Marked as Done")
    elif choice == "2":
            pass
    else:
        print("Not an Option")
        mark_done()


def add_list():#Appends what the user wants to a new line on the text file
    print("""
    Add To List Choices
    1. Add
    2. Exit
    """)
        
    choice = input("Choose a Number: ")



    if choice == "1":
        adding = input("What do you want to add to the to do list: ")
        
        with open("todo_list/list.txt", "a") as file:
            file.write(adding + "\n")
    elif choice == "2":
            pass
    else:
        print("Not an Option")
        add_list()
        


def remove_list():
    
    with open("todo_list/list.txt", "r+",) as toDoList:
        
        print("""
        Remove To List Choices
        1. Remove
        2. Exit
        """)
        
        choice = input("Choose a Number: ")

        if choice == "1":
            removing = input("What do you want to remove from the to do list: ")

            #Checks every line in the text file to see if it contains what the user wants to remove and rewrites the file without it
            for item in toDoList:
                if removing in item:
                    with open("todo_list/list.txt", "r") as file:
                        lines = file.readlines()
                    with open("todo_list/list.txt", "w") as file:
                        for line in lines:
                            if line.strip("") != item:
                                file.write(line)
            
            print("Removed Item")


        elif choice == "2":
            pass
        else:
            print("Not an Option")
            remove_list()


def display_list():
    with open("todo_list/list.txt", "r",) as file: #Prints the text file
        content = file.read()
        print("\nTo Do List:")
        print(content)


def main():#Runs the functions based on what the user inputs
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
        mark_done()
    elif choice == "3":
        remove_list()
    elif choice == "4":
        display_list()
    elif choice == "5":
        exit()
    else:
        print("Not an Option")


while True:#Keeps the program running until the user chooses to exit
    main()