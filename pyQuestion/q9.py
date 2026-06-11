#Q. A student will not be allow to sit for the exam if his/her attendance is less than 75%
a = int(input("Enter the number of class held: "))
b = int(input("Enter the number of class attend: "))

attend = (b/a)*100

if attend>=75:
    print("Student can sit for the exam")
else:
    print("Student cannot sit for the exam")