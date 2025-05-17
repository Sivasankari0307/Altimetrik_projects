def myfun(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for i in myfun(6):
    print(i)