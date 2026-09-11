#Name:T.S.S.Roshini
#Program:Capitalize the first letter of every word (Title Case), without using .title().
s=(input("Enter the Sentence:")).split(" ")
for i in range(len(s)):
    s[i]=s[i][0].upper()+s[i][1:]
print('After capitalizing each word:'," ".join(s))
#output
#Enter the Sentence:have a nice day
#After capitalizing each word: Have A Nice Day