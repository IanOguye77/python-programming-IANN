# create our first empty list
list1 = []

print(type(list1)) # returns class list

# lets add items to our empty list1
list1 = ["Cisco", "Juniper", "Avaya"]

# Lets us remember the len() from strings and use it on our list
print(len(list1))

# Lets see how we can access elements inside a list, Well the same way we did with characters in a string, using indexes
# access the first element in our list

print(list1[0])
print(list1[2])

print(list1[-2])
print(list1[-1])

# As with strings, if we enter an invalid index we will get an "IndexError" in return, stating that the list index is out of range

# To check that lists are mutable, lets replace an element in the list -> we just have to use the equal sign to modify this
list1[2] = "HP"
print(list1)

# To update a list, just type in the name of the variable pointing to the list an in between square brackets, you have to insert the index at which you want the replacement to be made, Finally, following the equal sign, just enter the new element and thats it.

# List Methods

# Lets consider list2
list2 = [-11, 2, 12]
# max value
print(max(list2))
# min value
print(min(list2))

# what about list of strings
list3 = ["a", "b", "c"]
print(max(list3))

print("a" > "A")

# print(max("a", "B", 100, -2))



# lets check the available list methods we have at hand

# First, we should learn how to append a new element to a list.consider list1
print(list1)

# To append an element to this list, just use the append() method

list1.append(100)
print(list1)

# we have 3 ways/options for removing list element(s)
#1. del command
# del list_name[element_index]
del list1[3]

list2 = [9, 99, 999]

list1.extend(list2)

print(list1)

#students_names = input("Enter the names of 5 students with no spaces separated with a comma: ")
#students_list = students_names.split(",") 
#print(students_list)

# print(list1.index(-11))

# append some values
list1.append(10)
list1.append(10)
list1.append(10)

# count the occurrence of 10
print(list1.count(10))

list2.append(1)
list2.append(25)
list2.append(500)

# sort the list in an ascending order
list2.sort()
print(list2)

#what is we want the elements sorted in a reverse or descending
list2.reverse()
print(list2)

# NB: The two methods youve just seen are modifying the list in place,meaning that after you apply the method there is no other list created.
# To sort the elements of a list and create a new list in memory at the same time you have the sorted() function available.

print(sorted(list2))
# print(list2) 

# Now, if you want to use the same function to reverse the order, just add an argument inside the parenthesis. This argument is called reverse and it must have the value of True assigned to it.
print(sorted(list2, reverse=True))

# You can use the help() command to know more about a bultin function
print(help(len))

# You can concatenate or repeat a list using plus and multiplication operator
print(list1 + list2)

# repeating a list
print(list2 * 5)

#list slices
# list slices allow us to extract various parts of a sequence.
# var1[5:10]

list3 = [1, 2, 3, 'a', 'b', 'c']

# Etract the following
list1 = [1, 2, 3]  

# user_age = int(input("enter your age: "))

# age_in_decades = user_age // 10

# print(f"You are {user_age} years old and you have lived for {age_in_decades} decades")

set1 = {1, 2, 3, 4}

set2 = {3, 4, 8}

print(set1.intersection(set2))
print(set2.intersection(set1))

# lets see which elements does set 1 have and set 2 doesnt have, by using the difference() method.
print(set1.difference(set2))
print(set2.difference(set1))

# To unify the two sets, you can use the union() method, and the result, also being a set (a collection of unique elements), will include element 3 just once.
# NB -> Do not confuse set union with concatentation 

print(set1.union(set2))

# Another thing you can do is remove a random element i the set by using the pop() method

# print(set1.pop())
set1.pop()
print(set1)

# We can clear a set using the clear() method 

set1.clear()
print(set1)



