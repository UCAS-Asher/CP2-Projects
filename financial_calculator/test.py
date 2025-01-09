money_amount = 0
intrest = 0
time = 0



money_amount = int(input("Money: "))
intrest = (int(input("Intrest: ")))/100
time = int(input("Time: "))

def calc(money_amount):
    money_amount = money_amount + money_amount*intrest
    return money_amount

calc(money_amount)*time

print(money_amount)

