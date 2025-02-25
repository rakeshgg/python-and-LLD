class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    """English speker"""

    def __init__(self):
        self.name = "Bristish"

    # note the different method name here!
    def speak_english(self):
        return "Hello!"


class Adapter:
    """This changes the generic method name to
    individualized method"""

    def __init__(self, object, **adapted_method):
        """change the name of the methods"""
        self._object = object

        """ add a new dictioanry items that established the mapping between """
        # for example, speak() will be translated to speak_korean() if
        self.__dict__.update(adapted_method)
        print(self.__dict__)

    def __getattr__(self, attr):
        """simply return the rest of attributes"""
        return getattr(self._object, attr)


# List to store speaker objects
objects = []
# create a korean objects
korean = Korean()
# create a british objects
british = British()
# Append the objects to the obejct list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))
for obj in objects:
    print("{} say {} \n".format(obj.name, obj.speak()))
