#Name:T.S.S.Roshini
#Program:Checking wheather given year is leap year or not
year=int(input("Enter the year\n"))
if year%400==0 or (year%4==0 and  year %100!=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
#output
#Enter the year
#2020
#2020 is leap year