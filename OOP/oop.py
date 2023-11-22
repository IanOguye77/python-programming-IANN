# OOP -> Object-Oriented programming
# Modelling things in form of objects

# object -> a real world entity
#        -> an instance of a class
#        -> may be regarded as an instance of a defiend class and attribute values for a particular object define the state of that object.

# Class -> is a template or blueprint that you use to create an object
#       -> is a data type containing its own variables, attributes and functions (which, by the way, in object-Oriented programming are called methods.)
# Example -> a blueprint of a house is a class, then the real house that will be built from that blueprint is the object
# Example -> Human is a class -> then we can create many people from the Human class

# Inheritance -> this is when a class may inherit (acquire) all the names and functionalities from an existing class.

# Syntax for a class
# class class_name:
#     pass

# THE __INIT__METHOD
# The special __init__ method is a class constructor
# The word init should be preceeded and followed by double underscore(__).
# The role of __init__ is to intialize some variables and the method is called whenever you create a new instance of the class in which it resides.
# Actually, it is the first code that is executed whenever you create a new instance of the class.

# Any special method or regular method within a class is defined using the def keyword, as you do with regular functions.
# The difference here is that each time you define a method inside a class, the first parameter inside the parameter is self

# Self is no more than just a reference to the current instance of the current.
# After typing self, you define any other parameters that you want to be defined and initialized whenever you create a new instance of the class which it resides.
# Our First Class
class MyRouter(object):
    "This is a class that describes a characteristics of a router"
    def __init__(self, routerName, model, serialNo, ios):
        self.routerName = routerName
        self.model = model
        self.serialNO = serialNo
        self.ios = ios
    def print_router(self, manuf_date):
        print("The Router Name is: ", self.routerName)
        print("The Router Model is: ", self.model)
        print("The Serial Number of the Router is: ", self.serialNO)
        print("The IOS Version of the Router is: ", self.ios)
        print("The model and date combined : ", self.model + manuf_date)
        # TO DO

# Create our first object
# To create an object, you simply type the class name and enter the arguments required by the __init__ method, in between the parenthenses - all of them except, except self, which is automatically passed by Python
# router1 = MyRouter("R1", "2600", "123456", "12.4")

# What can we do with this object
# First, you can access each of its attributes
# print(router1.routerName)
# print(router1.model)
# print(router1.serialNO)
# print(router1.ios)

# What else
# router1.print_router("9/1/2023")+

# from datetime import datetime
# print(datetime.now())

# router2 = MyRouter("R2", "7600", "232323", "12.2")

# router2.ios = "15.6"

# router2.print_router("-1234567890")

# INHERITANCE

# The child class -> class taht acquires/inherits from the super class (parent)
class MyNewRouter(MyRouter):
    def __init__(self, routerName, model, serialNo, ios, portsNo):
        MyRouter.__init__(self, routerName, model, serialNo, ios)
        self.portsNo = portsNo

    def print_new_router(self, string):
        print(string + self.model)

newRouter = MyNewRouter("newR1", "1800", "111111", "12.2", "10")

newRouter.print_router("-123")