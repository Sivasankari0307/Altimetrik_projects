# project: Student management system (oop-based app)

# Project title: Student Manager system

# Objective: To implement a CLI based application that manages student records(Add, View, Update, Delete)using oops

# classes and objects, encapsulation, dunder method

print("Welcome to the Student Management System")

class Student:
    def __init__(self, student_id, name, dept, grade):
        self.student_id = student_id
        self.name = name
        self.dept = dept
        self.grade = grade

    def to_dict(self):
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Department": self.dept,
            "Grade": self.grade
        }

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student.to_dict()
        return {f"Student '{student.name}' added successfully!", "data": self.students}

    def view_students(self):
        return self.students if self.students else {"No students found."}

    def update_student(self, student_id, name=None, dept=None, grade=None):
        if student_id in self.students:
            if name:
                self.students[student_id]["Name"] = name
            if dept:
                self.students[student_id]["Department"] = dept
            if grade:
                self.students[student_id]["Grade"] = grade
            return {"message": f"Student '{student_id}' updated successfully!", "data": self.students}
        return {"message": "Student not found."}

    def delete_student(self, student_id):
        """Delete a student record based on ID."""
        if student_id in self.students:
            del self.students[student_id]
            return {f"Student '{student_id}' deleted successfully!", "data": self.students}
        return {"message": "Student not found."}


def main():
    manager = StudentManager()

    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            grade = input("Enter Grade: ")
            student = Student(student_id, name, dept, grade)
            print(manager.add_student(student))

        elif choice == "2":
            print(manager.view_students())

        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new Name (press Enter to skip): ")
            dept = input("Enter new Department (press Enter to skip): ")
            grade = input("Enter new Grade (press Enter to skip): ")
            print(manager.update_student(student_id, name if name else None, dept if dept else None, 
                                         grade if grade else None))

        elif choice == "4":
            student_id = input("Enter Student ID to delete: ")
            print(manager.delete_student(student_id))

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Enter valid number")


if __name__ == "__main__":
    main()
