#Input three angle and check whether the triangle is possible or not. If triangle is possible, then check whether it is acute angle triangle, right angle triangle or abtuse angle triangle
"""
Acute - all angle <90
Right angle - any one angle =90
Abtuse angle - any one angle >90
"""

a = int(input("Enter 1st angle: "))
b = int(input("Enter 2nd angle: "))
c = int(input("Enter 3rd angle: "))

if a + b + c == 180:
    print("Triangle is possible")
    if a < 90 and b < 90 and c <90:
        print("It is acute angle triangle")
    elif a == 90 or b == 90 or c == 90:
        print("It is right angle triangle")
    else:
        print("It is abtuse angle triangle")
else:
    print("Triamglr is not possible")