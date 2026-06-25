#Input a multidigit number. WAP to check whether it is a spy umber or not (A number is said to be spy if the sum of the digit is equal to the product of the digit)

n = int(input("Enter a multidigit number: "))
total = 0
product = 1

while n!=0:
    d = n%10
    total = total + d
    product = product * d
    n = n//10
if total == product:
    print("It is a spy number")
else:
    print("It is not a spy nnumber")

