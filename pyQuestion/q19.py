#Write a program to find the sum of all natural number from 1 - 10 using while loop

i = 1
total = 0
while i <= 10:
    print(i, end = " ")
    total = total + 1
    i = i + 1
print(f"\nTotal is {total}")