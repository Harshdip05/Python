# A fixed value written directly in the program.
# It does not change during program execution.

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)


string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"
print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


a = True + 4
b = False + 10
print("a:", a)
print("b:", b)
# 
print(int(True))    # 1
print(int(False))   # 0


k = None  # if you dont know for now what is k 
a = 5
b = 6
print('Program exe')