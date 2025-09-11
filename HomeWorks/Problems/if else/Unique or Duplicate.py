# Unique or Duplicate (set + if-else)
# Write a program that takes a list of numbers. If all elements are unique, print "All unique", else print "Duplicates found".
# 👉 Example Input: [1, 2, 3, 4, 5] → Output: All unique
# 👉 Example Input: [1, 2, 3, 2, 5] → Output: Duplicates found

numbers = [1, 2, 3, 4, 4, 5] 
if len(numbers) == len(set(numbers)):
    print("All unique")
else:
    print("Duplicates found")
