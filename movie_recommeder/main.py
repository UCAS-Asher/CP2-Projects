#Asher Wangia, Movie Recommender
import csv

movie_storage = []

with open("movie_recommeder/Movies list.csv") as file:
    movies = csv.reader(file)
    next(movies)
    for row in movies:
        movie = {
       "Title": row[0],
       "Director": row[1],
       "Genre": row[2],
       "Rating": row[3],
       "Length(Minutes)": row[4],
       "Notable Actors": row[5]
   }
        movie_storage.append(movie)


def main():
    print("""
    This is a Movie Recommender
    1. Display
    2. Remove Books
    3. Search
    4. Display Books(Author and Name or All Details)
    5. Exit
    """)