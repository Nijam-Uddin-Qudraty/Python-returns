# set
"""
# set is used to store unique values.we can't use indexing because its unordered.
# if we add duplicate value it will ignore it and only store unique values.
# we can't update its value but add value using add function
# set itself mutable but we can't use immutable variable in it
"""
"""
# we can't create empty set using {} because it will create an empty dictionary
# s={}
# print(type(s)) # <class 'dict'>
"""
s = set() # correct way to create an empty set
print(type(s)) # <class 'set'>

l = [1,2,3]
s1 = set(l) # creating a set from a list
print(s1)
"""
can't convert list of lists because list is mutable
"""
l1 = [[1,2],[3,4]] # we can't use list of lists because list is mutable
# s2 = set(l1) # TypeError: unhashable type: 'list
d = {"a":1, "b":2}
s2 = set(d) # creating a set from a dictionary, it will only take keys
print(s2)

# we can perform set operations like union, intersection, difference etc.