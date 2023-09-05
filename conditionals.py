# Python Conditionals - if / elif / else
# in python we have the if, elif, else statements for decision making.
# delimiters
# indentation
# meaning if, for and while blocks, functions and classes.
# Using identation means that whitespaces are used as delimiters for code blocks. (whitespaces -> 4spaces in a row or you can just use the tab key)
# after every if/for/while or function or class definition, you must use a colon, so that python will know that it should expect an indented block right after that statement.

# if syntax
# if condition :
#     code(s) to execute if condition is true

x = 4

if x > 5:
    print("x is greater than 5")
    print(x * 2)
    

# Else
x = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# The else statement 

# Elif
# granular
# let's say we want to print "x is greater than 5" if indeed x is greater than 5, "x is equal to 5" in case x will become equal to 5 at some point and "x is less than 5" for all other cases. we should then add the elif statement in between if and else.
# The else statement should always be the last statement in an if/elif/else block

x = 4
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
    
    
# temp = float(input("Please enter the temperature: "))

# if temp > 23:
#     print("Cover Your Tomatoes")
# elif temp == 23:
#     print("Enjoy a Fruit")
# else:
#     print("Uncover your tomatoes")
    
# Write a python program that asks the user for their name and scores for 5 units then store them in a list/tuple/set/dictionary. Then calculates the average mark of the student> The program then grades the student based on the average mark. use the following range table to grade the student
# range         grade
# 80 - 100      A
# 70 - 79       B
# 60 - 69       C
# 50 - 59       D
# 0 - 49        F
# Print the output in a nice format

# create an empty list
subjects = []
# create a grade variable
grade = ""

print("===" * 20)

print("\t\t\tCPL Grading System")

print("===" * 20)

# prompt the user for the student name
student_name = input("Please Enter the student name: ")

# Prompt the user for the scores
eng = int(input("Enter marks for English: "))
if eng >= 0 and eng <= 100:
    subjects.append(eng)
else:
    print("English marks should be between 0 and 100")
kisw = int(input("Enter marks for Kiswahili: "))
math = int(input("Enter marks for Maths:  "))
sci = int(input("Enter marks for Science: "))
sst = int(input("Enter marks for Social Studies: "))

print("===" * 20)




# store the marks in the subjects list
all_subjects = {'english': eng, 'kiswahili': kisw}
all_subjects["english"] + all_subjects["kiswahili"]
sum(list(all_subjects.values()))

subjects.append(kisw)
subjects.append(math)
subjects.append(sci)
subjects.append(sst)

# compute the total score
# total_score = sum(subjects)

# find the average score
average_score = sum(subjects) / len(subjects)

# check the avergae score and grade the student
if average_score >= 80 and average_score <= 100:
    grade = "A"
elif average_score >= 70 and average_score <= 79:
    grade = "B"
elif average_score >= 60 and average_score <= 69:
    grade = "C"
elif average_score >= 50 and average_score <= 59:
    grade = "D"
elif average_score >= 0 and average_score <= 49:
    grade = "F"
# output the total score
# print(grade)

# Output the student Info
if average_score > 100:
    print("Invalid Score, Please enter valid marks!!!")
else:      
    print(f"Hello {student_name}, You have Scored {average_score}%, Which is Grade: {grade}.")

print("===" * 20)

# Next -> Python Loops -> For Loop then later While loop