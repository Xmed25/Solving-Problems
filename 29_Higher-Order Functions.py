# Higher-Order Functions
# filter(), map() & lambda

# Given:
# prices = [100, 250, 80, 400, 150]


# Write code that:
# 1. Uses filter() and lambda to select prices strictly greater than 150.
# 2. Uses map() and lambda to apply a 10% discount to those selected prices.
# 3. Converts both results into lists and prints them.
# Expected results:
# [250, 400][225.0, 360.0]



# Requirements
# - Use both filter() and map().
# - Use lambda expressions.
# - Do not use a loop or list comprehension as a replacement for these functions.

prices = [100, 250, 80, 400, 150]

filtering = list(filter(lambda value: value > 150, prices))
discount = list(map(lambda price: price * 0.9, filtering))

print(filtering)
print(discount)
