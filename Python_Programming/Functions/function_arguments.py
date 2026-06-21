# 1. Arbitrary Arguments (*args) or variable-length arguments
# 2. Positional Arguments or Required Arguments
# 3. Keyword Arguments
# 4. Default Arguments

# Functions with Arbitrary Arguments (*args) or variable-length arguments

def sum_numbers(*numbers):     # this number will be considered it has a tuple
     total = 0
     for i in numbers:
          total = total + i
     return total

print('sum of numbers using *args: ', sum_numbers(5, 10, 15, 20))
print('sum of numbers using *args: ', sum_numbers(1, 2, 3))
print('sum of numbers using *args: ', sum_numbers(100, 200, 300, 400, 500))
print('sum of numbers using *args: ', sum_numbers())
print('-------------------')

def myf(*args, **kwargs):
     for arg in args:
          print('Positional arguments (args): ', args)
     for key, value in kwargs.items():
          print('Keyword arguments (kwargs): ', key, value)
myf('Hey', 'There', name='Alice', age=30, city='New York')
print('-------------------')

# Functions with Positional Arguments or keyword Arguments

def cal(a, b):   # a and b are positional arguments
       print(a, b)
       return a + b
   
res = cal(5, 10)  # we are passing 5 and 10 as arguments to the function
print('sum is: ', res)

def cal1(x, y):
     print(x, y)
cal1(y=22, x=11)  # we are passing arguments using keyword

# default values can be assigned to positional arguments
def kal(a, m=20):
      print(a, m)
kal(333)

# mixing positional and keyword arguments
def mak(a, b, c):
      print(a, b, c)

mak(10, 20, 30)          # all positional arguments
mak(a=1, b=2, c=3)      # all keyword arguments
mak(100, c=300, b=200)  # mixing positional and keyword arguments
#mak(22, 33, b=44)    #  this is logical error as b is given twice and not allowed
# mak(10, b=2, 2)   # this will give error as positional argument follows keyword argument

# Function can return multiple values
def largest(a, b):
      if a>b:
            return a,b
      else:
            return b,a
print(largest(300, 400))
res = largest(50, 20)
print(res)
print(type(res)) # tuple
print('-------------------')

# Default Arguments
def myFunc(x, y=50):
      print('x:', x)
      print('y:', y)
myFunc(10)      # y will take default value 50
myFunc(10, 100) # y will take value 100
myFunc(x=5)     # y will take default value 50









































