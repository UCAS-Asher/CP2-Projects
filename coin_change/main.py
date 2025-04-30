#Asher Wangia, Coin Change Problem

# Get functions from other files to use
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
        country = get_country()#Get the country the user wants
        money = get_money(country)#Get the amount of money the user needs change for based on their country
        coin_change(country, money)#Give the user change based on their country and amount of money
        main()#Keep the function running
    elif choice == "2":
        print("Program End!")
    else:
        print("Not an Option")
        main()

main()