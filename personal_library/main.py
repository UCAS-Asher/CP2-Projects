#Asher Wangia, Personal Library Program

books = []
authors = []

running = True



def main():
    pass

    print("""
    This is a Library to store Books
    1. Add Books
    2. Remove Books
    3. Search
    4. Display Contents
    5.Exit
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        book = (input("What is the book you want to add: ")).lower
        author = (input("What is the author of the book you choose: ")).lower
        
        add()
    elif choice == "2":
        print(books)
        book = (input("What is the book you want to remove: ")).lower
        print(authors)
        author = (input("What is the author of the book you removed: ")).lower

        removelist()
    elif choice == "3":
        print("""
        1. Check for Author
        2. Check for Book
        """)
        
        search_choice = input("Choose a Number: ")

        if search_choice == "1":
            book = (input("List one book to find its author: ")).lower

            search_author()
            
            book_position = search_author()

            print("The author is",authors[book_position]) 
        elif search_choice == "2":
            author = input("List an authors name to find their books: ")

    return book, author


def add():
    book = main()
    author = main()
    
    books.append(book)
    authors.append(author)



def removelist():
    book = main()
    author = main()
    
    books.remove(book)
    authors.remove(author)


def search_author():
    book = (main())

    book_position = books.index(book)


    return book_position


def search_book():
    pass


while running == True:
    main()
