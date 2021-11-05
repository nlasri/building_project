# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:29:28 2021

@author: Alain Tran, Narjisse Lasri
"""

"""
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.
This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).
"""

from visualisation import *
from classes import *
from tkinter import *
import pickle


#__________________DESIGN OF BUILDING____________________
class Medium_design(Building): 
    """This class represent the medium design. This design use lines to represent the areas of the building.
       The color of each kind of area is used to design the building.
       In this design, the elements aren't representated.
    """
    def build_floor(self, fenetre):
        """This function creates the canvas which represent the building floor.

        Args:
            fenetre (tk): The window in which the canvas will be.

        Returns:
            canvas (Canvas): The canvas created
        """
        width=self.width*20
        height=self.height*20
        canvas = Canvas(fenetre, width=width, height=height, background='white')
        return canvas
        
    def build_areas(self, floor, canvas, height, fenetre):
        """Creation of the design of the building for a specific floor.

        Args:
            floor (list): List of all the room in a specific floor
            canvas (Canvas): Canvas in which the design will be represented
            height (float): Height of the floor
            fenetre (tk): The window in which the canvas will be.
        """
        place_room_2(floor, canvas, height) 
    

class High_design(Building): #design meilleur quali
    """This class represent the High design. This design use rectangle of colors to represent areas and its elements.
       The color of each kind of area/element is used to design the building.
       A thickness of 0.5 is assigned to the element door (which has normally a zero thickness).
    """
    def build_floor(self, fenetre):
        """This function creates the canvas which represent the building floor.

        Args:
            fenetre (tk): The window in which the canvas will be.

        Returns:
            canvas (Canvas): The canvas created
        """
        width=self.width*20
        height=self.height*20
        canvas = Canvas(fenetre, width=width, height=height, background='white')
        return canvas
    
    def build_areas(self, floor, canvas, height, fenetre):
        """Creation of the design of the building for a specific floor.

        Args:
            floor (list): List of all the room in a specific floor
            canvas (Canvas): Canvas in which the design will be represented
            height (float): Height of the floor
            fenetre (tk): The window in which the canvas will be.
        """
        place_room_3(floor, canvas, height, fenetre)


def construct_building(cls): #Constructeur
    """The constructor of the building. The constructor display a user interface which can get 
    the inputs of the user to construct a building.

    Args:
        my_entries (cls): Kind of design wanted : Medium_design or High_design
    """
    #Creation of a window for the user interface
    root = Tk()
    root.title("Entry Boxes")
    root.geometry("600x150")
    root.configure(background='LightSteelBlue2')
    title = Label(root, text = 'BUILDING', anchor = CENTER, justify = CENTER, bg='lightsteelblue4')
    title.grid(row = 0, columnspan = 7, sticky = 'nesw')
    
    #parameters of the building required
    my_entries=[]
    label = ['width', 'height', 'number of floor']
    for x in range(0,3):
        my_entry = Entry(root)
        my_entry.insert(0, label[x])
        my_entry.grid(row=1, column=x, pady=20, padx=5)
        my_entries.append(my_entry)

    #button to create the building
    my_button = Button(root, text="Create my building", command= lambda: creation_building(my_entries, root, cls), bg='lightsteelblue4')
    my_button.grid(row=6, column=0, pady=20)
    root.mainloop()
    

def creation_building(my_entries, root, cls): 
    """This function create a building from the inputs of the user

    Args:
        my_entries (list): inputs of the user
        root (tk): window which gets the input of the user
    """

    #Inputs of the user
    values = []
    for entry in my_entries:
        values.append(entry.get())

    #Destruction of the previous window
    root.destroy()

    #Creation of the building
    building_created = cls(float(values[0]), float(values[1]), int(values[2])+1)

    #Generate a new user interface
    generate_interface(building_created)

    return building_created

def generate_building(my_entries, building_created): 
    """This function generates a new element/area in the building from the inputs of the user
    An element can be created only if an area exists in the floor. The element will be in the last area created.
    The building is saved so that the user can use it later.

    Args:
        my_entries (list): inputs of the user
        building_created (Building): Building to modify
    """
    
    #Inputs of the user
    values = []
    for entry in my_entries:
        values.append(entry.get())

    #Insertion of the element/area
    if values[0]=='Element':
        element = Element(float(values[1]), float(values[2]), float(values[3]), float(values[4]))
        building_created.areas[int(values[5])][-1].add_element(element)
    elif values[0]=='Door':
        door = Door(float(values[1]), float(values[2]), float(values[3]), float(values[4]))
        if door.is_possible(building_created.areas[float(values[5])][-1]):
            building_created.areas[int(values[5])][-1].add_element(door)
        else:
            print("The door can't be there")
    else:
        if values[0]=='Area':
            area = Area(float(values[1]), float(values[2]), float(values[3]), float(values[4]))
        elif values[0]=='Room':
            area = Room(float(values[1]), float(values[2]), float(values[3]), float(values[4]))
        elif values[0]=='Corridor':
            area = Corridor(float(values[1]), float(values[2]), float(values[3]), float(values[4]))
        elif values[0]=='Outside':
            area = Outside(float(values[1]), float(values[2]), float(values[3]), float(values[4]))
        building_created.add_area(area, int(values[5]))
    design_building(building_created)

    #The building is saved
    file_building = open('building.obj', 'wb') 
    pickle.dump(building_created, file_building)


def design_building(building_created): #creation du design
    """Creation of the design of the building.

    Args:
        building_created (Building): Building to be displayed
    """
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
        

#_______________________________INTERFACE________________________________
def generate_interface(building_created):
    """Interface user to get the new elements/areas of the building.

    Args:
        building_created (Building): Building to modify
    """
    #Intro
    root = Tk()
    root.title("Entry Boxes")
    root.geometry("900x150")
    root.configure(background='LightSteelBlue2')
    title = Label(root, text = 'BUILDING', anchor = CENTER, justify = CENTER, bg='lightsteelblue4')
    title.grid(row = 0, columnspan = 7, sticky = 'nesw')

    #Selection
    my_label = Label(root, text='Element', bg='Dodger Blue')
    my_label.grid(row=1, column=0, pady=20, sticky = 'nesw')
    my_entries=[]

    #Kind
    OptionList = ["Area","Room","Corridor","Door", "Outside","Element"] 
    variable = StringVar(root)
    variable.set(OptionList[0])
    opt = OptionMenu(root, variable, *OptionList)
    opt.grid(row=1, column=1, pady=20, padx=5)
    my_entries.append(variable)

    #Coordinates and measures
    label = ['coordinate x', 'coordinate y', 'width', 'height', 'floor']
    for x in range(2,7):
        my_entry = Entry(root)
        my_entry.insert(0, label[x-2])
        my_entry.grid(row=1, column=x, pady=20, padx=5)
        my_entries.append(my_entry)

    #button
    my_button = Button(root, text="Create my building", command= lambda: generate_building(my_entries, building_created), bg='lightsteelblue4')
    my_button.grid(row=6, column=0, pady=20)

    # Button for closing
    exit_button = Button(root, text="Exit", command=root.destroy,  bg='lightsteelblue4')
    exit_button.grid(row=6, column=1, pady=20)

    root.mainloop()


def generate_interface_creation_building():
    """Interface to get the parameters of the building.
    """
    #Intro
    root = Tk()
    root.title("Entry Boxes")
    root.geometry("900x150")
    root.configure(background='LightSteelBlue2')
    title = Label(root, text = 'BUILDING', anchor = CENTER, justify = CENTER, bg='lightsteelblue4')
    title.grid(row = 0, columnspan = 7, sticky = 'nesw')

    #Selection
    my_label = Label(root, text='Element', bg='Dodger Blue')
    my_label.grid(row=1, column=0, pady=20, sticky = 'nesw')
    my_entries=[]

    #Kind
    OptionList = ["Area","Room","Corridor","Door", "Outside","Element"] 
    variable = StringVar(root)
    variable.set(OptionList[0])
    opt = OptionMenu(root, variable, *OptionList)
    opt.grid(row=1, column=1, pady=20, padx=5)
    my_entries.append(variable)

    #Coordinates and measures
    label = ['coordinate x', 'coordinate y', 'width', 'height', 'floor']
    for x in range(2,7):
        my_entry = Entry(root)
        my_entry.insert(0, label[x-2])
        my_entry.grid(row=1, column=x, pady=20, padx=5)
        my_entries.append(my_entry)

    #button
    my_button = Button(root, text="Create my building", command= lambda: generate_building(my_entries, building_created), bg='lightsteelblue4')
    my_button.grid(row=6, column=0, pady=20)
    root.mainloop()


if __name__ == "__main__":
    import os

    construct_building(High_design)

