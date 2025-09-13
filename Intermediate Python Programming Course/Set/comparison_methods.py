a = {1,2,3,4,5,6}
b= {3,4,6}
print(a.issubset(b)) # True if all elements of a are in b
print(b.issubset(a)) # True if all elements of b are in a
print(a.issuperset(b)) # True if a contains all elements of b
print(a.isdisjoint(b)) # checks common elements, returns false if no common elements