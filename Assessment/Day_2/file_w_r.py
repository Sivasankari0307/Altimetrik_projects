# create a file and write
file = open("my_file.txt", "w")
file.write("Hello, Hi, Welcome")
print("Success")
file.close()


# read the file
file = open("my_file.txt", "r")
print(file.read())
file.close()

# Append the file
file = open("my_file.txt", 'a')
file.write("Appending the text")
print("Appended successfully")
