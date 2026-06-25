#WAP in python to find the sum of the following series
"""
s=1/2 + 2/3 + 3/3 + 4/3 + ...... + n/(n+1)
"""

n = int(input("Enter a number: "))
total = 0

for i in range(1, n+1):
    total += i/(i+1)
print(f"Sum of the series is {total:.2f}")