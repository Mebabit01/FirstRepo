# Menu base program using while loop and if else

#Calculator


while True:
    print()
    print("----------CALCULATOR----------")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("------------------------------")


    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number only.")
        continue

    if ch == 1:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        res = a + b
    elif ch == 2:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        res = a - b
    elif ch == 3:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        res = a * b
    elif ch == 4:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        res = a/b
    elif ch == 5:
        break
    else:
        print("Invalid choice")