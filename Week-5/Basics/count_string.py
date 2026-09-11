#Name:T.S.S.Roshini
#Program:To Count the number of vowels, consonants, digits, and spaces in a string.
s=input("Enter the string:").lower()
cv=0;cs=0;cc=0;cd=0
for i in s:
    if i in "aeiou":
        cv+=1
    elif i==" ":
        cs+=1
    elif i is i.isdigit():
        cd+=1
    else:
        cc+=1
print("No of vowels:",cv)
print("No of consonants:",cc)
print("No of spaces:",cs)
print("No of digits:",cd)
#output
#Enter the string:I am a CSE student
#No of vowels: 6
#No of consonants: 8
#No of spaces: 4
#No of digits: 0