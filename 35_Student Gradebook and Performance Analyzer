# Problem — Student Gradebook and Performance Analyzer

# Requirements
# 1. Store student records with ID, name, and grades for multiple subjects.
# 2. Add students and update their grades.
# 3. Calculate each student's average grade.
# 4. Assign a letter grade based on configurable grading rules.
# 5. Identify the top student, lowest-performing student, and class average.
# 6. Find students who failed at least one subject.

# Example data
# students = [    {"id": 1, "name": "Ali", "grades": [90, 85, 95]},    {"id": 2, "name": "Mona", "grades": [70, 75, 80]},    {"id": 3, "name": "Omar", "grades": [40, 55, 45]},]



# Expected results

# Student ranking:
# 1. Ali  - 90.00 - A
# 2. Mona - 75.00 - C
# 3. Omar - 46.67 - F

# Top student: Ali
# Students who failed: Omar




students = [
    {"id": 1, "name": "Ali", "grades": [90, 85, 95]},
    {"id": 2, "name": "Mona", "grades": [70, 75, 80]},
    {"id": 3, "name": "Omar", "grades": [50, 60, 66]},
    {"id": 4, "name": "Ahmed", "grades": [80, 50, 89]}
]


def Analyze():
    sum_grades = []

    for student in students:
        grades = student["grades"]
        sum_grades.extend(grades)
        average = sum(grades) / len(grades)

        if average >= 90:
            assign = "A"
        elif average >= 75:
            assign = "B"
        elif average >= 60:
            assign = "C"
        else:
            assign = "F"

        print(f'{student["name"]}: {average:.1f} - {assign}')

    return sum_grades


def performance(sum_grades):
    top = max(sum_grades)
    low = min(sum_grades)

    print(f"Highest grade: {top}")
    print(f"Lowest grade: {low}")

    failed_students = [
        student["name"]
        for student in students
        if any(grade < 50 for grade in student["grades"])
    ]

    print(f"Students with a grade below 50: {failed_students}")


sum_grades = Analyze()
performance(sum_grades)
