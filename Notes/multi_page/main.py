#asher Wangia, 

# * imports everything






#How do you make multiple files in python?
    # Make a new file ending in .py
    # Snake Case file names
    # descriptive file names(Short)


#How do you get a function from another file?
from calc import addition as add, subtraction as sub, num
    # aliasing is where you import a function and give it a new keyword
print(add())
print(sub(num,8))

#How do you get variables from another file?
from calc import num
    
    
    #Can be obtained the same way as functions
    #Better to Return the variable instead

#How do you have a function with multiple returns?
def get_user_info():
    name = input ("What is your name: ")
    quest = input ("What is your quest: ")
    color = input ("What is your favorite color: ")
    
    return name, quest, color

name, quest, color = get_user_info()

print(quest)

#Why would you use multiple pages for a python project?
    # Easier to merge github branches
    # Modularity - breaking program into smaller more manageable pieces
    # Main should only include introduction to project and user interface
    # Functionality - keeps your code clean