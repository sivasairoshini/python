#Name:T.S.S.Roshini
#Program:Sum of Digits and Digit Reversal
def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n+sum_of_digits(n-1)
rev=0
def reverse_number(n):
    global rev
    if n==0:
        return rev
    else:
        digit=n%10
        rev=rev*10+digit
        return reverse_number(n//10)
n=int(input("Enter the number to find sum of digits upto that number:"))
print(sum_of_digits(n))
m=int(input("Enter the number to reverse:"))
print(reverse_number(m))
#output
#Enter the number to find sum of digits upto that number:20
#210
#Enter the number to reverse:456
#654