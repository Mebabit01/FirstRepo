#Input a basic salary of an employee. Write a progrgam in python to find the gross and net salary of an employee.
#Given:
"""da = 15% of basic (15/100)*basic hra = 10% of basic pf = 12% of basic gross = basic + da + hra net = gross + pf"""
bsalary=int(input("Enter basic salary: "))
da = 15/100 * bsalary
hra = 10/100 * bsalary
pf = 12/100 * bsalary
gross = da + hra + bsalary
net = gross + pf
print(f"Gross salary is: {gross}")
print(f"Net salary is: {net}")
