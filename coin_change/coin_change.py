import csv 

def coin_change(country, money):
    if country == "Australia":
        currency_1 = "Australian Dollar"
        currency_2 = "Cents"
    elif country == "Canada":
        pass
    elif country == "U.S.":
        pass
    
    def get_denominations():
        with open("coin_change/coin_denominations.csv", "r")as file:
            currencies = csv.reader(file)
            next(currencies)
            
            for currency in currencies:
                if currency[0] == country:
                    denominations = []
                    
                    for unit in currency:
                        try:
                            unit = int(unit)
                            denominations.append(unit)
                        except:
                            pass

        return denominations
    
    denominations = get_denominations()

    
    def change_coins(denominations, money, country):
        denominations.sort(reverse=True)
        change = {}
        remaining_money = money
        print(denominations)

        for unit in denominations:
            while remaining_money >= unit:
                remaining_money -= unit
                if country == "Japan":
                    change[unit] = "Yen Note"
                else:
                    if unit < 1:
                        change[unit] = "Coin"
                    else:


        if remaining_money == 0:
            return change


    coins = change_coins(denominations, money)
    if coins:
        print(f"Change for {money} {currency}:")
        for coin, amount in coins.items():
            print(f"{coin} x {amount}")
    else:
        print(f"Cannot make change for {money} {currency} with the denominations.")

    print("The country is", country, "and you will be coin changing", money, "money")
    print("You will Need:")

coin_change("Japan", 100000)
                