#Asher Wangia, Personal Portfolio
print("This is a portfolio or collection of works made by me and to use this you will need to type numbers for the options\n")

from area_calc import area_calculator as area_calc
from average_grade import av_grade
from cel_to_faren import cel_faren
from pass_gen import pass_gen
from morse_code import morse_code
from movie_recommender import movie_recommender

def main():
    print("""
    Portfolio Choices
    1. Area Calculator
    2. Average Grade Calculator
    3. Celsius To Farenheit
    4. Random Password Generator
    5.
    6.
    7. Exit
    """)

    port_choice = input("Choose a Number: ")

    if port_choice == "1":
        print("\nThis Project Helps You Calculate the Area for Shapes Using Measurements that the user gives")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use functions")
        area_calc()
    elif port_choice == "2":
        print("This project helps you calculate your average grade based on the grades in the clases you have")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use floats")
        av_grade()
    elif port_choice == "3":
        print("This project converts temperature in celsius to fahrenheit")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use inputs and numbers")
        cel_faren()
    elif port_choice == "4":
        print("This project will help you create a random password based on the requirements you choose")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use the string module")
        pass_gen()
    elif port_choice == "5":
        print("This project translates messages from english to morse code or messages in morse code to english")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use the string module")
        morse_code()
    elif port_choice == "6":
        print("This project displays to you a list of movies and recommends you movies based on categories")
        movie_recommender()
    elif port_choice == "7":
        print("Profolio End!")
        exit()
    else:
        print("Not an Option!")
        main()


while True:
    main()