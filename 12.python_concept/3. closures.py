"""
closures have to do with nested fucntions
"""


def foo(x):
    print(x)


# functiosn are obejcts and there type are funtions
print(type(foo))


# <class 'function'> - so we can pass
# another fun which return functions
def call_func(func, x):
    func(x)


call_func(foo, 5)
# call function with foo(5)


# nested functions
def outer(x):
    # inner is local to outer function scope
    def inner(y):
        print(x + y)

    return inner


func = outer(5)
# <function outer.<locals>.inner at 0x102f75760>
# inner function is local to outer functions
print(func)
func(6)
func(3)
func2 = outer(1)
func2(1)
# even func2, func1 are differnt even they works as same functiosn
# value are differnt

"""
may be i don't want to return inner
i will call to inner
"""


def outer(x):
    # inner is local to outer function scope
    def inner(y):
        print(x + y)

    inner(5)


outer(5)


# you can define even more nested functions
# nested functions
def outer(x):
    # inner is local to outer function scope
    def inner(y):
        def inner2(z):
            print(x + y + z)

        return inner2

    return inner


outer(5)(5)(5)


# lets talk about closures
def outer(x):
    def inner():
        print(x)

    return inner


func = outer(5)
# this inner function is know as closure
# beacuse it acess the free varaibles from enclosing functions
# free varaibles is any variables which is nonlocals to scope of the
# inner functions
# what exceesing value x in inner we endup excuting it until
# execution of outer functions is done
# in python we called this outer functions than define inner functions
# and return inner execution of outer function is done as soon as
# functions return from it is still accesing we paaed to it.
# this is kind of called as closure
"""
outer function has closed we still have acess to vakue
that have inside of it still using x

uses free variable from outer functions why called closure
beause execution of outer function is closed done finsig it
now still using values passed to outer functions inside of
closure closure functions that refer too.

"""
func()  # 5


# more advanced example of closure
def collection(x):
    # mutable objects, nodify inside inner also no need to
    # redefine
    lst = []

    # closure as excesing free variables
    def inner(value):
        lst.append(value)
        return lst

    return inner


add_value = collection(1)
# same list as excessing part of closure
# this is kind of benifits of closure kind of
# mimic class here methods using closure
print(add_value(1))
print(add_value(2))
print(add_value(3))
print(add_value(4))


# equivalnets class which achieve
# this behaviour
class Collection:
    def __init__(self):
        self.lst = []

    def add_value(self, value):
        self.lst.append(value)
        return self.lst


# lets check on imutable data
def counter(start):
    count = start
    # stored in immutable data type inside count variables
    # immutable we cannot directly change them
    # create new immutable data type and assigned that
    # count variables

    def increment(value):
        # UnboundLocalError: cannot access local
        # variable 'count' where it is not associated with a value
        count += value
        # local to this function count
        # new count variables
        # inside functons we dont haves acess to above count variables
        # of outer functions
        # we can acess it but cannot chnaged it !.e cannot reassingn to
        # it way to fix it in python using nonlocals
        return count

    return increment


count = counter(2)
print(count(1))
# UnboundLocalError: cannot access local
# variable 'count' where it is not associated with a value


def counter(start):
    count = start

    def increment(value):
        # fix
        nonlocal count
        # make count variables to nonlocal
        # to inner functions
        # referncing count variables to enclosing nonlocal var
        count += value
        # it way to fix it in python using nonlocals
        return count

    return increment


count = counter(2)
print(count(1))
print(count(1))
print(count(1))

"""
The things with nonlocals
you can use it as nested functions
class for this is following
"""


class Counter:
    def __init__(self, start):
        self.count = start

    def count(self, value):
        self.count += value
        return self.count


# we can replace above class using above closure
# that is the idea

"""
example

"""


def outer():
    def inner():
        def inner2():
            nonlocal x
            # non local x going to refernce the closed variable
            # 2 that talk about closest in and out var
            x = 2
            print("Inner2 x:", x)

        x = 3
        inner2()
        print("Inner x:", x)

    x = 4
    inner()
    print("Outer:", x)


"""
which x is going to modified

"""

outer()
