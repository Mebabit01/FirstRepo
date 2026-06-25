#Write a program in python to find the sum of all even number from 1-20 using while loop

i = 1
sum = 0
while i<=20:
    if i%2==0:
        print(i, end=" ")
        sum = sum + i
    i = i + 1
print(f"\nSum is {sum}")