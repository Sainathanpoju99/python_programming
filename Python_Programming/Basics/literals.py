'''Types of Literals in Python
1. String literals
2. Character literal
3. Numeric literals
4. Boolean literals
5. Literal Collections
6. Special literals
'''
# String literal
# Single and double quotes
jo = 'Jon'
ho = "Hon"
print(jo, ho)
a = 4
A = "Sally" #A will not overwrite a
print(a, A)

# Multi line string

m = '''geek     
            for
                geeks'''
print(m)


# Character Literal
x = 'a'
y = 'b'
z = 'c'
print(x)
print(y)
print(z)

# Numeric Literal: Integer and Float and Complex
# Interger Literal
# Binary Literal
a = 0b0100
# Decimal Literal
b = 50
# Octal Literal
c = 0o320
# Hexadecimal Literal
d = 0x12b
print(a, b, c, d)

#Float literal
e = 24.9
g = 55.33
print(e, g)

# Complex Literal
z = 8 + 6j
l = 55j
print(z, l)

# Boolean Literal
ad = (1 == True)
we = (3 == False)
er = True + 5
qw = False - 55
print("ad: ", ad)
print('we: ', we)
print('er: ', er)
print('qw: ', qw)

# Literal Collection
# 1. List Literal
number = [1, 2, 3]
name = ['amit', 'john', 1049]
print(number)
print(name)

#2. Tuple Literal
odd_number = (15, 551, 89)
even_number = (42, 4, 20)
print(odd_number)
print(even_number)

#3. Dictionary Literal
information = {'a': 'apple', 'data': 'server cannot reached', 'ab': 1049, 'ID': 204}
print(information)

#4. Set Literal:
matic_Data = {'r', 'Ta', 'WEG', '55'}
print(matic_Data)

# 5. Special Literal: Only one special literal is None and it is defines a null value. 
# If none is compared with anything else other then a 'None', it will return false
junk_remain = None
remain = (False == None)
remin = (True == None)
rem = (None == None)
print(junk_remain)
print(remain)
print(remin)
print(rem)



















































