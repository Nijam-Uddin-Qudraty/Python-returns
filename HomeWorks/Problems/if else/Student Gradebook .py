"""

Student Gradebook (dict + if-else)
Store student names and marks in a dictionary. Write a program to print each student’s grade (A, B, C, Fail) using if-else.
👉 Example Input: {"Alice":85, "Bob":60, "John":30}
👉 Example Output:

Alice → Grade A
Bob → Grade B
John → Fail


"""
d = {"Alice":85, "Bob":60, "John":30}
for i in d:
    if d[i]>=80:
        print(f"{i} -> Grade A")
    elif d[i]>=60:
        print(f"{i} -> Grade B")
    elif d[i]>=40:
        print(f"{i} -> Grade C")
    else:
        print(f"{i} -> Fail")