mylist1 = [1,2,3,4,5]
mylist2 = ['apple', 'banana', 'cherry']
mylist3 = [1, 'hello', 3.14, True]
print(type(mylist1))
print(mylist1)
print(mylist2)
print(mylist3)

# access items/values/objects from the list.
mylist4 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(mylist4[2])
print(mylist4[-1])
print(mylist4[0:3])
print(mylist4[1: 6])
print(mylist4[-7: -1])
print('------------------')

# change the value in the list
mylst = ['apple', 'banana', 'cherry']
print('before changing: ', mylst)
mylst[1] = 'blackcurrant'
print('changing the value in the list: ', mylst)
print('------------------')

#loop with list
for i in mylist4:
     print('for loop: ', i)

if 'melon' in mylist4:
    print('melon is present in the list')
else: 
     print('melon is not present in the list')

if 'jack' in mylist4:
    print('jack is present in the list')
else: 
     print('jack is not present in the list')
print('------------------')

# find the length of the list
print('length of the list: ', len(mylist4))
print('length of the list:, ', len(mylst))

# count of the occurrences of an element in the list
myldt = [1, 1, 1, 3, 3, 4, 5, 5, 5]
print('count of 5 in the list: ', myldt.count(5))

# sorting the list
numlist = [5, 2, 9, 1, 5, 6]
print('before sorting: ', numlist)
print('after sorted: ', sorted(numlist)) # ascending order
numlist.sort() # ascending order
print('after sorting using sort(): ', numlist)

print('after reverse sorting: ', sorted(numlist, reverse = True))
numlist.sort(reverse = True)
print('after sorting using sort() in descending order: ', numlist)
print('------------------')

# reversing the list items
mylist5 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print('original list: ', mylist5)
mylist5.reverse()
print('reversed list: ', mylist5)
print('------------------')
# adding items to the list
# using append() and insert()

mylist6 = ['apple', 'banana', 'cherry']
print('original list: ', mylist6)
mylist6.append('orange')
print('after appending: ', mylist6)
mylist6.insert(1, 'lemon')
print('after inserting: ', mylist6)

# remove items from the list
mylist7 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print('original list: ', mylist7)  
mylist7.remove('banana',)     # this accepts value to be removed
print('after removing banana: ', mylist7)

mylist7.pop(5) # accepts index to be removed
print('after popping index 5: ', mylist7)

del mylist7[1] #deletes the item at index 0
print('after deleting index 1: ', mylist7)

del mylist7  # deletes the entire list
#print(mylist7)  # raises an error as the list is deleted

# copying the list
listA = ['apple', 'banana', 'cherry']
listB = listA.copy()
print('listA: ', listA)
print('listB: ', listB)

listC = list(listA)
print('listC: ', listC)

# joining two lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print('joined list: ', list3)

list1.extend(list2)
print('after extending list1 with list2: ', list1)

for i in list2:
     listA.append(i)
print('after appending list2 items to listA: ', listA)

list1.extend(list2)
print('after extending list1 with list2: ', list1)
















