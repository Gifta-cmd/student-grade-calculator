# Student Grade Calculator

print("===== STUDENT GRADE CALCULATOR =====")

student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")

subjects = ["Python", "Java", "C Programming", "HTML", "Mathematics"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

highest = max(marks)
lowest = min(marks)

print("\n========== STUDENT RESULT ==========")
print("Student ID :", student_id)
print("Name       :", name)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("------------------------------------")
print("Total      :", total)
print("Average    :", round(average, 2))
print("Highest    :", highest)
print("Lowest     :", lowest)
print("Grade      :", grade)

if average >= 50:
    print("Result     : PASS")
else:
    print("Result     : FAIL")

print("====================================")