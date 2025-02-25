class DrawingAPIOne(object):
    """Impelemntaion-specific abstarction: concrete class one"""

    def draw_circle(self, x, y, radius):
        print("API 1 drwaing ({},{} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Impelemntaion-specific abstarction: concrete class two"""

    def draw_circle(self, x, y, radius):
        print("API 2 drwaing ({},{} with radius {}!)".format(x, y, radius))


class Circle(object):
    """Impelemntaion-independet abstarction:
    for example there could be a rectangle
    """

    def __init__(self, x, y, radius, drawing_api):
        """Intialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation specif abstraction
        taken care by another
        """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementaton independent"""
        self._radius *= percent


# Build the First circle objects using api one
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# draw a circle
circle1.draw()
# Build the Second circle objects using api two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# draw a circle
circle2.draw()
"""
The bridge pattern is effective when you have
so many different kind of classes involved in
your hierachy and make sense to seperate this
classes into differnt hierachy

"""
