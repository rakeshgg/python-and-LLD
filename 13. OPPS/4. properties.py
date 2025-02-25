"""
special attribute
problem occured with traditional attributes
and how property can fix it.

"""


class Person:
    # make claases name menigful
    # how, every single instances need to be one of whaterver your class
    # name is
    def __init__(self, name):
        self.name = name
        self.salary = 0


p = Person("Tim")
# i can do this but issue is
# i don't have negative salary
# my salary canot be -ve value
# so no way to enforce this outisde class
p.salary = -100
"""
one way to fix this is make salary as provate attribute
self._salary = 0
private attribute can only be modified only
from inside class not accesible anything out
side of class.
attribute is public here

in oops a private attribute is attribute
which can be modified and exceesd inside
a class

oposite of provate is public attribuite
like name, In python no notion of real
private attribute
only convetion is python
so make setter not to modify

"""


class Person1:
    # make claases name menigful
    # how, every single instances need to be one of whaterver your class
    # name is
    def __init__(self, name):
        self.name = name
        self._salary = 0

    # defining setter
    def set_salary(self, salary):
        # private by convetion
        if salary < 0:
            raise ValueError("This is Invalid")
        self._salary = salary


p = Person1("Tim")
p.set_salary(100)
# still change the salary
# p.salary = -100
# so properties comes in pictures


class Person2:
    # make claases name menigful
    # how, every single instances need to be one of whaterver your class
    # name is
    def __init__(self, name):
        self.name = name
        self._salary = 0

    # defining setter
    def set_salary(self, salary):
        # private by convetion
        if salary < 0:
            raise ValueError("This is Invalid")
        self._salary = salary

    def get_salary(self):
        return round(self._salary)

    # to make property
    # put getter and setter
    salary = property(get_salary, set_salary)
    # avoid people directly modifying salary
    # without going to checks i have set-up
    # combine getter and setter together and
    # use when you performs p.salary = 100 operations


p = Person2("Tim")
p.salary = 100
# set_salary() methods is called with p, p.salary = 100
# wroking fine
# during getting salary get_salary called
print(p.salary)
# you can seilde people modifying
# outside of class


class Person3:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    # getter setting
    @property
    def salary(self):
        return round(self._salary)

    # this is the setter
    # @property.setter
    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("This is Invalid")
        self._salary = salary

    # setter and getter name should be same


class Time:
    def __init__(self):
        self._second = None

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError("Invalid!")
        self._second = second


t = Time()
t.second = 100
print(t.second)
