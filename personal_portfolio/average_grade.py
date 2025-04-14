#Asher Wangia, Average Grade

def av_grade():
    
    periods = []
    try:
        periods_num = int(input("How many classes do you have: "))
    except:
        print("Not a Number!")
        av_grade()
    

    def get_periods():
        periods = {}
        for num in range(periods_num):
            period = input(f"What is class number {num}:")
            
            try:
                grade = float(input("What is your grade in the class(Percent): "))
            except:
                print("Not a Percent!")
                get_periods()
            
            periods[period] = grade

        return periods
        
    periods = get_periods()

    def calculate_grade(periods):
        grades = list(periods.values())
        grades_total = 0
        for grade in grades:
            grades_total += grade

        average_grade = grades_total/len(grades)
        average_grade = round(grade, 2)

        return average_grade
    
    average_grade = calculate_grade(periods)


    print(f"Your average grade is {average_grade}%")

av_grade()