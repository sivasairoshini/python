#Name:T.S.S.Roshini
#Program:To counts the frequency of each character in a string and stores the result in a dictionary.
x=input("Enter a string:").lower()
d={}
for n in x:
    if n not in d:
        d[n]=x.count(n)
print("Frequencies of charcters in string:",d)
#output
#Enter a string:Roshini
#Frequencies of charcters in string: {'r': 1, 'o': 1, 's': 1, 'h': 1, 'i': 2, 'n': 1}