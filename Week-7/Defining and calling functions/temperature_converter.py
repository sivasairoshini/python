#Name:T.S.S.Roshini
#Program:Temperature Converter (Nested Function Calls)
def celsius_to_fahrenheit(c):
    f=(c*(9/5))+32
    print(f"Celsius:{c}->Fahrenheit:{f}")
def fahrenheit_to_celsius(f):
    c=(f-32)*(5/9)
    print(f"Fahrenheit:{f}->Celsius:{c}")
choice=int(input("Enter the choice:\n1.Celsius → Fahrenheit\n2.Fahrenheit → Celsius\n"))
match choice:
    case 1:
        c=int(input("Enter the celsius value\n"))
        celsius_to_fahrenheit(c)
    case 2:
        f=int(input("Enter the fahrenheit value\n"))
        fahrenheit_to_celsius(f)
    case _:
        print("Invalid choice")
#output
#Enter the choice:
#1.Celsius → Fahrenheit
#2.Fahrenheit → Celsius
#1
#Enter the celsius value
#38
#Celsius:38->Fahrenheit:100.4
#Enter the choice:
#1.Celsius → Fahrenheit
#2.Fahrenheit → Celsius
#2
#Enter the fahrenheit value
#97
#Fahrenheit:97->Celsius:36.111111111111114