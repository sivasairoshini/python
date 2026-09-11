#Name:T.S.S.Roshini
#Program:Check if a string contains only digits, only alphabets, or is alphanumeric.
s=input("Enter the string:")
if s.replace(" ","").isdigit():
    print("String contains contains only digits")
elif s.replace(" ","").isalpha():
    print("String contains only alphabets")
elif s.replace(" ","").isalnum():
    print("String contains only both digits and alphabets")
else:
    print("String contains special chracters")
#output
#Enter the string:First 1
#String contains only both digits and alphabets