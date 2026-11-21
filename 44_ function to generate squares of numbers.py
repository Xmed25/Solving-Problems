# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

def gen():
  g=[x**2 for x in range(1,21)]
  return g
print(gen()[:5])

# another method

def gen():
  list=[]
  for x in range(1,21):
    list.append(x**2)
  return list
print(gen()[:5])
