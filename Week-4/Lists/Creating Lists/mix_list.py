#Name:T.S.S.Roshini
#Program:Creating mixed list and printing them
mix_list=[1,2.5,"Roshini",True,[25,45,57]]
for i in range(len(mix_list)):
    print(f"Type of element at index {i} is {type(mix_list[i])}")
#output
#Type of element at index 0 is <class 'int'>
#Type of element at index 1 is <class 'float'>
#Type of element at index 2 is <class 'str'>
#Type of element at index 3 is <class 'bool'>
#Type of element at index 4 is <class 'list'>