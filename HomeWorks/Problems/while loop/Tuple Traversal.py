"""
Tuple Traversal (tuple + while loop)
Traverse tuple and print elements.
👉 Example Input: (100, 200, 300)
👉 Example Output:

100
200
300
"""
t=(100, 200, 300)
i = 0
while(i<len(t)):
    print(t[i])
    i+=1