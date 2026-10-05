# Problem 1 — Filter & Transform

# Given:
# numbers = [3, 8, 12, 5, 20, 7, 14, 9]

# Write a program that creates a new list containing:

# Only numbers that are even
# Only numbers greater than 10
# Store their squares
# Expected Output:
# [144, 400, 196]

numbers = [3, 8, 12, 5, 20, 7, 14, 9]

result=[u**2 for u in numbers if u > 10 and u%2==0 ]
print(result)


# using for loop 

numbers = [3, 8, 12, 5, 20, 7, 14, 9]
res=[]
for i in numbers:
  if i>10 and i%2==0:
    res.append(i**2)
print(res)
