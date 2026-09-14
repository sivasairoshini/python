#Name:T.S.S.Roshini
#Program:To demonstrate advanced regular expressions using variable name validation, alternation, quantifier ranges, and named groups.
import re
s=input("Enter the identifier:")
result=re.match(r"^[_a-zA-Z][0-9a-zA-Z]*$",s)
if result is None:
    print("Invalid")
else:
    print("Valid")
#Enter the identifier:2sum
#Invalid
sentence = "I have a cat, my friend has a dog, and my neighbor has a bird as a pet."
s2=r"cat|dog|bird"
mh=re.findall(s2,sentence)
print(mh)#['cat', 'dog', 'bird']
hc=r"^#([a-fA-F0-9]{3}|[0-9a-fA-Z]{6})$"
code=input("Enter the hexadecimal code:")
mt2=re.match(hc,code)
if mt2:
    print("Valid:",mt2.group())
else:
    print("Invalid")
#Enter the hexadecimal code:#ffa
#Valid: #ffa
#Name capturing using p<>
log = "2024-06-01 ERROR Disk full"
pattern = r"(?P<date>\d{4}\-\d{2}\-\d{2}) (?P<level>\w+) (?P<message>.*)"
result = re.match(pattern, log)
print("Date:", result.group("date"))
print("Level:", result.group("level"))
print("Message:", result.group("message"))
#Date: 2024-06-01
#Level: ERROR
#Message: Disk full