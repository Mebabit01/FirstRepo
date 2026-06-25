#Input a number. WAP in python to check whether it is a prime number or not

n = int(input("Enter a number: "))
c = 0

for i in range(1, n+1):
    if n%i==0:
        c += 1
if c == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")