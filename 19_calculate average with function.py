# Problem
# Write a function:
# calculate_average()
# It should accept any number of numbers using *args and return their average.

# Example:
# print(calculate_average(10, 20, 30))

# Expected:
# 20.0

def calculate_average(*args):
  return sum(args)/len(args)
print(calculate_average(10,20,30))
