# Type casting and type conversion
# Type casting is when you change an object data type to another data type
# Type conversion is when you change the data type of an object 
# to another data type

num = 254
print(float(num))

bum = 553.22544
print(int(bum))

sum = '225'
print(type(int(sum)))

dum = '55.325499'
print(type(float(dum)))

print(type(str(dum)))

r = 6+5j
print(complex(r))


f = 55.30
print(complex(f))


# Decimal Numbers
a = 1.1
b = 2.2
c = a+b
print(c)

f = 1.2
d = 1.0
s = f-d
print(s)

import decimal
d = decimal.Decimal('1.5')
g = decimal.Decimal('2.5')
b = d + g
print(b)

# Implicit Type Casting:
num_int = 5
num_float = 666.3321
result = num_int + num_float
print(result)
print(type(result))

# Explicit Type Casting:
num_str = '552'
num_intt = int(num_str)
print(num_intt)
print(type(num_intt))










