s = {1,2,"a"}
s.add(3)
# s.pop() # removes random element
# s.remove("a") # removes  element, requires element name to be passed
s.discard("b") # removes element, used to handle error if element not found
# s.clear() # removes all elements
print(s)

"""
We can do mathmatical set operations like union, intersection, difference etc.
"""
A = {1,2,3,4}
B = {3,4,5,6}
# print(A.union(B)) # {1, 2, 3, 4, 5, 6} (A ∪ B)
# print(A.intersection(B)) # {3, 4}  # common elements of A and B (A ∩ B)

"""
A - B
elements of A but not in B
"""
print(A.difference(B)) # {1, 2} A-B

"""
B - A
elements of B but not in A
"""
print(B.difference(A)) # {5, 6} B-A
"""
# symmetric difference means uncommon value of both sets
which it removes common values of both sets
common elements of A and B are removed
A △ B = (A ∪ B) – (A ∩ B)
"""

print(A.symmetric_difference(B)) # {1, 2, 5, 6} elements of A or B but not in both

"""
we can also use operators to perform set operations
| is used as union, & is used as intersection and ^ used as symmetric difference
- is used as difference
"""
# print(A | B) # union
# print(A & B) # intersection 
# print(A - B) # difference A-B
# print(B - A) # difference B-A
# print(A ^ B) # symmetric difference

"""
we can perform update operations using those set operation methods
"""
A.update("c") # adds 'c' to set A
print(A)
# A.intersection_update(B) # A = A ∩ B
# A.difference_update(B) # A = A - B
# A.symmetric_difference_update(B) # A = A △ B
# we can use these in reverse case
# for example B.intersection_update(A) # B = B ∩ A
