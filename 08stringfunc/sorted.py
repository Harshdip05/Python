# sorted() returns a list, not a string
# Sorting is based on ASCII / Unicode values.

text = "hello world"

print(sorted(text))
print(sorted(text,reverse=True))


# Time complexity: O(n log n)