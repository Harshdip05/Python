# menu driven calculator

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

op = input("enter operation(+ - * /): ")

if op=="+":
    print("addition: ",num1+num2)
elif  op=="-" :
    print("Subtraction: ",num1-num2)
elif op=="*":
    print("multiplication: ",num1*num2)
elif op=="/":
    print("division: ",num1/num2)     
else:
    print("you entered wrong op")    



print()


menu = input('''
HI! How can I help  you
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawal
4. Enter for exit 
''')

if menu == "1":
    print("pin change")
elif menu == "2":
    print("balance")
elif menu=="3":
    print("withdrawal")    
elif menu=="4":
    print("exit")
else:
    print("entered wrong menu")    