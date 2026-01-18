# 
print(input("enter your name: "))
print(input())  # kya type karna hai we dont know

# input() always returns data as a string (str).
age = input("enter age: ")
print(age,type(age))


# implicit
5/6 # answer is in float

# explicit (type casting)
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
print("sum is: ",num1+num2)
print(type(num1),type(num2))


# 
z = 2+3j
print(z)
print(1+z)
print(z.real)
print(z.imag)

# print(int(z)) wrong