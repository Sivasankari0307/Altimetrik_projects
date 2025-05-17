# generate OTP 
# random generator

import random

def generate_otp(length=6):
    otp = ''
    for _ in range(length):
        otp += str(random.randint(0,9))
    return otp

# Usage
otp = generate_otp()
print("Your OTP will be:", otp)
