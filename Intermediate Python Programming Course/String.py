# immutable so can't modify but supports indexing
a = 10
b = "nuub"
f_string = f"Player number {a} is a {b}"
str_format = "This {}, is number {} ".format(a,b)
formatting = "Things seems harder when you are a %s" %b
print(formatting)

c = "   Hi  "
print(c.strip() ) #removes extra spaces


li = ["a","b","c"]
print("-".join(li)) # Joins values from a list
d = "hi bd"

print(d.split()) # splits to list
print(d.replace("hi", "bye")) # replaces value

print(d.startswith("h")) # checks values
print(d.endswith("d"))

print(d.find("i")) # finds index