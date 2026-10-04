# Problem
# Create a set containing the even numbers from 1 to 10.

# Using Set Comprehension
even_numbers = {k for k in range(1, 11) if k % 2 == 0}
print(even_numbers)

# Using For Loop and add()
even_numbers = set()

for x in range(1, 11):
    if x % 2 == 0:
        even_numbers.add(x)

print(even_numbers)
