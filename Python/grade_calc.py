marks = input("Please enter your marks: ")
mark = int(marks)
if mark >= 80:
    grade = "A+"
elif mark >= 70:
    grade = "A"
elif mark >= 60:
    grade = "A-"
elif mark >= 50:
    grade = "B"
else:
    grade = "F"

print("Your grade is", grade)

