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
