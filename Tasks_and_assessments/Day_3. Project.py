# project: Student management system (oop-based app)

# Project title: Student Manager system

# Objective: To implement a CLI based application that manages student records(Add, View, Update, Delete)using oops

# classes and objects, encapsulation, dunder method

# Student Class
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def __eq__(self, other):
        return self.student_id == other.student_id


# Student Manager Class
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    def update_student(self, student_id, name=None, age=None, grade=None):
        for student in self.students:
            if student.student_id == student_id:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
                print(f"Student {student_id} updated successfully!")
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student_id} deleted successfully!")
                return
        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            student = Student(student_id, name, age, grade)
            manager.add_student(student)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            name = input("Enter new Name (press Enter to skip): ")
            age = input("Enter new Age (press Enter to skip): ")
            grade = input("Enter new Grade (press Enter to skip): ")
            manager.update_student(student_id, name if name else None, age if age else None, grade if grade else None)

        elif choice == "4":
            student_id = input("Enter Student ID to delete: ")
            manager.delete_student(student_id)

        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
