import random 

jackpot = random.randint(1,100)
print("jackpot",jackpot)

user = int(input("enter number: "))
print("user",user)

while jackpot != user:
    if user<jackpot:
        print("galat! guess higher")
    else:
        print("galat! guess lower")    
