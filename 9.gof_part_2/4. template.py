import sys
from abc import ABC, abstractmethod


# template
class AbstractClass(ABC):
    # this class inherit from abstarct base class
    # to allow the use of @abstractmethod decorator
    def template_method(self):
        """
        This is the template methods that contains a collection
        of method to stay the same, to be overriden, and to be
        overriden optionally
        """
        # call default
        # not overriden
        self.__always_do_this()
        # can be overriden based on your need
        self.do_step_1()
        self.do_step_2()

    def __always_do_this(self):
        # This is protected methods that should not be overriden
        name = sys._getframe().f_code.co_name
        print("{}.{}".format(self.__class__.__name__, name))

    @abstractmethod
    def do_step_1(self):
        # this method is overridden
        pass

    @abstractmethod
    def do_step_2(self):
        # this method is overridden
        pass

    def do_this_or(self):
        print("You can overide me but you do not have to")


class ConcreteClassA(AbstractClass):
    # this class inherit from the abstarct class featuring the
    # template method
    def do_step_1(self):
        print("doing step1 for concrete class A......")

    def do_step_2(self):
        print("doing step2 for concrete class A........")


class ConcreteClassB(AbstractClass):
    # this class inherit from the abstract class
    # featuring the template method.
    def do_step_1(self):
        print("doing step1 for concrete class B......")

    def do_step_2(self):
        print("doing step2 for concrete class B........")

    def do_this_or(self):
        print("doing my own businesss")


# instatiate concrete classes
a = ConcreteClassA()
a.template_method()
# concrete class B
b = ConcreteClassB()
b.template_method()

"""
ConcreteClassA.__always_do_this
doing step1 for concrete class A......
doing step2 for concrete class A........
ConcreteClassB.__always_do_this
doing step1 for concrete class B......
doing step2 for concrete class B........

"""
