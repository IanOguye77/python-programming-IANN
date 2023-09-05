# break, continue and pass
# The break and continue are used to handle the flow of a while or a for loop in a python program, meaning the programmer can interrupt or restart the execution of a loop structure, in certain conditions.

# Lets start with the break statement

#1. Break
#break is used to terminate the loop in which it resides
#lets see how break works

# for number in range(10):
#     if number == 7:
#         break
#     print(number)

# list1 = [4, 5, 6]
# list2 = [10, 20, 30]

# for x in list1:
#     for y in list2:
#         if y == 20:
#             break
#         print(x * y)
#     print("outside the nested loop")
    
#2. Continue
# When python stumbles upon a continue statement inside a for or while loop, it ignores the rest of the code below, for the current iteration, goes up to the top of the loop and immediately starts the next iteration

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        if y == 20:
            continue
        print(x * y)
    print("outside the nested loop")
    
# 3. Pass 
# Pass is the equivalent of "do nothing". it is actually just a placeholder, for whenever you want to leave the addition of a piece of code for later and move on to write other segments of your program.  
# Pass helps you to keep the syntax of your progrsm vslid and not get an error returned when running the program.
# if 10 == 10:
#     pass

# print(10)

# Challenge time
# create a times table from 1-12
# Hint: nested for loop

# Assignment
# Create a scientific calculator that performs the following operations
# addition, subtration, multiplication, division, power of the number, square root, modulus, interger division, logarithm, sin, cosine and tangent     
    