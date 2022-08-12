sub1 = int(input("Enter the marks of first subject: ")) #getting sub1 mark
sub2 = int(input("Enter the marks of second subject: ")) #getting sub2 mark
sub3 = int(input("Enter the marks of third subject: ")) #getting sub3 mark
sub4 = int(input("Enter the marks of fourth subject: ")) #getting sub4 mark
sub5 = int(input("Enter the marks of fifth subject: ")) #getting sub5 mark
if (sub1,sub2,sub3 >=90 and sub4,sub5 >=40): #condition for above 90% in 3 sub and above 40% in other 2 sub
    print("Result: Pass")
elif (sub1,sub2,sub3 >=75 and sub4,sub5 >=50): #condition for above 75% in 3 sub and above 50% in other 2 sub
    print("Result: Pass")
else:
    (sub1>=60,sub2>=60,sub3>=60,sub4>=60,sub5>=60)
    print("Result: Pass") #condition for pass if five subjects >= 60