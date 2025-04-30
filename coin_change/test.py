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
        currency_2 = "Yen Coin"
    else:
        print("Unsupported country.")
        return

    def get_denominations():
        with open("coin_change/coin_denominations.csv", "r") as file:
            currencies = csv.reader(file)
            next(currencies)  # Skip the header
            for currency in currencies:
                if currency[0] == country:
                    return [float(unit) for unit in currency[2:]]
        return []  # Return empty if country not found

    denominations = get_denominations()
    if not denominations:
        print("No denominations available for the selected country.")
        return

    def change_coins(denominations, money):
        change = {}
        remaining_money = round(money, 2)  # Handle float precision issues

        for unit in sorted(denominations, reverse=True):  # Start with the largest denomination
            count = int(remaining_money // unit)
            if count > 0:
                remaining_money = round(remaining_money - count * unit, 2)  # Update remaining money
                if unit < 1:  # Coins
                    change[f"{int(unit * 100)} {currency_2}"] = count
                else:  # Bills
                    change[f"{int(unit)} {currency_1}"] = count

        if remaining_money > 0:  # Unable to make exact change with denominations
            print(f"Remaining money that cannot be converted: {remaining_money}")
            return None

        return change

    change = change_coins(denominations, money)
    if change:
        print(f"The country is {country}, and you will be changing {money} money")
        print("You will need:")
        for unit_name, amount in change.items():
            print(f"{amount} x {unit_name}")
    

# Example Usage
coin_change("Japan", 554)
