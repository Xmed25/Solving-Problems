# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def puzzle(heads, legs):
    assume = heads * 2
    difference = legs - assume
    rabbit = difference // 2
    chicken = heads - rabbit
    return rabbit, chicken
print(puzzle(35, 94))
