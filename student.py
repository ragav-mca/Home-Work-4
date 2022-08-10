sub1 = int(input("Enter the marks of first subject: ")) #getting sub1 mark
sub2 = int(input("Enter the marks of second subject: ")) #getting sub2 mark
sub3 = int(input("Enter the marks of third subject: ")) #getting sub3 mark
sub4 = int(input("Enter the marks of fourth subject: ")) #getting sub4 mark
sub5 = int(input("Enter the marks of fifth subject: ")) #getting sub5 mark
avg = (sub1+sub2+sub3+sub4+sub5)/5 #to find avg of five subjects
if (avg>=60): 
    print("Result: Pass")
elif (avg>=90 in sub1,sub2,sub3 and avg>=40 in sub4,sub5): #condition for above 90% in 3 sub and above 40% in other 2 sub
    print("Result: Pass")
elif (avg>=75 in sub1,sub2,sub3 and avg>=50 in sub4,sub5): #condition for above 75% in 3 sub and above 50% in other 2 sub
    print("Result: Pass")
else:
    print("Result: Fail") #condition for fail if it does not satisfies above two conditions