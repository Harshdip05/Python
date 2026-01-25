## Accessing sustrings from string

# A string is a sequence of characters.
# Each character has a position number, called an index.

s = "Hello World"

print(s)
print(s[0])
print(s[10])

# print(s[44])  # IndexError: string index out of range
# s[0] = "M"    # TypeError: 'str' object does not support item assignment

print(s[-1])
# print(s[-15])  # IndexError: string index out of range
# s[-1] = "M"      # TypeError: 'str' object does not support item assignment

print(len(s))



# Base address = starting memory location of data
# It is the address where the first element is stored in computer memory.
# address = base_address + index × size
# Indexing starts from 0 because the index represents the offset from the base memory address.
# The first element is at offset 0, so its index is 0.
# This allows faster and simpler memory access without extra calculations.