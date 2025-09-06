""" accessing multiple values using methods keys(), values() and items() returns 
    values as tuple or list of tuples"""
mydict = {"name": "John", "age": 30, "city": "New York"}
# print(mydict.values()) # returns all values of the dictionary
# print(mydict.keys()) # returns all keys of the dictionary
# print(mydict.items()) # returns all key-value pairs of the dictionary as a list of tuples
# print(type(mydict.items())) # <class 'dict_items'>
# print(mydict.get("name")) # accessing value using get() method
# mydict.clear() # removes all key-value pairs from the dictionary
mydict.pop("age") # removes the key-value pair with the given key
mydict.popitem() # removes the last inserted key-value pair
mydict.setdefault("country", "USA") # adds a new key-value pair if the key doesn't exist
newdict = dict.copy(mydict) # creates a shallow copy of the dictionary
keyDict = dict.fromkeys(["roll", "age", "score"], 0) # creates a new dictionary with given keys and default value
print(keyDict)

# we can also delete a key-value pair using del keyword
# del mydict["city"] # removes the key-value pair with the given key

