#Ask the user for an integer.
# Reverse its digits.
# Example:
# Input: 12345
# Output: 54321
# Another:
# Input: 908
# Output: 809
# Challenge
# Try solving it without converting the number to a string.

reverse=0

num=int(input("Enter a number: "))

while num>0:
  
  digit=num%10
  reverse=reverse*10+digit
  num//=10
  
print(reverse)
