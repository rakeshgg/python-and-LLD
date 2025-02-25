# This init.py files run every times import the packages
# so when you import packages one time init.py runs.
# Initialize the packages inside it
print("Init")
# what we can do inside is import the module
# directly to the packages
import code.a
import code.b

# import .a is a relative import
# packagename.a, a and b belongs to code package
# when run this File
# ModuleNotFoundError: No module named 'code.a'; 'code' is not a package - why in this file not works
# Region is module_and_package is main modules i serch packages staring from this
# main modules so when go to init.py i am not usually using this code packages
# because i am inside init.py
# if import from main_module its work as now package can exist in python
# execution environments than init.py runs and code exist
# from code.a import A
# package_ name.module import is absolute import
# relative import
