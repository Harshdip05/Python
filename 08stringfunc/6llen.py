# String Functions

# len() returns the number of items in an object.
# len(obj)


a = "hello world"
print(len(a),a)

b = "hello\nworld"  # newline characters
print(len(b),b)

print(len("😊"))  # unicode characters


# print(len(123))  # Using len on non-iterables


"""
'python'
stored as ['p', 'y', 't', 'h', 'o', 'n']
so len("python") == number of elements
"""


# why is len() fast ?
# Time complexity O(1) and not O(n)