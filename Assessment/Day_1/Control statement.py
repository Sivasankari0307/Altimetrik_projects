# Finding the sales commission

salesman_id = input(int("Enter the salesman_id:"))
sales_value = input(float("Enter the sales value:"))

if sales_value <= 10000:
    commission = 0
elif sales_value>10001 and sales_value<50000: 
    commission = sales_value * 0.1
elif sales_value>=50001 and sales_value<100000:
    commission= sales_value*0.3
elif sales_value>100000:
    commission= sales_value*0.2

print(f"Salesman_Id:, {salesman_id}, Commission:", {commission} )


# condition: 10% of sales if sales value >= 50000 else commission is zero
# condition: sv upto 10000 comm=0
# condition: sv bw 10001 to 50000 comm=10%
# condition: sv > 100000 comm=20%


stud_id = input(int("Enter 3 subjects:"))
Tamil = input(int("Enter the tamil mark: "))
English = input(int("Enter the English mark: "))
Maths = input(int("Enter the Maths mark: "))

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