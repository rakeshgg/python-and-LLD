"""
let possible state is on and off

"""


# base class
class AtmState:
    name = "state"
    allowed = []

    def goNext(self, state):
        if state.name in self.allowed:
            print("current state", self, " switched to: ", state.name)
            self.__class__ = state
        else:
            print(
                "current state", self, " switching to: ", state.name, " not possible!"
            )

    def __str__(self):
        return self.name


# concrete class
class Off(AtmState):
    name = "off"
    allowed = ["on"]


# concrete class
class On(AtmState):
    name = "on"
    allowed = ["off"]


# context class
class ATM:
    def __init__(self):
        # set current state to off state
        self.current = Off()

    def setState(self, state):
        # invoke current state of gonext objects
        self.current.goNext(state)


atm = ATM()
atm.setState(On)
atm.setState(Off)
atm.setState(On)
