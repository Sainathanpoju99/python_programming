#Arithmetic Operators:
val1 = 250
val2 = 391

res = val1 + val2
print("Addition of two numbers: \n", res)

res1 = val1 - val2
print("Subtraction of two numbers: \n", res1)

res2 = val1 * val2
print("Multiplication of two numbers: \n", res2)

res3 = val1 / val2
print("Division of two numbers: \n", res3)

res4 = val1 % val2
print("Modulus of two number: \n", res4)

res5 = val1 ** val2
print("Exponentiation of two numbers: \n", res5)

res6 = val1 // val2
print("Floor division of two numbers: \n", res6)

# Difference between / and // operator:
a = 555
b = 10
result = a // b
print("Print the floor division value: \n", result)

result1 = a / b
print("Print the division value: \n", result1)      

# Difference betweeen * and ** operator:
c = 10
d = 20
result2 = c * d
print("Print the multiplication value: \n", result2)

result3 = c ** d
print("Print the exponentiation value: \n", result3)

list = ['py'] * 5
print("Print the list: \n", list)

arr = ['sunday', 'monday', 'tuesday', 'wednesday']
# without using asterisk
print(' '.join(map(str,arr))) 
# using asterisk
print (*arr) 
#----------------------------------------------------
# Comparison Operators:
a= 10
b = 25
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
#----------------------------------------------------
# Logical Operators:
# And Or Not
x = True
y = False
print("Logical Operator: ", x and y)
print(x or y)
print(not y)
#----------------------------------------------------
# Bitwise Operators: 
# Bitwise - NOT, Shift, AND, OR, XOR
w = 11
e = 22
print("Bitwise AND Operator: ", w & e)
print("OR Operator: ", w | e)
print("NOT Operator: ", ~w) 
print("XOR Operator: ", w ^ e)
print("Right Shift Operator: ", w >> 2)
print("Left Shift Operator: ", w << 2)
#----------------------------------------------------
# Assignment Operators:
r = 5
t = 9
r += t
print("Addition Assignment Operator: ", r)
r -= t
print("Subtraction Assignment Operator: ", r)
r *= t
print("Multiplication Assignment Operator: ", r)
r /= t
print("Division Assignment Operator: ", r)
r %= t
print("Modulus Assignment Operator: ", r)
r **= t
print("Exponentiation Assignment Operator: ", r)
r //= t
print("Floor Division Assignment Operator: ", r)
r = 5
t = 9
r &= t
print("Bitwise AND Assignment Operator: ", r)
r |= t
print("Bitwise OR Assignment Operator: ", r)
r ^= t
print("Bitwise XOR Assignment Operator: ", r)
r >>= t
print("Right Shift Assignment Operator: ", r)
r <<= t
print("Left Shift Assignment Operator: ", r)
#----------------------------------------------------
# Walrus Operator:
# The walrus operator is a new operator in Python 3.8 that allows you to assign values to variables as part of an expression.
# The walrus operator is :=, and it is useful when you want to assign a value to a variable as part of an expression.
u = [1,2,3,4,5]
while(i := len(u)) > 2:
    u.pop()
    print(i)
#----------------------------------------------------
# Membership Operators:
# Membership operators are used to test if a sequence is presented in an object.
# in, not in
list = [1, 2, 3, 4, 5]
str = 'Hello World'
dist = {1: 'apple', 2: 'banana', 3: 'cherry'}
print(2 in list)
print('M' in str)
print('fff' in dist)

print(2 not in list)
print('M' not in str)
print('fff' not in dist)

#Contains() method:
import operator
print(operator.contains(list, 2))
print(operator.contains(str, 'M'))
print(operator.contains(dist, 'fff'))
# checking an integer in a list
print(operator.contains([1, 2, 3, 4, 5], 2))
# checking a character in a string
print(operator.contains("Hello World", 'O'))
# checking an integer in aset
print(operator.contains({1, 2, 3, 4, 5}, 6))
# checking for a key in a dictionary
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}, 3))
# checking for an integer in a tuple
print(operator.contains((1, 2, 3, 4, 5), 9))

# Identity Operators:
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
# is, is not 

num1 = 5
num2 = 5

a = [1, 2, 3]   
b = [1, 2, 3]
c = a

s1 = 'hello world'
s2 = 'hello world'
# IS Operator:True if the variables on either side of the operator point to the same object in the memory and false otherwise.
print('Identity Operator: ', num1 is num2)
print(a is b)
print(a is c)
print(s1 is s2)
print(s2 is s1)
#IS NOT Operator: True if both variables on the either side of the operator are not the same object in the memory location otherwise it evaluates False
print('Identity Operator: ', num1 is not num2)
print(a is not b)       
print(a is not c)
print(s1 is not s2)
print(s2 is not s1)

# Python program to illustrate the use
# of 'is' and '==' operators
a = [1, 2, 3]
b = [1, 2, 3]
# using 'is' and '==' operators
print(a is b)
print(a == b)
#----------------------------------------------------
''' Ternary Operator: is used to assign different values to a variable based on a condition.
Syntax: [on_true] if [expression] else [on_false] '''

# If else:
a1 = 10
res = 'Even' if a1 & 2 == 0 else 'Odd'
print('Ternary Operator: ', res)

# nested if else:
a2 = -10
res1 = 'Positive' if a2 > 0 else 'Negative' if a2 < 0 else 'Zero'
print('Ternary Operator: ', res1)

# Tuple
a3 = 8
res3 = ('Even', 'Odd')[a3 % 2 == 0]
print(res3)

# Dictionary
a4 = 10
a5 = 20 
res4 = {True: a4, False: a5}[a4 > a5]
print(res4)

#Python lambda function:
max = (lambda x,y: x if x > y else y)(a4, a5)
print('Lambda Function: ', max)

# With print function:
print('a4 is greater' if a4> a5 else 'a5 is greater')
#----------------------------------------------------
# Precedence and Associativity of Operators:
# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
	print("Hello! Welcome.")
else:
	print("Good Bye!!")

if (name == "Alex" or name == "John") and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# Associativity 
# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)

# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)

# left-right associativity
print(5 - (2 + 3))

# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)

#Operators Precedence and Associativity in Python
expression = 100 + 200 / 10 - 3 * 10
print(expression)





















