#### 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np
#### 2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)
#### 3. Create a null vector of size 10 (★☆☆)
arr=np.zeros(10)
print(arr)
#### 4. How to find the memory size of any array (★☆☆)
import sys
print(sys.getsizeof(arr))
#### 5. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
ze=np.zeros(10)
ze[4]=1
print(ze)
#### 5. Create a vector with values ranging from 10 to 49 (★☆☆)
vector=np.arange(10,50)
#### 7. Reverse a vector (first element becomes last) (★☆☆)
print(vector[::-1])
#### 8. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
matrix=np.arange(9).reshape(3,3)
print(matrix)
#### 9. Find non-zero elements from [1,2,0,0,4,0] (★☆☆)
l=[1,2,0,0,4,0]
x=np.array(l)
print(x[x>0])
#### 10. Create a 3x3 identity matrix (★☆☆)
matrix=np.eye(3)
print(matrix)
#### 11. Create a 3x3x3 array with random values (★☆☆)
tensor=np.random.random((3,3,3))
print(tensor)
#### 12. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
md=np.random.random((10,10))
print(np.max(md))
print(np.min(md))
#### 13. Create a random vector of size 30 and find the mean value (★☆☆)
rn=np.random.random((30))
print(np.mean(rn))

# Problem 14  
# Create a NumPy array containing the following numbers:
# [10, 20, 30, 40, 50]

# Tasks:
# 1. Print the array.
# 2. Print its shape.
# 3. Print its data type.
# 4. Print its size.
import numpy as np
arr=np.arange(10,51,10)

print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.size)

# Problem 15 
# Given:
# import numpy as np  
# numbers = np.array([10, 20, 30, 40, 50])

# Tasks:
# 1. Add 5 to every element.
# 2. Multiply every element by 2.
# 3. Subtract 10 from every element.
# 4. Divide every element by 5.
import numpy as np  

numbers = np.array([10, 20, 30, 40, 50])

numbers+=5
print(numbers)
print(numbers*2)
print(numbers-10)
print(numbers/5)

# Problem 16 
# Given:
# numbers = np.array([15, 25, 35, 45, 55, 65])

# Tasks:
# 1. Print the first element.
# 2. Print the last element.
# 3. Print the third element.
# 4. Print the elements from index 1 to 4.
# 5. Replace the second element with 100.
import numpy as np

numbers=np.arange(15,66,10)

print(numbers[0])
print(numbers[-1])
print(numbers[2])
print(numbers[1:4])
numbers[1]=100
print(numbers)

# Problem 17
# Given:
# [12, 45, 67, 23, 89, 34, 90, 10]

# Tasks:
# 1. Print numbers greater than 50.
# 2. Print numbers smaller than 30.
# 3. Print all even numbers.
# 4. Count how many numbers are greater than 40.
import numpy as np

nums=np.array([12, 45, 67, 23, 89, 34, 90, 10])

print(nums[nums>50])
print(nums[nums<30])
print(nums[nums%2==0])
print(len(nums[nums>40]))

# Problem 18 
# Given:
# scores = np.array([85, 90, 75, 60, 95, 80, 70])

# Tasks:
# 1. Calculate the total score.
# 2. Calculate the average score.
# 3. Find the maximum score.
# 4. Find the minimum score.
# 5. Calculate the standard deviation.
import numpy as np
scores = np.array([85, 90, 75, 60, 95, 80, 70])

print(np.sum(scores))
print(np.mean(scores))
print(np.max(scores))
print(np.min(scores))
print(np.std(scores))

# Problem 19 
# Given:
# sales = np.array([    [100, 200, 300],    [150, 250, 350],    [200, 300, 400]])

# Tasks:
# 1. Print the first row.
# 2. Print the second column.
# 3. Print the value 250.
# 4. Calculate the sum of each row.
# 5. Calculate the sum of each column
import numpy as np
sales = np.array([   
  [100, 200, 300],   
  [150, 250, 350],   
  [200, 300, 400]])

print(sales[0])         # First row

print(sales[:,1])       # Second Column

print(sales[1][1])      

row=np.sum(sales,axis=1) # Sum of each row
col=np.sum(sales,axis=0) # Sum of each column

