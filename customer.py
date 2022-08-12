#question 1 and 3
onion = 20 #price of one kg onion
tomato = 10.5 #price of one kg tomato
budget = int(input("Enter the budget:")) #customers budget
city = input("Enter the City: ")
petrol_expenses = 0.03*budget #calculating petrol expenses
print("Petrol Expenses ", petrol_expenses)
x = budget//onion #dividing onions price with customers budget
y = budget//tomato #dividing tomatos price with customers budget
print("Onion quantity is",x) 
print("Tomato quantity is",y)

#question 2
onion_chennai = 30 #price of 1kg onion at chn
onion_trichy = 27 #price of 1kg onion at trichy
onion_madurai = 34 #price of 1kg onion at mdu100
chennai_parking = 5
new_budget = budget - petrol_expenses
if city == "chennai": #declaring if statement
    new_budget = new_budget - chennai_parking
    print("Onion quantity in Chennai", new_budget//onion_chennai) #dividing chn's onion price with budget
if city  == "Trichy":
    print("Onion quantity in Trichy", new_budget//onion_trichy) #dividing trichy's onion price with budget
if city == "Madurai":
    print("Onion quantity in Madurai", new_budget//onion_madurai) #dividing mdu's onion price with budget        



    


