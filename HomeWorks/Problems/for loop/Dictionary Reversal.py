"""Dictionary Reversal (dict + for loop)
Reverse key-value pairs in a dictionary.
👉 Example Input: {1:"a", 2:"b", 3:"c"}
👉 Example Output: {"a":1, "b":2, "c":3}"""
d = {1:"a", 2:"b", 3:"c"}

d1= {j:i for i,j in d.items() }
print(d1)
