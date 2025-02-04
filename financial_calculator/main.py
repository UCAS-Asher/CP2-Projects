#Asher Wangia Financial Calculator
#This is the financfial calculator program

run = True

#This function gets the use inputs and runs the other functions
def main():


    print("""
    1. Save Goal Calculator
    2. Compound Intrest Calculator
    3. Budget Allocator
    4. Sale Price Calculator
    5. Tip Calculator
    6. Exit The Program
    """)
    tool = input("Choose a Number: ")
    
    if tool == "1":
        save_goal(float(input("How much money is your goal: ")), float(input("How much is the deposit monthly: ")))
    elif tool == "2":
        compound_intrest_calc(float(input("How much money did you initially add: ")), (float(input("How much is the intrest in percent: ")))/100, float(input("How many years do you wait: ")))
    elif tool == "3":
        budget_allocator(float(input("What is your income each month: ")))   
    elif tool == "4":
        sale_price_calc(float(input("What is your price: ")), (float(input("What is your discount in percent: ")))/100)
    elif tool == "5":
        tip_calc(float(input("What is the initial Bill: ")), (float(input("How much percent are you tipping:")))/100)
    else:
        exit()


#This function gets the amount of time it will take to save up and prints it
def save_goal(goal,deposit):
    
    time = goal/deposit
    print("It will take you",round(time, 1),"months to save up")



#This function gets the amount of money you will get from the intrest and prints it
def compound_intrest_calc(money,intrest,time):

    for x in range(time):
        money += (money*intrest)

    print("You ended off with $",round(money, 2))


#This function divides the income you get each month between 4 categories and prints it
def budget_allocator(income):
    housing = income*0.30
    savings = income*0.20
    entertainment = income*0.30
    other_needs = income*0.20

    print("You should spend $",round(housing, 2),"on housing")
    print("You should spend $",round(savings, 2),"on savings")
    print("You should spend $",round(entertainment, 2),"on entertainment")
    print("You should spend $",round(other_needs, 2),"on other necessary things")
    


#This function get the price with the discount applied and prints it
def sale_price_calc(price,discount):
    price -= price*discount
    print("This is your discounted price in dollars: $",round(price, 2))



#This function gets the price with the tip added and prints it 
def tip_calc(price,tip):
    price += price*tip  
    print("Your final bill including the tip is: $",round(price, 2))

while True:
    main()
    