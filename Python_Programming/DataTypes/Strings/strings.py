string_0 = "Payout should be 0"
print(string_0)
print(type(string_0))

string_1 = "Welcome to the Python world"
print("\nString with the use of double quotes")
print(string_1)
string_2 = 'Wellcome Guys'
print('\n String with the use of single quptes')
print(string_2)
string_3 = '''I'm a geek python'''
print('\n String with the use of triple quotes')
print(string_3)
string_4 = '''Geeks
for
lifetime
union
'''
print('\nString with the use of multiline string')
print(string_4)


'''
GenzTester
0123456789
-10-9-8-7-6-5-4-3-2-1
'''
string_5 = 'GenzTester'
print('Initial String: ', string_5)
print('First char of the string: ', string_5[0]) # Positive Indexing
print('Last char of the string: ', string_5[-1]) # Negative Indexing

# String Slicing:
print('\nSlicing char from 2-6: ', string_5[2:5])
print('Slicing char b/w' + 
      ' 3rd and 2nd last char: ', string_5[3:-2])
print('\nPrint till 7th index: ', string_5[:7])
print('Print between both index: ', string_5[1:8])

# String Reversed:
print('\nReversing a string: ', string_5[::-1])
print('Reversing a string: ', string_5[::-5])
rev = "".join(reversed(string_5))
print('Reversing a string rev: ', rev)

# String deleting/updating
# Python strings are immutable and they cannot be updated directly
# We are converting string to a list
string_6 = 'JabbaGabba'
print('\nInitial String: ', string_6)
# One way to convert
list_conv = list(string_6)
list_conv[4] = '2'
strr = ''.join(list_conv)
print('Updating the char at 4th index: ', strr)

# Another way to convert
strr1 = string_6[0:4] + '2' + string_6[5:]  # String slicing method
print(strr1)

# Updating entire string
string_7 = 'Entire String'
print('\nInitial String: ', string_7)
string_7 = 'Updated the Entire String'
print('Updated String: ', string_7)

# Deleting the character from the string using slicing method
print('Initial String: ', string_7)
strr2 = string_7[0:6] + string_7[15:]
print('Deleting a char from the string and then concatenated: ', strr2)

# Deleting the entire string: after deleting a string will get an error 
'''del string_7
print('\nTrying to print the deleted string: ', string_7) '''

# Escape Sequencing 
string_8 = '''I'm a "Geeky"'''
print("\nInitila String with the use of triple quotes: " )
print(string_8)

string_9 = 'I\'m a "greek"'
print('\n Escaping single quotes: ') # Escaping Single quote
print(string_9)

# Escaping Double Quotes
String10 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String10)

# Printing Paths with the
# use of Escape Sequences
String11 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String11)

# Printing Paths with the
# use of Tab
String12 = "Hi\tGeeks"
print("\nTab: ")
print(String12)

# Printing Paths with the
# use of New Line
String13 = "Python\nGeeks"
print("\nNew Line: ")
print(String13)

# To ignore the escape sequences in a string 
# We use r or R as a raw string
String14 = "This is \110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ")
print(String14) 

string_15 = r'This is \110\145\154\154\157'
print('\nPrinting raw string in octal format: ')
print(string_15)

string_16 = "This the HEX value: \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print('\nPrinting the raw string in hex format: ')
print(string_16)
string_17 = r'This the HEX value: \x47\x65\x65\x6b\x73 in \x48\x45\x58'
print('\nPrinting the raw string in hex format: ')
print(string_17)


# String formatting
dummy = '{} {} {}'.format('John', 'Is a Python', 'Developer')
print('Printing the default order: ')
print(dummy)

dummy1 = '{0} {2} {1}'.format('John', 'Python', 'Developer')      # Postitional formatting
print('Printing string in positional order: ')
print(dummy1)

dummy2 = '{a} {0} {b}'.format('John', a = 'is a', b = 'developer')      # Keyword formatting
print('Printing string in order in keywords: ')
print(dummy2)

dummy3 = '{0:b}'.format(16)   # formatting of integers
print('\nBinary representation of 16 is: ')
print('dummy3:', dummy3)

dummy4 = '{0:e}'.format(165.5458)   # formatting of floats
print('\nExponent representation of 165.5458: ')
print(dummy4)

dummy5 = '{0:2f}'.format(1/6)       # rounding off integers
print('\none-sixth is: ')
print(dummy5)

# String alignments with formatting:
dummy6 = '|{:<10}|{:^10}|{:>10}|'.format('Greeks',
                                       'For',
                                       'World')
print('\nLeft, center and right alignment with formatting: ')
print(dummy6)








































































































































































