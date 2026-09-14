#Name:T.S.S.Roshini
#Program:To demonstrate the use of match(), search(), and fullmatch() methods in regular expressions.
import re
s="NASA and USA are leading organizations in space research. Scientists from different countries are working together to develop advanced technologies for future missions."
b=re.findall(r"[A-Z]+\b",s)
print(b)#['NASA', 'USA']
c=re.finditer(r"\w{6,}",s)
for i in c:
    print(i.group(),i.span())
#leading (17, 24)
#organizations (25, 38)
#research (48, 56)
#Scientists (58, 68)
#different (74, 83)
#countries (84, 93)
#working (98, 105)
#together (106, 114)
#develop (118, 125)
#advanced (126, 134)
#technologies (135, 147)
#future (152, 158)
#missions (159, 167)
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
d=re.findall(r"\$\d\.\d{1,2}",prices)
print(d)#['$3.50', '$1.20', '$4.75']
print(len(d))#3