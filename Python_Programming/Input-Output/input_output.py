amount = 1250.995
print("Amount: ${:.3f}".format(amount))

print("Python", end ='@')

print("GeeksforGeeks")

print('G', 'F', 'G', sep='')
print('G', 'F', 'G', sep='-')
print('G', 'F', 'G', sep='@')


name = 'Jay'
fromm = 'Delhi'
print(f"Hello, I'm {name} and I'm from {fromm}.")

# Taking input from the user
num = int(input("Enter a value: "))
add = num + 5
# Output
print("The sum is %d" %add)


# Prompting the user for input
age_input = input("Enter your age: ")


# Converting the input to an integer
age = int(age_input)
# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


q = 'hello'
w = 10
e = 112.33
r = False
t = ('apple', 'banana', 'cherry')
y = ['apple', 'banana', 'cherry']
u = {'name': 'John', 'age': 25}

print(type(q))
print(type(w))
print(type(e))
print(type(r))
print(type(t))
print(type(y))
print(type(u))


num = int(input('Enter a number?\n'))  # \n ---> newline  ---> It causes a line break
print(num, " " , type(num))

floatNum = float(input('Enter a float number?\n'))
print(floatNum, " " , type(floatNum))

string = str(input('Enter a string?\n'))
print(string, " " , type(string))











































