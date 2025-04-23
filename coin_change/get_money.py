def get_money(country):
    money = input("How much money do you want to coin change(Only Up to Two Decimals): ")

    try:
        float(money)
    except:
        print("Not a Number!")
        money = get_money(country)


    if country == "Japan":
        try:
            int(money)
        except:
            print("That Country Does not do Decimals")
            money = get_money(country)

        money == int(money)
    else:
        try:
            float(money)
        except:
            print("Not a Number!")
            get_money()

        if money != round(float(money), 2):
            print("Too Many Decimal Points!")
            money = get_money(country)

        money = float(money)


    return money

print(get_money("america"))