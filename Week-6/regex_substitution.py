#Name:T.S.S.Roshini
#Program:To demonstrate re.sub() and re.subn() for replacing and modifying patterns in a given text.
import re
text = """Please contact John at john@gmail.com for more information.
You can also email our support team at support@example.com.
For queries, contact admin@company.org."""
s=re.sub(r"[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}","[EMAIL HIDDEN]",text)
print(s)
#Please contact John at [EMAIL HIDDEN] for more information.
#You can also email our support team at [EMAIL HIDDEN].
#For queries, contact [EMAIL HIDDEN].
names="Doe, John"
n=re.sub(r"(\w+), (\w+)",r"\2 \1",names)
print(n)#John Doe
nd="I have 5 apples and 20 kiwis"
def double(match):
    n=int(match.group())
    return str(n*2)
nd2=re.sub(r"\d+",double,nd)
print(nd2)#I have 10 apples and 40 kiwis
text2 = "Wait!!! What are you doing??? Really!!! I can't believe it!!!"
text3=re.subn("!+","!",text2)
print(text3)#("Wait! What are you doing??? Really! I can't believe it!", 3)
