# Problem — Maximum Number

# Write a function:

# find_max(a, b, c)

# It should receive 3 numbers and return the largest number.

# Example:
# print(find_max(10, 25, 7))

# Expected:

# 25

# Challenge: Don't use max().

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(find_max(10, 25, 7))
