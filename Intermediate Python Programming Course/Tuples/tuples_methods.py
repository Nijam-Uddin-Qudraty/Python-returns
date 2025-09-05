mytuple = ("apple", 1, True, 'a','b','a','c','a')
# tuple methods
# -----------------------------------#
print(len(mytuple)) # length of the tuple
print(mytuple.count("a")) # counts how many times the given element appears in the
print(mytuple.index(1)) # returns the index of the given element

""" we can't add or remove elements from a tuple because its immutable
    but we can concatenate a tuple with another tuple to make a new tuple
"""
list1 = [1,2,3]
mytuple = mytuple + tuple(list1) # extends the tuple by adding elements of the given list at the end of the tuple
print(mytuple)
# -----------------------------------#