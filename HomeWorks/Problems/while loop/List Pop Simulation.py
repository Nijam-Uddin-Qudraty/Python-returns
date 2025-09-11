"""
List Pop Simulation (list + while loop)
Keep popping elements until list is empty.
👉 Example Input: [10, 20, 30]
👉 Example Output:

Removed: 30
Removed: 20
Removed: 10
List is empty now
"""
a=[10, 20, 30]
while(True):
    if len(a)>0:
        print("Removed: ",a[-1])
        a.pop()
    else:
        print("List is empty now")
        break
    
