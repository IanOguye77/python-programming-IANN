import sqlite3

# check the version
print(sqlite3.sqlite_version)

# create a demo database
db = "demo.db"

# Connect to the db
conn = sqlite3.connect(db)

# print(conn)

# Create a cursor object
cursor = conn.cursor()
# C - create
# R - read/retrieve
# U - update
# D - delete

# Createbour first table -> employees
query = '''
    CREATE TABLE IF NOT EXISTS employee (
        id integer PRIMARY KEY AUTOINCREMENT,
        full_name char(30) not null,
        age int not null,
        email char(50)
    )
    '''

# execute the query
cursor.execute(query)

# close the connection
# conn.close()
# close the connection

# success message if the table was created
print("Created table Employees...")

# 1. CREATE
# let's create employees
# create_query = "INSERT INTO employee (full_name, age, email)VALUES ('Employee 5', 22, 'employee1@email.com')"


# execute query
# cursor.execute(create_query)

# commit changes
conn.commit()

print("Inserted Data")

# R -> Read
# Let's read data from database
# create our read/fetch query
read_query = "SELECT id, full_name, age, email FROM employee"
read_query = "SELECT * FROM employee"

# execute our fetch query
cursor.execute(read_query)

# Get all the employees from the database
employees = cursor.fetchall()

# Display the results
# print(employees)
# for employee in employees:
#     print(employee[1])

# fetch one record/employee
# select_one_query = "SELECT * FROM employee"
# cursor.execute(select_one_query)
# employee = cursor.fetchone()
# print(employee)

select_many_query = "SELECT * FROM employee"
cursor.execute(select_many_query)
employees = cursor.fetchmany(3)
# print(employees)

# Reading Data Using Parameters
params = (22,)

query = "SELECT * FROM employee WHERE age > ?"
cursor.execute(query, [20])
employees_above_20 = cursor.fetchall()
print(employees_above_20)

# U - Update
# update_query = "UPDATE employee SET age = ? WHERE email = ?"
# cursor.execute(update_query, (25, "employee2@email.com"))
# conn.commit()
# updated_employee = cursor.fetchone()
# print(updated_employee)

# D - Delete
# Lets delete employee
# delete_query = "DELETE FROM employee WHERE id = ?"
# cursor.execute(delete_query, (1,))
# conn.commit()

# delete_query = "DELETE FROM employee"
# cursor.execute(delete_query)
# conn.commit()


