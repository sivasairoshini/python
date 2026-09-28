#Name:T.S.S.Roshini
#Program:Variable-Length Arguments (*args)
def total_marks(*marks):
    su=sum(marks)
    ave=su/len(marks)
    print("--Sum & Average--")
    print("Sum of Marks = ",su)
    print("Average of marks = ",ave)
total_marks(100,96,98)
total_marks(96,99,92,99,100)
total_marks(99)
#output
#--Sum & Average--
#Sum of Marks =  294
#Average of marks =  98.0
#--Sum & Average--
#Sum of Marks =  486
#Average of marks =  97.2
#--Sum & Average--
#Sum of Marks =  99
#Average of marks =  99.0