print(row)
print(col)

# Problem 20 – Sales Analysis 
# Given:
# products = ["Laptop", "Keyboard", "Mouse", "Monitor"]
# sales = np.array([    [1200, 1500, 1800],    [800, 900, 1100],    [500, 700, 650],    [1000, 1200, 1400]])

# Tasks:
# 1. Calculate the total sales for each product.
# 2. Find the product with the highest total sales.
# 3. Calculate the average sales for all products.
# 4. Find the highest single sales value.
import numpy as np

products = ["Laptop", "Keyboard", "Mouse", "Monitor"]

sales = np.array([
    [1200, 1500, 1800],
    [800, 900, 1100],
    [500, 700, 650],
    [1000, 1200, 1400]
])

for x in range(len(products)):
  print(f"{products[x]}: Total {sales[x].sum()} ,  Average = {sales[x].mean():.2f}")
  
high_index=np.argmax(np.sum(sales,axis=1))
print(f"the product with the highest total sales is {products[high_index]} : {np.sum(sales,axis=1).max()}")

high = np.max(sales)
print(high)
# Problem 21
# Given:
# import numpy as np
# arr = np.array([    [10, 20, 30],    [40, 50, 60],    [70, 80, 90]])

# Tasks:
# 1. Print the element 50.
# 2. Print the second row.
# 3. Print the third column.
# 4. Print the first two rows.
import numpy as np
arr = np.array([    
       [10, 20, 30],  
       [40, 50, 60],  
       [70, 80, 90]])
print(arr[1][1])  #the element 50.
print(arr[1])     #the second row.
print(arr[:,2])   #the third column.
print(arr[0:2])   #the first two rows


# Problem 22 – Conditional Filtering
# Given:
# arr = np.array([12, 45, 67, 23, 89, 34, 90, 56, 11])

# Tasks:
# 1. Extract all numbers greater than 40 and less than 90.
# 2. Extract all even numbers greater than 20.
# 3. Replace all numbers below 30 with 0.
import numpy as np
arr = np.array([12, 45, 67, 23, 89, 34, 90, 56, 11])
print(arr[(arr>40)&(arr<90)])
print(arr[(arr>20)&(arr%2==0)])
arr[arr<30]=0
print(arr)


# Problem 23 
# Given:
# sales = np.array([    [1200, 1500, 1800],    [800, 900, 1100],    [500, 700, 650],    [1000, 1200, 1400]])

# Tasks:
# 1. Calculate the total sales for each product (row).
# 2. Calculate the total sales for each month (column).
# 3. Find the highest total product sales.
import numpy as np
sales = np.array([    
  [1200, 1500, 1800],
  [800, 900, 1100],    
  [500, 700, 650],    
  [1000, 1200, 1400]])

data=np.sum(sales,axis=1)
print(data)
print(np.sum(sales,axis=0))
print(data.max())



# Problem 24 – Find Maximum and Minimum Indices
# Given:
# arr = np.array([15, 82, 34, 91, 27, 63, 45])

# Tasks:
# 1. Find the maximum value.
# 2. Find its index.
# 3. Find the minimum value.
# 4. Find its index.
import numpy as np
arr = np.array([15, 82, 34, 91, 27, 63, 45])
print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.argmin())

# Problem 25 
# Given:
# arr = np.array([45, 12, 89, 23, 67, 34, 90, 10])

# Tasks:
# 1. Sort the array in ascending order.
# 2. Sort it in descending order.
# 3. Extract the three largest values.
import numpy as np
arr = np.array([45, 12, 89, 23, 67, 34, 90, 10])
                                         
arr.sort()
print(arr)
print(arr[::-1])
print(arr[-3:])

# Problem 26 
# Given:
# arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 10])

# Tasks:
# 1. Find all unique values.
# 2. Count how many times each unique value appears.
# 3. Find the most frequent value.
import numpy as np
arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 10])
print(np.unique(arr))
unique, counts = np.unique(arr, return_counts=True)
print(unique)
print(counts)
print(unique[counts.argmax()])

# Problem 27 
# Given:
# arr = np.arange(1, 25)

