#Name:T.S.S.Roshini
#Program:Password Strength Checker
import re
def check_password(pw):
    failed = []
    if len(pw) < 8:
        failed.append("At least 8 characters")
    if not re.search(r"[A-Z]", pw):
        failed.append("At least one uppercase letter")
    if not re.search(r"[a-z]", pw):
        failed.append("At least one lowercase letter")
    if not re.search(r"\d", pw):
        failed.append("At least one digit")
    if not re.search(r"[!@#$%^&*]", pw):
        failed.append("At least one symbol from !@#$%^&*")
    return failed
password = input("Enter password: ")
result = check_password(password)
if result:
    print("Failed rules:")
    for rule in result:
        print("-", rule)
else:
    print("Password is valid")
#output
#Enter password: Abc12!
#Failed rules:
#- At least 8 characters
#Enter password: abcdefgh
#Failed rules:
#- At least one uppercase letter
#- At least one digit
#- At least one symbol from !@#$%^&*
#Enter password: Abcd1234!
#Password is valid