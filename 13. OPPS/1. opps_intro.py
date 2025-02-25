x = 1
# variable is storing the objects
# which is an integer that a value 1
# this is an objects.
y = "strings"
# this is also objects type of obejcts is string
z = [1, 2, 3]  # type list
# All data types we are creating new obejcts of instant of particular type.

print(type(x))
# <class 'int'>
# class defined behaviour of int data type
# x + y
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# both obejct are of differnt types
print(y.upper())
# print(x.upper())
# AttributeError: 'int' object has no attribute 'upper'

# Type of obejcts are very very importants


def fun():
    pass


print(type(fun))
# <class 'function'>
"""
Instances is an existence of an objects
of a specific class
x = 1
creating instances of int class with value 1
y = "hello"

A Method is kind of function when you call only instances
of a class
st = "string"
st.upper() -> function acting on istnaces of class
"""

# Anything has type that are classes
# blueprint defined behaviour of all the instances of
# that type
