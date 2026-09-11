#Name:T.S.S.Roshini
#Program:Reverse the order of words in a sentence (without reversing each word).
s=input("Enter the sentence:")
l=s.split(" ")
s=l[::-1]
reverse_string=" ".join(s)
print("Reversed order of words:",reverse_string)
#output
#Enter the sentence:Good girl
#Reversed order of words: girl Good