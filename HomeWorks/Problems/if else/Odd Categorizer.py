"""
Even/Odd Categorizer (list + dict + if-else)
Take a list of numbers and categorize them into even and odd inside a dictionary.
👉 Example Input: [1, 2, 3, 4, 5, 6]
👉 Example Output:

{"even": [2, 4, 6], "odd": [1, 3, 5]}
"""
li = [1, 2, 3, 4, 5, 6]
d = {"even":[i for i in li if i%2==0], "odd":[j for j in li if j%2!=0]}
print(d)