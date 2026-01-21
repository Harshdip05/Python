# MULTIPLE CONDITIONS = and  or  not

# email = "harsh11@gmail.com"
# password = "123"

email = input("Enter your email: ")
password = input("Enter your password: ")


if email=="harsh11@gmail.com" and password=="1234":
    print("Welcome")
elif email=="harsh11@gmail.com" and password != "1234":
    print("Incorrect Password") 
    password = input("Enter password again: ")
    if password == "1234":
        print("Welcome, finally")
    else:
        print("beta tumse na ho payega")    
else:
    print("Not Correct input")    


print()

# not 
is_logged_in = False
if not is_logged_in:
    print("Please login")
