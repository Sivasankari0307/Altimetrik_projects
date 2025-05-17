# example 2
try:
    numerator = int(input("Enter a numerator:"))
    denominator = int(input("Enter a denominator:"))
    #division operation
    result = numerator/denominator
    
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
    
except ValueError:
    print("Error, Invalid input. Please enter numeric values!")
    
else:
    print("Result is:", {result})

finally:
    print("Execution completed, Thank you")
    
