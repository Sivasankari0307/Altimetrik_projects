class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks} marks"
    
    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.marks + other.marks
    
s1 = Student("Anirudh", 65)
s2 = Student("Siva", 66)

print(s1)   # __str__
print(len(s1))  # __len__
print(s1 +s2)   # __add__


