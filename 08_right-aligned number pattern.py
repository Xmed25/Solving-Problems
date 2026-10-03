# Problem : Right-Aligned Number Pattern
# Write a Python program that takes an integer n from the user and prints a right-aligned number pattern.
# Example

# Input:

# 5

# Output:

#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

num = int(input("Enter a number: "))

for i in range(1,num+1):
  for j in range(num-i):
    print(" ",end="")
  for k in range(1,i+1):
    print(k,end=" ")
  print()
