# Python code​​​​​​‌​‌‌​​‌​​‌​‌‌‌​​‌​​‌​‌​​​ below
# Use print("messages...") to debug your solution.
class InterceptingValidator:

    def __init__(self):
        # store ref to validator
        self._validator = None
        # embeded input
        self._input = "t"

    def set_validator(self, validator):
        # set validator objects
        self._validator = validator

    def validate(self):
        # invoke validate methods of validator
        return self._validator.validate(self._input)


class NumberValidator:
    """Checks if the input is a number or not"""

    def validate(self, input):
        int_or_not = None
        try:
            user_input = int(input)
            print("Your input " + str(user_input) + " is an integer!")
            # Your code goes here
            int_or_not = True

        except ValueError:
            print("Your input " + input + " is not an integer!")
            # Your code goes here
            int_or_not = False

        return int_or_not


def check_input(ival):
    # Your code goes here
    validator = NumberValidator()
    ival.set_validator(validator)
    return ival.validate()


# This is how your code will be called.
# You can edit this code to try different testing cases.
ival = InterceptingValidator()
result = check_input(ival)
print(result)
