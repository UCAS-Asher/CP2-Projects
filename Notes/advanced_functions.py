#Asher Wangia, Advanced Functions Notes

#1. What is a helper function?
    #A function you write to call another function
def is_int(user_input):
    try:
        int(user_input)
    except:
        print("Please give me a number.")
        is_int(input("How old are you\n"))
    return int(user_input)
    
def age():
    old = is_int(input("How old are you\n"))

    print(f"Cool. You are{old}")

age()

#2. What is the purpose of a helper function?
    #Make your functions less bloated

#3. What is an inner function?
    #A function that exists inside of another function

def add(a):
    b = int(input("Give me a number\n"))

    def addition():
        print(a+b)

    addition()

#add(2)

import logging

logging.basicConfig(level=logging.INFO)

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")
        return func(*args, *kwargs)
    return wrapper

@logger
def adder(a,b):
    return a+b



#4. What is the scope of a variable in a function WITH an inner function?
    #everything contained within the outer funcion

#5. Why do we use inner functions?
    #less parameters, less returns and it has access to all of the outer functions

#6. What is a closure function?
    #Allows your function to remember information across multiple functions
    #a closure function allows you to remember values across multiple calls
def add(a):

    def addition(b):
        return a+b

    return addition

base = add(10)

#print(base(5))
#EXAMPLE

def math(income):

    def perc(amount, type):
        percent = amount/income
        print(f"Your {type} is ${amount}, and that is {percent} of your income")

def user_inputs(type):
    return int(f"What is your monthly {type}\n$")

income = user_inputs("income")
rent = user_inputs("rent")
utilities = user_inputs("utilities")
#7. Why do we write closure functions?

#8. What is recursion?
    #When you call a function inside of itself

#9. How does recursion work?
    #Calling the function inside of itself giving it new information
