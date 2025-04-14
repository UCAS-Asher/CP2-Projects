#Asher Wangia, Average Grade

def av_grade():
    
    per1 = float(input("What is your grade for 1st period: "))

    per2 = float(input("What is your grade for 2nd period: "))

    per3 = float(input("What is your grade for 3rd period: "))

    advis = float(input("What is your grade for Advisory period: "))

    per6 = float(input("What is your grade for 6th period: "))

    per7 = float(input("What is your grade for 7th period: "))

    per8 = float(input("What is your grade for 8th period: "))

    grade = (per1+per2+per3+advis+per6+per7+per8)/7

    grade = (round(grade, 2))

    print("Your average grade is", grade, "%")