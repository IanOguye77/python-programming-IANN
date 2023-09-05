# nested if statements

# string1 = "Cisco"

# if "i" in string1:
#     if len(string1) > 4:
#         if type(string1) == str:
#          print(string1, len(string1))

# You can express the above program like this
# if "i" in string1 and len(string1) > 4 and type(string1) == str:
#     print(string1, len(string1), type(string1))
    
# user_int = int(input("Please enter an interger: "))

# if type(user_int) is int:
#     if user_int > 10:
#         print("it is an interger and greater than 10")
#     elif user_int == 10:
#         print("it is an interger and equal to 10")
         
#     else:
#         print("it is an interger and less than 10")
        
# Nested for loop
# lets assume we have two lists and we want to multiply each element of the first by each element of the second. For this we iterate over both lists at the same time, take each element into account, do the multiplications and return the results.

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        print(x * y)
    print(x)
    
