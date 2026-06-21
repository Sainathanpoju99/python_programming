# Unary Operator:
a = 2.315
b = -2.6654

c = -a
print('minus operator: ', c)
c = -b
print('minus operator: ', c)

c = +a
print('plus operator: ', c)
c = +b
print('plus operator: ', c)

a = 2
b = -2
c = ~a 
print('Bitwise NOT/Invert operator value of 1: ', c)
c = ~b
print('Bitwise NOT/Invert operator value of -1: ', c)
c = ~a + 1
print('Bitwise NOT/Invert operator value of 2: ', c)

# Addition Operator:
a = 4
b = -5
d = a+b
print('Addition operator1: ', d)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
d = []
for i in range(len(a)):
    d.append(a[i] + b[i])
    print('Addition operator2: ', d)

# Subtraction Operator:
a = 4
b = -5

d = a - b
print("Subtraction value 1: ",d)
print("Subtraction values: ")
a = [1, 4, 5] 
b = [1, 2, 3]
for i in range(len(a)):
    print(a[i] - b[i])

result = [x - y for x, y in zip(a, b)] # List comprehension alternative way to write the above code
print('res', result)


# Multiplication Operator:
a = 4
b = -5
c = 5.02

# This * operator performs 
# Multiplication of two 
# operands or numbers
d = a * b
print("Multiplication value 1:", d)

d = a * c
print("Multiplication value 2:", d)

# Division Operator:
a = 20
b = -5
c = 5.02

# This '/' operator performs 
# Division of two operands 
# or numbers
d = a / b
print("Division value 1:", d)

d = a / c
print("Division value 2:", d)

# Exponentiation Operator:
a = 5
b = 3
c = -3

# This ** operator performs 
# Exponential operation of two 
# operands or numbers
d = a ** b
print("Exponent value 1:", d)

d = a ** c
print("Exponent value 2:", d)

# Modulus Operator:
a = 12
b = 5
c = 3

# This % operator performs Modulus 
# of two operands or numbers and 
# return the remainder
d = a % b 
print("Modulus value 1:", d)

d = c % b
print("Modulus value 2:", d)

#----------------------------------------------------
# Python code to Demonstrate the Exponential Operactor
a = 2
b = 5
# using double asterisk operator
c = a**b
print(c)
# using double asterisk operator
z = 2 * (4 ** 2) + 3 * (4 ** 2 - 10)
print(z)
















