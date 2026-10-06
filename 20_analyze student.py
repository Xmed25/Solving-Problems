# Problem - analyze student
# Write a function:
# analyze_student(name, **scores)
# Example:

# analyze_student(
#     "Ahmed",
#     math=90,
#     python=85,
#     english=80
# )

# The function should print:

# Student: Ahmed
# Average: 85.0



def analyze_student(name, **scores):
  print(f"Student: {name}\nAverage: {sum(scores.values())/len(scores)}")
  
analyze_student("Ahmed",math=90, python=85,english=80)
