#Input a multidigit number. WAP in python to find the reverse of the number.

n = int(input("Enter a multidigit nnumber: "))
rev = 0

while n!=0:
    d = n%10
    rev = rev*10 + d
    n = n//10
print(f"Reverse is {rev}")