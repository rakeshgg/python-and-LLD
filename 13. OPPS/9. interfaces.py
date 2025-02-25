"""
Interface like abstract class except it only contains abstarct methods
Interface constinas no Implementaion details whatever no code other than
the defination of methods and it will raise not the Implemented error
Inside of any of those single methods. so point of interface is to
discribe out of the methods anything that inherit the interfaces

Interfcaes are useful in java - typed language
in Python its not a thing
so you make how to make interface in python
it's truely not interface its type of initialized class

Other prgraming language you can make interfcae. in python faking
interfcaes not truely interfcae

"""


class RunCodeInterface:
    # most implemnts this methods
    # abstarct class
    # Interface have no logic inside it
    # whole point is to define types in other language
    # not really use in python
    def compile_code(self):
        raise NotImplementedError("you must implemnt compile_code()")

    def execute_code(self):
        raise NotImplementedError("you must implemnt execute_code()")


class GoCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Go code")

    def execute_code(self):
        print("Execute Go code")


class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Jave code")

    def execute_code(self):
        print("Execute Go code")


def run_code(code: RunCodeInterface):
    """
    In Python the type of obejcts matter
    but we try to run this methods if they
    don't run the methods, python is waek typed
    langugae. in stronlgly typed language
    you actually need to define type of parameters

    """
    code.compile_code()
    code.execute_code()


go = GoCode()
run_code(go)
