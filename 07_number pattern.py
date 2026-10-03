# Problem: Number Pattern
# Given an integer n, print the following pattern:
#
# Input: 5
#
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
