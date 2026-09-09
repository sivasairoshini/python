#Name:T.S.S.Roshini
#Program:To merge two dictionaries into one using the update() method and the | operator.
d1={'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103'}
d2={'Neeraja': '104', 'Ram Sai': '105'}
print("Combining dictionaries using '|' ",d1|d2)
d1.update(d2)
print("Combining dictionaries using update()",d1)
#output
#Combining dictionaries using '|'  {'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Neeraja': '104', 'Ram Sai': '105'}
#Combining dictionaries using update() {'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Neeraja': '104', 'Ram Sai': '105'}
