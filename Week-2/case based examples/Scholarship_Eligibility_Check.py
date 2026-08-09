#Name:T.S.S.Roshini
#Program:Scholarship Eligibility Check
percentage=int(input("Enter your percentage\n"))
family_income=int(input("Enter your family income\n"))
status=percentage>85 or (percentage>75 and family_income<200000)
print(type(status))
if status:
    print("You're eligible for scholarship")
else:
    print("You are not eligible for scholarship")
#output
#Enter your percentage
#98
#Enter your family income
#3000000
#<class 'bool'>
#You're eligible for scholarship