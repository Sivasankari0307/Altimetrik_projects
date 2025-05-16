stud_id = int(input("Enter the student id:"))
Tamil = int(input("Enter the tamil mark: "))
English = int(input("Enter the English mark: "))
Maths = int(input("Enter the Maths mark: "))

subject_marks = (Tamil+English+Maths)/3

avg = subject_marks/len(3)
if Tamil>=40 and English>=40 and Maths>=40:
    result="pass"
    if avg >=80:
        grade="A+"
    elif avg>=60 and avg<80:
        grade="A"
    elif avg<=40 and avg<60:
        grade="B"
else:
    result="fail"
    grade="Needs improvement"

print(f"Id: {stud_id}| Average: {avg}| Result: {result}| Grade: {grade}")



