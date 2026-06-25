#WAP in python to find the sum of the series
# S = 1 + 4 + 9 + 16 + ... + 100

sum = 0

for i in range(1, 11):
    sum += i**2
print(f"Sum of the series is {sum}")