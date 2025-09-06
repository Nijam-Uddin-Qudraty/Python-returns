""" Dictionary contains two element- key and value.
    keys must be unique and immutable (string, number, tuple) 
    A dictionary is Python’s built-in hash table that stores key-value pairs, 
    providing fast access and flexibility.
    """



# creating a dictionary
# -----------------------------------#
mydict = {} # literal
mydict = {"name": "John", "age": 30} # literal with initial values
"""we dontt need to use quotes for keys if we use constructor"""
myDict = dict(name="John", age=30)
""" we can also create a dictionary using integer as keys, 
    then we won't need to use quotes for the keys."""
myDict = {1: "apple", 2: "banana"}

# we can convert a list of tuples, list of lists or two lists into a dictionary using dict() constructor
# list of tuples
myDict = dict([(1, "apple"), (2, "banana"), (3, "cherry")])
# list of lists
myDict = dict([[1, "apple"], [2, "banana"], [3, "cherry"]])

# dictionary comprehension
squares = {i: i*i for i in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# -----------------------------------#


# accessing dictionary elements
# -----------------------------------#
print(mydict["name"]) # accessing value using key
mydict["age"] = 31 # updating value using key
print(mydict.get("age")) # accessing value using get() method
"""if we update a key that doesn't exist it will create a new key-value pair"""
mydict["city"] = "New York" # creates a new key-value pair
# -----------------------------------#



