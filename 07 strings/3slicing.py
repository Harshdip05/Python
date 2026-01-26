# String slicing means extracting a portion (substring) of a string using indexes.
        # string[start:end:stop]

s = "Hello world"

print(s[0:5])
print(s[2:3])

print(s[0:])
print(s[:11])
print(s[:])
print(s[::])

print(s[0:6:2])
print(s[::2])

print(s[::-1])   ## reverse string

print(s[0:6:-1])   # when step size negative then start with big nummber
print(s[6:0:-1])

print(s[-1:-8])
print(s[-1:-8:-1])  # whenever use negative indexing then first number greater than second
print(s[-8:-1])


print(s[0:100])
# print(s[100])  # IndexError: string index out of range