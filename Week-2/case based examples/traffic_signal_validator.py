#Name:T.S.S.Roshini
#Program:Traffic Signal Validator
valid_colours=["red","yellow","green"]
colour_entered=input("Enter the colour of traffic signal\n").lower()
if colour_entered in valid_colours:
    print("valid traffic signal color")
else:
    print("Invalid traffic signal color")
#output
#Enter the colour of traffic signal
#red
#valid traffic signal color