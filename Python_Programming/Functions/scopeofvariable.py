# Global vs Local Scope of Variables
# Global Variables: Defined outside any function, accessible anywhere in the code.
# Local Variables: Defined inside a function, accessible only within that function.

a = 225 # Global variable

def my_function():
     x = 22 # Local variable
     print('Inside function, x:', x)
     print('Inside function (Global): , a:', a) # Accessing global variable

my_function()
print('Outside function, a:', a) # Accessing global variable
# print('Outside function, x:', x) # This will raise an error as x is
print('-------------------')


m = 332 # Global variable

def another_function():
     m = 100 # Local variable
     print('Inside another_function, m:', m) # Accessing local variable
another_function()
print('Outside another_function, m:', m) # Accessing global variable
print('-------------------')



# Using global variable in local scope and updating values
# Modifying global variable inside a function using 'global' keyword
# Without 'global' keyword, a new local variable is created
# To modify the global variable, we need to declare it as global inside the function
# Using 'global' keyword
# Example: 
fff = 555 # Global variable
def yet_another_function():
     global fff
     fff = 999 # Modifying global variable
     print('Inside yet_another_function, fff:', fff) # Accessing modified global variable
yet_another_function()
print('Outside yet_another_function, fff:', fff) # Accessing modified global
print('-------------------')


# Declare the global variable inside the function
def sample_function():
     global xr
     xr = 777 # This will create a global variable
     print('Inside sample_function, xr:', xr)
sample_function()
print('Outside sample_function, xr:', xr) # Accessing global variable



















