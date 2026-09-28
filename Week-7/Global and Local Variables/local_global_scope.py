#Name:T.S.S.Roshini
#Program:Local vs Global Scope
counter=0
def show_local():
    counter=75
    print("counter inside function:",counter)
show_local()
print("counter outside function:",counter)
#output
#counter inside function: 75
#counter outside function: 0