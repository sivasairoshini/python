#Name:T.S.S.Roshini
#Program:To add a single element to a set using add() and multiple elements using update().
s={57,7,45,18,33,96,4,88}
print("Initial Set:",s)
s.add(264)
print("Set after adding 1 element:",s)
s.update({23,19,64})
print("Set after adding mutliple elements using update():",s)
#output
#Initial Set: {96, 33, 4, 7, 45, 18, 88, 57}
#Set after adding 1 element: {96, 33, 4, 7, 264, 45, 18, 88, 57}
#Set after adding mutliple elements using update(): {96, 33, 64, 4, 7, 264, 45, 18, 19, 23, 88, 57}