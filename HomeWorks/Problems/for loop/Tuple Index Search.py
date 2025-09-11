"""
Tuple Index Search (tuple + for loop)
Find all indexes of element 20 in a tuple.
👉 Example Input: (10, 20, 30, 40, 20, 50)
👉 Example Output:

20 found at indexes: [1, 4]
"""

t = (10, 20, 30, 40, 20, 50)
print("20 found at indexes: ",[i for i,j in enumerate(t) if j==20])