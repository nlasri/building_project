"""
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.
This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).
*What does this example do?
The first example achieves this by using an abstract base
class for a building, where the initializer (__init__ method) specifies the
steps needed, and the concrete subclasses implement these steps.
In other programming languages, a more complex arrangement is sometimes
necessary. In particular, you cannot have polymorphic behaviour in a constructor in C++ -
see https://stackoverflow.com/questions/1453131/how-can-i-get-polymorphic-behavior-in-a-c-constructor
- which means this Python technique will not work. The polymorphism
required has to be provided by an external, already constructed
instance of a different class.
In general, in Python this won't be necessary, but a second example showing
this kind of arrangement is also included.
*Where is the pattern used practically?
*References:
https://sourcemaking.com/design_patterns/builder
*TL;DR
Decouples the creation of a complex object and its representation.
"""

from visualisation import *

# Abstract Building
class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


# Concrete Buildings

class Simple_design(Building):
    def build_floor(self):
        self.floor = np.zeros((self.largeur, self.longueur)) #longueur et largeur du batiment pour faire le tableau de base
        
    def build_room(self, signe):
        placer_room(self.rooms, self.floor, signe) #placer les rooms dans le building
    
    def build_truc(self, signe):
        placer_room(self.truc, self.floor, signe) #placer un élement dans le building

class Medium_design(Building):
    def build_floor(self):
        self.floor = Canvas(fenetre, width=longueur*20 + 20, height=largeur*20 + 20, background='white')
        
    def build_room(self, color):
        placer_room_2(self.rooms, self.floor, color, "room") #placer les rooms dans le building
    
    def build_truc(self, color):
        placer_room_2(self.truc, self.floor, color, "room") #placer un élement dans le building


def construct_building(cls, color_list):
    building = cls()
    building.build_floor(color_list[0])
    building.build_size(color_list[1])
    return building




def main():
    """
    >>> house = House()
    >>> house
    Floor: One | Size: Big
    >>> flat = Flat()
    >>> flat
    Floor: More than One | Size: Small
    # Using an external constructor function:
    >>> complex_house = construct_building(ComplexHouse)
    >>> complex_house
    Floor: One | Size: Big and fancy
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()