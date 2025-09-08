# Tuple 


#---------------------------------------#
# What is a tuple? How is it different from a list?
"""
Tuple is immutable variable in python, which used store multiple item in single variable.
but its values cannot be changed after creation.
Generally it used when returning multiple values from function. and also used as key in dictionary.
as the the dictinary keys must be immutable.
"""
# ***************************************#
"""
List and tuple are seems to be similar but there are many differences between them.
- List is mutable whereas tuple is immutable.
It means we can change or update list value, but we can't change tuple value after creation.
- List is defined using square brackets [] whereas tuple is defined using parentheses ().
- In list there are many function to update and modify but in tuple there are only 
two functions count() and index().
- Tuple is faster than list.
- Tuple uses less memory than list.
- Tuple is time efficient than list.
- Tuple can be used as key in dictionary but list cannot be used as key in dictionary.
"""
#---------------------------------------#

#---------------------------------------#
# Write a tuple containing the names of 5 countries.
countries = ("India", "USA", "UK", "Canada", "Australia")
print(countries)
#---------------------------------------#

#---------------------------------------#
# Can you change the value of a tuple after creating it? Why or why not?
"""
No, we cannot change the value of a tuple after creating it because tuple is immutable.
In tuple we can extend its value adding another tuple but we cannot change/update the existing value.
"""
#---------------------------------------#

#---------------------------------------#
# How do you access the last element of a tuple?
"""
We can access the last element of a tuple using negative indexing.
"""
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-1]) # Output: 5
#---------------------------------------#

#---------------------------------------#
# Convert the tuple (10, 20, 30) into a list.
my_tuple = (10, 20, 30)
listOfTuple = list(my_tuple)
print(listOfTuple)
#---------------------------------------#

#---------------------------------------#
# Given a tuple t = (1, [2, 3], 4), can you modify t[1][0]? Why or why not?
"""
Yes, we can modify t[1][0]. Because though tuple is immutable while storing list inside tuple,
it stores the reference of list. and list is mutable. So if we modify the list it doesn't means that
we are modifying or changing the tuples value. We are changing existing list value.
We are simply changing the value of the reference, isn't updating or changing directly.
"""
t = (1, [2, 3], 4)
t[1][0] = 5
print(t) # Output: (1, [5, 3], 4)