# Tasks:
# 1. Reshape it into a 4×6 array.
# 2. Reshape it into a 2×3×4 array.
import numpy as np
arr = np.arange(1, 25)
print(arr.reshape(4,6))
print(arr.reshape(2,3,4))

# Problem 28 
# Given:
# a = np.array([10, 20, 30, 40, 50])
# b = np.array([15, 20, 25, 40, 60])

# Tasks:
# 1. Find elements where a is greater than b.
# 2. Find elements where both arrays have equal values.
# 3. Count how many elements are equal.
# 4. Calculate the difference a - b.
import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([15, 20, 25, 40, 60])
print(a[a>b])
print(a[a==b])
print(len(a[a==b]))
print(a-b)

# Problem 29 
# Given the scores array:
# 1. Calculate the average score of each employee.
# 2. Find the highest score of each employee.
# 3. Find the lowest score of each employee.
# 4. Calculate the average score of each subject.
# 5. Find the employee with the highest overall average.

import numpy as np

employees = np.array([
    ["Goku", "IT", 85, 90, 88],
    ["Vegeta", "Sales", 78, 82, 80],
    ["Gohan", "IT", 92, 95, 94],
    ["Piccolo", "HR", 75, 80, 78],
    ["Trunks", "Sales", 88, 85, 90],
    ["Luffy", "IT", 95, 91, 96],
    ["Zoro", "HR", 70, 75, 72],
    ["Nami", "Sales", 90, 92, 89],
    ["Light", "IT", 83, 87, 85],
    ["L", "HR", 98, 96, 97]
])

names = employees[:, 0]
scores = employees[:, 2:].astype(int)
avg_scores = np.mean(scores, axis=1)
max_scores = np.max(scores, axis=1)
min_scores = np.min(scores, axis=1)
subject_avg = np.mean(scores, axis=0)
best_index = np.argmax(avg_scores)

print("Employee Statistics:")

for i in range(len(names)):
    print(
        f"{names[i]}: Average = {avg_scores[i]:.2f}, "
        f"Highest = {max_scores[i]}, "
        f"Lowest = {min_scores[i]}"
    )

print("\nSubject Averages:")
print(f"Subject 1: {subject_avg[0]:.2f}")
print(f"Subject 2: {subject_avg[1]:.2f}")
print(f"Subject 3: {subject_avg[2]:.2f}")

print("\nBest Employee:")
print(f"{names[best_index]}: {avg_scores[best_index]:.2f}")

# Problem 30 
# Create a NumPy array containing the numbers from 1 to 10.

# Requirements:
# - Use np.arange().
# - Store the array in a variable named arr.
# - Print the array.
# - Print the sum of all its elements.
import numpy as np
arr=np.arange(1,11)
print(arr)
print(arr.sum())

# Problem 31 
# You are given the following array:
# import numpy as np
# numbers = np.array([12, 45, 23, 67, 34, 89, 15, 56])

# Write a program to calculate and print:
# 1. The maximum value.
# 2. The minimum value.
# 3. The average value.
# 4. The number of elements in the array.
import numpy as np
numbers = np.array([12, 45, 23, 67, 34, 89, 15, 56])

print(np.max(numbers))
print(np.min(numbers))
print(np.mean(numbers))
print(numbers.size)

# Problem 32 
# You have a dataset containing daily temperatures:
# import numpy as np
# temperatures = np.array([22, 25, 19, 30, 27, 33, 24, 28, 35, 21])

# Write a program to:
# 1. Print the first 4 temperatures.
# 2. Print the last 3 temperatures.
# 3. Print the temperature at index 5.
# 4. Print every second element in the array.
import numpy as np
temperatures = np.array([22, 25, 19, 30, 27, 33, 24, 28, 35, 21])
print(temperatures[:4])
print(temperatures[-3:])
print(temperatures[5])
print(temperatures[::2])

# Problem 33 
# You are given two arrays:
# import numpy as np
# a = np.array([10, 20, 30, 40, 50])
# b = np.array([2, 4, 6, 8, 10])

# Write code to print:
# 1. a + b
# 2. a - b
# 3. a * b
# 4. a / b
# 5. a ** 2
import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**2)

