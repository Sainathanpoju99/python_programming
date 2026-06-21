# creating a tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(type(mytuple))

mytuple1 = (11, 22, 33, 44, 55)
mytuple2 = (1, "hello", 3.14, True)
print(mytuple1, mytuple2)
print(mytuple2[2])
print(mytuple1[-2])
print(mytuple1[-2: -1])

mytuple3 = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'apple', 'mango')
print(mytuple3.count('apple'))
print(mytuple3.index('cherry'))
print(len(mytuple3))

## range of indexes
print(mytuple3[2:5])
print(mytuple3[:4])
print(mytuple3[3:])
print(mytuple3[-4:-1])

#change the value in the tuple
# mytuple3[1] = 'blackcurrant'  # 'tuple' object does not support item assignment
# convert the tuple values into list and change the value

'''mytuple3[1] = 'blackcurrant'  # 'tuple' object does not support item assignment
print(mytuple3)'''

templist = list(mytuple3)
print('list converted from tuple: ', templist)
templist[2] = 'blackcurrant' 
print('after changing the value in the tuple: ', templist)
print(type(templist))

# convert it into tuple
mytuple3 = tuple(templist)
print(mytuple3)
print(type(mytuple3))


# retrive the data from the tuple using for loop
mytpl = ('apple', 'banana', 'cherry')

for i in mytpl:
     print(i)

if 'banana' in mytpl:
     print('exists in the tuple')
else:
     print('no more items in the tuple')

# adding and removing the values to the tuple
#mytp1[3] = 'orange'
#print(mytp1)
#print(mytpl.remove('banana'))  # 'tuple' object has no attribute 'remove'
   

# joining two tuples
mytp = ('a', 'b', 'c')
mytp1 = (1, 2, 3)
mytp2 = mytp + mytp1
print('joined tuple: ', mytp2)
print(type(mytp2))





























