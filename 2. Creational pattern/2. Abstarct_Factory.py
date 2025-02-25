class Dog:
    """One of objects to be returned"""

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrerte Factory eg: return two objects"""

    """ our concrete products are dog objects and dog food"""
    """ unlike factory pattern that create one objects"""
    """ dog factory produces group of two related items Dog and dog
    food in the context of abstract factory patterns"""

    def get_pet(self):
        """retrun Dog objects"""
        return Dog()

    def get_food(self):
        """return Dog Food objects"""
        return "Dog Food!"


class PetStore:
    """PetStroe houses our Abstarct Factory"""

    def __init__(self, pet_factroy=None):
        """pet factory is our Abstarct Factory"""
        """ pet_factroy concrete factory"""
        self._pet_factroy = pet_factroy

    def show_pet(self):
        """utility methods to diaply the details of objects returns
        by our concrete Factory.
        """
        pet = self._pet_factroy.get_pet()
        pet_food = self._pet_factroy.get_food()

        print("our pet is '{}!".format(pet))
        print("our pet say hello by '{}!".format(pet.speak()))
        print("its food is '{}!".format(pet_food))


# Create a concrete Factory
factory = DogFactory()
# Create pet store housing our Abstract Factory
shop = PetStore(factory)
# Invoke the Utility methods to show the details of our pet
shop.show_pet()
"""
Adding another concrete Factory such as a cat Factroy is easy and elegant
which is one of benifits of using the abstarct factory patterns

"""
