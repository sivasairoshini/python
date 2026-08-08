#Name:T.S.S.Roshini
#Program:Username Generation
name=input("Enter your name\n")
roll_number=input("Enter your roll number\n")
username=name[:name.rindex(" ")]+roll_number[-2:]
username=username.replace(" ","")
print("your username is :",username.lower())
#Output
#Enter your name
#Siva Sai Roshini Tirumareddi
#Enter your roll number
#25341A05L5
#your username is : sivasairoshinil5
