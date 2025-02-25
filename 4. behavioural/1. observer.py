class Subject:  # Represents what is being observerd
    def __init__(self):
        self._observers = []
        # this is refernce to all observers
        # Note that this is one to many relations

    def attach(self, observer):
        # if the observer is not already in observer List
        # append the observer to the List
        # this methods accept the observer
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        # simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # for all the observer in the list
        # dont notify the observer who is actually updating the
        # alert the observer
        for observer in self._observers:
            if modifier != observer:
                # alert the observer
                observer.update(self)


class Core(Subject):
    # inherit from subject class
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # set the name of core
        self._temp = 0  # initialize the temperature of core

    @property  # getter that get the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # setter that set the core temperature
    def temp(self, temp):
        self._temp = temp
        # notify the observer when somebody change the core temperature
        self.notify()


# observer class
class TempViewer:
    def update(self, subject):
        # alert method invoked when temp value changes
        print("Temp viewer:{}temperature {}".format(subject, subject.temp))


# lets create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")
# lets create our observer
v1 = TempViewer()
v2 = TempViewer()
# let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)
# let's change the temperature of our first core
c1.temp = 80
c1.temp = 90
# both observer got notified evry time core temperature changes
