# USER DEFINED FUNCTIONS:

# PARAMETERIZED FUNCTIONS:
def fun(name):
    print('hello', name)
fun('Shak')


# FUNCTIONS WITH DEFAULT ARGUMENTS:
def fun(x, y=50):
    print('x:', x)
    print('y:', y)
fun(30)

# KEYWORD ARGUMENT FUNCTIONS:
def func(gname, bname):
    print(gname, 'is a', bname, 'dine')
func(bname = 'Mye', gname = 'Don')


# VARIABLE LENGTH ARGUMENT FUNCTIONS:
def fun(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
fun('jay', 'pitts', name='Jay', age=30, max=10)


# FUNCTIONS WITH RETURN VALUE
def fun(num):
    return num * 2
res = fun(10)
print(res)


# LAMBDA FUNCTIONS
res = lambda x: x * x
print(res(4))




