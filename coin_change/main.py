#Asher Wangia, Coin Change Problem
import csv

from coin_change import coin_change
from get_money import get_money

def main():
    print("""
    Countries to Change Money From
    1. America
    2. Japan
    3. Australia
    """)
    
    country = input("Choose a Number: ")

    if country == "1":
        country = "America"
    elif country == "2":
        country = "Japan"
    elif country == "3":
        country = "Australia"
    else:
        print("Not a Country")
        main()

    
    coin_change(country, get_money(country))


while True:
    main()
