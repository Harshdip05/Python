"""
isinstance() is used to check:
whether a value belongs to a particular data type or class.
"""

"""
type() → checks exact type
isinstance() → checks family relationship
"""

# isinstance(object, class)


x = 10
print(isinstance(x, int))


print(isinstance(True, int))


print(isinstance(10, (int, float)))  #Checks multiple types at once.
