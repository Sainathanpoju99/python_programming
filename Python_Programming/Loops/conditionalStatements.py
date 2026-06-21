# Conditional Statements:
# if, elif, else
# if statement: Executes a block of code if the condition is true.

# if Condition:
abc = 100
if abc > 99:
    print("abc is greater than 99")

age = 19
if age > 18: print("Eligible to Vote.")  #short hand if statement

# if else condition:
name1 = "Error"
if name1 == "Error1":
    print("Name is Error")
else:
    print("Name is not Error")  # else statement: Executes a block of code if the condition is false.

name2 = "Error"
er = "Correct" if name2 == "error" else "Wrong"
print(f"Result: {er}")  # Ternary operator: A shorthand way to write an if-else 

#elif statement:
price = 150.60
if price >= 150:
    print("Done")
elif price > 100 and price < 150:
    print("Good deal")
else: 
    print("Find a better deal")

age =25

if age <= 18:
    print("You are a minor")
elif age <= 19:
    print("Your a teenager")
elif age >= 35:
    print("You are an adult")
else: 
    print("Adult")

# Nested if statement:
agee = 25
is_member = True
if agee >= 20:
    if is_member:
        print("30% discount")
    else: 
        print("10% discount")
else: 
    print("No discount")

#if
a = 20
if a > 10:
    print('a is not greater than 30 ')

# if else
if a > 30:
    print('a is not greater than 30 ')
else:
    print('a is greater than 30 ')

"""if elif else"""
if a == 30:
    print('a is equal to 30')
elif a < 30:
    print('a is less than 30')
else:
    print('a is greater than 30')

#Short hand if else
print('a is less than 15') if a < 15 else print('a is greater than 15') 


# Nested if condition:
if a < 50:
    if a % 2 == 0:
        print('a is less than 50 and even')

    