# Problem — Indexed Filtering

# Given:

# names = ["Ahmed", "Ali", "Omar", "Hassan", "Mina"]
# scores = [85, 60, 92, 55, 78]

# Create a list containing:

# index: name → score

# but only for students who scored 70 or higher.

# Expected:
# [
#     "0: Ahmed → 85",
#     "2: Omar → 92",
#     "4: Mina → 78"
# ]

names = ["Ahmed", "Ali", "Omar", "Hassan", "Mina"]
scores = [85, 60, 92, 55, 78]

students=[f"{i} -> {name} : {score}" for i,(name,score) in enumerate(zip(names,scores)) if score>=70]
print(students)


# using loop

names = ["Ahmed", "Ali", "Omar", "Hassan", "Mina"]
scores = [85, 60, 92, 55, 78]


for i,(name,score) in enumerate(zip(names,scores)):
  if score>=70:
    print(i,name,score)
