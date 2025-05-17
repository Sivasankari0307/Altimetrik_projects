# read and write to a csv file

# writing to a csv file

import csv

data = [ [ "Name", "Age", "Domain"], ["Siva", 23, "DS"], ["Siva", 20, "HR"], ["Sam", 2, "DA"] ]

with open('student_data.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read the csv file
with open('student_data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)