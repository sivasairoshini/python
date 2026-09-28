#Name:T.S.S.Roshini
#Program:Lambda for Dictionary Value Sorting
items={"Pen": 15,"Book": 120,"Pencil": 10,"Bag": 750,"Bottle": 250}
sorted(items,key=lambda x:x[1])
print("Soterd items",items)
#output
#Soterd items {'Pen': 15, 'Book': 120, 'Pencil': 10, 'Bag': 750, 'Bottle': 250}