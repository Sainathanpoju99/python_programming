import Ani_Module, Brd_Module

Ani_Module.fly()
Ani_Module.color()

Brd_Module.fly()
Brd_Module.color()


# Approach 2
# whichever we import first it will call the recent module related functions
from Brd_Module import *
Brd_Module.fly()
Brd_Module.color()

from Ani_Module import *
Ani_Module.fly()
Ani_Module.color()





