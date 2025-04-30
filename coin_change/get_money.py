def get_money(country):
    if country == "Japan":#Japan Doesnt Use Decimals
        money = input("How much money do you want to coin change(No Decimals): ")
        
        try:
            money = int(money)#Check if 
        except:
            print("That Country Does not do Decimals")
            money = get_money(country)

    else:#Other Countries that use decimals
        money = input("How much money do you want to coin change(Only Up to Two Decimals): ")

        try:
            money = float(money)
        except:
            print("Not a Number!")
            money = get_money(country)

        if money != round(float(money), 2):#Check too see if the users input is above 2 decimals
            print("Too Many Decimal Points!")
            money = get_money(country)



    return money

