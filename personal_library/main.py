#Asher Wangia, Personal Library Program

books = set()
authors = set()
storage = {}


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
        print("Book Names:",books)
    elif choice == "5":
        exit()
    

#This function adds a book to the library along with all its other details
def add_library(book, author, genre, year, pages):   
    
    if book in books:
        print("Book has Alredy Been Added")
    else:
        books.add(book)
        authors.add(author)
        storage.update({book: [author,genre,year,pages]})


#This function removes a book from the library
def removelist(book):
    if book in books:
        books.remove(book)
        del storage[book]
    else:
        print("Not In Library")


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
   







while True:
    main()
