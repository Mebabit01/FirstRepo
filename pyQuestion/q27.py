#Input a nnumber. WAP in python to check whether it is an armstrong number or not (A number is said to be armstrong if sum of a cube of its digits is equal to the number itself)

n = int(input("Enter a multidigit number: "))
dummy = n
total = 0

while n!=0:
    d = n%10
    total = total + d**3
    n = n//100
if dummy == total:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
