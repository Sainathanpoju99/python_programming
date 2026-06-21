# Approach 1:
import a
import b

aobj = a.Animal()
aobj.display()

bobj = b.Bird()
bobj.display()


# Approach 2
from a import Animal
from b import Bird

aaobj=Animal()
aaobj.display()

bbobj=Bird()
bbobj.display()


# Approach 3
from a import *
from b import *

aaobj=Animal()
aaobj.display()

bbobj=Bird()
bbobj.display()












