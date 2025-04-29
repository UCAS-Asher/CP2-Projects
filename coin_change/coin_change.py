import csv 

def coin_change(country, money):
    if country == "Australia":
        currency_1 = "Australian Dollar Bill"
        currency_2 = "Cent Coin"
    elif country == "Canada":
        currency_1 = "Canadian Dollar Bill"
        currency_2 = "Cent Coin"
    elif country == "U.S.":
        currency_1 = "Dollar Bill"
        currency_2 = "Cent Coin"

    
    def get_denominations():
        with open("coin_change/coin_denominations.csv", "r")as file:
            currencies = csv.reader(file)
            next(currencies)
            
            for currency in currencies:
                if currency[0] == country:
                    denominations = []
                    
                    for unit in currency[2:]:
                            unit = float(unit)
                            denominations.append(unit)
        
        return denominations
    
    denominations = get_denominations()

    
    def change_coins(denominations, money, country):
        change = {}
        remaining_money = money

        for unit in denominations:
            while remaining_money >= unit:
                remaining_money -= unit
                if country == "Japan":
                    try:
                        change[f"{str(unit)} {"Yen Note"}"] = change[f"{str(unit)} {"Yen Note"}"] + 1
                    except:
                        change[f"{str(unit)} {"Yen Note"}"] = 1
                else:
                    try:
                        if unit < 1:
                            change[f"{str(unit*100)} {currency_2}"] = change[f"{str(unit*100)} {currency_2}"] + 1
                        else:
                            change[f"{str(unit)} {currency_1}"] = change[f"{str(unit)} {currency_1}"] + 1
                    except:
                        if unit < 1:
                            change[f"{str(unit*100)} {currency_2}"] = 1
                        else:
                            change[f"{str(unit)} {currency_1}"] = 1
        
        print(remaining_money)

        if remaining_money == 0:
            return change




    change = change_coins(denominations, money, country)
    if change:
        print("The country is", country, "and you will be coin changing", money, "money")
        print("You will Need:")
        for unit_name, amount in change.items():
            print(f"{amount} x {unit_name}")
    else:
        print("Cannot provide change with the current denominations in this country")


coin_change("Canada", 554.55)


                