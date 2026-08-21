#Name:T.S.S.Roshini
#Program:Checking wheater entered date is correct or not
year=int(input("Enter the year\n"))
month=int(input("Enter the month\n"))
day=int(input("Enter the day\n"))
if month > 0 and month < 13:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if day > 0 and day < 30:
                print("Valid")
            else:
                print("Invalid")
        else:
            if day > 0 and day < 29:
                print("Valid")
            else:
                print("Invalid")
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 0 and day < 32:
            print("Valid")
        else:
            print("Invalid")
    else:
        if day > 0 and day < 31:
            print("Valid")
        else:
            print("Invalid")
else:
    print("Invalid")
#output
#Enter the year
#2025
#Enter the month
#12
#Enter the day
#5
#Valid