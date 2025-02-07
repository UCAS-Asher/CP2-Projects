#Asher Wangia, Personal Library Program

books = set()
authors = set()
storage = {}

def main():
    pass

    print("""
    This is a Library to store Books
    1. Add Books
    2. Remove Books
    3. Search
    4. Display Books
    5. Exit
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        add_library(input("What is the book you want to add: ").lower(), input("What is the author: ").lower(), input("What is the genre: ").lower(), input("What year the book released: ").lower(), input("What is the reading level: ").lower())
    elif choice == "2":
        print(books)
        removelist(input("What is the book you want to remove: ").lower())
    elif choice == "3":  
        search(input("Which Book do you want to Search: ").lower())
    elif choice == "4":
        print(books)
    elif choice == "5":
        exit()
    


def add_library(book, author, genre, year, reading_level):   
    
    if book in books:
        print("Book has Alredy Been Added")
    else:
        books.add(book)
        authors.add(author)
        storage.update({book: [author,genre,year,reading_level]})

def removelist(book):
    if book in books:
        books.remove(book)
        del storage[book]
    else:
        print("Not In Library")


def search(book):
    if book in storage:
        print(storage[book])
    else:
        print("Not Found")
   







while True:
    main()
