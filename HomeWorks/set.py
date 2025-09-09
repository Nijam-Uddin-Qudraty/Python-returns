# Set
#---------------------------------------#
# What is a set in Python? How is it different from a list?
"""
Set is a collection of unique data. We cannot store duplicate values in set.
We cannot change or update the value of set after creation. but we can remove a value
and then add a new value. Set is mainly hash based collection.
So if we want to get access of value we cannot use index. Instead we have to use loop or
membership operator to access the value of set.
"""
#---------------------------------------#

#---------------------------------------#
# Write a Python program to find the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
setUnion = set1.union(set2)
print(setUnion)
setUnion2 = set1 | set2
print(setUnion2)   
#---------------------------------------#

#---------------------------------------#
# What happens if you add duplicate elements to a set?
"""
If we add duplicate elements to a set, it will ignore the duplicate values and only keep unique values.
"""
#---------------------------------------#

#---------------------------------------#
# How do you check if an element exists in a set?
"""
We can check if an element exists in a set using the 'in' keyword.
"""
#---------------------------------------#

#---------------------------------------#
# Write a program to find the intersection of {1,2,3,4} and {3,4,5,6}.
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
setIntersection = setA.intersection(setB)
print(setIntersection)