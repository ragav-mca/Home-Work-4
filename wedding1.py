lunch_per_person = int(input("Enter the cost of lunch per person: "))
breakfast_per_person = lunch_per_person // 2
hall_per_person = lunch_per_person // 3
number_of_persons = int(input("Enter the number of persons: "))
parking_per_person = (hall_per_person * number_of_persons) * 0.1
total_per_person = lunch_per_person + breakfast_per_person + hall_per_person + parking_per_person 

total_cost_for_all_persons = total_per_person * number_of_persons
decoration_cost = (hall_per_person * number_of_persons)//2

total_expense_wedding = total_cost_for_all_persons + decoration_cost
print("Total Expense for the Wedding: ",total_expense_wedding)
