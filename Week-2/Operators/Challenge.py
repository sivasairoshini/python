#Name: T.S.S.Roshini
#Program:Login validator
username="sivasairoshini"
password=135780
inname=input("Enter your username:\n")
inpassword=int(input("Enter your password:\n"))
login_success=(inname==username and inpassword==password)
if login_success:
    print(login_success)
    print("login successfull and credentials matched")
else:
    print(login_success)
    print("Credentials not matched")
#output
#Enter your username:
#ramsai
#Enter your password:
#58798
#False
#Credentials not matched