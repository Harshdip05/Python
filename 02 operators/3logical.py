# Logical operators are used to combine conditions and return True or False.
#                       and   or   not
# Logical operators work with: relational operators


# truthy and falsy values
        # Python decides this automatically when using:
        # if    while    logical operators (and, or, not)


# Python uses short-circuit evaluation.
                # AND → stops at False 
                # OR  → stops at True  
print("" or "Python")
print(False and print("Hi"))
print(10 > 5 or print("Hello"))
print(1 and 0)
print(1 or 0)

print()

print(not 1)
print(not 10)
print(not "hello")
print(not False)