"""
class contains blu-print how instances behaves

"""


# convernton of class pascal case
# BigCar,
class Person:
    pass


# new data type of person
p1 = Person()
print(p1)
# <__main__.Person object at 0x10448ef10>
# __main__ denotes this class defined to main file
print(type(p1))
# <class '__main__.Person'> # type Person


# creating instances have some information
# associated with
# Initializing class and class construtors
class Person:
    def __init__(self, x):
        print(x)
        self.x = x
        # this is attribute


p1 = Person(1)
p2 = Person(2)


class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


a = Fruit("Apple", 100)
a.color = "Red"
"""
Purpose of classes, how to create a good class
class is to store common behaviour between instances
Int, String, These are all unique act as same behaviour
string - len, methods

they encaptulates all behaviour through instances in one place
when you want specific type of behaviours you create objects of
specific class you have excessed all differnet type of behaviours

"""
