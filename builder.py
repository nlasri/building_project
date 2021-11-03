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
from classes_2 import *
from tkinter import *


# Concrete Buildings

class Simple_design(Building):
    def build_floor(self):
        self.floor = np.zeros((self.largeur, self.longueur)) #longueur et largeur du batiment pour faire le tableau de base
        
    def build_room(self, signe):
        placer_room(self.rooms, self.floor, signe) #placer les rooms dans le building
    
    def build_truc(self, signe):
        placer_room(self.truc, self.floor, signe) #placer un élement dans le building

class Medium_design(Building):
    def build_floor(self, fenetre):
        width=self.width*20
        height=self.height*20
        canvas = Canvas(fenetre, width=width, height=height, background='white')
        return canvas
        
    def build_areas(self, canvas, height, fenetre):
        placer_room_2(self.areas, canvas, height) 
    

class High_design(Building):
    def build_floor(self, fenetre):
        width=self.width*20
        height=self.height*20
        canvas = Canvas(fenetre, width=width, height=height, background='white')
        return canvas
    
    def build_areas(self, canvas, height, fenetre):
        placer_room_3(self.areas, canvas, 'blue', height, fenetre)


def construct_building(cls):

    #Test ajouter des Areas
    building = cls(40, 20, 2)

    room1 = Area(0,0, 10, 10)
    building.add_area(room1, 1)

    room2 = Area(12, 0, 10, 10)
    building.add_area(room2, 1)

    room3 = Area(0,10, 10, 10)
    building.add_area(room3, 1)

    #Test ajouter des elements
    element1 = Element(1,1, 2,2)
    building.areas[1][0].add_element(element1)

    element2 = Element(5,5, 2,2)
    building.areas[1][0].add_element(element2)

    #Test ajouter room
    chambre = Room(12,10, 10, 10)
    building.add_area(chambre, 1)

    #Test ajouter corridor
    corridor = Corridor(10, 0, 2, 20)
    building.add_area(corridor, 1)

    
    fenetre = Tk()
    floor = building.build_floor(fenetre)
    building.build_areas(floor, building.get_height()*20, fenetre)
    floor.pack()
    fenetre.mainloop()
    return building


if __name__ == "__main__":
    building = construct_building(Medium_design)