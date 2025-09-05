
# unpacking a tuple
# -----------------------------------# 
# t = (1, 2, 3)
# a, b, c = t
# print(a) # 1

# t1 = (1, 2, 3, 4, 5)
# a,*b,c,d= t1
# print(a) # 1
# print(b) # [2, 3]
# print(c) # 4
# print(d) # 5


# t = (1, (2, 3), 4)
# a, (b, c), d = t
# print(a, b, c, d)   # 1 2 3 4

""" while unpacking a tuple the number of variables on the left side must be equal 
    to the number of elements in the tuple
    But we can ignore any element by using _ as a variable name
    e.g:-
    a, b, _, d = t1  # ignores the 3rd element of the tuple
    However if we want to unpack some elements and ignore others we can use * to ignore those elements
    """
t = (1, 2, 3, 4, 5, 6, 7)

a, b, *_, c, d = t
print(a, b, c, d)   # 1 2 6 7