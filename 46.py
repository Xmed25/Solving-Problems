# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

def gen():
    data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even = []
    for e in range(len(data)):
        if data[e] % 2 == 0:
            even.append(data[e])
    return even
print(gen())

# another method 

def gen():
  data=(1,2,3,4,5,6,7,8,9,10)
  even=[]
  for e in data:
    if e%2==0:
      even.append(e)
  return even
even=gen()
print(even)
