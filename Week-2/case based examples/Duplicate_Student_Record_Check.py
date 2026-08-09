#Name:T.S.S.Roshini
#Program:Checking for Duplicate Student Records
student1={"name":"Roshini",
"age":18,
"branch":"CSE"
}
student2={"name":"Ram Sai",
          "age":18,
          "branch":"ECE"}
student3={"name":"Ram Sai",
          "age":18,
          "branch":"ECE"}
print(id(student1))
print(id(student2))
print(id(student3))
print("wheather student1 is student2??",student1 is student2)
print("wheather student2 is student3??",student2 is student3)
print("wheather student1 is student2??",student1 == student2)
print("wheather student2 == student3??",student2 == student3)
#output
#4345046848
#4345455168
#4345457472
#wheather student1 is student2?? False
#wheather student2 is student3?? False
#wheather student1 is student2?? False
#wheather student2 == student3?? True