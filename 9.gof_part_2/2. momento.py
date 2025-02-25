import pickle

# pickle module used to serialize and deceralize python objects.
# translete a objects into tech stream before saving it into File - pickle
# the reverse is also possible refer to as deserailizing
"""
use pickle module in our example to demonstarte how we can save
the obejcts at a certain time and restore it previous state.

"""


class Originator:
    def __init__(self):
        self._state = None

    def create_memento(self):
        # turn original obj in char streams
        # vars return dictionary containing all the attribute value pairs
        # of an objects.
        return pickle.dumps(vars(self))

    def set_memenot(self, memento):
        # to store previous state of an obejcts
        # first deseralize our memenoto objects
        # which provide the snapshot of previous
        # objects.
        previous_sate = pickle.loads(memento)
        # then use var function to wipe out
        # The current state
        vars(self).clear()
        # finally replace the current state with previous state
        vars(self).update(previous_sate)


# momento in actions
originator = Originator()
print(vars(originator))
# store the current state
memento = originator.create_memento()
originator._state = True
print(vars(originator))
# use moenot objects to store previous state
originator.set_memenot(memento)
# check previous state has been restored
print(vars(originator))
# None repersent the initial state
