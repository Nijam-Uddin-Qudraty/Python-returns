"""
Dictionary Search (dict + while loop)
Continuously ask user for a key until "exit".
👉 Example Dictionary: {"id":1, "name":"Sami", "age":25}
👉 Input: name → Output: Sami
👉 Input: salary → Output: Not found
👉 Input: exit → Program stops
"""
d = {"id": 1, "name": "Sami", "age": 25}
while True:
    key = input("Enter a key or 'exit' to stop: ")
    if key == "exit":
        break
    else:
        print(d.get(key, "Not found"))