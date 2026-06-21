# Variable are containers to store values.
# Python is a type inferred language, we don't need to explicitly define the variable type.
a = 10
b = 'John'
c = 3.0
print(a)
print(b)
print(c)

# Multple values to multiple variables
q, w, e = 254, 1049.225, 'data warehouse'
v = b = n = "JavaScript" # One value to multiple variables
print(q, w, e)
print(v)
print(b)
print(n)



#Unpack a collection:
fruits = ['apple', 'orange', 'cherry']
f, g, h = fruits
print(f, g, h)
print(f + g + h) # '+' operator to add multiple variables

'''Rules for naming variables.
snake_case
MACRO_CASE
camelCase
CapWords

my_name
current_salary

Python is case-sensitive. So num and Num are different variables. For example,
var num = 5 
var Num = 55
print(num) # 5
print(Num) # 55 

Also, avoid using keywords like if, True, class, etc. as variable names'''

# Casting and get the type of variable
raj = str(51)
ron = int(55620)
eon = float(352)
print(raj, ron, eon) #casting
print(type(raj)) #type of
print(type(ron))
print(type(eon))
print(type(raj), type(eon))

#########################################
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#####################

# Camel Case 
myVariableName = 'Python'
# Pascal Case
MyVariableName = "Jython"
# Snake Case
my_variable_name = 'Numpy'
print(my_variable_name, MyVariableName, myVariableName);

''' Global Variables: Variables that are created outside of a function
Also global variables can be used by everyone 
both inside of the function and outside
'''
page = 'awesomeness of the wallet'
def myfunc():
    print("Paystack is: " + page)
myfunc()

def myfunct():
    page = 'Gango' # variable inside a function
    print("details are: " + page)
myfunct()
print("Paystake is: " + page)

def myValue():
    # global keyword used to create a variable inside a function 
    # and this variable is local and can only be used inside the function
    global page
    page = "homepage"
myValue()
print('Paystack is: ' + page)

# Exercise:
useFeatureValue = 'Tentative boberman'
def myPip():
    global useFeatureValue
    useFeatureValue = 'Handsome Values to represent'
    print('useFeatureValue: ' + useFeatureValue);
myPip()
print(useFeatureValue)






