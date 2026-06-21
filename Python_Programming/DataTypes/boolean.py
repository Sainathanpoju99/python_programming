a = True
b = False
print(type(a))
print(type(b))

x = 15
y = 225
print(bool(x == y))
x = None
print(bool(x))
x = ()
print(bool(x))
x = {}
print(bool(x))
x = 0.0
print(bool(x))

x = 'Greek'
print(bool(x))


# Boolean Operators: OR / AND /  NOT / == (equivalent) / != (Not equivalent)


# OR Operator:
'''
true true = true
true false = true
false true = true
false false = false
'''

a = 2
b = 5
c = 10
if (a > b or b < c):
    print(True)
else: 
    print(False)

if a or b or c:
        print('Atleast one number has boolean value as true')
else:
     print('Atleast one number has boolean value as false')


# AND Operator:
'''
true    true    = true
false   true    = false
true    false   = false
false   false   = false
'''
if (a > b and b < c):
    print(True)
else: 
    print(False)

if a and b and c:
        print('Atleast one number has boolean value as true')
else:
     print('Atleast one number has boolean value as false')


# Not Operator:
'''
 A      Not A
true    false
false   true
'''
a = 5
if not a:
     print('Boolean value of a is False')
else:
     print('Boolean value of a is True')

a = 0
if not a:
     print('Boolean value of a is False')
else:
     print('Boolean value of a is True')

# == & != Operator:
v = 5
c = 2
if v == 0:
     print(True)
if v == c:
     print(True)
if v != c:
     print(True)
     
# is Operator: test whether two variables belong to the same object. 
x = 10
y = 10

if x is y:
    print(True)
else:
    print(False)

x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"]
print(x is y)
         
# in Operator: checks for the membership i.e. checks if the value is present 
# in a list, tuple, range, string, etc.
# Create a list
animals = ["dog", "lion", "cat"]
# Check if lion in list or not
if "lion" in animals:
    print(True)
else: 
     print(False)
     







