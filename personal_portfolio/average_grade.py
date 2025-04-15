#Asher Wangia, Average Grade

def av_grade():

    
    def use():

        try:
            periods_num = int(input("How many classes do you have: "))
        except:
            print("Not a Number!")
            use()
        

        def get_periods():
            periods = {}
            for num in range(1,periods_num+1):
                try:
                    grade = float(input(f"What is your grade in class number {num}(Percent): "))
                except:
                    print("Not a Percent!")
                    get_periods()
                
                periods[num] = grade

            return periods
            
        periods = get_periods()

        def calculate_grade(periods):
            grades = list(periods.values())
            grades_total = 0
            for grade in grades:
                grades_total += grade

            average_grade = grades_total/len(grades)
            average_grade = round(average_grade, 2)

            return average_grade
        
        average_grade = calculate_grade(periods)


        print(f"Your average grade is {average_grade}%")
        av_grade()

    print("""
    Choices
    1. Use Average Grade Calculator
    2. Exit""")

    choice = input("Choose a Number: ")

    if choice == "1":
        use()
    elif choice == "2":
        print("Program End!")
    else:
        print("Not an Option!")
        av_grade()
