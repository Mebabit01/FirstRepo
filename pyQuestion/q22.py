#Input a number. WAP in python to find the sum of digit
n = int(input("Enter a number: "))
sum = 0

while n!=0:
    d = n%10
    sum = sum + d
    n = n//10
print(f"Sum of this number is {sum}")

