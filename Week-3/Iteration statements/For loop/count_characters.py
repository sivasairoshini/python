#Name:T.S.S.Roshini
#Program:To count the number of vowels, consonants, digits, and spaces in a given string.
string=input("Enter the String\n")
string=string.lower()
countv=0;countc=0;countd=0;counts=0;countsp=0
for i in string:
    if i.isalpha():
        if i in "aeiou":
            countv+=1
        else:
            countc+=1
    elif i.isdigit():
        countd+=1
    elif i==" ":
        counts+=1
    else:
        countsp+=1
print(f"Number of vowels={countv}")
print(f"Number of consonants={countc}")
print(f"Number of digits in ={countd}")
print(f"Number of spaces={counts}")
print(f"Number of special symbols={countsp}")
#output
#Enter the String
#hello world
#Number of vowels=3
#Number of consonants=7
#Number of digits in =0
#Number of spaces=1
#Number of special symbols=0