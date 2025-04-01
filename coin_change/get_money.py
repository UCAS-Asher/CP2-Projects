def get_money(country):
    money = input("How much money do you want to coin change(Only Up to Two Decimals): ")

    try:
        money = float(money)
    except:
        print("Not a Number!")
        get_money()

    
    round_money = round(money, 2)

    if money == round_money:
        pass
    else:
        print("Too Many Decimal Points!")
        get_money(country)

    if country == "Japan":
        print("That Country Does not do Decimals")
        get_money(country)

    return money