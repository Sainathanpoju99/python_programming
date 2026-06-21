my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

mydict = {
     'name': 'Alice',
     'age': 30,
     'city': 'New York',
     'mobile': 1234567890
}

print(my_dict)
print(mydict)

# approach 2: using dict() constructor/function
mydict1 = dict(name='Bob', age=25, city='Los Angeles')
print(mydict1)

# using a key haveing multiple values
mydc = {
     'car1': ['BMW', 'Audi', 'Mercedes'],
     'car2': ('Toyota', 'Honda', 'Ford'),
     'car3': {'Nissan', 'Mazda', 'Subaru'},
     'year': 2026
     }
print(mydc)
print('-------------------')
# accessing dictionary values
# using key
print(mydc['car1'])
print(mydc['year'])

# using get() method
print(mydc.get('car2'))
print(mydc.get('car3'))
print('-------------------')

# using keys() method - will return only keys in the dictionary
print('get keys: ', mydc.keys())

# using values() method - will return only values in the dictionary
print('get values: ', mydc.values())

# using items() method - will return key-value pairs as tuples in a list
print('get items: ', mydc.items())
print('-------------------')

# updating/adding dictionary values
mydc['year'] = 2027
print('updated year: ', mydc['year'])
mydc.update({'year': 2028})
print('updated year using update(): ', mydc['year'])
mydc.update({'car3' : {'kia', 'polo', 'cerato'}})
print('updated car3 using update(): ', mydc)
mydc['car2'] = {'Tesla', 'Rivian', 'Lucid'}
print('updated car2: ', mydc)
mydc['car4'] = {'Jaguar', 'Land Rover', 'Range Rover', 'Defender', 'Discovery'}
print(['after adding car4: ', mydc])
mydc['model'] = 2024
mydc.update({'color' : 'Red'})
print('after adding model and color: ', mydc)

print('-------------------')

# check if key exists in dictionary ( search key)
if 'car3' in mydc:
     print('Exisits')
else:
     print('Not exists')
print('-------------------')  

# removing items from dictionary
# using pop() method: - removes item with specified key
rev_mydc = mydc.pop('car1')
print('after removing car1 using pop(): ', mydc)
print('removed value: ', rev_mydc)
print('-------------------')

# using popitem() method - removes last inserted item (in python 3.7+)
rev_mydc1 = mydc.popitem()
print('after removing last item using popitem(): ', mydc)
print('removed item: ', rev_mydc1)
print('-------------------')

# using del keyword - removes item with specified key
del mydc['car2']
print('after removing car2 using del: ', mydc)

'''del mydict1 # deletes the entire dictionary variable
print('after deleting mydict1: ', mydict1)  # This will raise an error as mydict1 is deleted
'''

# using clear() method - removes all items from the dictionary but keeps the dictionary variable
mydccc = dict(name='Charlie', age=28, city='Chicago')
mydccc.clear()
print('after clearing mydccc using clear(): ', mydccc)
print('-------------------')

# copying a dictionary
# using copy() method
dimDT = {'A': 1, 'B': 2, 'C': 3}
mydc_copy = dimDT.copy()
print('copied dictionary using copy(): ', mydc_copy)
# using dict() constructor
mydc_copy1 = dict(mydc_copy)
print('after copying using dict(): ', mydc_copy)
print('-------------------')

# nested dictionary
nested_dict = {
     'person1': {'name': 'David', 'age': 35, 'city': 'Miami'},
     'person2': {'name': 'Eva', 'age': 29, 'city': 'Seattle'},
     'person3': {'name': 'Frank', 'age': 40, 'city': 'Boston'}
}    
print('nested dictionary: ', nested_dict)
# accessing nested dictionary values
print('person2 name: ', nested_dict['person2']['name'])
print('person3 city: ', nested_dict.get('person3').get('city'))
print('-------------------')

# using length of dictionary
print('lenght of nested_dict:', len(nested_dict))

# looping with dictionary
for x in nested_dict:
     print(x)  # prints keys

for x in nested_dict.keys():
     print(x)  # prints keys

for x1 in nested_dict['person2']:
     print('gets the person2 values: ', x1)  # prints keys of person2

for x1 in nested_dict.values():
     print(x1)  # prints values

for x1 in nested_dict:
     print('prints all the values of all keys', nested_dict[x1])  # prints values

for x1, y1 in nested_dict.items():
     print('prints key and values: ', x1, y1)  # prints key and values
print('-------------------')

# using dictionary comprehension : to create a dictionary in a single line of code 
squared_dict = {x: x**2 for x in range(6)}
print('squared dictionary using comprehension: ', squared_dict)
print('-------------------')









































