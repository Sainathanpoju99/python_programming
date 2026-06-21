# Example 1
# print('welcome'   # Syntax error

# Example 2 : Exception
#n = 10
#res = n/0       # ZeroDivisionError: division by zero
#print(res)

# Example 3
#x = '10'        #TypeError
#x = int('10')
#x = int('wel')      #ValueError
#print(x+5)

# Handling exception using try and except
# 5
try:
    print(x)
except NameError:
    print('NameError thrown')
except:
    print('some other exception:')

# 6: else with try
# We can execute the else block of code when there is no errors were raised

try:
    print('hello')
except:
    print('something went wrong')
else:
    print('goodbye')

# 7: finally block
try:
    #print(z)
    print('welcome')
except:
    print('something went wrong')
finally:
    print('this is finally block')

# 8: try, except, else, finally
# try:
#     n = int(input('Enter the number: '))
#     res = 100 / n
# except ZeroDivisionError:
#     print('ZeroDivisionError: You cannot divide by zero')
# except ValueError:
#     print('ValueError: Enter a valid number')
# else:
#     print('Result: ', res)
# finally:
#     print('finally exception completed...')

# 9: try block inside another try block
try:
    file = open('E:/Automation_Scripts/PyCharm/Python_Coding/Python_Programming/my_file.txt', 'r')  # w to write
    try:
        file.write('hello_world')
    except:
        print('Something went wrong when writing to the file')
    finally:
        file.close()
except:
    print('Something went wrong when opening the file')


# 10: Customized/raise exception
# As a python developer, you can choose to throw an exception if a condition occurs
# To throw (or raise) an exception, use the 'raise' keyword
# x = -1
# if x < 0:
#     raise Exception('Sorry no number below zero')

# next
# x1 = 'hello'
# if not type(x1) is int:
#     raise TypeError('only integers are allowed')

# next: how the developer raise exceptions
def set(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    print('Age:', age)

set(5)
#usage of the function
try:
    set(-10)
except ValueError:
    print('Invalid data provided')
print('-----------------')

#Catching multiple excetions:
a = ['10', 'twenty', 33]
try:
    total = int(a[0] + a[1])
except (ValueError, TypeError) as e:
    print('Error: ', e)
except IndexError:
    print('Index out of range')






















