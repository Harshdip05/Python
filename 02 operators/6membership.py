# Membership operators are used to check whether a value exists inside a sequence.
#        in = present            not in = absent
# Works with:  string list tuple set dictionary

print("D" in "DELHI")
print("d" in "DELHI")  # case sensitive

print("d" not in "DELHI") 

print()



d = {"a": 1, "b": 2}
print("a" in d)   # Is "a" a KEY in dictionary?
print(1 in d)     #  # Is 1 a KEY in dictionary?
# Checks keys, not values in dict

print(1 in d.values())
print(("a", 1) in d.items())
print(d.items())

print()

print(3 in {1, 2, 3})
print(10 in (5, 10, 15))
print(5 in [1,2,3,4,5])
print(8 not in [1, 2, 3])

print()

print(3 in [1,2,[3,4]])  # [3,4] is one element
print(5 in [])
print(5 in range(1, 10))


print()

print(True in [1, 2, 3])    # True == 1
print(True in [ 2, 3])
print(False in [0, 2, 3])    # False == 0
print(1 in [True, False])
# print(5 in 12345)  # TypeError: argument of type 'int' is not iterable


# membership(in)  VS equality(==) operator
# in VS is