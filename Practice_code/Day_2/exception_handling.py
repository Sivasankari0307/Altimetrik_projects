# Exception Handling
try:
    a = int(input("Enter a radius: "))
    
except ValueError:
    print("Please enter valid number")
    
else:
    print("Diameter of the circle:", 2*a)


    