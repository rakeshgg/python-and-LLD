"""
Method is a functions that acts on instances
of class This methods are special unlike functions
they can excess the attribute associated with it.

"""


class Person:
    # special methods
    def __init__(self, name):
        self.name = name
        self.age = None
        # good default value is None
        self.weight = 0

    # self as first parmters
    # as isntances
    def say_hello(self):
        print(f" hello, {self.name}")

    # setter setting value to age
    def add_age(self, age):
        self.age = age

    # getter methods is getting the values
    def get_age(self):
        return self.age


p1 = Person("Tim")
# p1.__init__("TIM")
p1.say_hello()
p1.add_age(24)
p1.get_age()


class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        # swap the bool value
        self.locked = not self.locked
        """
        if self.locked == True:
            self.locked = False
        else:
            self.locked = True
        """

    def increment(self):
        if self.locked:
            raise Exception("The counter is Locked!")
        self.count += 1

    def decremnet(self):
        if self.locked:
            raise Exception("The counter is Locked!")
        self.count -= 1

    def print_count(self):
        print(f"The current cout is {self.count}")


counter = Counter()
counter.increment()
counter.decremnet()
counter.print_count()
counter.increment()
counter.print_count()
counter.toggle_lock()
counter.increment()
"""
modiying attributes at instance level - self

"""
