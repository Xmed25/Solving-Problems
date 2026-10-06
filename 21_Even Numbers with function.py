# Problem — Even Numbers

# Write a function called count_even().

# The function receives a list of numbers and returns the number of even numbers.

# Example:
# numbers = [10, 7, 4, 9, 12, 5]

# print(count_even(numbers))

# Expected:

# 3

def count_even(num):
    even=0
    for e in num :
        if e%2==0:
            even+=1
    return even
print(count_even([10, 7, 4, 9, 12, 5]))
