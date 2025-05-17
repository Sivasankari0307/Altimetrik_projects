# filter function

names = ['siva', 'iniya', 'swetha', 'hari','kicha']
filtered_names  = list(filter(lambda x: len(x)==5, names))
print ("Filtered names:", filtered_names)