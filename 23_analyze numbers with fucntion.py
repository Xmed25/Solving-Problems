# analyze_numbers(*numbers)

# The function should return three things:

# Sum
# Average
# Number of even numbers
# Example:
# result = analyze_numbers(10, 15, 20, 25, 30)

# print(result)

# Expected:

# (100, 20.0, 3)

def analyze_numbers(*num):
    even=0
    for e in num:
        if e%2==0:
            even+=1
    return sum(num),sum(num)/len(num),even
    
result=analyze_numbers(10, 15, 20, 25, 30)
print(result)
