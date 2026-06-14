#A company decided to give bonus to employee according to the following criteria
"""
Time period of service                                  Bonus
>10 years                                               10%
>=6 and <=10 years                                      8%
<6 years                                                5%
Ask user for their salary and year of service and print net bonus and amount
"""


s = int(input("Enter your salary: "))
y = int(input("Enter year of experience: "))

if y>10:
    b = (10/100)*s
    a = s + b
elif y<=6 and y<=10:
    b = (8/100)*s
    a = s + b
else:
    b = (5/100)*s
    a = s + b

print(f"Bonus is: {b}\nNet amount is: {a}")
