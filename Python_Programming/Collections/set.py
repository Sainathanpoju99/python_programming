set1 = {10, 20 , 30, 40, 50}
set2= {'a', 'b', 'c', 'd'}
set3 = {'apple', 10, 20.5, True}
set4 = set()  # empty set
set5 = {1, 2, 3, 4, 5, 1, 2, 3}  # duplicate values will be ignored
set6 = {'apple', 'banana', 'cherry'}
print('set1: ', set1)
print('set2: ', set2)
print('set3: ', set3)
print('set4: ', set4)
print('set5 (duplicate values ignored): ', set5)
print('set6: ', set6)    

print('------------------------------------')         
# accessing set items
# sets are unordered, so we cannot access items using indexing
# we cannot even change the items in the set as sets are unchangeable, but we can add new items (because set does not support indexing)

# accessing using for loop

myset = {'apple', 'banana', 'cherry'}
for items in myset:
     print('set items: ', items)

# check if the values exist in the set using IN and NOT IN
print('banana' in myset)   # True
print('orange' in myset)   # False

if 'orange' in myset:
     print('orange is present in the set')
else:
     print('orange is not present in the set')

# find length of the set/number of items in the set
print('length of the set: ', len(myset))

# count() method is not available for set 
# Not possible to count occurrences as set do not allow duplicate values
'''print('count of items in the set: ', myset.count('cherry')) 
# AttributeError: 'set' object has no attribute 'count' '''

#sorting a set
# sets are unordered, so we cannot sort them in place
# but we can use the sorted() method to return a sorted list of the set items and the output will be a list
myset1= {3, 1, 4, 2, 5}
sorted_set = sorted(myset1)
print('sorted set: ', sorted_set)

#reverse the set items
# sets are unordered, so we cannot reverse them in place
# but we can use the sorted() method with reverse=True to return a sorted list of the set items in reverse order
reversed_set = sorted(myset1, reverse=True)
print('reversed set: ', reversed_set)
print('------------------------------------')

# Adding items to a set
myset3 = {'apple', 'banana', 'cherry'}
myset3.add('orange')  # add() method to add a single item
print('set after adding orange: ', myset3)
myset3.update(['mango', 'grape'])  # update() method to add multiple items
print('set after adding mango and grape: ', myset3)

print('-------------------------------------')

# Removing items from a set
# approach 1: using remove() method
myset4 = {'apple', 'banana', 'cherry', 'orange'}
myset4.remove('orange')
print('set after removing orange: ', myset4)

# approach 2: using discard() method - does not raise error if item not found
myset4.discard('banana')
print('set after discarding banana: ', myset4)
myset4.discard('kiwi')  # no error if item not found
print('set after discarding kiwi (not found): ', myset4)

# approach 3: using pop() method - randomly removes an item
myset5 = {'apple', 'banana', 'cherry'}
popped_items = myset5.pop() # removes and returns an arbitrary item
print('popped item: ', popped_items)
print('set after popping an item: ', myset5)

print('-----------------------------')

# deleting the entire set
myset6 = {'apple', 'banana', 'cherry'}
del myset6
#print(myset6)  # This will raise an error as the set is deleted

print('-----------------------------')

# copying a set
# copy() method
original_set = {'apple', 'banana', 'cherry'}
copied_set = original_set.copy()
print('original set: ', original_set)
print('copied set: ', copied_set)

# using set() constructor
another_copied_set = set(original_set)
print('another copied set using set() constructor: ', another_copied_set)
print('-----------------------------')

# joining two sets
# approach 1: using union() method
setA = {1, 2, 3}
setB = {4, 5, 6}
setC = setA.union(setB)
print('set after union using union() method: ', setC)

# approach 2: using | operator - pipe operator
setD = setA | setB
print('set after union using | operator: ', setD)

# approach 3: using update() method - adds items from one set to another
setE = {1, 2, 3}
setE.update({4, 5, 6})
print('set after updating setE with setB: ', setE)

print('-----------------------------')

# retrieving common items between two sets
# approach 1: using intersection() method
setX = {1, 2, 3, 4, 5}
setY = {4, 5, 6, 7, 8}
setZ = setX.intersection(setY)
print('common items using intersection() method: ', setZ)

# approach 2: using & operator
setW = setX & setY
print('common items using & operator: ', setW)
































