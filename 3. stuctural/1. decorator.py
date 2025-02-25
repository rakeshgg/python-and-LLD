from functools import wraps


def make_blink(function):
    """Define the Deocrator"""

    # this make the decorator transaparent in iterms of its name
    # and docstring
    @wraps(function)
    # define the inner function
    def decorator():
        # grab the return value of functions to be decorated
        ret = function()
        # process the return value
        # add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# Apply the decorator here
@make_blink
def hello_word():
    """original function!"""
    return "Hello word!"


print(hello_word())

# check the result of decorating
# name of functions
print(hello_word.__name__)
# print doc string
print(hello_word.__doc__)
# check the function name is still same as the function being called
# check the docstring is same as that of function being called
"""
we can add decorator pattern to add additional features transaparently
to an existing functions very easily in python
"""
