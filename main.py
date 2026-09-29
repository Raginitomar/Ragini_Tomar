print("SMART STUDENT ANALYSIS")

name = input("Enter student name:")
m1 = float(input("Enter marks in python:"))
m2 = float(input("Enter marks in math:"))
m3 = float(input("Enter marks in english:"))
m4 = float(input("Enter marks in physics:"))
m5 = float(input("Enter marks in communication:"))

total = m1 + m2 + m3 + m4 +m5
percentage = total / 5

print("\n--- Student Report ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")