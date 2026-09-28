#Name:T.S.S.Roshini
#Program:Bank Account Simulation 
balance=1000
def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited:", amount)
    print("Current balance:", balance)
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount withdrawn:", amount)
        print("Current balance:", balance)
    else:
        print("Insufficient funds!")
        print("Current balance:", balance)
while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit(amount)
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)
    elif choice == 3:
        print("Current balance:", balance)
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
#output
#--- Bank Menu ---
#1. Deposit
#2. Withdraw
#3. Check Balance
#4. Exit
#Enter your choice: 1
#Enter deposit amount: 57000
#Amount deposited: 57000.0
#Current balance: 58000.0
#
#--- Bank Menu ---
#1. Deposit
#2. Withdraw
#3. Check Balance
#4. Exit
#Enter your choice: 4
#Thank you!