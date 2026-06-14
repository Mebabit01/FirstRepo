#Input selling and cost price of an item. Write a program in python to fing the profit and loss and their percentage
sell = int(input("Enter selling price: "))
cost = int(input("Enter cost price: "))

if cost > sell:
    loss = cost - sell
    print(f"Loss is {loss}")
elif sell > cost:
    profit = sell - cost
    print(f"Profit is {profit}")
else:
    print("No loss No profit")