# Creating a class along with object instantiation
class MyClass:
     def myfunc(self):
          pass
     def display(self, name):
          print(name)

# Creating object of the class
obj = MyClass()
obj.myfunc()
obj.display('Hello, This is my first OOPs program in Python!')

obj1 = MyClass()
obj1.myfunc()
obj1.display('Hello from obj1!')
print('-------------------')

# Instance method and static method example
class MyClassInstanceStatic:
     def instance_method(self):
          print('this is an instance method')
     
     @staticmethod
     def static_method(self, number):
          print('this is a static method')
          print(self, 'number is:', number)

instObj = MyClassInstanceStatic()
instObj.instance_method()     # calling instance method
instObj.static_method('Self is considered as parameter: 22' , 42)  # calling static method#
instObj.static_method(250, 100)

# MyClassInstanceStatic.instance_method()  # calling instance method using class name by passing the object
MyClassInstanceStatic.static_method(22, 88) # calling static method using class name


# Define the variables inside the class (class variables) and inside the methods (instance variables)
class MyClassVariables:
     a , b = 10, 20  # class variables
     def add(self):
          print(self.a + self.b)

     def mul(self):
          print(self.a * self.b)
calObj = MyClassVariables()
calObj.add()
calObj.mul()
print('-------------------')

# Local variables, Global variables, and Class variables
e, f, g = 5, 10, 15  # global variables
class MyClassVar:
     x, y = 100, 200 # class variables
     def sample_method(self, g, w):
          print('Prints local varilable: ', g + w)   # g is local variable, w is local variable
          print('Prints class variables: ', self.x + self.y) # accessing class variables
          print('Prints globals variable: ', e + f + g)  # accessing global variables
varObj = MyClassVar()
varObj.sample_method(50, 60)
print('-------------------')

# Local variables, Global variables, and Class variables [Names of variables are same]
x, y = 10, 20  # global variables
class MyClassVar:
     x, y = 100, 200 # class variables
     def sample_method(self, x, y):
          print('Prints local varilable: ', x + y)   # g is local variable, w is local variable
          print('Prints class variables: ', self.x + self.y) # accessing class variables
          print('Prints globals variable: ', globals()['x'] + globals()['y'])  # accessing global variables
varObj = MyClassVar()
varObj.sample_method(50, 60)
print('-------------------')

# Class with constructor
class MyclassConstructor:
     def __init__(self):
          print('This is constructor!!!!!!')
     def display(self):
          print('This is display method')
     def show(self, w, e):
          return w + e
objCons = MyclassConstructor()  # constructor is called automatically
objCons.display()
result = objCons.show(10, 20)
print('Sum from show method: ', result)
print('-------------------')         

# Constructor with parameters and class variables
class MyclassConstructorParam:
     name = 'fibernet'   # class variable
     def __init__(self, name):
          print(name) # accessing constructor parameter
          print(self.name)  # accessing class variable using self
objConsParam = MyclassConstructorParam('ACT') # passing argument to constructor
print('-------------------')


# Class with constructor and method
class emp:
     def __init__(self, ename, eage, esalary):
          self.name = ename
          self.age = eage
          self.salary = esalary
     def display(self):
          print('Employee Name: ', self.name)
          print('Employee Age: ', self.age)
          print('Employee Salary: ', self.salary)
emp1 = emp('John Doe', 30, 60000)
emp2 = emp('Jane Smith', 28, 65000)
emp1.display()
emp2.display()
print('-------------------')

# class with dectructor
class MyClassDestructor:
     def __init__(self):
          print('Constructor called')
     def __del__(self):
          print('Destructor called, object is being deleted')
objDel = MyClassDestructor()
del objDel  # explicitly deleting the constructor object to call destructor
print('-------------------')




# Example of __str__ method and object representation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)
print('---------------------')

# Getter and setter methods example
class Employee:
     
     def __init__(self, first, last):
          self.first = first
          self.last = last
          
     @property
     def email(self):
          return '{}.{}@email.com'.format(self.first, self.last)

     @property
     def fullname(self):
          return '{} {}'.format(self.first, self.last)

     @fullname.setter
     def fullname(self, name):
          first, last = name.split(' ')
          self.first = first
          self.last = last

     @fullname.deleter
     def fullname(self):
          print('Delete Name!')
          self.first = None
          self.last = None

emp1 = Employee('John', 'Doe')
emp1.fullname = 'Jane Smith'  # using setter to change the name

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname  # using deleter to delete the name

# Method Overriding example
class Parent:
     def show(self):
          print('This is parent class method')
class Child(Parent):
     def show(self):
          print('This is child class method')

Ogb = Child()
Ogb.show()  # calls the child class method
print('-------------------')


# Static Method and Class Method example
class MyClassStatic:
     @staticmethod  # static method
     def static_method():
          print('This is a static method')
     @classmethod
     def class_method(cls):
          print('This is a class method', cls) # accessing class using cls parameter

MCS = MyClassStatic()
MCS.static_method()
MCS.class_method()




