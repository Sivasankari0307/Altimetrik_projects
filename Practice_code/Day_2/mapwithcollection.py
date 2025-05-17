# list comprehension
# Using map with a collection

numbers = [2, 4, 6, 8, 10]
sqrt_num = list(map(lambda x: x**2, numbers))
print("Squared number:", sqrt_num)

# Another example

marks = [75, 30, 90, 55]
Grade = list(map(lambda x: "Pass" if x >= 40 else "Fail", marks))
print("Grades of the students:", Grade) 

# set 

names = ("siva", "iniya", "swetha")
uppercase_names = set(map(str.upper, names))
print(uppercase_names) 

# Dictionary

scores = {"siva": 85, "iniya": 75, "swetha": 90}
avg_marks = dict(map(lambda x: (x[0], x[1] + 5), scores.items()))
print(avg_marks)

