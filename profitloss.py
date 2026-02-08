actual_cost = float(input("please enter the products price:"))
sale_amount = float(input("please enter the sales amout here:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0} ".format(amount))
else:
    print(" profit is equal to(0)")