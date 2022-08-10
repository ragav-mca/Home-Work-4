lunch = int(input("Enter the cost of lunch per person")) #getting the cost for lunch
breakfast = lunch//2 #dividing the cost of lunch 
hall = lunch//1/3 #dividing the cost of 1/3rd lunch price
decoration = hall//2 #dividing the cost of hall by 2
parking = hall//1/10 #dividing the cost of hall by 10%  
print("Cost of Lunch ",lunch)
print("Cost of breakfast ",breakfast)
print("Cost of Hallcper Person ",hall)
print("Cost of Decoration ",decoration)
print("Cost of Parking ",parking)

total_cost = lunch+breakfast+hall+decoration+parking #adding all the expense
bride_expense = total_cost//2 #dividing the total cost
groom_expense = total_cost//2 #dividing the total cost
bride_savings = 50000
print("Total Expense: ",total_cost)
print("Bride Expense: ",bride_expense)
print("Grooms Expense: ",groom_expense)