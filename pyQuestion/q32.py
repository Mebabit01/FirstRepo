#Input a number. WAP in python to find the factor of the number

n = int(input("Enter a number: "))
print(f"the factor of {n} are: ")

for i in range(1, n+1):
    if n%i==0:
        print(i, end = " ")