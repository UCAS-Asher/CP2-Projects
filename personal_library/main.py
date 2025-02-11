#Asher Wangia, Personal Library Program

library = []


#This function runs other functions based on your choices
def main():
    pass

    print("""
    This is a Library to store Books
    1. Add Books
    2. Remove Books
    3. Search
    4. Display Books Names
    5. Exit
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        add_library(input("What is the book you want to add: ").lower(), input("What is the author: ").lower(), input("What is the genre: ").lower(), input("What year was the book released: ").lower(), input("What is the amount of pages: ").lower())
    elif choice == "2":
        print("Book Names:",books)
        removelist(input("What is the book you want to remove: ").lower())
    elif choice == "3":  
        print("Book Names:",books)
        print("""
        Choices
        1. Simple Display
        2. Detailed Display
        """)
        search(input("Choose a Number: ").lower(),input("Which Book do you want to Search: ").lower())
    elif choice == "4":
        print("""
        Choices
        1. Simple Display
        2. Detailed Display
        """)
        
        display_type = input("Choose a Number: ")
        
        if display_type == "1":
            display_simple()
        elif display_type == "2":
            display_complex()
    elif choice == "5":
        exit()
    

#This function adds a book to the library along with all its other details
def add_library(book, author, genre, year, pages):   
    
    title = input("What is the book you want to add: ").lower(), 
    author = input("What is the author: ").lower(), 
    genre = input("What is the genre: ").lower(), 
    year = input("What year was the book released: ").lower(), 
    pages = input("What is the amount of pages: ").lower()

    book = {
       "Title": book,
       "Author": author,
       "Genre": genre,
       "Realese Date": year,
       "Pages": pages
   }

    library.append(book)
    print("Book Added")
    


#This function removes a book from the library
def removelist(to_remove):
    for book in library:
        if to_remove in book["title"]


#This function displays the details of a book based on which type of display is chosen
def search(search_type,book):
    if book in storage:
        if search_type == "1":
            print("Book:", book)
            print("Author:",storage[book][0])
        elif search_type == "2":
            print("Book:",book)
            print("Author:",storage[book][0])
            print("Genre:",storage[book][1])
            print("Publish Date:",storage[book][2])
            print("Pages:",storage[book][3])
    else:
        print("Not a Book")
   



def display_simple():
    for book in storage:
        print("Book:", book)
        print("Author:",storage[book][0])
        print(" ")
def display_complex():
    for book in storage:
        print("Book:", book)
        print("Author:",storage[book][0])
        print("Genre:",storage[book][1])
        print("Publish Date:",storage[book][2])
        print("Pages:",storage[book][3])
        print(" ")

while True:
    main()
