''' Python Strings: Immutability is the property of an object according to which we can not 
change the object after we declared or after the creation of it 
and this Immutability in the case of the string is known as string immutability in Python.

Some other datatypes in Python are immutable such as strings, numbers (integers, floats, complex numbers), tuples, and frozensets.
Mutable objects are that we can modify according to our requirements and use according to our use. A few examples of them are List, Dictionary, and Set.

Benefits of Immutable Objects
Hashability and Dictionary Keys: Immutable objects can be used as keys in dictionaries because their hash value remains constant, ensuring that the key-value mapping is consistent.
Memory Efficiency: Since immutable objects cannot change their value, Python can optimize memory usage. Reusing the same immutable object across the program whenever possible reduces memory overhead.
Thread Safety: Immutability provides inherent thread safety. When multiple threads access the same immutable object, there’s no risk of data corruption due to concurrent modifications.
Predictability and Debugging: With immutability, you can be confident that a given object’s value will not change unexpectedly, leading to more predictable and easier-to-debug code.
Performance Optimization: Immutable objects facilitate certain performance optimizations, such as caching hash values for quick dictionary lookups.
'''

# Ways to Deal with Immutability
# String Slicing and Reassembling
# String Concatenation
# Using the join() method
# Using String Formatting
# Converting to Mutable Data Structures

# String Slicing and Reassembling
name = "Aradya"
name_1 = 'S' + name[1:]
print('Updated name after slicing and reassembling: ', name_1)

# String Concatenation
dame = 'Hey'
vam = dame + ', Learn!'
print('\nUpdated string after concat: ', vam)

# Using the join() method
jam = ['Helix', 'My Son Melix']
dam_join_string = ' '.join(jam)
print('\nUpdated name of after joining the string: ', dam_join_string)

# Using String Formatting
teLe = "Formatted"
new_format = 'Hello {}'.format(teLe)
print(new_format)

# Converting to Mutable Data Structures
my_string = 'Random, data value..'
convert_list = list(my_string)
convert_list[0] = 'No, r'
new_String = ''.join(convert_list)
print("\nPrints the updated srting with new changes: ", new_String)




















































