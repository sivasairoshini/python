#Name:T.S.S.Roshini
#Program:To Check if a given string is a palindrome
string=input("Enter the string:").lower()
rev=string[::-1]
if rev==string:
    print("Palindrome")
else:
    print("Not a Palindrome")
#output
#Enter the string:race car
#Not a Palindrome