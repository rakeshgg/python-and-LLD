# this class being visited
class House(object):
    def accept(self, visitors):
        """Interface to accept visitors"""
        # triggers the visiting operations!
        visitors.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "Worked on By", hvac_specialist)

    def work_on_electriciy(self, electrician):
        # note that we have now refernce to electrician objects
        # visitor is electrician
        print(self, "Worked on By", electrician)

    def __str__(self):
        """simply return the calss name when the house object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract Visitor"""

    def __str__(self):
        """simply return the class name when the visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    # inherit from parent class
    """Concrete Visitors:HvacSpecialist"""

    def visit(self, house):
        # note visistor now has refernce
        house.work_on_hvac(self)


class Eletrician(Visitor):
    # inherit from parent class Visitior
    """Concrete Visitors:Eletrician"""

    def visit(self, house):
        # note that the visitors have refernce to house obejcts
        house.work_on_electriciy(self)
        # note the visitor now have refernce


# Create an HVAC Specilaist
hv = HvacSpecialist()
# create an electrician
e = Eletrician()
# create a house
home = House()
# let the house accept the HVAC Specialist and work on the house
home.accept(hv)
# let house work on electrician and work on the house by invoking
home.accept(e)
"""
The visitors pattern are very vertile in the sense that
you can make it work on various elements
"""
