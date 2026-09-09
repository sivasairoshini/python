#Name:T.S.S.Roshini
#Program:To find the item with the highest price and the item with the lowest price.
d={"soap":100,"towel":200,"gold":10000,"silver":1500}
max=0;min=d["soap"]
for x,y in d.items():
    if y>max:
        max=y
    if y<min:
        min=y
print(f"Highest Price:{max}")
print(f"Lowest price:{min}")
#output
#Highest Price:10000
#Lowest price:100