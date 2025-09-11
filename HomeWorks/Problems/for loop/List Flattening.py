"""
List Flattening (list + for loop)
Given a nested list, flatten it.
👉 Example Input: [[1, 2], [3, 4], [5]]
👉 Example Output: [1, 2, 3, 4, 5]
"""

l1 = [[1, 2], [3, 4], [5]]
l2 = [j for i in l1 for j in i]
print(l2)
