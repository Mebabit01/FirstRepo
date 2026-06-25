#Write a program in python to fid the sum of all the numbers which are divisible by 3 but not 5 from 1 - 30 using while loop.
i = 1
sum = 0
while i<=30:
    if i%3==0 and i%5!=0:
        print(i, end = " ")
        sum = sum + i
    i = i + 1
print(f"\nSum is {sum}")