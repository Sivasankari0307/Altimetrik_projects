# Polymorphism example 

# 2. Duck Typing example

class Trainer:
    def get_role(self):
        print("Trainer teaches student")

class Student:
    def get_role(self):
        print("Student learns new skills")

class Admin:
    def get_role(self):
        print("Admin manages the system")

class Student:
    def get_role(self):
        print("Student learns new skills")

def show_role(person):
    person.get_role()


# User input

choice = input("Enter your choice:")
if choice == "Trainer":
    show_role(Trainer())
elif choice == "Student":
    show_role(Student())
elif choice == "Admin":
    show_role(Admin())