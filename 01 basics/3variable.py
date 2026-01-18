# static vs dynamic typing
# static(early) vs dynamic(late) binding


# Variable Naming Rules
# Cannot start with a number,No special characters, no spaces,Cannot use Python keywords
# variable can start with letter and underscore
_= "harsh"
print(_)
# first-name is wrong variable name

# naming conventions
# use snakecase and for constants use UPPERCASE
first_name = "Virat"
ROLL_NO = 7
# avoid camelcase and pascal case


a,b,c=1,2,3
print(a,b,c)

x=y=z=5
print(x,y,z)


# Keywords cannot be used as variable names
# Keywords are case-sensitive
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.iskeyword("for"))  
print(keyword.iskeyword("python"))


# Comments are lines that Python ignores during execution.
# single line comment
"""multiple line comment"""