"""
"""

import copy


class Prototype:

    def __init__(self):
        # creating dict objects which need to be cloned
        self._objects = {}

    def register_object(self, name, obj):
        """Register an objects"""
        """ object need to clone and name as key when storing
        in dict objects"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        """ delete objects from dict"""
        del self._objects[name]

    def clone(self, name, **attr):
        """clone a registerd objects and update its attribute"""
        """
         The prototypical objects already stored in our dict objects
         refernce by saying self._objects
        """
        obj = copy.deepcopy(self._objects.get(name))
        # this is perfectly fine if you don't want to chnage
        # anything if objects cloned
        # if want to change some attribute of objects
        # you are cloning then its nice
        # to have a way to update the attributes obj.__dict__
        # uodate
        obj.__dict__.update(attr)
        return obj


# In this case we are cloning a car objects
class Car:

    def __init__(self):
        self.model = "Skylark"
        self.tires = "Red"
        self.engine = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


# clone prototype
c = Car()  # prototypical objects to be cloned
print(c)
prototype = Prototype()
prototype.register_object("skylark", c)
c1 = prototype.clone("skylark")
# we just cloned to prototypical objects
# print the cloned objects
print(c1)
