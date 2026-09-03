# 🟢 Problem 5: Factorial

# Write a program that calculates factorial.
# Example:
# Input:
# 5
# Output:
# 120
# Because:
# 5! = 5*4*3*2*1

factorial=1
num=int(input("Enter a number: "))
if num==0:
    print("The Factorial of 0 is : 1")
elif num<0:
    print("Factorial doesn't exist for negative numbers.")
else:
    for x in range(1,num+1):
        factorial*=x
print(f"The Factorial of '{num}' is : {factorial}")
