# Problem 1 - Pokemon search using Pandas
import pandas as pd

data=pd.read_csv(r"PATH FILE !",index_col="Name")

pokemon=input("Enter a pokemon: ").strip().capitalize()

try:
    print(f"Pokemon: {data.loc[pokemon]}")
except KeyError:
    print(f"{pokemon} not found !")

# Problem 2 – Create a DataFrame 
# Create a DataFrame containing the following data:
# Name	Age	Salart
# Spongebob	21	10000
# Patrick	23	5000
# Squidward	25	7000

# Tasks:
# 1. Import pandas as pd.
# 2. Create the DataFrame.
# 3. Print the DataFrame.
# 4. Print the first 2 rows.
import pandas as pd

data={
    "Name":["Spongbob","Patrick","Squidward"],
    "Age":[21,21,25],
    "Salary":[10000,5000,7000]
}

data=pd.DataFrame(data,index=["Employee 1 ","Employee 2 ","Employee 3"])
print(data)
print(data.head(2))

# Problem 3 – Select Columns 

# Given this DataFrame:
# data = {    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],    "Price": [15000, 300, 500, 4000],    "Quantity": [5, 20, 15, 8]}



# Tasks:
# 1. Print only the Product column.
# 2. Print only the Price column.
# 3. Print Product and Quantity together.
import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [15000, 300, 500, 4000],
    "Quantity": [5, 20, 15, 8]
}

data=pd.DataFrame(data)
print(data["Product"])
print(data["Price"])
print(data[["Product","Quantity"]])


# Problem 4 – Filtering Data 
# Using the same DataFrame from Problem 3:

# Tasks:
# 1. Find products with a price greater than 1000.
# 2. Find products with a quantity less than 10.
# 3. Find products with a price equal to 500.

import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [15000, 300, 500, 4000],
    "Quantity": [5, 20, 15, 8]
}

data=pd.DataFrame(data,index=[1,2,3,4])

print(data[data["Price"]>1000])
print(data[data["Quantity"]<10])
print(data[data["Price"]==500])

# Problem 5 – Using .loc[]
# data = {    "Name": ["Tom", "Jerry", "Spike", "mike"],    "Age": [21, 25, 19, 23],    "Score": [85, 90, 75, 95]}



# Tasks:
# 1. Select the row where Name is Tom.
# 2. Select the row where Age is greater than 20.
# 3. Display only the Name and Score columns for Mike.
# 4. Find the student with the highest score.
import pandas as pd

data = {
    "Name": ["Tom", "Jerry", "Spike", "Mike"],
    "Age": [21, 25, 19, 23],
    "Score": [85, 90, 75, 95]
}

data=pd.DataFrame(data)

print(data[data["Name"]=="Tom"])
print(data[data["Age"]>20])
print(data.loc[data["Name"]=="Mike", ["Name","Score"]])
print(data["Score"].max())

# 6. Import pandas under the alias pd.

import pandas as pd
 
# 7. Print the version of pandas that has been imported.

print(pd.__version__)

# 8. Print out all the version information of the libraries that are required by the pandas library.

pd.show_versions()

# import numpy as np
# Consider the following Python dictionary data and Python list labels:

# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 9. Create a DataFrame df from this dictionary data which has the index labels.

import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

data=pd.DataFrame(data,index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
# 10. Display a summary of the basic information about this DataFrame and its data (hint: there is a single method that can be called on the DataFrame).
print(data.describe)
 
# 11. Return the first 3 rows of the DataFrame df.
print(data.head(3))
 
# 12. Select just the 'animal' and 'age' columns from the DataFrame df.
print(data[["animal","age"]])
 
# 13. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
print(data.loc[data.index[[3,4,8]],["animal","age"]])
 
# 14. Select only the rows where the number of visits is greater than 3.
print(data[data["visits"]>3])
 
# 15. Select the rows where the age is missing, i.e. it is NaN.
print(data[data["age"].isnull()])
 
# 16. Select the rows where the animal is a cat and the age is less than 3.
print(data[ (data["animal"]=="cat") & (data["age"]<3)])

# 17. Select the rows the age is between 2 and 4 (inclusive).
print(data[data["age"].between(2,4)])
 
# 18. Change the age in row 'f' to 1.5.
data.loc["f","age"]=1.5
print( data)
 
# 19. Calculate the sum of all visits in df (i.e. find the total number of visits).
print(data["visits"].sum())
 
# 20. Calculate the mean age for each different animal in df.
print(data.groupby("animal")["age"].mean())
