#Name:T.S.S.Roshini
#Program:Default Arguments
def calculate_price(price, tax_rate=18, discount=0):
    final_price=price+tax_rate+discount
    print("Final Price = ",final_price)
calculate_price(500)
calculate_price(1500,25)
calculate_price(1000,19,10)
#output
#Final Price =  518
#Final Price =  1525
#Final Price =  1029