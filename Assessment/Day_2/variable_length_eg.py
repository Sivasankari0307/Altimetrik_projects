# variable length argument

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,5,4,8,6,2,4,5,8))


