#Name:T.S.S.Roshini
#Program:Demonstration of Regular Expression Methods
import re
a="1024 requests were served in 3 seconds"
b=re.search(r"served",a)
print(b)#<re.Match object; span=(19, 25), match='served'>
s="12345"
s1=re.fullmatch(r"\d+",s)
print(s1)#<re.Match object; span=(0, 5), match='12345'>
print(s1.group())#12345
s2="123a5"
s3=re.fullmatch(r"\d+",s2)
print(s3)#None
#match() it searches at the start only
#fullmatch() it searches entire string