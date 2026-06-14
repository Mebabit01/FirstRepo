#Input a sale of a salesman. Write a program in python to find and display the commision based on the following criteria
"""
sale                           commision
upto 10000                     5% 0f sales
upto 10000 and <= 30k          10% of sales
upto 3ok and <=50k             15% of sales
50k                            20% of sales
"""

s = int(input("Enter a sales: "))
if s<=10000:
    com = (5/100)*s
elif s>10000 and s<=30000:
    com = (10/100)*s
elif s>30000 and s>=50000:
    com = (15/100)*s
else:
    com = (20/100)*s

print(f"Your commision is {com:.2f}")