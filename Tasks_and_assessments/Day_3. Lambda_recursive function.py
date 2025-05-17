# Write a lambda function to find biggest among 3 numbers

biggest_number = lambda x, y, z : max(x, y, z)

# User input
x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
z = int(input("Enter the value of z:"))

print("Finding the biggest number:", biggest_number(x, y, z))

# write a recursive function to find Fibonacci series of given range

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# user input
n = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ,")