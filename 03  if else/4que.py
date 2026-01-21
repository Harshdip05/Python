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
