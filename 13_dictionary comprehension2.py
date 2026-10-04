# problem:

# students = [
#     ("Ahmed", 85),
#     ("Ali", 60),
#     ("Omar", 92),
#     ("Hassan", 55),
#     ("Mina", 78)
# ]

# Using dictionary comprehension, create a dictionary containing only students who scored 70 or higher.

# Expected structure:

# {
#     "Ahmed": 85,
#     "Omar": 92,
#     "Mina": 78
# }

#

students = [
    ("Sandy", 85),
    ("Spongebob", 60),
    ("Squidward", 92),
    ("Patrick", 55),
    ("Eugene", 78)
]

passed_students={student:score for student,score in students if score>=70}
print(passed_students)
