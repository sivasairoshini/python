#Name:T.S.S.Roshini
#Program:File Permission Flags
read = 4
write = 2
execute = 1
permissions = read|write
write_permission = (permissions & write) != 0
print("Permissions:", permissions)
print("Write permission set:", write_permission)
#output
#Permissions: 6
#Write permission set: True