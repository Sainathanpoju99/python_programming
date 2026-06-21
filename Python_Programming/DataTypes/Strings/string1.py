name = str('job')
print(type(name))

str = 'welcome' 
print(str + 'programming')
print(str *3)

# slicing strings
mystr = 'welcome'
print(mystr[0])  
print(mystr[1:3])      # first character
print(mystr[:6])
print(mystr[2:])
print(mystr[1:-1])
print(mystr[-5:-3])

#Formatting string
age = 30
str1 = f'my age is {age}'
print(str1)
print(f'my age is {age + 5}')

priceOftheItems = 33
print(f'the price of the item is {priceOftheItems:.5f} dollars')  # formatting to 2 decimal places
print(f'the price of the item is {priceOftheItems * 20.45222:.4f} dollars')  
print('the price is', priceOftheItems)

# IN and NOTIN with strings -- returns boolean value
str2 = 'welcome to programming'
print('programming' in str2)   # True
print('ff' in str2)            # False
print('welcome' not in str2)  # False
print('ff' not in str2)       # True

#captialize() 
s = 'hello Python PPorld'
print('Captialization string: ', s.capitalize())
print(s.casefold())
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(str.center(25))
print(str.center(25, '-'))
print(str.center(25, '-'))
print("hello {}".format(s))

# find() and index() searches the string for a substring and returns the index of first occurrence of the substring
# if substring is not found, find() returns -1 whereas index() raises a ValueError
m = 'manage'
print(m.find('e'))
print(m.find('ma'))
print(m.index('a'))
print(m.index('g'))
#print(m.index('q'))  #ValueError: substring not found

# count() returns the number of occurrences of a substring in the given string
print('count value: ', m.count('a'))
print('count value', m.count('na'))

# replace() replaces all occurrences of a substring with another substring
print('replace : ', m.replace('ma', 'ab'))

# isalnum() returns True if all characters in the string are alphanumeric
d = 'abc123'
print(d.isalnum())
e = 'abc@123'
print(e.isalnum())

#isalpha() returns True if all characters in the string are alphabetic
f = 'abcde'
print(f.isalpha())
f1 = 'abc123'
print(f1.isalpha())

# isdecimal() returns True if all characters in the string are decimal characters
g = '12345'
print('isdecimal: ', g.isdecimal())
g1 = '123a45'
print(g1.isdecimal())

# isdigit() returns True if all characters in the string are digits
h = '67890'
print('isdigit returns: ', h.isdigit())
h1 = '6789a0'
print('isdigit returns: ', h1.isdigit())
h2 = '1.345'  # superscript 2
print('isdigit returns: ', h2.isdigit())


# isnumeric() returns True if all characters in the string are numeric
i = '12345'
print('isnumeric returns: ', i.isnumeric())
i1 = '123.45'
print('isnumeric returns: ', i1.isnumeric())

# isupper() returns True if all characters in the string are uppercase
# islower() returns True if all characters in the string are lowercase
mm = "jackkUU"
print('isupper returns: ', mm.isupper())
print('islower returns: ', mm.islower())
mm1 = "JACKKU"
print('isupper returns: ', mm1.isupper())
print('islower returns: ', mm1.islower())
































