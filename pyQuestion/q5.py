#Input a time in second. Write a program in python to convert the time into hours, minutes and second
t = int(input("Enter the time in second: "))
h = t//3600
t = t%3600
m = t//60
s = t%60

print(f"hours is: {h}")
print(f"Minutes is: {m}")
print(f"Seconds is: {s}")