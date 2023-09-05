my_string = "This is my first string"
print(my_string)
my_new_string = """ This\
                    is\
                    my\
                    new\
                    string"""
print(my_new_string)
# one character - one element
string1 = "Cisco Router"
# How to extract the first character of the string
# variable_name[index]
print(string1[0])
# Extract the space character
print(string1[5])
print(string1[-8])
print(string1[2])
# print("Hello Everyone!")
#len() function
print(len(string1))
newspaper = """What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham."""
# print(len(newspaper))
print(string1[11])
# print(string1[100]) # returns an IndexError -> index out range 
a = "Cisco Switch"
print(a.index("i"))
# You can find how many times a character appears in a sequenc/string -> index() function
print(a.count("i"))
print(a.count("c"))
print(a.count("C"))
#you can search for a sequence inside a string -> find()method
print(a.find("sco")) # returns 2
# if python doesn't find a match -> returns -1
print(a.find("xyz")) # returns -1 
# turn a string to upper -> upper()
print(a.upper())
# turn a string to lower -> lower()
print(a.lower())
# strings are immutable -> lower() and upper()only returns a copy of the string
print(a)
# You can also verify that a string starts or end with a particular character or a substring using startswith() and endswith()
print(a.startswith("C"))
print(a.startswith("c"))

print(a.endswith("h"))
print(a.endswith("tch"))

# Three important methods when working with string
# 1. strip()
# Eliminates all white spaces at the start and end of a string
b = "    Cisco Switch   "
print(b)
print(b.strip())

b = "$$$Cisco Switch$$$$$"
print(b)
print(b.strip("$"))

# replace() function ->
b = "    Cisco Switch   "
print(b.replace("i", "#"))

# 2. split()
# splits a string into substrings
# The result of this method is a list
d = "Cisco,Juniper,HP,Avaya,Nortel"
print(d.split(","))
# 3. join()
# C_i_s_c_o

a = "Cisco Switch"
print("_".join(a))
a = 2
a = 4
a = 6
print(a)
first_name="Ian"
last_name="Oguye"

print("My name is " + first_name + " " + last_name)

# 2. using the format() method
print("My name is {} {}. ".format(first_name, last_name))
print("My name is {fname} {lname}. ".format(fname = first_name, lname = last_name))




# 3. f-string foematter
print(f"My name is {first_name} {last_name}.")

user_age = 18
print(f"I am {user_age} years old")

print("Hello Everyone, " + "My name is {fname} {lname} ".format(fname = first_name, lname = last_name)  + "and" + " " + f"I am {user_age} years old. ")

print("Hello Everyone, My name is " + first_name + " " + last_name + " and I am " + str(user_age) + "years")

x = "Cisco"
print("o" in x)
print("c" in x)
print("C" not in x)
string1 = "0 E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

# lets extract the first IP Address in our string1 ->10.110.8.9
print(string1[ -9:-1])
print(string1[ -5:])
print(string1[ :-5])
print(string1[ :55])

# skip every second character using a string
# variable_name[start_index:stop_index:step]
print(string1[::2])


# reverse a string using a step(-1)

print(string1[::-1])


first_name = "Ian"
last_name = "Oguye"

print("My name is {} {}. ".format(first_name, last_name))

# Prompt the user to enter their name and age 
user_name = input("Please enter your name: ")
user_age = int(input("enter your age too: "))

#calculate/convert their age in seconds
age_in_seconds = user_age * 365.25 * 24 * 60 * 60

# Print out the user info in a nice format

print(f"Hello {user_name}, You are {user_age} years old and youve lived for {age_in_seconds} seconds")





