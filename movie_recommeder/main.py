#Asher Wangia, Movie Recommender
import csv

movie_storage = []

with open("CP2-Projects/movie_recommeder/movie_list.csv") as file:
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


def main():
    
    print("""
    This is a Movie Recommender
    1. Display All Movies
    2. Get Recommendation
    3. Filter Movies
    4. Exit Program
    """)

    choice = input("Choose a Number: ").lower()

    if choice == "1":
        display_movies()
    elif choice == "2":
        recommend_movie()
    elif choice == "3":
        pass
    else:
        exit()


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


def recommend_movie():
    recommend_movies = []
    
    
    genre = input("What genre do you like: ")
    rating = input("What rating do you like: ")
    
    
    with open("CP2-Projects/movie_recommeder/movie_list.csv") as file:
        movies = csv.reader(file)
        next(movies)
        for movie in movie_storage:
            for row in movies:
                if genre in row and rating in row:
                    recommend_movies.append(movie["Title"])
                
    print(recommend_movies)
    

while True:
    main()