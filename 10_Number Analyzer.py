# Problem  — Number Analyzer

# Write a program that asks the user to enter a number and prints:

# Is it positive, negative, or zero?
# Is it even or odd?

# Example:

# Input:
# 7

# Output:
# Positive
# Odd

while True:
  num=int(input("Enter a number: "))
  if num==0:
    print("Zero is neither positive nor negative.")
    print("Zero is even.")
  elif num>0:
    print("Positive")
    if num%2==0:
      print("Even")
    else:
      print("Odd")
  else:
    print("Negative")
    if num%2!=0:
      print("Odd")
    else:
      print("Even")
