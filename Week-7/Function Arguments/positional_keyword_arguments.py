#Name:T.S.S.Roshini
#Program:Positional and Keyword Arguments
def student_info(name, roll_no, branch):
    print("----Student Details----")
    print(f"Name:{name}")
    print(f"Roll No:{roll_no}")
    print(f"Branch:{branch}")
student_info("Roshini",64,"CSE")
student_info(roll_no=43,branch="Mech",name="Sandhya")
#output
#----Student Details----
#Name:Roshini
#Roll No:64
#Branch:CSE
#----Student Details----
#Name:Sandhya
#Roll No:43
#Branch:Mech