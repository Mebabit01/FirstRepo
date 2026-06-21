#Input three number. Write a program to check whether they are equal or not, if they are equal. Find the greatest of three number?

a = int(input("Enter 1st angle: "))
b = int(input("Enter 2nd angle: "))
c = int(input("Enter 3rd angle: "))

if a == b == c:
    print("They are equal")
else:
    print("They are not equal")
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    else:
        max = c
    
    print(f"Greatest among three is {max}")