# Problem - is_even()
# Write a function called is_even() that:

# Takes one number.
# Returns True if the number is even.
# Returns False if it is odd.

# Example:

# print(is_even(8))

# Expected:

# True

def is_even(num):
  if num%2==0:
    return True
  else:
    return False
print(is_even(6))
