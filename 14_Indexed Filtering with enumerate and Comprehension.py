# Problem — Indexed Filtering with enumerate and Comprehension

# Given:

# names = ["Patrick", "Spongebob", "Sandy", "Squidward", "Shamshon"]
# scores = [85, 60, 92, 55, 78]

# Using enumerate() + list comprehension, create a list containing the names of students who scored 70 or higher, along with their index.

# Expected:

# [
#     "0: Ahmed",
#     "2: Omar",
#     "4: Mina"
# ]

names = ["Patrick", "Spongebob", "Sandy", "Squidward", "Shamshon"]
scores = [85, 60, 92, 55, 78]

students=[f"{i}:{name}" for i,(name,score) in enumerate(zip(names,scores)) if score>=70]
print(students)
