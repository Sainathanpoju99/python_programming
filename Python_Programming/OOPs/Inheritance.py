# SINGLE LEVEL INHERITANCE EXAMPLE
# Example 1
class person:
     def m1(self):
          print('This is m1 method of person class')
     
class student(person):
     def m2(self):
          print('This is m2 method of student class')
s = student()
s.m1()
s.m2()
print('-------------------')

# Example 2
class A:
     x, y = 10, 20
     def add(self):
          print('Addition of A class:', self.x + self.y)
class B(A):
     p, q = 100, 200
     def mul(self):
          print('Multiplication of B class:', self.p * self.q)
d = B()
d.add()
d.mul()
print('-------------------')

# MULTI-LEVEL INHERITANCE EXAMPLE
class A:
     x, y = 10, 20
     def add(self):
          print('Addition of A class:', self.x + self.y)
class B(A):
     p, q = 100, 200
     def mul(self):
          print('Multiplication of B class:', self.p * self.q)
class C(B):
     r, s = 1000, 2000
     def sub(self):
          print('Subtraction of C class:', self.s - self.r)
e = C()
e.add()
e.mul()
e.sub()
print('-------------------')

# Another example of Multi-Level Inheritance
class persons:                     # base class
     def __init__(self, name):     
          self.name = name
class employees(persons):          # employees inherits persons class
     def show_role(self):
          print(self.name, 'is an employee')
class manager(employees):          # manager inherits employees class
     def department(self, dept):
          print(self.name, "manages", dept, "department")
mng = manager('Alice')
mng.show_role()
mng.department('Sales')
print('-------------------')

# Another example of Multi-Level Inheritance with constructor
class Grandfather:
     def __init__(self, grandfather_name):
          self.grandfather_name = grandfather_name

class Father(Grandfather):
     def __init__(self, father_name, grandfather_name):
          super().__init__(grandfather_name)
          self.father_name = father_name

class Son(Father):
     def __init__(self, son_name, father_name, grandfather_name):
          self.son_name = son_name
          super().__init__(father_name, grandfather_name)
     def print_name(self):
          print('Grandfather Name:', self.grandfather_name)
          print('Father Name:', self.father_name)
          print('Son Name:', self.son_name)

s = Son('Bob', 'Charlie', 'David')
print(s.grandfather_name)
print(s.father_name)
print(s.son_name)
s.print_name()
print('-------------------')


#HIERARCHICAL INHERITANCE EXAMPLE
# Example 1
class A:
     x, y = 10, 20
     def add(self):
          print('Addition of A class:', self.x + self.y)
class B(A):
     p, q = 100, 200
     def mul(self):
          print('Multiplication of B class:', self.p * self.q)
class C(A):
     r, s = 1000, 2000
     def sub(self):
          print('Subtraction of C class:', self.s - self.r)

saa = B()
saa.add()
saa.mul()

caa = C()
caa.add()
caa.sub()
print('-------------------')

# Example 2
class person:
     def __init__(self, name):
          self.name = name
class employee(person):
     def show_role(self):
          print(self.name, 'is an employee')
class Intern(person):
     def show_role(self):
          print(self.name, 'is an intern')

emp1 = employee('David')
emp1.show_role()

int1 = Intern('Eva')
int1.show_role()
print('-------------------')

# Example 3
class Parent:
     def func1(self):
          print('This is function 1 of Parent class')
class Child1(Parent):
     def func2(self):
          print('This is function 2 of Child1 class')
class Child2(Parent):
     def func3(self):
          print('This is function 3 of Child2 class')
c1 = Child1()
c1.func1()
c1.func2()

c2 = Child2()
c2.func1()
c2.func3()
print('-------------------')

# MULTIPLE INHERITANCE EXAMPLE
# Example 1
class A:
     x, y = 10, 20
     def add(self):
          print('Addition of A class:', self.x + self.y)
