#Input a number. Write a program to check whether it is a single digit, double digit, triple digit or more than three digit
a = int(input("Enter a number: "))
if a>=0 and a<=9:
    print("It is a single digit number")
elif a>=10 and a<=99:
    print("it is a double digit number")
elif a>=100 and a<=999:
    print("It is a triple digit number")
else:
    print("It is more than three digit number")