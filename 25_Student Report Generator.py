# Problem — Student Report Generator

# You are building a small program for a school.

# Write a function:

# generate_report(name, scores)

# The function receives:

# name → student's name
# scores → a list of scores

# Example:

# generate_report("Ahmed", [85, 72, 91, 60])

# The function should:

# Calculate the student's average.
# Find how many subjects he passed.
# Passing score = 60
# Find the student's highest score.
# Find the student's lowest score.
# Print a report like:
# Student: Ahmed
# Average: 77.0
# Passed: 3
# Highest: 91
# Lowest: 60
# Status: Passed

# The student is:

# "Passed" if average >= 60
# "Failed" otherwise
#  Rules

# Don't use:

# sum()
# max()
# min()


def report(name,scores):
  
  big=float("-inf")
  low=float("inf")
  subjects_passed=0
  total_score=0
  
  for score in scores:
    
    total_score+=score
    
    if score>big:
      big=score
    if score<low:
      low=score
    if score>=60:
      subjects_passed+=1
      
  avg=total_score/len(scores)
  
  print(f"""
  Student:{name}
  Average:{avg}
  Passed:{subjects_passed}
  Highest:{big}
  Lowest:{low}
  """)

report("Ahmed",[85, 72, 91, 60])
