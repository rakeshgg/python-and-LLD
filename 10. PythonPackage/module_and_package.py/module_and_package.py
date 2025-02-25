"""
There is something main module in python
print(__name__) - way to check main module, you
got __main__ this run python files
region is you can import python files from module like this



"""

# import function modules
# same directory where module you are aceesing from
import functions

# import all codes from inside functions module
# rename module as differnts
import functions as f

# all the import goes to top of your programe
# considerd best practise
# import specific things from functions
# from functions import foo, bar, Test

# import everything from modules
# from functions import *
# this is dangerous to use only use if accesing everything from modules


print(__name__)
print("run")
functions.foo()
functions.bar()
t = functions.Test()
print(t)
f.foo()
# foo()
# bar()

# circular Imports
# import in both files functions, module_and_packages
# when you import it actually run codes in a module one time
# so avoid circular imports
# one main module can imports stuff from all
# other modules rather than importing
# here so its confusion
# __name__ == '__main__'
print(__name__)
"""
functions.py code not run as its name is not __main__

"""
if __name__ == "__main__":
    print("modules and packages")


# Packages Concepts
# import package
# import code

# import code.a (package_name.module name)
# when import runs one time to that file - print a
# import code.a
# import code  - print Init -- when import package init runs
# import code - print init, a, b
