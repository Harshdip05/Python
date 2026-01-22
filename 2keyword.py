# Keywords are words that:
    # have special meaning in Python
    # cannot be used as variable names
    # are part of Python syntax

import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))


keyword.iskeyword("for")     # True
keyword.iskeyword("while")   # True
keyword.iskeyword("apple")   # False
keyword.iskeyword("sum")     # False