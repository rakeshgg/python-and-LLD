def foo():
    print("Foo")


def bar():
    print("Bar")


class Test:
    pass


print(__name__)
# if name of module is __main__
# than we run the modules
if __name__ == "__main__":
    print("hello word")
# but if we import the modules its name is not __main__
# its name is name of module
