class Dog:
    """A simple dog class"""

    def __init__(self, name) -> None:
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    """A simple cat class"""

    def __init__(self, name) -> None:
        self._name = name

    def speak(self):
        return "Meow!"


# external functions
# adding new class a cat not too much changes just add key in get_pets
def get_pet(pet="dog"):
    """The Factory Methods"""
    """ Mission to create objects and return that """
    """ dog is key in dictionary """
    pets = dict(dog=Dog("Hope"), cat=Cat("Billi"))
    """ provided key to return """
    return pets[pet]


d = get_pet("dog")
# invoking speak methods of dog objects
print(d.speak())
c = get_pet("cat")
# invoking cat speak methods
print(c.speak())
# addition of new pet type is easy for this
# The way factory pattern is implemnted here is slightly differnt from factory
# methods in typicall oops language beacuse we are trying to take fully
# advatages all built-in features of python in the course.
