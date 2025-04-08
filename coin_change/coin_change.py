import csv 

def coin_change(country, money):
    print("The country is", country, "and you will be coin changing", money, "money")
    print("You will Need:")
    
    def get_denominations():
        with open("coin_change/coin_denominations.csv", "r")as file:
            areas = csv.reader(file)
            next(areas)
            
            for area in areas:
                if area[0] == country:
                    currency = area[1]
                    denominations = []
                    
                    denominations.append(area[2:])

        return currency, denominations
    
    change_info = get_denominations()

    currency = change_info[0]
    denominations = change_info[1]

    
    def change_coins(denominations, money):
        denominations.sort(reverse=True)
        change = {}
        remaining_money = money

        for unit in denominations:
            while remaining_money >= unit:
                remaining_amount -= unit
                change[unit] = change.get(unit, 0) + 1

        if remaining_money == 0:
            return change
        else:
            return None


    coins = change_coins(denominations, money)
    if coins:
        print(f"Change for {money} {currency}:")
        for coin, amount in coins.items():
            print(f"{coin} x {amount} {'Yen Note' if currency == "Yen" else currency  }")
    else:
        print(f"Cannot make change for {money} {currency} with the denominations.")

                
                
      