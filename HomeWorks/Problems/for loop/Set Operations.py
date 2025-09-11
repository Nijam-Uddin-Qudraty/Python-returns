"""
Set Operations (set + for loop)
Find all unique vowels in a string.
👉 Example Input: "Programming is awesome"
👉 Example Output: {'a', 'i', 'o', 'e'}
"""

s = 'Programming is awesome'
a = {i for i in s if ((i=='a') or (i == 'e') or (i=='o') or (i =='i') or (i=='u'))}
print(a)