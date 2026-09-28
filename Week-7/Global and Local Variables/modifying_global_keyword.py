#Name:T.S.S.Roshini
#Program:Modifying a Global Variable Using the global Keyword
counter=0
def increment_counter():
    global counter
    counter=counter+1
print("Initial counter value:",counter)
increment_counter()
print("Counter after 1st call:",counter)
increment_counter()
print("Counter after 2nd call:",counter)
increment_counter()
print("Counter after 3rd call:",counter)
increment_counter()
print("Counter after 4th call:",counter)
increment_counter()
print("Counter after 5th call:",counter)
#output
#Initial counter value: 0
#Counter after 1st call: 1
#Counter after 2nd call: 2
#Counter after 3rd call: 3
#Counter after 4th call: 4
#Counter after 5th call: 5