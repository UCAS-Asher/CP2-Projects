#Asher Wangia, Celsius to Fahrenheit

def cel_faren():

    def use():
        try:
            celsius = float(input("What is your tempreature in celsius: "))
        except:
            print("Not a Number!")
            cel_faren()

        fahrenheit = (celsius*9/5)+32
        fahrenheit = round(fahrenheit, 1)

        print("Your tempreature is",celsius, "degrees celsius,",fahrenheit, "degrees fahrenheit." )
        cel_faren()
    
    print("""
    Choices
    1. Celcius to Fahrenheit
    2. Exit""")

    choice = input("Choose a Number: ")

    if choice == "1":
        use()
    elif choice == "2":
        print("Program End")
