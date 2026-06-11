#Input a nnumber. Write a program in python to check whether a number in buzz or not. (A number is said to be buzz if it is divisible by 7 or last digit is 7)
a = int(input("Enter a number: "))

if a%7==0 or a%10==7:
    print("It is a Buzz number")
else:
    print("it is not a Buzz number")