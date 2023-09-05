# Booleans - logical Operators
# Lets evaluate some basic expressions

print(1 == 1) # returns True
print(1 == 2) # returns False

print("Python" == "python") # return False
print(type("Python") == type("python")) #return True
print(3 <= 4) #return True

# There are three main boolean operations, each of them having a specific operator namely -> "and", "or" and "not"
# 1. and -> means both operands should be True, in order to have the entire erpression evaluated as True
a = (1 == 2)
b = (2 == 3)

print(a and b) # returns False

# 2. or -> if at least one of the expressions evaluates to True, then the final result is True. If they are both False, then the final result will be False, as well.
# -> When using "or", it is enough if only one expression is True, in order to have True as the final result.

# 3. not -> means simply denying an expression. if that expression is True, then denying it will result to False and vice-versa
print(not(1 == 1)) 

# # log in application

# # database values
# username_db = "dennis"
# password_db = "password"

# # user credentials -> from the user
# userName = "dennis"
# password = "password"

# # log in the user
# if userName == username_db and password == password_db:
#     # if username matched ... log in the user
#     print("Logged in Successfully")
# else:
#     # raise an error
#     print("Invalid Username or Password...")

# bool() function -> to help us evaluate values and expressions as True or False
# Lets use bool() to check the always False values
print("==============================================")
print(bool(None))
print(bool(0))
print(bool(0.0))

# Lets use bool() to check the always True values
print("==============================================")
print(bool(1))
print(bool(1.1))
print(bool("Hello"))
print(bool([]))


