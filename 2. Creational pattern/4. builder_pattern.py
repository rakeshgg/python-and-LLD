"""
Goal is to build car objects and print its details
"""


class Director:
    """Director its build the car"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        """return car methods"""
        return self._builder.car


class Builder:
    """Abstract Builde"""

    """ create a car objects and keep its attributes"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkbuilder(Builder):
    """Concrete Builders"""

    """ provides parts and tools to work on director class"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car:
    """product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)


# Create concrete builder
builder = SkyLarkbuilder()
# director take concrete builder and put it to works
director = Director(builder)
# construct cars
director.construct_car()
# get ref of car methods
car = director.get_car()
print(car)
"""
Builder pattern seperate class from process of building complex objects
This way creating similar objects required similar steps
let say you want to build Mustang insted of skylark all you have to do
add another concrete builder for mustang
"""