# Problem 34 
# You are given an array of student grades:
# import numpy as np
# grades = np.array([45, 78, 92, 55, 33, 88, 67, 95, 49, 81])

# Write a program to:
# 1. Select all grades greater than or equal to 70.
# 2. Select all grades below 50.
# 3. Select all grades between 60 and 90 (inclusive).
# 4. Count how many students passed (grade ≥ 50).
import numpy as np
grades = np.array([45, 78, 92, 55, 33, 88, 67, 95, 49, 81])

print(grades[grades>=70])
print(grades[grades<50])
print(grades[(grades>=60) & (grades<=90)])
print(len(grades[grades>=50]))

# Problem 35 
# You have the following array:
# import numpy as np
# numbers = np.arange(1, 13)

# Write a program to:
# 1. Reshape the array into 3 rows and 4 columns.
# 2. Print the new array.
# 3. Print its shape.
# 4. Print its number of dimensions.
import numpy as np
numbers = np.arange(1, 13)
print(numbers.shape)
arr=numbers.reshape(3,4)
print(arr)
print(arr.shape)
print(arr.ndim)

# Problem 36 
# You have a dataset containing product prices:
# import numpy as np
# prices = np.array([250, 100, 350, 200, 100, 450, 250, 300, 150, 350])

# Write a program to:
# 1. Sort prices from smallest to largest.
# 2. Sort prices from largest to smallest.
# 3. Extract only unique prices (remove duplicates).
# 4. Find the number of unique prices.
import numpy as np
prices = np.array([250, 100, 350, 200, 100, 450, 250, 300, 150, 350])

print(np.sort(prices))
print(np.sort(prices)[::-1])
unique,count=np.unique(prices,return_counts=True)
print(unique)
print(count)

# Problem 37 
# You have a dataset of student grades across three subjects:
# import numpy as np
# grades = np.array([    [80, 90, 70],    [60, 75, 85],    [90, 95, 100],    [70, 80, 75]])

# Each row represents a student, and each column represents a subject.

# Write a program to:
# 1. Calculate the total grades for each student.
# 2. Calculate the average grade for each subject.
# 3. Find the highest grade for each student.
# 4. Find the lowest grade for each subject.
import numpy as np

grades = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 100],
    [70, 80, 75]
])

print(np.sum(grades,axis=1))
print(np.mean(grades,axis=0))
high=np.max(grades,axis=1)
print(high)
print(np.min(grades,axis=0))

# Problem 38 
# A company records its monthly online and store sales.
  
# import numpy as np
# online_sales = np.array([500, 700, 900, 600])
# store_sales = np.array([800, 600, 1000, 900])

# Write a program to:
# 1. Combine both arrays into one array.
# 2. Calculate the total online sales.
# 3. Calculate the total store sales.
# 4. Calculate the difference between store and online sales for each month.
# 5. Calculate the average of all sales combined.
import numpy as np
online_sales = np.array([500, 700, 900, 600])
store_sales = np.array([800, 600, 1000, 900])

print(np.concatenate((online_sales,store_sales)))
print(np.sum(online_sales))
print(np.sum(store_sales))
print(store_sales-online_sales)
print(np.mean(np.concatenate((online_sales,store_sales))))

# Problem 39 
# Final beginner challenge
# A small company wants to analyze its daily sales.

# Use this dataset:
# import numpy as np
# sales = np.array([    1200, 1500, 900, 2300, 1800,    2700, 1100, 3000, 2100, 1600])

# Write a program that calculates and prints:
# 1. Total sales.
# 2. Average sales.
# 3. Highest sale.
# 4. Lowest sale.
# 5. All sales greater than the average.
# 6. Number of sales greater than the average.
# 7. Sales sorted from highest to lowest.
# 8. Index of the highest sale.
# 9. Number of sales greater than or equal to 2000.
import numpy as np

sales = np.array([
    1200, 1500, 900, 2300, 1800,
    2700, 1100, 3000, 2100, 1600
])

print(np.sum(sales))
print(np.mean(sales))
print(np.max(sales))
print(np.min(sales))
print(sales[sales>np.mean(sales)])
print(np.sort(sales)[::-1])
print(np.argmax(sales))
print(len(sales[(sales>=2000)]))




