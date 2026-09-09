#Name:T.S.S.Roshini
#Program:to check whether a given key exists in a dictionary before accessing it.
d={"Name":"Roshi","Age":20,"Branch":"Cse"}
if "Name" in d:
    print("Name exists in dictionary",d.get("Name"))
else:
    print("Name doesn't exist")
#output
#Name exists in dictionary Roshi