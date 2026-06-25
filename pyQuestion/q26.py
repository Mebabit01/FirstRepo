#Input a number. WAP in python to check whether it is a palimdrome or not (A number is said to be palindrome if the reverse of the nnnumber is the same as the original number)

n = int(input("Enter a multidigit number: "))
dummy = n
rev = 0

while n!=0:
    d = n%10
    rev = rev*10 + d
    n = n//10
if rev == dummy:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")

