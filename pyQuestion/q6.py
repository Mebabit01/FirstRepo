#Input a number. Write a program in python to check whether the number is odd or even
a = int(input("Enter a number: "))

if a%2==0:
    print("Even")
else:
    print("Odd")

"""This is a short form with same results
print("Even" if a%2==0 else "odd")"""