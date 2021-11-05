# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:29:28 2021

@author: Alain Tran, Narjisse Lasri
"""

import numpy as np
from tkinter import *
from classes import *


def placer_room_2(area, canvas, height):
    """Generate the medium design.
        This design use lines to represent the areas of the building.
        The color of each kind of area is used to design the building.
        In this design, the elements aren't representated.

    Args:
        area (list): List of all the room in a specific floor
        canvas (Canvas): Canvas in which the design will be represented
        height (float): Height of the floor
    """
    for room in area:
        canvas.create_line(room.coordinate_x*20, height - room.coordinate_y*20, (room.coordinate_x)*20, height - (room.coordinate_y+room.height)*20, fill=room.color) #mur est
        canvas.create_line((room.coordinate_x+ room.width)*20, height - room.coordinate_y*20, (room.coordinate_x+ room.width)*20, height - (room.coordinate_y+room.height)*20, fill=room.color) #mur ouest
        canvas.create_line(room.coordinate_x*20, height - room.coordinate_y*20, (room.coordinate_x + room.width)*20, height - room.coordinate_y*20, fill=room.color) #mur nord
        canvas.create_line((room.coordinate_x)*20, height - (room.coordinate_y+room.height)*20, (room.coordinate_x+ room.width)*20, height - (room.coordinate_y+room.height)*20, fill=room.color) #mur sud
        canvas.create_text((room.coordinate_x*20+room.coordinate_x*20+room.width*20)/2, height -(room.coordinate_y + room.coordinate_y + room.height)*10, text=room.name, font="Arial 16 italic", fill="blue")
            
def placer_room_3(area, canvas, height, fenetre):
    """Generate the high design.
       This design use rectangle of colors to represent areas and its elements.
       The color of each kind of area/element is used to design the building.
       A thickness of 0.5 is assigned to the element door (which has normally a zero thickness).

    Args:
        area (list): List of all the room in a specific floor
        canvas (Canvas): Canvas in which the design will be represented
        height (float): Height of the floor
        fenetre (tk): The window in which the canvas will be.
    """
    for room in area:
        canvas = Canvas(fenetre, width=room.width*20, height=room.height*20, background=room.color)
        canvas.place(x=room.coordinate_x*20, y=height - room.coordinate_y*20 - room.height*20)
        canvas.create_text(room.width*10, room.height*10, text=room.name, font="Arial 10 italic", fill="black")
        for element in room.elements:
            if type(element)==Door:
                if element.height==0:
                    element.height=0.5
                elif element.width==0:
                    element.width=0.5
            canvas_element = Canvas(canvas, width=element.width*20, height=element.height*20, background=element.color)
            canvas_element.place(x=element.coordinate_x*20, y=room.height *20 - element.coordinate_y*20 - element.height*20)
                        




