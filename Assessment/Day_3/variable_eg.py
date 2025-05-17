class Employee:
    company_name = "Altimetrik"  # class variable
 
    def __init__(self, eid, ename, salary):
        self.eid = eid
        self.ename = ename
        self.salary = salary
        self.bonus = salary * 0.10
        self.total_salary = self.bonus + self.salary
 
    def display(self):
        print(f"The ID of the employee: {self.eid}")
        print(f"The name of the employee: {self.ename}")
        print(f"The company name: {Employee.company_name}")
        print(f"The salary of the employee: {self.salary}")
        print(f"The total salary: {self.total_salary}")
 
    # method with return type and no parameter
    def annual_bonus(self):
        return self.salary * 20
 
    # method with no return and with parameter
    def attendance_with_bonus(self, present_days):
        self.present_days = int(input("Enter the total number of present days: "))
        if self.present_days >= 150:
            avg_salary = self.salary * 0.25
            total_salary = self.salary + avg_salary
            return total_salary
        else:
            avg_salary = self.salary * 0.10
            total_salary = self.salary + avg_salary
            return total_salary
   
    @staticmethod
    def welcome_message():
        print(f"Welcome to {Employee.company_name}, have a nice day!!!")
 
 
def main():
    print("**Employee Details**")
    print("_" * 30)
    Employee.welcome_message()
    e1 = Employee(101, "Siva", 20000)
    e2 = Employee(102, "Sam", 15000)
    e3 = Employee(103,"Hari" , 30000)
    e1.display()
    print("_" * 30)
    e2.display()
    print("_" * 30)
    e3.display()
    print("_" * 30)
 
    print(f"Annual bonus for {e1.ename}: {e1.annual_bonus()}")
    print("_" * 30)
    print(f"Annual bonus for {e2.ename}: {e2.annual_bonus()}")
    print("_" * 30)
    print(f"Annual bonus for {e3.ename}: {e3.annual_bonus()}")
    print("_" * 30)
 
    print(f"The salary according to the attendance {e1.ename}: {e1.attendance_with_bonus(200)}")
    print("_" * 30)
    print(f"The salary according to the attendance {e2.ename}: {e2.attendance_with_bonus(100)}")
    print("_" * 30)
    print(f"The salary according to the attendance {e3.ename}: {e3.attendance_with_bonus(100)}")
    print("_" * 30)
 
 
 
if __name__ == "__main__":
    main()