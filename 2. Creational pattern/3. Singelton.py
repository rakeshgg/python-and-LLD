class Borg:
    """The Borg design patterns"""

    """ Global variable declarations"""
    _shared_data = {}  # attribute dictionary

    def __init__(self):
        # make an attribute dictionary
        self.__dict__ = self._shared_data


class Singelton(Borg):
    """The singelton class"""

    """ by inherting from Borg class its argumnts for
        single class construtors by inhereting single class shared
        attributes among all various instances when ever we create
        a instance of borg class it will share same set of attributes
        in the dictionary.
        This setup essentially make the borg objects an oops form of
        global variables. borg objects here to maintains a dictioanry of
        our first acroynm.
    """

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the attribute of dictionary, providing dictionary of acroynm
        # every time a new objects get created
        self._shared_data.update(kwargs)

    def __str__(self):
        # return the attribute dictionary for priniting
        return str(self._shared_data)


# lets create a singelton objects and add our first acroynm
x = Singelton(HTTP="Hyper Text transafer protocols")
# print the objects
# the output shows the content of the borg attribute dictionary
# which is key and value pair of our acronym
print(x)

# lets create another singelton object and
# if it refrs to same attribute dictionary
# by adding another acronym
y = Singelton(SNMP="Simple Network managemnt protocols")
print(y)
# added new one in above
# {'HTTP': 'Hyper Text transafer protocols', 'SNMP': 'Simple Network managemnt
# protocols'}
# the way we implemnted singelton is differnet from its classical version
# but python
# way still does the jobs may be even better
print(x)
# {'HTTP': 'Hyper Text transafer protocols', 'SNMP':
# 'Simple Network managemnt protocols'}
