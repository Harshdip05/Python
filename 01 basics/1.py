# python is case sensitive language

print("hello world")
print('hello world')
print("""hello world""")

print(1234)
print(1.11)

print(True)
print("True")

print("hello","how","are","you")
print("hello","how","are","you",sep="-")   # sep works when there are two  or more objects

print("hello",end="\n")   # end = "\n" is default , end decides what is printed at end
print("world")


print("hello",end="+++")   
print("world")

print(print.__doc__)   # docstring