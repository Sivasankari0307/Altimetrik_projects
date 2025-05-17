# write data to a file

#writing emp details to a file

with open('employees.txt','w') as file:
    file.write("ID, Name, Dept, Salary\n")
    file.write("101, Siva, DS, 50000\n")
    file.write("102, Iniya, Bio-tech, 60000\n")    
    file.write("103, Sam, DA, 70000\n")

# Reading data from a file
# reading emp data

try:
    with open('employees.txt','r') as file:
        for line in file:
            print(line.strip()) #removing extra spaces
except FileNotFoundError:
    print("Error: File not found.")

#Appending data to a file
#Adding new employee data

with open('employees.txt','a') as file:
    file.write("104, Sankari, HR, 62000\n")

print("New employee added successfully.")

# Handling exception in file handling
try:
    with open('non_existing_file','r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")