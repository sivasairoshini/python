#Name:T.S.S.Roshini
#Program:To unpack a tuple of 5 student marks into 5 separate variables and print their average
t=(96,99,92,98,100)
std1,std2,std3,std4,std5=t
print(f"Std1:{std1},Std2:{std2},Std3:{std3},Std4:{std4},Std5:{std5}")
average=(std1+std2+std3+std4+std5)/5
print("Tuple:",t)
print("Average of 5 students marks is",average)
#output
#Std1:96,Std2:99,Std3:92,Std4:98,Std5:100
#Tuple: (96, 99, 92, 98, 100)
#Average of 5 students marks is 97.0