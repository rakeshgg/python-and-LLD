"""
Static Methods
Static methods is a methods which sits inside a class
doesnot acess with cls or self keywords
so doesnot act on class or instances of class
Similar to class methods the points is to better organise
your code. and keep related code together. may be you have
static methods the utility functions some sorts you should keep inside class
because higly related to class, math etc
"""


class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    @staticmethod
    def average_from_graded(grades):
        # no cls, no self
        return sum(grades) / len(grades)

    def average_from_graded_1(self):
        # no cls, no self
        # not possible to use grades[:2]
        # as it will use all the grades
        return sum(self.grades) / len(self.grades)


s1 = Student("Tim", [80, 90, 100])
s2 = Student("Tim", [60, 90, 100])
# static methods to calculate avargae of grades of all student

# call on isntaces
averages = s1.average_from_graded(s1.grades)
# doesnot have acess of s1.graded so passed
print(averages)

# call on class
averages = Student.average_from_graded(s2.grades)
print(averages)
# best way to think it as
# Functions that sit inside a class no acess to instance or class
# attributes
# just look on 1st two graded so static methods are useful
averages = Student.average_from_graded(s2.grades[:2])
# instnace methods not possible to run as - grades[:2]
# give flexibility so region to use static methods
averages = Student.average_from_graded(s2.grades + s1.grades)
# avarge of all graded across all the students
print(averages)
# give flexibility to use as function

# Static Attributes - Same as Class Attributes


class Student1:
    # static attribute or class attribute
    gravity = -9.8
    num_of_students = 0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades


class Student3:
    grade_bump = 2.0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    def average(self):
        # instance methods
        return sum(self.grades) / len(self.grades)

    @classmethod
    def average_from_grades_plus_bump(cls, grades):
        # calculate avarage of all grades pass to it
        averages = cls.average_from_grades(grades)
        return min(averages + cls.grade_bump, 100)

    """
    class methods has acess to realted methods for class
    attribute, static methods are part of the class so
    static methods can be used by class methods
    Theretically inside static methdos we can still
    use class attributes still acess other class methods
    we can do as Student.grade_bump however it is not
    a good practise inside a static methods suppose to acts
    just like a functions not rely outside of functions
    it should not rely on class attribute class methods
    like, insted it shoudl just work independetly so
    called staticmethods. if in static method required
    to acess instant attributes, class attributes anything
    related to class, instances than change it to class methods
    """

    @staticmethod
    def average_from_grades(grades):
        # no cls, no self
        return sum(grades) / len(grades)
