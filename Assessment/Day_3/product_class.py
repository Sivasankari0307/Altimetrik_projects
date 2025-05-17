# Product class

class std_details:

    #constructor
    def __init__(self, std_id, std_name, grade, dept):
        self.student_id = std_id
        self.student_name = std_name
        self.student_grade = grade
        self.student_dept = dept

    #method to display product details
    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Grade: {self.student_grade}")
        print(f"Student Department: {self.student_dept}")

#main function
def main():
    print("Students Details")
    print("****************")
    #creating object of product class
    s1 = std_details(1, "Siva", "A+", "DS")
    s2 = std_details(2, "Sankari", "B", "DA") 

    s1.display()
    s2.display()   

if __name__== "__main__":
    main()