#Asher Wangia, Personal Library Program

library = []
books = []

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
        add_library()
    elif choice == "2":
        print("Book Names:", books)
        removelist(input("What book would you like to remove: ").lower)
    elif choice == "3":  
        print("""
        Search Choices
        1. Title
        2. Author
        3. Genre
        4. Publish Date
        5. Pages
        """)
        search()
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
def add_library():   
    
    title = input("What is the book you want to add: ").lower(), 
    author = input("What is the author: ").lower(), 
    genre = input("What is the genre: ").lower(), 
    year = input("What year was the book released: ").lower(), 
    pages = input("What is the amount of pages: ").lower()

    book = {
       "Title": title,
       "Author": author,
       "Genre": genre,
       "Release Date": year,
       "Pages": pages
   }
    books.append(title)
    library.append(book)
    print("Book Added")
    


#This function removes a book from the library
def removelist(to_remove):
    for book in library:
        if to_remove in book["Title"]:
            library.remove(book)
    


#This function displays the details of a book based on which type of display is chosen
def search():
    search_by = input("What option would you like to search by: ").lower()
   
    if search_by == "1":
        search_title = input("What book title would you like to search for: ").lower

        for book in library:
            if search_title in book["Title"]:
                print("Book:", book["Title"])
                print("Author:", book["Author"])
                print("Genre:", book["Genre"])
                print("Release Date:", book["Release Date"])
                print("Pages:", book["Pages"])

    elif search_by == "2":
        searching = input("What book author would you like to search for: ").lower

        for book in library:
            if searching in book["Title"]:
                print("Book:", book["Title"])
                print("Author:", book["Author"])
                print("Genre:", book["Genre"])
                print("Release Date:", book["Release Date"])
                print("Pages:", book["Pages"])

    elif search_by == "3":
        pass
    elif search_by == "4":
        pass
    elif search_by == "5":
        pass


def display_simple():
    for book in library:
        print("Book:", book["Title"])
        print("Author:", book["Author"])
        print(" ")

def display_complex():
    for book in library:
        print("Book:", book["Title"])
        print("Author:", book["Author"])
        print("Genre:", book["Genre"])
        print("Release Date:", book["Release Date"])
        print("Pages:", book["Pages"])
        print(" ")

while True:
    main()
