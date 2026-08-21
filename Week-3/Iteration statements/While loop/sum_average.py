#Name:T.S.S.Roshini
#Program:To calculate sum and average of numbers
n=int(input("Enter the number\n"))
sum=0;count=0;x=n
while n!=0:
    sum+=n%10
    n=n//10
    count+=1
average=sum/count
print(f"{sum} is the sum of digits in {x}")
print(f"{average} is the average of digits in {x}")
#output
#Enter the number
#25
#7 is the sum of digits in 25
#3.5 is the average of digits in 25