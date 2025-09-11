"""
Unique Number Collector (set + while loop)
Keep asking user for numbers until -1. Store unique numbers in a set.
👉 Example Input: 5, 10, 5, 20, -1
👉 Example Output:

Unique Numbers: {10, 20, 5}
"""
s= set()
while(True):
    n = int(input())
    if n== -1:
        break
    else:
        s.add(n)

print("Unique Numbers: ",s)