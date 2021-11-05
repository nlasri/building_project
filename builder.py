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
from interface_2 import *


# Concrete Buildings

class Simple_design(Building): # Peut etre a enlever
    def build_floor(self):
        self.floor = np.zeros((self.largeur, self.longueur)) #longueur et largeur du batiment pour faire le tableau de base
        
    def build_room(self, signe):
        placer_room(self.rooms, self.floor, signe) #placer les rooms dans le building
    
    def build_truc(self, signe):
        placer_room(self.truc, self.floor, signe) #placer un élement dans le building

class Medium_design(Building): #Design avec des barres, on ne voit pas les éléments dessus
    def build_floor(self, fenetre):
        width=self.width*20
        height=self.height*20
        canvas = Canvas(fenetre, width=width, height=height, background='white')
        return canvas
        
    def build_areas(self, canvas, height, fenetre):
        placer_room_2(self.areas, canvas, height) 
    

class High_design(Building): #design meilleur quali
    def build_floor(self, fenetre):
        width=self.width*20
        height=self.height*20
        canvas = Canvas(fenetre, width=width, height=height, background='white')
        return canvas
    
    def build_areas(self, floor, canvas, height, fenetre):
        placer_room_3(floor, canvas, 'blue', height, fenetre)


def construct_building(cls): #Constructeur
    #Creation of a window
    root = Tk()
    root.title("Entry Boxes")
    root.geometry("600x150")
    root.configure(background='LightSteelBlue2')
    title = Label(root, text = 'BUILDING', anchor = CENTER, justify = CENTER, bg='lightsteelblue4')
    title.grid(row = 0, columnspan = 7, sticky = 'nesw')
    #parameters of the building
    my_entries=[]
    label = ['width', 'height', 'number of floor']
    for x in range(0,3):
        my_entry = Entry(root)
        my_entry.insert(0, label[x])
        my_entry.grid(row=1, column=x, pady=20, padx=5)
        my_entries.append(my_entry)

    #button
    my_button = Button(root, text="Create my building", command= lambda: creation_building(my_entries, root, cls), bg='lightsteelblue4')
    my_button.grid(row=6, column=0, pady=20)
    root.mainloop()


def creation_building(my_entries, root, cls): #PErmet de créer le building à partir des valeurs que l'utilisateur donne
    values = []
    for entry in my_entries:
        values.append(entry.get())

    root.destroy()

    #Create building
    building_created = cls(int(values[0]), int(values[1]), int(values[2])+1)

    generate_interface(building_created)

    return building_created

def generate_building(my_entries, building_created): #génère un nouvel element du building à partir des valeurs données à l'interface
    #Attention mettre dans le readme ou à un endroit le fonctionnment du truc : un élément ne peut etre créé que si une pièce existe dans l'étage. Les éléments sont attribués à la dernière pièce créée
    values = []
    for entry in my_entries:
        values.append(entry.get())

    if values[0]=='Element':
        element = Element(int(values[1]), int(values[2]), int(values[3]), int(values[4]))
        building_created.areas[int(values[5])][-1].add_element(element)
    else:
        if values[0]=='Area':
            area = Area(int(values[1]), int(values[2]), int(values[3]), int(values[4]))
        elif values[0]=='Room':
            area = Room(int(values[1]), int(values[2]), int(values[3]), int(values[4]))
        elif values[0]=='Corridor':
            area = Corridor(int(values[1]), int(values[2]), int(values[3]), int(values[4]))
        elif values[0]=='Outside':
            area = Room(int(values[1]), int(values[2]), int(values[3]), int(values[4]))
        building_created.add_area(area, int(values[5]))
    design_building(building_created)

def design_building(building_created): #creation du design
    i=0
    for floor_areas in building_created.areas.values():
        fenetre = Tk()
        floor = building_created.build_floor(fenetre)
        building_created.build_areas(floor_areas, floor, building_created.get_height()*20, fenetre)
        floor.pack()

        #Display floor
        title = Label(fenetre, text = 'Floor'+str(i), anchor = CENTER, justify = CENTER, bg='lightsteelblue4')
        title.pack()
        # Button for closing
        exit_button = Button(fenetre, text="Exit", command=fenetre.destroy)
        exit_button.pack(pady=20)

        i+=1
        
        

if __name__ == "__main__":
    building = construct_building(High_design)

    