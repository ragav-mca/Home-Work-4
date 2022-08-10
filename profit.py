actual_cake = 20
selling_cake = 40
actual_bread = 10
selling_bread = 15
emp_salary = 100
emp = 2
customers = 10
def profit(actual_cake, selling_cake): #Function to calculate Profit
    profit = (selling_cake - actual_cake)
    return profit
def loss(actual_cake, selling_cake):
    loss = (actual_cake - selling_cake)
    return loss
if(selling_cake > actual_cake):
    print(profit(actual_cake, selling_cake),"Profit")
elif(actual_cake > selling_cake):
    print(loss(actual_cake, selling_cake),"Loss")   
else:
    print("No Profit No Loss!")
#x = float(input("Quantity of bread: "))
#y = float(input("Quantity of cake: "))
#for customer in range(10):
#    print("Quantity of bread is", x + customers)
#    print("Quantity of cake is", y + customers)
