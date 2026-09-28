#Name:T.S.S.Roshini
#Program:Function Returning Multiple Values
def mv(num):
    mi=min(num)
    ma=max(num)
    avg=(sum(num))/len(num)
    return mi,ma,avg
l=[1,2,3,4,5,9,80,30]
minimum,maximum,average=mv(l)
print(f"Minimum={minimum}")
print(f"Maximum={maximum}")
print(f"Average={average}")
#output
#Minimum=1
#Maximum=80
#Average=16.75