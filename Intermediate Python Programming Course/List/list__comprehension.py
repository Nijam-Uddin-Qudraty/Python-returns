# List comprehension
# -----------------------------------#
list_num = []
# this part used see this example of list comprehension
# for i in range(1,11):
#     list_num.append(i)
# multiplier = input("Enter the multiplier: ")
# list_factor = [i*int(multiplier) for i in list_num]

# this part used to see the example of zip function
# although its not practical to use zip function here
# list_chart= list(zip(list_num, list_factor))
# for n, m in list_chart:
#     print(f"{n} * {multiplier} = {m}")


# practical example of list comprehension
# -----------------------------------#
# multiplier = int(input("Enter the multiplier: "))
# # list comprehension to create multiplication table for given multiplier
# table = [f"{n} × {multiplier} = {n*multiplier}" for n in range(1, 11)]

# for line in table:
#     print(line)
# print("\n".join(table)) # prints each element of the list in new line but making it a string

# -----------------------------------#

# list comprehension for conditional statements
# -----------------------------------#
# list_even = [i for i in range(1, 21) if i % 2 == 0]
# print(list_even)
# -----------------------------------#b