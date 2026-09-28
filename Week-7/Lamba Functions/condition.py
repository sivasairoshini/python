#Name:T.S.S.Roshini
#Program:Lambda with Conditional Expression
l= [45, 72, 33, 88, 56, 91]
a=lambda i:"Pass" if i>=40 else "Fail"
for i in l:
    print("Marks: ",i," status : ",a(i))
#output
#Marks:  45  status :  Pass
#Marks:  72  status :  Pass
#Marks:  33  status :  Fail
#Marks:  88  status :  Pass
#Marks:  56  status :  Pass
#Marks:  91  status :  Pass