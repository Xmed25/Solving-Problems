# Sets & comprehensions

# Given this list:
# nums = [12, 0, -3, 8, 12, 5, 0, 9]


# Create a new list that:
# - Contains only positive numbers.
# - Contains no duplicates.
# - Is sorted in ascending order.
# - Does not modify the original list.
# Expected output:
# [5, 8, 9, 12]

nums = [12, 0, -3, 8, 12, 5, 0, 9]

mylist=list({i for i in nums if i>0})
numbers=sorted(mylist)
print(numbers)
