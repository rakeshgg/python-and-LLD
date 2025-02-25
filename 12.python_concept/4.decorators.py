import time

"""
Decorator are functions which is used to call another functions
@property
@staticmethod
@classmethod
take func as parameters and inforce some behaviour and call them

decorator uses in Nested functions.
decorator should work for any type of functions so using *args, **kwargs
"""


def decorator(func):
    def wrapper(x):
        print("warapper function called func!", x)
        result = func()
        return result

    return wrapper


# this foo got passes as functions
# in decorator than return wrapper and
# called wrapper functions arg passed to foo
# what ever arg here get passed to wrapper functions
# changing foo function actually to be wrapper
@decorator
def foo():
    print("foo")


foo(1)

"""
# retrun wrapper and that
# wrapper func called with arg passed by foo
def foo():
    print("foo")


# redefing foo
foo = decorator(foo)
# excatly waht @decorator syntax does
foo(1)
# above is same as @decorator
"""

"""
define in genric ways
This decorator can we used by any function with
any parameters
"""


def decorator1(func):
    def wrapper(*args, **kwargs):
        print("warapper function called func!")
        result = func(*args, **kwargs)
        # store result of function calls
        # and return it
        return result

    # allow to take any number of positional, kwargs
    return wrapper


@decorator1
def foo1(x, y, z=None):
    print(x, y, z)


foo1(2, 3)
foo1(2, 3, 4)

"""
timer decorator

"""


def timer(func):
    # you can write logic here also
    def wrapper(*args, **kwargs):
        current_time = time.time()
        # gives number of second occured
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - current_time
        print("time taken to execute:", total_time)
        return result

    return wrapper


@timer
def loop():
    # _ is known as anyonymous var
    for _ in range(100000):
        pass


loop()


@timer
def get_max(x, y, z):
    loop()
    return max(x, y, z)


print(get_max(1, 2, 3))

"""
use of multiple decorators

"""


def pretty_printer(func):
    def warapper(*args, **kwargs):
        print()
        result = func(*args, **kwargs)
        print()
        return result

    return warapper


@timer
@pretty_printer
def print_numbers(num):
    for i in range(num):
        # print(i)
        pass


print_numbers(5)

"""
Two decorator things become complicated
@timer
@pretty_printer - closest to function so it called first
def print_numbers(num):

print_numbers = pretty_printer(print_numbers)
print_numbers = timer(print_numbers)
print_numbers()

# in one line
print_numbers = timer(pretty_printer(print_numbers))

"""
