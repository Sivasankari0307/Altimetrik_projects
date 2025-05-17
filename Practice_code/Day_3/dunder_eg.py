# Create a class employee with __init__, __str__, __add__ to add salaries

class Employee:
    def __init__(self, emp_name, emp_salary):
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def __str__(self):
        return f"{self.emp_name} has {self.emp_salary} as their salary"
    
    def __len__(self):
        return len(self.emp_name)

    def __add__(self, other):
        return self.emp_salary + other.emp_salary
    
s1 = Employee("Hari", 50000)
s2 = Employee("Siva", 45000)

print(s1)   # __str__
print(s2)   # __str__
print(len(s1))  # __len__
print(len(s2))   # __len__
print("Sum of the employees salary:", s1 + s2)   # __add__



