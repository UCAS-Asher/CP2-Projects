#Asher Wangia, Movie Recommender
import csv
def movie_recommender():
    movie_storage = []

    #Gets the movies from the file then puts the rows into dictionaries that are appended to a list
    with open("personal_portfolio/movie_list.csv") as file:
        movies = csv.reader(file)
        next(movies)
        for row in movies:
            movie = {
        "Title": row[0],
        "Director": row[1],
        "Genre": row[2],
        "Rating": row[3],
        "Length": row[4],
        "Actors": row[5]
    }
            movie_storage.append(movie)

    #Gets the User's First choice at what they want to do then runs the function
    def movie_main():
        
        print("""
        This is a Movie Recommender
        1. Display All Movies
        2. Get Recommendation
        3. Exit Program
        """)

        choice = input("Choose a Number: ")

        if choice == "1":
            display_movies()
        elif choice == "2":
            recommend_movie()   
        else:
            print("Program End!")

    #Displays each of the movies in the list they are contained in nicely
    def display_movies():
        for movie in movie_storage:
            print("Movie:", movie["Title"])
            print("Director:", movie["Director"])
            print("Genre:", movie["Genre"])
            print("Rating: ", movie["Rating"])
            print("Length(Minutes):", movie["Length"])
            print("Notable Actors:", movie["Actors"])
            print(" ")
            print(" ")
        
        movie_main()

    #Gets the filters the user wants and prints out a movie if it fits all the criteria
    def recommend_movie():
        
        filters = []
        add_filters = True

        while add_filters == True:
            print("""
            Filters
            1. Title
            2. Director
            3. Genre
            4. Rating
            5. Length
            6. Notable Actors
            7. Done
            """)

            movie_filter = input("Choose a Number: ").lower()

            if movie_filter == "1":
                filters.append("1")
                filter_title = input("What Title: ")
            elif movie_filter == "2":
                filters.append("2")
                filter_director = input("What Director: ")
            elif movie_filter == "3":
                filters.append("3")
                filter_genre = input("What Genre: ")
            elif movie_filter == "4":
                filters.append("4")
                filter_rating = input("What Rating: ")
            elif movie_filter == "5":
                filters.append("5")
                filter_length_min = int(input("What Length In Minutes Minimum: "))
                filter_length_max = int(input("What Length In Minutes Maximum: "))
            elif movie_filter == "6":
                filters.append("6")
                filter_actor = input("What Notable Actor: ")
            else:
                add_filters = False
        
        print("\nHere are some movies that are recommended\n")
        
        for movie in movie_storage:
            movie_good = True
            
            if "1" in filters and filter_title not in movie["Title"]:
                movie_good = False
            if "2" in filters and filter_director not in movie["Director"]:
                movie_good = False
            if "3" in filters and filter_genre not in movie["Genre"]:
                movie_good = False
            if "4" in filters and filter_rating not in movie["Rating"]:
                movie_good = False
            if "5" in filters and int(movie["Length"]) not in range(filter_length_min,filter_length_max+1):
                movie_good = False
            if "6" in filters and filter_actor not in movie["Actors"]:
                movie_good = False
            
            if movie_good == True:
                print("Movie:", movie["Title"])
                print("Director:", movie["Director"])
                print("Genre:", movie["Genre"])
                print("Rating: ", movie["Rating"])
                print("Length(Minutes):", movie["Length"])
                print("Notable Actors:", movie["Actors"])
                print(" ")
                print(" ")

        movie_main()

    movie_main()
