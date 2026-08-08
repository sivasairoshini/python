#Name:T.S.S.Roshini
#Program:Employee Salary and Bonus
salary=float(input("Enter your Base Salary\n"))
for i in range(1,4):
    salary+=salary*(0.10)
    print(f"Your salary in year {i} is ₹{salary}")
#output
#Enter your Base Salary
#50000
#Your salary in year 1 is ₹55000.0
#Your salary in year 2 is ₹60500.0
#Your salary in year 3 is ₹66550.0