#Name:T.S.S.Roshini
#Program:Email validation
import re
def is_valid_email(s):
    pattern = r"^[\w.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$"
    return re.match(pattern, s) is not None
valid = ["roshini@gmail.com", "test123@yahoo.in","abc.def@company.org","student_1@college.edu"]
invalid = ["no-at-sign.com","a@b.c","@gmail.com","abc@gmail"]
for email in valid:
    print(email,":", is_valid_email(email))
for email in invalid:
    print(email,":", is_valid_email(email))
#roshini@gmail.com : True
#test123@yahoo.in : True
#abc.def@company.org : True
#student_1@college.edu : True
#no-at-sign.com : False
#a@b.c : False
#@gmail.com : False
#abc@gmail : False