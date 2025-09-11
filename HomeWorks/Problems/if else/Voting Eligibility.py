""" Given a list of tuples [(name, age), ...], check who is eligible to vote (age ≥ 18).
 Print eligible and not-eligible names separately.
 👉 Example Input: [("Rafi", 20), ("Mina", 16), ("Kamal", 25)]
👉 Example Output:

Eligible: Rafi, Kamal
Not Eligible: Mina
"""
#---------------------------------------#
close = False
li = []
while(close==False):
    print("Two value, one string and one number")
    print("Must use one word on string and space as separator")
    print("Write Close to stop")
    t = input()
    if t == "Close":
        close=True
        break
    else:
        inpt= t.split()
        inpt[1]=int(inpt[1])
        li.append(tuple(inpt))

print(li)

eligible = []
not_eligible = []
for i,a in li:
    print(i,a)
    if a>=18:
        eligible.append(i)
    else:
        not_eligible.append(i)

print(f"Eligible: {(eligible)} \n Not Eligible: {not_eligible}")


