# Tuples


my_tuple = ()
print(type(my_tuple))
print(my_tuple)

my_tuple = (9)
print(type(my_tuple))

my_tuple = (9,)
print(type(my_tuple))

# lets populate our tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# tuples - indexing
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[-2])

# my_tuple[1] = 10 -> returns a type error : tuple object doesnt support item assignment

tuple1 = ("Cisco", "2600", "12.4")

(vendor, model, ios) = tuple1

print(vendor)
print(model)
print(ios)

# This is also called tuple packing and unpacking and you can see it as a kind of mapping betwwen elements of different tuples.

tuple2 = (1, 2, 3, 4)
(w, x, y, z) = tuple2

(a, b, c) = (10, 20, 30)
print(a)
print(b)
print(c)
# Tuple Methods

# As with strings and lists, we can perform some basic operations on tuples too

#We can use the len() function to find out the number of elements of a tuple

print(len(tuple2))

# We have the min() and max() functions available in finding the lowest and greatest value inside a tuole

print(min(tuple1))
print(max(tuple2))

tuple3 = ("Jane", "Janet")
print(min(tuple3))

print(tuple2 + (5, 6, 7))
print(tuple2 * 3)
# (1, 2, 3, 4) 
print(tuple2[0:4]) 
# (1, 2)
print(tuple2[-4: -2])
#(1, 3)
print(tuple2[::2])

# You can check if an element is a member of a tuple or not using 'in' and 'not in'
print(3 in tuple2)
print(3 not in tuple2)
print(5 not in tuple2)

# we can use the 'del' command to delete the entire tuple
del tuple2
print(tuple2)


