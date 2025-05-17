# Creating a set
my_set = {1, 2, 3}
another_set = set([3, 4, 5])

# Adding elements
my_set.add(4)

# Removing elements - removes an element from the set
my_set.remove(1)

# discard - removes an element, but does not raise an error of not found
my_set.discard(3)

# Set operations

#union
union_set = my_set | another_set # Equivalent to my_set.union(another_set)
#intersection
intersection_set = my_set & another_set # Equivalent to my_set.intersection(another_set)
#difference
difference_set = my_set - another_set # Equivalent to my_set.difference(another_set)

#clear
my_set.clear()

print("Union of a sets:", union_set)
print("Intersection of a sets:", intersection_set)
print("Difference of a sets:", difference_set)
print("Set after clear:", my_set)
