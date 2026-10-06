# Problem — Student Analyzer

# Write:
# student_info(name, **scores)

# The function should:

# Print the student's name.
# Calculate the average.
# Return the average.
# Example:
# average = student_info(
#     "Ahmed",
#     Python=90,
#     English=80,
#     Math=70
# )

# print(average)

# Expected:

# Student: Ahmed
# Average: 80.0
# 80.0

# You must use **kwargs.

def student_info(name, **scores):
    print(f"Student:{name}")
    avg=sum(scores.values())/len(scores)
    print(f"Average:{avg}")
    return avg

average=student_info(
    "Ahmed",
    Python=90,
    
    English=80,
    Math=70
)
print(average)
