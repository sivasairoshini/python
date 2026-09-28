#Name:T.S.S.Roshini
#Program:Combining All Argument Types
def order_summary(customer, *items, discount=0, **extra):
    print(f"Name:{customer}")
    print(f"Ordered Items:{items}")
    print(f"Discount:{discount}")
    print(extra)
order_summary("Meera", "Laptop", "Mouse", discount=10,delivery_address="Hyderabad", gift_wrap=True)
#output
#Name:Meera
#Ordered Items:('Laptop', 'Mouse')
#Discount:10
#{'delivery_address': 'Hyderabad', 'gift_wrap': True}