# python is case sensitive language,high level lang
# A high-level language is human-readable and abstracts hardware details.
# A low-level language is close to hardware and provides direct memory control.

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


print("hello"+"world")
print("hello","world")