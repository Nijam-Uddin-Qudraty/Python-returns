# Dictionary

#---------------------------------------#
# 1. What is a dictionary in Python?

""" A dictionary is used to store multiple items in a single variable. Its store data in key-value pair.
Its an hashable object. We can access the value using its key.
Just because its keys are hashable we cannot access the value using index. We have to use key to access the value.
"""
#---------------------------------------#

#---------------------------------------#
# 2. Create a dictionary of 3 students with their names as keys and ages as values.
students = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 19
}
print(students)
#---------------------------------------#

#---------------------------------------#
# 3. How do you access the value of a dictionary using a key?
print(students["Alice"])  # Output: 20
#---------------------------------------#
# 4. Write a program to update the value of a dictionary key.
students["Alice"] = 21
print(students["Alice"])  # Output: 21
#---------------------------------------#

#---------------------------------------#
# 5. What will happen if you try to access a key that does not exist in a dictionary?
"""
If we try to access a key that does not exist in a dictionary, it will raise a KeyError.
"""
#---------------------------------------#
# 6.What is the difference between dict.get(key) and dict[key]? Show with an example.
"""
The key difference between dict.get(key) and dict[key] is dict[key] returns a keyerror 
if there is no key found in the dictionary whereas dict.get(key) returns None.
It make the code more useful and avoid unnecessary errors.
"""
#---------------------------------------#

#---------------------------------------#
# 7. Explain how nested dictionaries work with an example of storing student data (name, subjects, marks).
"""
Dictionaries which contains mutliple dictionaries inside it are called nested dictionaries.
Basically after creating a dictionary, we can make its value another dictionary.
In case of nested dictionaries we have to use keys of the parent dictionary to access the child dictionary.
if the child dictionary contains multiple data then we may have to use keys indexing to access the data even if
dictionaries do not support indexing generally.
"""
students={
    1: {'name': "Nizam", 'subjects':{'Math': 90, 'Science': 85}},
    2: {'name': "Aman", 'subjects':{'Math': 80, 'Science': 88}},
    3: {'name': "Raju", 'subjects':{'Math': 70, 'Science': 75}},
}
print(students)
print(f"{students[1]['name']} got {students[1]['subjects']['Math']} in {list(students[1]['subjects'].keys())[0]}")