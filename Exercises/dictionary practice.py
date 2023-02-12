students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grades = {}

for students in students_scores:
    score = students_scores[students]
    if score > 90:
        students_grades[students] = "Outstanding"
    elif score > 80:
        students_grades[students] = "Exceeds Expectations"
    elif score > 70:
        students_grades[students] = "Acceptable"
    else:
        students_grades[students] = "Fail"

print(students_grades)