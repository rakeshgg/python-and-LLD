class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


# inherit from abstarct class, components
class Child(Component):
    """Concrete Class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        # this is where we store the name of your child items
        self.name = args[0]

    def component_function(self):
        # print the name of your child item here
        print("{}".format(self.name))


# inherit from abstarct class, components
class Composite(Component):
    """concrete class and maintains the tree recursive stucture"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        # this is where we store name of the composite object
        self.name = args[0]
        # this is where we keep our child items
        self.children = []

    def append_child(self, child):
        """method to add a new child items"""
        self.children.append(child)

    def remove_child(self, child):
        """method to remove child item"""
        self.children.remove(child)

    def component_function(self):
        # print the name of composite object
        print("{}".format(self.name))
        # iterate through the child objects and Invoke their components
        # function to print their names
        for i in self.children:
            i.component_function()


# Build composite submenu 1
sub1 = Composite("Submenu1")
# create a new child sub_menu 11
sub11 = Child("Sub menu 11")
# create a child submenu 12
sub12 = Child("Sub menu 12")

# add submenu 11 to submenu 1
sub1.append_child(sub11)
# add submenu 12 to submenu 1
sub1.append_child(sub12)
# build a top-level composite menu
top = Composite("top_menu")
# build a submenu 2 that is not composite
sub2 = Child("submenu2")
# Add the composite submenu 1 ti the top level composite menu
top.append_child(sub1)
# Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)
# lets test if our compoiste pattern works
top.component_function()
