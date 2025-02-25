"""
Inheritance
One class can inherit functionality of other class.
bunch of related class in a programe Manager class
Employee class, Owner class, person class all classes
related to each other
No duplicate code, easier to debug, easier to modify

PloyMorphisum: its orginate from biology the terms poly means
many and morphisum means form. The context of objects oriented
programing we can treat obejcts as differnetly based on context
we are using it.
single obejcts have multiple characteristic and exibit different
behaviours how treating in our programe.

if you are a manager you are also employee
if employee you are also a person

all employee as normal People

"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f" hi my name is {self.first_name} {self.last_name}")


# really bad no need to rewrite the code
# specially of Employee is a person
# use inheritance
"""
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f" hi my name is {self.first_name} {self.last_name}")

    def test(self):
        print("test")
"""


# Person is a Super class
# child class or drived class
# one directional relationship
class Employee(Person):
    def test(self):
        print("test")


e = Employee("Time", "Programer")
# every thing inside person you can use
# in Employee class
e.say_hello()
x = Person("Time", "Programer")
x.say_hello()
# AttributeError: 'Person' object has no attribute 'test'
# x.test()
e.test()


# Override methods on super class or base class
# sometimes stuff in super class we want to change they works
# overide methods in child class or drived class
class Employee1(Person):
    # overriden the parent function
    def say_hello(self):
        print("-----")
        # use parent functions
        # super give acess to parent class
        super().say_hello()
        print("-------")


e = Employee1("Time", "Programer")
e.say_hello()


# how to override the constructors
class Employee2(Person):
    def __init__(self, first_name, last_name, salary):
        # no self is here region this super
        # implicitly pass self for me
        # when you override construtors of super class
        # manualy call the constructors
        super().__init__(first_name, last_name)
        # my own attributes
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"my salary is {self.salary}")


class Manager(Employee2):
    # any instance of manger is Employee and Person
    # if instnace hiearcies like these than polymorphisum
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department


class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth


m = Manager("tim", "abc", 2000, "Sports")
m.say_hello()

o = Owner("tim", "abc", 2000)
o.say_hello()
# what type of each of one instances are
# intresting question
print(type(o))
# <class '__main__.Owner'>
print(isinstance(o, Person))
# True
# owner is a person


class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    # which one is parents class
    # both A and B are parents of c
    pass


c = C()


# op - A
# what going to print
# which one is true super class
# which one is defined 1st is a Super class - A
# A, B look in the inorder form A has init yes it does use this done
# if A dont have methods look to B, which one is Encounters First will done
class C(A, B):
    def __init__(self):
        super().__init__()
        # super reference to A
        # if A doesnot have methods we are looking at
        # Reference B


# This is called MRO (method resoulation order of inheritance in clases)
# main, ist super ifnot, 2nd super etc -> MRO

# Duck Typing - PolyMorphisum


class Duck:
    def swim(self):
        print("Swiming duck")

    def fly(self):
        print("Flying duck")


class Whale:
    def swim(self):
        print("Swiming duck")


animals = [Duck(), Duck(), Whale()]
for animal in animals:
    animal.swim()
    animal.fly()
    # crash on whale as no swim methods
    # python does not told before runing that its incorrect
    # Lot of programing during compilation it Fails
    # Look type how they use obj have no methods defined
    # python doesnot care I am going to try anyway
    # python when you try to use methods and attributes
    # of an obejcts it doesnot exit, it does tries
    # python tried it
