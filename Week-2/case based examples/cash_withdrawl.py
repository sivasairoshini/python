#Name:T.S.S.Roshini
#Program:ATM Cash Withdrawl
balance=int(input("Enter your account balance\n"))
w_amount=int(input("Enter the amount you want to withdraw\n"))
if balance>w_amount and w_amount%100==0:
    balance=balance-w_amount
    print(f"You have withdrawn ₹{w_amount} and your remaining balance is ₹{balance}")
else:
    print("You have insufficient funds in your account")
#output
#Enter your account balance
#10000
#Enter the amount you want to withdraw
#4500