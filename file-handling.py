# working with files in python

# we use the open() function when working with files
# the open()function takes in 2 parameters when you want to open a file 
# The params:
# 1. filename (name of the file that you want to open)
# 2. mode (mode that you want to open the file with)

#We have several modes:
# 1. read -> 'r' : opens a file for reading and raises an error if the file doesn't exist
# 2. append -> 'a' : opens a file to append to it, creates the file if it doesn't exist
# 3. write -> 'w' : opens a file to write to it, overwrites the existing content, creates the file if it doesn't exist
# 4. create -> 'x' : creates a new file

# # 1. Reading from a file
# file = open("fruits.txt", "r")
# file_contects = file.read()
# file.close()
# print(file_contects)

# # 2. appending to a file
# fruit = "berries"

# file = open("fruits.txt", "a")
# file.write(fruit + "\n")
# file.close()

# # 3. writing to file
# file = open('fruits.txt', 'w')
# fruit = "oranges"
# file.write(f"{fruit}\n")
# file.close()

# 4. delete
import os
os.remove("fruits.txt")

# 1. write a short python script which queries the user for input(infinite loop with exit possibility) and writes the input to a file

# 2. Add another option to your user interface: the user should be able to output the data stored in the file in the terminal

# 3. store user input in a list(instead of directly adding it to a file) and write that list to the file -> using JSON and PICKLE