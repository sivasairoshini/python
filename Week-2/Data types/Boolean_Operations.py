#Name: T.S.S.Roshini
#Program:Boolean Operations
#Task:A3.1-Booleans
is_raining=input("Is it raining?(True/False)\n")=="True"
has_umbrella=input("Do you have umbrella?(True/False)")=="True"
print(type(is_raining))
print(type(has_umbrella))
print(is_raining and has_umbrella)
print(is_raining or has_umbrella)
print(not is_raining)
print(not has_umbrella)
#output
#Is it raining?(True/False)
#True
#Do you have umbrella?(True/False)False
#<class 'bool'>
#<class 'bool'>
#False
#True
#False
#True