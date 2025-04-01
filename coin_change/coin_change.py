import csv 

def coin_change(country, money):
    print("The country is", country, "and you will be coin changing", money, "money")
    print("You will Need:")
    
    with open("coin_change/coin_denominations.csv", "r")as file:
        coins = csv.reader(file)
        
        for currency in coins:
            if currency[0] == country:
                pass
      