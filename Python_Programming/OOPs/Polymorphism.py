class human:
     def say_hello(self, name=None):    # method with default argument
          if name is not None:
               print('Hello ' + name)   # method with argument
          else:
               print("Hello")

h = human()
h.say_hello()          # calling method without argument
h.say_hello('Alice')   # calling method with argument
print('-------------------')

# example 2
class calculation:
     def add(self, a, b, c=0):   # method with default argument
          return a + b + c
calc = calculation()
print(calc.add(10, 20))
print(calc.add(10, 20, 30))

#  compile time polymorphism is not possible in Python as it is dynamically typed language
class calculator:
     def miltiply(self, a=1, b=2, *args):
          result = a*b
          for num in args:
               result *= num
          return result
     
calc = calculator()
print('default arguments:', calc.miltiply()) # uses default values 1 and 2
print('two arguments:', calc.miltiply(5, 4)) # uses 5 and 4
print('multiple arguments:', calc.miltiply(2, 3, 4, 5, 54, 88, 55)) # uses 2, 3, 4, and 5
print('-------------------')


# Mthod overriding (run time polymorphism)
class Animal:
     def sound(self):
          return 'Animal makes a sound'
class Dog(Animal):
     def sound(self):
          return 'Dog barks'
class Cat(Animal):
     def sound(self):
          return 'Cat meows'
                 
animals = [Animal(), Dog(), Cat()]
for animal in animals:
     print(animal.sound())   # calls the overridden method based on the object type
     
















