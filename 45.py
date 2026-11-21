# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

def gen():
  list=[x**2 for x in range(1,21)]
  return list
list=gen()
print(list[-5:])
