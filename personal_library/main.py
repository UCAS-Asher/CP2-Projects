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
        books.append(book)
        authors.append(author)
    elif choice == "2":
        print(books)
        book = (input("What is the book you want to remove: ")).lower
        print(authors)
        author = (input("What is the author of the book you removed: ")).lower
    elif choice == "3":
        search_choice = input("Choose a Number")

    return book, author


def add():
    book = main()
    author = main()

    books.append(book)
    authors.append(author)


def remove():
    book = main()
    author = main()
    
    books.remove(book)
    authors.remove(author)


while running == True:
    main()
