#Input a number and a range. WAP in python to print the multiplication table of a number

a = int(input("Enter a number: "))
b = int(input("Enter the range: "))

for i in range(a, b + 1):
    print(f"{a}x{i}={a*i}")