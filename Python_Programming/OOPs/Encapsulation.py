class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0
    #Getter method
    def get_marks(self):
        return self.__marks
    # Setter Method
    def set_marks(self, marks):
        if marks <= 100:
            self.__marks = marks
        else:
            print('Invalid marks. Marks must be <=100')

stu = Student('John')
stu.set_marks(90)
print(stu.get_marks())


# Example 1
class Employee:
    def __init__(self, name, salary):
        self.__salary = salary
        self.name = name
    def get_salary(self):
        return self.__salary

em = Employee('Frederick', 65000)
print(em.name)
print(em.get_salary())

# Public members
class Employee1:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(self.name)

empp = Employee1('Derick')
empp.display_name()
print(empp.name)


# Protected Members
class Employee2:
    def __init__(self, name, age):
        self.name = name    #public
        self._age = age     #protected

class SubEmpl(Employee2):
    def show_age(self):
        print('Age: ', self._age)

empa = SubEmpl('Derick', 30)
print(empa.name)
empa.show_age()


# Private members
class Employee3:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def show_salary(self):
        print('Salary: ', self.__salary)

emp11 = Employee3('John', 5402)
emp11.show_salary()
print(emp11.name)

# Declaring protected and private methods
class BankAccount:
    def __init__(self):
        self.balance = 1500
    def _show_balance(self):
        print(f'Balance: ${self.balance}')  #protected method
    def __update_balance(self, amount):
        self.balance += amount      #private method
    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print('Invalid deposit amount')
account = BankAccount()
account._show_balance()
account.deposit(5500)


# Getter and Setter methods
class Employee33:
    def __init__(self):
        self.__salary = 500000  #private method
    def get_salary(self):
        return self.__salary
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print('Invalid salary amount')

emp111 = Employee33()
print(emp111.get_salary()) ## Access salary using getter

emp111.set_salary(150000)
print(emp111.get_salary())  # Update salary using setter










