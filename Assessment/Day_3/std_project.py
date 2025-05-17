class Student:
    def __init__(self, student_id, student_name, dept, grade):
        self.student_id = student_id
        self.student_name = student_name
        self.dept = dept
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.student_name}, Dept: {self.dept}, Grade: {self.grade}"

class StudentManager:
    def __init__(self):
        self.students = {}
    
    
    def add_student(self, student_id, student_name, dept, grade):
         student = Student(student_id, student_name, dept, grade) 
         self.students[student_id] = student 
         return "Student added successfully"

    def view_students(self):
        return {student.student_id: vars(student) for student in self.students} if self.students else "No student records found."

    def update_student(self, student_id, student_name=None, dept=None, grade=None):
        for student in self.students:
            if student.student_id == student_id:
                if student_name: student.student_name = student_name
                if dept: student.dept = dept
                if grade: student.grade = grade
                return "Student record updated successfully!"
        return "Student ID not found!"

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return "Student record deleted successfully!"
        return "Student ID not found!"

manager = StudentManager()
print(manager.add_student(101, "Siva", "CS", "A"))
print(manager.add_student(102, "Iniya", "IT", "B"))
print(manager.view_students())  
print(manager.update_student(101, grade="A+"))
print(manager.delete_student(102))
print(manager.view_students())  
