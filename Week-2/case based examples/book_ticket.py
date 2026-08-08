#Name:T.S.S.Roshini
#Program:Calculating Ticket Price
n=int(input("Enter the number of tickets you want to book\n"))
price=n*250
if price>500:
    price-=100
    print("You are eligible for discount of ₹100 and Your fare is ₹",price)
else:
    print("Your fare is ₹",price)
#output1
#Enter the number of tickets you want to book
#4
#You are eligible for discount of ₹100 and Your fare is ₹ 900
#output2
#Enter the number of tickets you want to book
#2
#Your fare is ₹ 500