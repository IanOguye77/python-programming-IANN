# person1 = input("Enter the name of your first friend: ")
# person2 = input("Enter the name of your second friend: ")
# person3 = input("Enter the name of your third friend: ")

# friends = [person1, person2, person3]
# print(friends)
friends = input("Enter three friend names, separated by commas (no spaces please): ").split(",") # returns a list of strings

people = open("people.txt", 'r')
people_nearby = people.readlines()
# people_nearby = [person.strip("\n") for person in people.readlines()]
people_nearby = []
for person in people.readlines():
    people_nearby.append(person.strip("\n"))
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

with open('nearby_friends', 'w') as f:
    for friend in friends_nearby_set:
        print(f"{friend} is nearby, plan a meetup with them!")