class B:
     p, q = 100, 200
     def mul(self):
          print('Multiplication of B class:', self.p * self.q)
class C(A, B):
     r, s = 1000, 2000
     def sub(self):
          print('Subtraction of C class:', self.s - self.r)

cb = C()
cb.add()
cb.mul()
cb.sub()
print('-------------------')

# Example 2
class person():
     def skills(self):
          print('Person can have multiple skills')
class employee():
     def role(self):
          print('Employee works in an organization')
class intern(person, employee):
     def duration(self):
          print('Internship duration is 6 months')

intn = intern()
intn.skills()
intn.role()
intn.duration()
print('-------------------')

# Example 3
class mother():
     mothername = ''
     def mother(self):
          print(self.mothername)
class father():
     fathername = ''
     def father(self):
          print(self.fathername)
class child(mother, father):
     def parents(self):
          print('Father name is: ', self.fathername)
          print('Mother name is: ', self.mothername)
chh = child()
chh.fathername = 'John'
chh.mothername = 'Rossy'
chh.parents()
print('-------------------')

#  HYBRID INHERITANCE EXAMPLE
# Example 1
class A:
     def funcA(self):
          print('This is function A from class A')
class B(A):
     def funcB(self):
          print('This is function B from class B')
class C(A):
     def funcC(self):
          print('This is function C from class C')
class D(B, C):
     def funcD(self):
          print('This is function D from class D')
d = D()
d.funcA()
d.funcB()
d.funcC()
d.funcD()
print('-------------------')

# Example 2
class person:
     def info(self):
          print('This is person class')
class employee(person):
     def emp_info(self):
          print('This is employee class')
class student(person):
     def stu_info(self):
          print('This is student class')
class working_student(employee, student):
     def work_stu_info(self):
          print('This is working student class')
ws = working_student()
ws.info()
ws.emp_info()
ws.stu_info()
ws.work_stu_info()
print('-------------------')

# Example 3
class Person:
     def __init__(self, name):
          self.name = name

class Employee(Person):
     def __init__(self, name):
          super().__init__(name)

     def role(self):
          print(self.name, 'is an employee')

class Project:
     def __init__(self, project_name):
          self.project_name = project_name

     def show_project(self):
          print('Project Name is:', self.project_name)

class TeamLead(Employee, Project):
     def __init__(self, name, project_name):
          Employee.__init__(self, name)
          Project.__init__(self, project_name)

     def show_details(self):
          print(self.name, 'is leading the project', self.project_name)


tl = TeamLead('Frank', 'AI Development')
tl.show_details()
tl.role()
tl.show_project()
print(person.mro())

print('-------------------')


# Method overriding in Inheritance
class A:
     def m1(self):
          print('This is m1 method of class A')
class B(A):
     def m1(self):
          print('This is m1 method of class B')
          super().m1()
b = B()
b.m1()
print('-------------------')

# Calling parent class variables using child class
class A:
     x, y = 10, 20

class B(A):
     p, q = 100, 200
     
     def display(self, d, f):
          print('Method parameter values:', d, f)      # local variables
          print('Accessing parent class variables:', self.x, self.y)
          print('Accessing child class variables:', self.p, self.q)
bobj = B()
bobj.display(500, 600)
print('-------------------')

# Overriding variables
class parent:
     name = 'scott'

class child(parent):
     name = 'john'
     def show(self):
          print('Child class name:', self.name)           # accessing child class variable
          print('Parent class name:', super().name)       # accessing parent class variable
cobj = child()
cobj.show()
print('-------------------')

# Overriding methods
class Bank:
     def rate_of_interest(self):
          return 0
class SBI(Bank):
     def rate_of_interest(self):
          return 7.5
class ICICI(Bank):
     def rate_of_interest(self):
          return 8.0
     
sbi = SBI()
icici = ICICI()
print('SBI Rate of Interest:', sbi.rate_of_interest())
print('ICICI Rate of Interest:', icici.rate_of_interest())


# 






























