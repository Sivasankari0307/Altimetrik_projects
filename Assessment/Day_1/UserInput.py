# Employee data 

#input from user
emp_id = int(input("Enter the employee id:"))
name = input("Enter the employee name:")
job = input("Enter the job:")
basic_pay = int(input("Enter the basic pay:"))

allowances = 0.05*basic_pay if job=="manager" else 0.08*basic_pay if job=="developer" else 0.1*basic_pay if job=="analyst" else 0
  
payable_salary = basic_pay + allowances

# Employee id with calculated values
print(f"{name}, {emp_id}, {allowances} ,{payable_salary}")

