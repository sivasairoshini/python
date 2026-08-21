#Name:T.S.S.Roshini
#Program:To check the type of character
char=input("Enter the character\n")
if char.isdigit():
    print(f"{char} is digit")
elif char.isalpha():
    char=char.lower()
    if char=='a'or char=='e' or char=='i' or char=='o' or char=='u':
        print(f"{char} is a alphabet and its a vowel")
    else:
        print(f"{char} is a alphabet and its a consonent")
else:
    print(f"'{char}' is a special symbol")
#output
#Enter the character
#!
#'!' is a special symbol