"""
"""

import types

# Import the types module
# types module support the dynamic createion of new types


class Strategy:
    """The strategy pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"
        # if the reference to the function is provided as arg,
        # replace the default execute
        # methods with given functions
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        # this get replaced by another version
        """default method that prints the name of Strategy being"""
        print("{} is used the!".format(self.name))


# Replacemnts method 1
def strategy_one(self):
    print("{} is used to execute the methods 1".format(self.name))


# Replacemnts method 2
def strategy_two(self):
    print("{} is used to execute the methods 2".format(self.name))


# let's create our default strategy
s0 = Strategy()
# let's execute our default strategy
s0.execute()
# Let's create our first variation of our default strategy
# by providing
s1 = Strategy(strategy_one)
# let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
# let's set its name
s2.name = "Strategy Two"
# Let's execute the strategy
s2.execute()
