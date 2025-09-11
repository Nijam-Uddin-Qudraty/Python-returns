"""
Word Frequency Counter (dict + for loop)
Count how many times each word appears in a string.
👉 Example Input: "apple banana apple orange banana apple"
👉 Example Output:

{"apple": 3, "banana": 2, "orange": 1}

"""
a = "apple banana apple orange banana apple"
d = {"apple": 0, "banana": 0, "orange": 0}
for words in a.split():
    d[words]+=1
print(d)