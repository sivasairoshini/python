#Name: T.S.S.Roshini
#Program:Age Calculator
#Task:A1.1-Integers
age=int(input("Enter your age\n"))
current_year=int(input("Enter Current year\n"))
birth_year=current_year-age
print("Type of age variable",type(age))
print("Type of current_year variable",type(current_year))
print("Type of birth_year variable",type(birth_year))
age_in_2050=2050-birth_year
print("You're born in the year",birth_year)
print("Your age in 2050 will be",age_in_2050)
#Output
#Enter your age
#18
#Enter Current year
#2026
#Type of age variable <class 'int'>
#Type of current_year variable <class 'int'>
#Type of birth_year variable <class 'int'>
#You're born in the year 2008
#Your age in 2050 will be 42