# find sum of 3 digit num entered by user  

user1 = input("enter num : ")
print(user1)
print("sum is: ",int(user1[0])+int(user1[1])+int(user1[2]))

print()


user2 = int(input("enter num:"))
print(user2)
 
r1 = user2  % 100
r2 = user2 % 10
print(r2)
r3 = user2//100
print(r3)
r4 = user2//10
r5 = r4%10
print(r5)

print("sum is: ", r2+r3+r5)


print()

user3 = int(input("enter num:"))
print(user3)

a = user3 % 10
user3 = user3 // 10
b = user3 % 10
user3 = user3 // 10
c = user3 % 10
print("sum is: ",a+b+c)


# we will do it by loop