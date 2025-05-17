# Multi keyword arguments

# Keyword arguments allow you to pass arguments to a function by explicitly

def show_profile(**info):
    for key,value in info.items():
        print(f"{key}: {value}")

show_profile(name="Siva", age=23, location="Salem")
show_profile(name="Alice", age=25, location="Chennai")
show_profile(name="Bob", age=27, location="Bangalore")


# to find number of words present in the string
def no_of_words(str):
    count = str.split()
    length_ = len(count)
    print(f"No_of_words:{str}:{length_}")


no_of_words("Hello")
no_of_words("Hi, Everyone")


