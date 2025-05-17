# default argument - the with default value will be used if the arguments is not passed but the user

# we used when the arguments are optional, the default value is used

#Sub function
def sub(x,y):
    return x-y

#Add function
def add(a,b=2):
    return a+b

print("Sub:",sub(9,5))
print("Sub:",sub(2,8))

print("Add:",add(9,5))
print("Add:",add(2,8))