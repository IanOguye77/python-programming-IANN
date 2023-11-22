# JSON -> JavaScript Object Notation
# python comes with a bultin module/file with the json so you cannot have a file with the same name(json.py)
# To use python json module, ypu have to import it
import json

# if you help with json
# print(help(json))
# print(dir(json))

# 1. Converting to a python object (from a JSON string)

# JSON object -> has double quotes
person = '''{
    "name": "Pach",
    "age": 18,
    "city":"Juba"
}'''

# Convert to json string/object
# We use loads() to convert a python object to a json string
person_json_data = json.loads(person)
print(person_json_data)

# Python object -> has single quotes
print({"name":"Pach", "age":18})

# 2. convert to json
product = {
    'name': 'Product 1',
    'code': 'F999',
    'price': 159.99,
    'quantity': 6
}

product_json_data = json.dumps(product)
print(product_json_data)
# print(type(product_json_data))

# Create a list of "person" dictionaries with a name, age and a list of hobbies for each person.
# Convert the list of person to a json string
persons = [
    {
    'name': 'Ian',
    'age': 18,
    'hobbies': ['Gaming', 'dancing', 'eating']
   },
   {
    'name': 'Nai',
    'age': 19,
    'hobbies': ['Swimming', 'coding']
   },
   {
    'name': 'Ani',
    'age': 20,
    'hobbies': ['Painting', 'Travelling']
   }
]
print(persons)
# extract painting
print(persons[2]['hobbies'][1])
# person_json_data = json.dumps(person)
# print(person_json_data)
