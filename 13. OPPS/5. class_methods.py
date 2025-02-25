"""
we covered clas methods and class attributes
class attribute and methods different from instances
Methods because they acts on class itself not on the
instnaces
class methods is specific to actual class
class attribute is associated with class
no acess to instance information soley related
to class.

"""


class Car:
    # class attribute, not associated with class
    # put above all the methods
    numbers_of_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.numbers_of_cars = 1


# associated with class
Car.numbers_of_cars += 3
c1 = Car("Ford", "Edge")
c2 = Car("mazda", "3")
print(Car.numbers_of_cars)
# class attributes not instances attributes
# priority first search in instaces than class attribute
print(c1.numbers_of_cars)
print(Car.numbers_of_cars)


class Car1:
    # class attribute, not associated with class
    # put above all the methods
    numbers_of_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car1.numbers_of_cars += 1


c1 = Car1("Ford", "Edge")
c2 = Car1("mazda", "3")

"""
Every instanecs of class has access of class attribute
and can modify class attribute if you want that would
be sustend across all of the instances all see the changes
"""


class Car2:
    numbers_of_cars = 0
    wheels = 4
    # class attribute if for whole class

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car2.numbers_of_cars += 1

    # class methods, act on class not instace
    # cls mandatory parameters - name of class
    # cls refernce class name
    @classmethod
    def update_number_of_cars(cls, cars):
        cls.numbers_of_cars = cars
        print("run")


c1 = Car2("Ford", "Edge")
c2 = Car2("mazda", "3")
Car2.update_number_of_cars(5)
print(c1.numbers_of_cars)
print(Car2.numbers_of_cars)
# call class methods on instances
# work same way as
c2.update_number_of_cars(10)
print(c1.numbers_of_cars)


class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius**2)

    @classmethod
    def permiter(cls, radius):
        return 2 * cls.pi * radius

    # when modify pi both of this
    # class methods is automatically update to you
    # grouping methods together all methods related to
    # circle so put in circle class
    @classmethod
    def get_area_and_perimeter(cls, radius):
        # use two class methods inside another
        return cls.area(radius), cls.permiter(radius)


print(Circle.area(4))
print(Circle.get_area_and_perimeter(4))
