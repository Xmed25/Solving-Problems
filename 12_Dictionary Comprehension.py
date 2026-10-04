# Problem — Square Numbers Dictionary
# Create a dictionary where:
# Key   → number
# Value → square of the number
#
# Expected Output:
# {1: 1, 2: 4, 3: 9, 4: 16}



# Method 1 — Dictionary Comprehension


squares = {x: x**2 for x in range(1, 5)}

print(squares)



# Method 2 — For Loop


squares = {}

for x in range(1, 5):
    squares[x] = x**2

print(squares)

