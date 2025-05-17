# Library system inheritance code

# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Child class (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def show_details(self):
        super().show_details()
        print(f"File Size: {self.file_size} MB")

# Child class (inherits from Book)
class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    
    def show_details(self):
        super().show_details()
        print(f"Pages: {self.pages}")

# Creating objects
ebook = EBook("Python Basics", "Sivasankari", 5)
printed_book = PrintedBook("Python Advanced", "Iniya", 300)

ebook.show_details()
printed_book.show_details()
