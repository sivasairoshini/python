#Name: T.S.S.Roshini
#Lab:05
#Task:challenge
#Program:average marks rounded to 2 decimals
m1,m2,m3=map(int,input("enter the marks of 3 subjects").split())
average=(m1+m2+m3)/3
print(f"average marks are{average:.2f}")
