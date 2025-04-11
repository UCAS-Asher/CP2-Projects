#Asher Wangia, Area Calculator
def area_calculator():

    def square():
        width = float(input("What is your Width: "))
        length = float(input("What is your Length: "))
        area = width*length
        return f"Your area is : {area}"

    def rectangle():
        width = float(input("What is your Width: "))
        length = float(input("What is your Length: "))
        area = width*length
        return f"Your area is : {area}"


    def triangle():
        height = float(input("What is your Height: "))
        base = float(input("What is your Base: "))
        area = height*base/2
        return f"Your area is : {area}"


    def circle():
        radius = float(input("What is your Radius: "))
        area = 3.14*radius**2.0
        return f"Your area is : {area}"


    def trapezoid():
        base1 = float(input("What is your First Base: "))
        base2 = float(input("What is your Second Base: "))
        height = float(input("What is your Height: "))
        area = ((base1+base2)/2)*height
        return f"Your area is : {area}"



    def area_calc_main():
        print("""
        Area Calculator Choices
        1. Get Area For a Square
        2. Get Area For a Rectangle
        3. Get Area For a Triangle
        4. Get Area For a Circle
        5. Get Area For a Trapezoid
        6. Exit Program
        \n""")

        action = input("Choose a Number: ")

        if action =="1":
            print(square())
        

        elif action =="2":
            print(rectangle())

        elif action =="3":
            print(triangle())

        elif action =="4":
            print(circle())

        elif action =="5":
            print(trapezoid())

        else:
            print("Program End!")
            exit()

    while True:
        area_calc_main()
