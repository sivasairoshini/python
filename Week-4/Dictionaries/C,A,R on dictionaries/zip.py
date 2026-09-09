#Name:T.S.S.Roshini
#Program:Dictionary from two separate lists (one of keys and one of values) using zip().
Names=["Raju","Neeraja","Ram Sai","Roshini","Kumari"]
marks=[96,99,92,98,100]
d=dict(zip(Names,marks))
print("Dictionary created from zip()",d)
#output
#Dictionary created from zip() {'Raju': 96, 'Neeraja': 99, 'Ram Sai': 92, 'Roshini': 98, 'Kumari': 100}