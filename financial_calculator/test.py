




def calc(money_amount):
    money_amount = int(input("Money: "))
    intrest = (int(input("Intrest: ")))/100
    time = int(input("Time: "))
    while time > 0:
        money_amount += money_amount*intrest
        time -=1
    return money_amount



