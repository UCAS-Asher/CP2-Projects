#Asher Wangia Financial Calculator
#This is the financfial calculator program

run = True

#User Interface that contains all the print statements
def main():
    global price
    global discount
    global tip
    global run
    global income
    global housing
    global savings
    global entertainment
    global other_needs
    global money
    global intrest
    global time
    global goal
    global deposit


    print("""
    1. Save Goal Calculator
    2. Compound Intrest Calculator
    3. Budget Allocator
    4. Sale Price Calculator
    5. Tip Calculator
    6. Exit The Program
    """)
    tool = input("Choose One Number: ")
    
    if tool == "1":
        goal = int(input("How much money is your goal: "))
        deposit = int(input("How much is the deposit monthly: "))
        save_goal()
        print("It will take you",time,"months to save up")
    elif tool == "2":
        money = int(input("How much money did you initially add: "))
        intrest = (int(input("How much is the intrest in percent: ")))/100
        time = int(input("How many years do you wait: "))
        compound_intrest_calc()
        print("You ended off with $",money)
    elif tool == "3":
        income = int(input("What is your income each month: "))
        budget_allocator()
        print("You should spend $",housing,"on housing")
        print("You should spend $",savings,"on savings")
        print("You should spend $",entertainment,"on entertainment")
        print("You should spend $",other_needs,"on other necessary things")
    elif tool == "4":
        price = int(input("What is your price: "))
        discount = (int(input("What is your discount in percent: ")))/100
        sale_price_calc()
        print("This is your discounted price in dollars: $",price)
    elif tool == "5":
        price = int(input("What is the initial Bill: "))
        tip = (int(input("How much percent are you tipping:")))/100
        tip_calc()
        print("Your final bill including the tip is: $",price)
    elif tool == "6":
        run = False
    else:
        print("Invalid Option")
        main()

#divides the goal by the deposit to get the amount of time it take to save up for a goal
def save_goal():
    global goal
    global deposit
    global time

    time = goal/deposit


#Adds the intrest in the bank multiple times till the time is over
def compound_intrest_calc():
    global money
    global intrest
    global time

    for x in range(time):
        money += (money*intrest)

#Divides the income into certain percentages to show where the budget should go
def budget_allocator():
    global income
    global housing
    global savings
    global entertainment
    global other_needs

    housing = income*0.30
    savings = income*0.20
    entertainment = income*0.30
    other_needs = income*0.20

    

#Subtracts the discounted price
def sale_price_calc():
    global price
    global discount

    price -= price*discount
    

#adds the tip to the total bill    
def tip_calc():
    global price
    global tip

    price += price*tip  


while run == True:
    main()
    