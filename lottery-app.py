# Lottery App
import random

# we need three functions
# 1. for getting the user lucky numbers
# 2. for generating the winning numbers
# 3. for displaying a menu to the user

def menu():
    # ask the user for the numbers 
    user_numbers = get_player_numbers()
    # create lottery numbers
    lottery_numbers = create_lottery_numbers()
    # print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    prize = 100 ** len(matched_numbers)
    print(f"The winning numbers were: {lottery_numbers}")
    print(f"You matched {matched_numbers} numbers and won Kes{prize}")
# a function to create the winning numbers -> rondom module
def create_lottery_numbers():
    # values = []
    # for value in range(6):
    #     values.append(random.randint(1, 20))
    # return values
    # create an empty set for the random lucky numbers
    values = set()
    # loop as long as the length of the set is less than 6
    while len(values) < 6:
        values.add(random.randint(1, 50))
        # return the values set
    return values

# a function to get user numbers for the lottery draw
def get_player_numbers():
    # prompt the user for six numbers
    numbers_csv = input("Enter Six Numbers Separated by comma: ")
    # create a set of numbers from this numbers_csv
    numbers_list = numbers_csv.split(",")
    # create an empty set to add the numbers
    numbers_set = set()
    # use a for loop to add the number in the empty set
    for number in numbers_list:
        numbers_set.add(int(number))
    # return the set
    return numbers_set
    
# print(create_lottery_numbers())
# print(get_player_numbers())
menu()