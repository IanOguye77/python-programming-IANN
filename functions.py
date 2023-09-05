# Functions

# A function is a block of code that performs a specific task when called/invoked
# for a function to execute it must be invoked/called
# To call a function, you simply type the name of the function followed by parenthesis outside the function

# syntax
# def function_name():
#     code to execute goes here

# lets create our function that greets everyone
# def greet_everyone():
#     print("Hello, Everyone!!!")
    
# greet_everyone()

# # why use functions?
# # 1. Allow code manageability
# # 2. Allow code reusability
# # 3. Reduce code repetition

# def my_function():
#     sum = 3+ 7
#     print(sum)

# my_function()

# # Parameters
# # is a value passed to the paranthesis of a function definition -> (variable(s))
# #  information passed into a function

# # Arguments
# # is a value passed to the parenthesis of a function call
# def greet_user(user_name):
#     print(f"Hello, {user_name}")
    
# greet_user("Ian")

# def add_three_numbers(a, b, c):
#     print(a + b + c)

# add_three_numbers(10, 20, 30)
# add_three_numbers(40, 20, 30)
# add_three_numbers(50, 20, 30)
# add_three_numbers(60, 20, 30)
# add_three_numbers(70, 20, 30)

# return keyword
# is used to terminate a function and then return a value
def productOfTwoNums(a, b):
    return a * b

product = productOfTwoNums(3, 4)
print(product + 38)

# Write a python program that has five functions where the first one returns the name of the user, second returns the age of the user, third returns the age in seconds the user has lived, fourth returns the deacde and the fifth prints/returns the user information in a nice format

def user_name():
    name = input("Please Enter Your Name: ")
    return name
def user_age():
    age = input("Please Enter Your age: ")
    return int(age)
def user_age_in_seconds(age):
    return age * 365.25 * 24 * 60 * 60
def decades_lived(age):
    return age // 10
def display_user_info():
    userName = user_name()
    userAge = user_age()
    ageInSeconds = user_age_in_seconds(userAge)
    decades = decades_lived(userAge)
    
    print(f"Hello {userName}, You have lived for {decades} decades, {ageInSeconds} seconds, whih means you are {userAge} years old.")
    
display_user_info()

    