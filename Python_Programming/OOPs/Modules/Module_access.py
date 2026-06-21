# Approach 1:
import Operations_func

Operations_func.add(10, 20)
Operations_func.mul(40, 20)

print('Age is: ', Operations_func.person['age'])


#Aprroach 2
from Operations_func import mul
mul(33, 44)

from Operations_func import add, mul, person

add(11, 22)
mul(53, 45)
print(person['country'])

# Approach 3 
# we can access everything from the module if * is used.
from Operations_func import * 
add(11, 22)
mul(53, 45)
print(person['name'])



















