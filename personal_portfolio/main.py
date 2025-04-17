#Asher Wangia, Personal Portfolio
print("This is a portfolio or collection of works made by me and to use this you will need to type numbers for the options of projects you want to see\n")#Tells the user how to use the portfolio

#These import the functions for the project I am proud of
from area_calc import area_calculator as area_calc
from average_grade import av_grade
from cel_to_faren import cel_faren
from pass_gen import pass_gen
from morse_code import morse_code
from movie_recommender import movie_recommender

def main():
    #Print out the choices of projects the user can choose from
    print("""
    Portfolio Choices
    1. Area Calculator
    2. Average Grade Calculator
    3. Celsius To Farenheit
    4. Random Password Generator
    5. Morse Code Translator
    6. Movie Recommender
    7. Exit
    """)

    port_choice = input("Choose a Number: ")#This gets the choice of the project the user wants to see

    if port_choice == "1":#This gets port_choice and runs the specific project and prints out its description based on the user's choice
        print("\nThis Project Helps You Calculate the Area for Shapes Using Measurements that the user gives")#This tells the user about what the project does
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")#This tells the user about how I found the programming process for the project
        print("In this project I learned how to use functions")#This tells the user about what I learned in the project
        area_calc()#This runs the project the user chose
        main()#This keeps the program running until the user chooses to leave
    elif port_choice == "2":
        print("This project helps you calculate your average grade based on the grades in the clases you have")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use floats")
        av_grade()
        main()
    elif port_choice == "3":
        print("This project converts temperature in celsius to fahrenheit")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use inputs and numbers")
        cel_faren()
        main()
    elif port_choice == "4":
        print("This project will help you create a random password based on the requirements you choose")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use the string module")
        pass_gen()
        main()
    elif port_choice == "5":
        print("This project translates messages from english to morse code or messages in morse code to english")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use the string module")
        morse_code()
        main()
    elif port_choice == "6":
        print("This project displays to you a list of movies and recommends you movies based on categories")
        print("I Found the Process of Programming this project when taking a Computer Programming Class In 9th Grade")
        print("In this project I learned how to use CSV files")
        movie_recommender()
        main()
    elif port_choice == "7":
        print("Profolio End!")#This prints out the program ended and does not keep the program running
    else:
        print("Not an Option!")#This tells the user that their choice was not an option available
        main()#Keeps the program running


main()#This starts the program