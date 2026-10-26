# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:

# Use "for" to iterate the tuple Use tuple() to generate a tuple from a list.


def problem():
    tu=(1,2,3,4,5,6,7,8,9,10)
    li=list(tu)
    even_list=[x for x in li if x%2==0]
    even=tuple(even_list)
    print(even)

problem()
