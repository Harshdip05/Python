## STRINGS IN PYTHON ARE IMMUTABLE
        # once created → cannot be changed
        # every “edit” creates a new string object
        # old string remains unchanged in memory

s = "hello world"
# variable s stores a reference
# string object lives in the heap
# stack heap

# s[0] = "H"  #TypeError: 'str' object does not support item assignment


print()


# del deletes a reference (variable name), not the object itself.
# Python removes the binding between a variable and an object.
m = "hello"
del m
# print(m)
# hello eligible for garbage collection


print()

v = "hello world"
del v[-1:5:2] 
print(v)
# You cannot delete characters
# You cannot delete slices
# You cannot modify string memory

# del on slices works only for mutable objects like:
# lists
# bytearray
# array