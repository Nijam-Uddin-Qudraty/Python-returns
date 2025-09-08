# List 


#---------------------------------------#
# How do you create a list in Python? Write an example.
fruits = ["apple", "banana", "cherry"]
print(fruits)
#---------------------------------------#

#---------------------------------------#
# What is the difference between append() and extend() in a list?

# ***************************************#

# append() adds single element at the end of the list whereas extend() adds multiple elements
# from iterable variables like list, tuple, set etc. 
#Every element of the iterable is added to the list as separate element.
#---------------------------------------#

#---------------------------------------#
# Write a Python program to find the maximum and minimum values in a list.
numbers = [10, 20, 4, 45, 99]
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
#---------------------------------------#

#---------------------------------------#
# How do you remove duplicate values from a list?

# ***************************************#

# we can just simply convert the list to a set, because sets do not allow duplicate values.
# Then convert it back to a list if needed.
my_list = [1, 2, 2, 3, 4, 4, 5]
setOfList= set(my_list)
print(setOfList)
unique_list = list(set(my_list))
print(unique_list)

# ***************************************#

# we can also do this using a loop
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
#---------------------------------------#


#---------------------------------------#
# If you have fruits = ["apple", "banana", "mango"], how do you replace "banana" with "orange"?

fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)
#---------------------------------------#

#---------------------------------------#
# Given a nested list: [[1,2], [3,4], [5,6]], write code to flatten it into [1,2,3,4,5,6].
nested_list = [[1, 2], [3, 4], [5, 6]]

list1= []
for i in nested_list:
    for j in i:
        list1.append(j)
print(list1)

# ***************************************#

list2 =[j for i in nested_list for j in i]
print(list2)

#---------------------------------------#
# What will happen if you use a list as a default argument in a function? Why is it dangerous?
# if i use a list as default argument in a function it will share its memory address to the function
# and if we modify the list inside the function it will modify the original list as well.
# When we pass mutable objects like lists or dictionaries as default arguments, 
# it creates the object only once during function definition, not each time the function is called.
# This can lead to unexpected behavior if the object is modified.
#---------------------------------------#
