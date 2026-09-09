#Name:T.S.S.Roshini
#Program:To remove a key from a dictionary using pop(), and safely remove a key that may not exist using get() with a default value.
d={'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Neeraja': '104', 'Ram Sai': '105'}
d.pop("Neeraja")
print("After removing Neeraja:",d)
print(d.get("Rishi"))
print(d)
#output
#After removing Neeraja: {'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Ram Sai': '105'}
#None
#{'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Ram Sai': '105'}