# accessing dictionary elements
# -----------------------------------#
myDict = {"name": "John", "age": 30}

# for key in myDict: # iterating through keys
#     print(key) # prints keys

# for key in myDict.keys(): # iterating through keys
#     print(key) # prints keys

""" while we try to access data using loop with a dictionary it will iterate through keys by default
    so if we want to access values we have to use values() method"""
for value in myDict.values(): # iterating through values
    print(value) # prints values

for k,v in myDict.items(): # iterating key-value pairs
    print(k, v) # prints key-value pairs

for i, (key, value) in enumerate(myDict.items()):
    print(i, key, value)

# passing value to a fucntion
def func(name, age):
    print(f"Name: {name}, Age: {age}")
func(**myDict) # unpacking dictionary while passing to a function