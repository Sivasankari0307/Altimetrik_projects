#List examples

#create a list
fruits = ["apple", "mango", "amla", "biriyani"]

if fruits.count("banana")==1:
    print("Banana is presenting in an list")
else:
    print("Banana is not presenting in an list")

#fruits.remove("banana")

#Append
fruits.append("banana")

#remove
fruits.remove("biriyani")

#sort
fruits.sort()

#reverse
fruits.reverse()

#count
count_fruits = fruits.count("banana")
print("Count of banana:", count_fruits)

#index
index_ = fruits.index("amla")
print("Index_of_amla:", index_)

#using for loop
for i in fruits:
    print(i)