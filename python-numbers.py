
# num1 = 10
# num2 = 2.5

# # check the type of our variables
# print(type(num1))
# print(type(num2))


# # operations
# # Addition 1 + 2 
# print(4 + 2)
# # Subtraction 2 - 1
# print(2 - 1)
# # Division 5 / 2
# print(5 / 2)
# # interger division 5 // 2
# print(5 // 2)
# # Multiplication 4 * 2
# print(4 * 2)
# # Raising to power 4 ** 2
# print(4 ** 2)
# # Modulo (means finding out the reminder after the division of one number by another) 5 % 2
# print(4 + 2)

# # 2. Comparison
# # less than
# print(4 < 2)
# # greater than
# print(4 > 2)
# # less than or equal to <=
# print(4 <= 2)
# # greater than or equal to >=
# print(4 >= 2)
# # equals ==
# print(4 == 2)
# # Not equal !=
# print(4 != 2)

# # convert a float to an int 
# print(int(1.7))

# # convert an integer to a float
# print(float(2)) # the float() will ad .0

# # more function
# # 1. abs() absolute function 

# # 2. comparing two numbers
# # max() and min()

# first_name = "Ian"
# last_name = "Oguye"

# print("My name is {} {}. ".format(first_name, last_name))

# Prompt the user to enter their name and age 
user_name = input("Please enter your name: ")
user_age = int(input("enter your age too: "))

#calculate/convert their age in seconds
age_in_seconds = user_age * 365.25 * 24 * 60 * 60

# Print out the user info in a nice format

print(f"Hello {user_name}, You are {user_age} years old and you have lived for {age_in_seconds} seconds")

user_age = int(input("enter your age"))

age_in_decades = user_age // 10
print(f"You are {user_age} years old and you have lived for {age_in_decades} decades")



