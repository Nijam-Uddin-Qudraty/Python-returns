"""
Sum Until Limit (list + while loop)
Keep adding numbers until sum exceeds 100. Print how many numbers were added.
👉 Example Input: [20, 30, 25, 40, 15]
👉 Example Output:

Sum exceeded 100 after adding 4 numbers"""
sum=0
count=0
numbers = [20, 30, 25, 40, 15]
i=0
while i < len(numbers):
    sum += numbers[i]
    count += 1
    if sum > 100:
        break
    i += 1
print(f"Sum exceeded 100 after adding {count} numbers")