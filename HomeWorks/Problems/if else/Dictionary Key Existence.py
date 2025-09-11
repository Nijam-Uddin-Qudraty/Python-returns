# Dictionary Key Existence (dict + if-else)
# Check if a user-input key exists in a dictionary.
# 👉 Example Dictionary: {"id":101, "name":"Tarek", "age":22}
# 👉 Input: name → Output: Value: Tarek
# 👉 Input: salary → Output: Key not found

d = {"id":101, "name":"Tarek", "age":22}
userInput = input()
if userInput in d:
    print("Value:", d[userInput])
else:
    print("Key not found")
