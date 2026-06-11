#Find area of triangle
a = int(input("Enter the 1st side: "))
b = int(input("Enter 2nd side: "))
c = int(input("Enter 3rd side: "))

s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"Area of triangle is {area:.2f}")