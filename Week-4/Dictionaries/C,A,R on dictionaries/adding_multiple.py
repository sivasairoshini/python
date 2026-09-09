#Name:T.S.S.Roshini
#Program:To add 3 new key-value pairs to an existing dictionary.
d={'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Neeraja': '104', 'Ram Sai': '105'}
print("Initial dictionary:",d)
d.update({"hiranmai":106,"Raju":107,"Ramesh":108})
print("After adding:",d)
#output
#Initial dictionary: {'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Neeraja': '104', 'Ram Sai': '105'}
#After adding: {'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Neeraja': '104', 'Ram Sai': '105', 'hiranmai': 106, 'Raju': 107, 'Ramesh': 108}