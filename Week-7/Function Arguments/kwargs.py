#Name:T.S.S.Roshini
#Program:Keyword Variable-Length Arguments (**kwargs)
def build_profile(**details):
    print("---Profile Card---")
    for key,value in details.items():
        print(key,":",value)
build_profile(age=18, city="Vizag", hobby="Coding")
build_profile(age=20, city="Hyderabad", hobby="Reading", course="CSE")
build_profile(city="Bangalore", hobby="Photography", favorite_color="Blue")
#output
#---Profile Card---
#---Profile Card---
#age : 18
#city : Vizag
#hobby : Coding
#---Profile Card---
#age : 20
#city : Hyderabad
#hobby : Reading
#course : CSE
#---Profile Card---
#city : Bangalore
#hobby : Photography
#favorite_color : Blue