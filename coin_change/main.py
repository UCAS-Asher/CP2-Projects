#Asher Wangia, Coin Change Problem

from coin_change import coin_change
from get_money import get_money
from get_country import get_country

def main():
    print("""
    Choices
    1. Get Change For Money
    2. Exit Program
    """)
    choice = input("Choose a Number: ")

    if choice == "1":
        country = get_country()
        money = get_money(country)
        coin_change(country, money)
        main()
    elif choice == "2":
        print("Program End")
    else:
        main()

