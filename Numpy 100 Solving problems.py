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


