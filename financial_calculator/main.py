#Asher Wangia Financial Calculator
#this is the financfial calculator program
intrest = 0
time = 0
money_amount = 0

def tip_calc():
    pass

def sale_price_calc():
    pass

def compound_intrest_calc(money_amount,time):
    while time > 0:
        money_amount += money_amount*intrest
        time -= 1
        return money_amount
def budget_allocator():
    pass

def save_calc():
    pass

def main(money_amount,intrest,time):
    print("""
    1. Save Goal Calculator
    2. Compound Intrest Calculator
    3. Budget Allocator
    4. Sale Price Calculator
    5. Tip Calculator
    """)
    tool = input("Choose One Number: ")
    
    if tool == "1":
        save_calc()
    elif tool == "2":
        money_amount = int(input("How much money is in your account at the start: "))
        intrest = (float(input("How much is your intrest in percent: ")))/100
        time = int(input("How many years: "))
        compound_intrest_calc(money_amount,time)
        print("Here is your total amount of money after intrest",money_amount)

    elif tool == "3":
        budget_allocator()
    elif tool == "4":
        sale_price_calc()
    elif tool == "5":
        tip_calc()
    pass

main(money_amount,intrest,time)
    