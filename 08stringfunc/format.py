name = "Alex"
age = 20

print("My name is {} and I am {} years old".format(name, age))

print("My name is {} and I am {} years old".format(age, name))

print("My name is {0} and I am {1} years old".format(name, age))

print("{name} is {age} years old".format(name="Alex", age=25))  #named arguments

print("{0} is {1} years old".format("Alex", 25))  #positonal


# Number formatting means:
        # How you want a number to look when printed.
        # You don’t change the number — only how it appears.

num = 12.34567
print("{:.2f}".format(num))
print("{:.2%}".format(num))  