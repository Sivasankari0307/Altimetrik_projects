# Write a menu driven program to perform the following operation:

# Task:

# To write a file 
def write_file(filename):
    try:
        with open(filename, 'w') as file:
            content = input("Enter content to write into the file: ")
            file.write(content)     
            print("File written successfully.")
    except TypeError :
        print(f"Error writing to file.")

# To read a file 
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:", content)
            print("File read successfully")
    except FileNotFoundError:
        print("File does not exist. Please write to the file first.")
    except TypeError:
        print(f"Error reading file.")

# To append a file 
def append_file(filename):
    try:
        with open(filename, 'a') as file:
            content = input("Enter the content to append to the file: ")
            file.write("\n" + content)
            print("Content appended successfully.")
    except TypeError:
        print(f"Error appending to file.")


# Main program
filename = "sample_file.txt"

print("Welcome to the File Management System")
print("1: Write to a file")
print("2: Read from a file")
print("3: Append to a file")
print("4: Exit")

while True:
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            write_file(filename)
        elif choice == 2:
            read_file(filename)
        elif choice == 3:
            append_file(filename)
        elif choice == 4:
            print("Exit.")
            break
        else:
            print("Please enter a number between 1 and 4.")
    
    except ValueError:
        print("Please enter a numeric value.")
