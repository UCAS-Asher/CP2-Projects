#Asher Wangia, Personal Portfolio
print("This is a portfolio or collection of works made by me and to use this you will need to type numbers for the options\n")

from area_calc import area_calculator as area_calc
from average_grade import av_grade

def main():
    print("""
    Portfolio Choices
    1. Area Calculator
    2. Average Grade Calculator
    3.
    4.
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
        pass
    elif port_choice == "4":
        pass
    elif port_choice == "5":
        pass
    elif port_choice == "6":
        pass
    elif port_choice == "7":
        print("Profolio End!")
        exit()
    else:
        print("Not an Option!")
        main()


while True:
    main()