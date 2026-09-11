#Name:T.S.S.Roshini
#Program:To Find the longest word in a sentence.
s=input("Enter the sentence:")
l=s.split()
print("Longest word is:",max(l,key=len))
#output
#Enter the sentence:have a nice day
#Longest word is: have