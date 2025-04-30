import csv

def coin_change(country, money):
    # Define currency names
    if country == "Australia":
        currency_1 = "Australian Dollar Bill"
        currency_2 = "Cent Coin"
    elif country == "Canada":
        currency_1 = "Canadian Dollar Bill"
        currency_2 = "Cent Coin"
    elif country == "U.S.":
        currency_1 = "Dollar Bill"
        currency_2 = "Cent Coin"
    elif country == "Japan":
        currency_1 = "Yen Note"


    def get_denominations():
        with open("coin_change/coin_denominations.csv", "r") as file:
            currencies = csv.reader(file)
            denominations = []
            next(currencies)  # Skip the header labels
            for currency in currencies:#Gets a specific country in the CSV file
                if currency[0] == country:
                    denominations = currency[2:]#Get the Denominations of that country
    
        return denominations

    denominations = get_denominations()

    def change_coins(denominations, money):
        change = {}
        remaining_money = round(money, 2)  # Handle issues with decimals
        
        for unit in denominations:
            unit = float(unit)
            count = int(remaining_money // unit)#Get the amount of times the denomination can go into the money
            if count > 0:
                remaining_money = round(remaining_money - count * unit, 2)  # Update remaining money
                
                if unit < 1:  # Change For Coins
                    change[f"{int(unit * 100)} {currency_2}"] = count
                else:  # Change For Bills
                    change[f"{int(unit)} {currency_1}"] = count

        if remaining_money > 0:  # If unable to make change with current denominations
            print(f"Cannot Convert Everything to Change with Current Denominations, Here Is The Remaining money that cannot be converted: {remaining_money}")
            return None
        else:
            return change

    change = change_coins(denominations, money)
    if change:#If money can have change made succesfully
        print(f"The country is {country}, and you will be changing {money} money")
        print("You will need:")
        for unit_name, amount in change.items():
            print(f"{amount} x {unit_name}")#Print the denomination and how much of it is needed
    

# Example Usage
coin_change("U.S.", 554.54)
