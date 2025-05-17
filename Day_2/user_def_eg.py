# write a user defined function to find the given number is perfect number or not

#function with arguments and return value

def is_perfect_num(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
    
# calling the function

if __name__ == "__main__":   # call under the main thread
    n = int(input("Enter a number:"))
    if is_perfect_num(n):
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")

