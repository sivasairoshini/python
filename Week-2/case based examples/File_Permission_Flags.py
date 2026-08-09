#Name:T.S.S.Roshini
#Program:File Permission Flags
Read=4;Write=2;Execute=1
combined_flags=Read | Write
print("Combined flags:",combined_flags)
write_permission=combined_flags & Write
print("Has write permission???",bool(write_permission))
#output
#Combined flags: 6
#Has write permission??? True
