import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
# Check the version of pandas installed
print(pd.__version__)

#Lets a dictionary
courses = {
    "course_name": ["Python", "Pandas", "Java", "PHP"],
    "course_fee": [45000, 40000, 45000, 45000],
    "duration": ["25days", "23days", "30days", "26days"]
}

#Create dataframe indexes
index_labels = ["a1", "a2", "a3", "a4"]

#Create a pandas dataframe
df = pd.DataFrame(data=courses, index=index_labels)


# print(df)
# create a db connection 
conn = sqlite3.connect("cinema.db")

print(sqlite3.sqlite_version)

query = "SELECT * FROM card"
query = "SELECT * FROM seat"

dataframe = pd.read_sql(query, conn)


# Scatter graph
dataframe.plot(x="seat_id", y="price", kind='pie')
plt.show()

print(dataframe)