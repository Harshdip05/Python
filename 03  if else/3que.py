# min of 3 number

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print(num1,num2,num3)

if num1>num2 and num1>num3:
    print("Num1 is greater than all: ",num1)
elif num2 > num3 and num2>num1:
    print("num2 is greater than all: ",num2)
elif num3>num1 and num3>num2:
    print("num3 is greater than all: ",num3)     
else:
    print("they are equal")       


print()


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a<b and a<c :
    print("a is smallest: ",a)
elif b<c :
    print("smallest is b: ",b)
else:
    print("smallest is c: ",c)        