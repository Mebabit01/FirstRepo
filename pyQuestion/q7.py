#Program to check whether a 3 input angle is possible or not to make triangle
a = int(input("Enter 1st angle: " ))
b = int(input("Enter 2nd angle: "))
c = int(input("Enter 3rd angle: "))

s = a + b + c

if s==180:
    print("Triangle is possible")
else:
    print("Triangle is not possible")