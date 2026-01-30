# Python compares characters using ASCII / Unicode values.

text = "hello world"

print(max(text))
print(min(text)) # space is min in text

# A–Z  → 65–90
# a–z  → 97–122

# This is not numeric max/min, it’s character comparison.
print(max("123"))
print(min("123"))


# Find max occurring character
# Find min occurring character

# max() and min() work in O(n) time