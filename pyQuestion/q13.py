#Input a number. Write a program in python to display the appropriate message according to the following criteria
"""
a). Divisible by 2 but not 5
b). Divisible by 5 but not 2
c). Divisible by both 2 and 5
d). Not divisible by both 2 and 5
"""
a = int(input("Enter a number: "))

if a%2==0 and a%5!=0:
    print("Divisible by 2 but not 5")
elif a%5==0 and a%2!=0:
    print("Divisible by 5 but not 2")
elif a%2==0 and a%5==0:
    print(" Divisible by both 2 and 5")
else:
    print("Not divisible by both 2 and 5")