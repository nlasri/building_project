import numpy as np
from tkinter import *


building = np.array([[[0, 0, 4, 4], [5, 0, 4, 4]],[[0, 4, 4, 4], [5, 4, 4, 4]]])
couloir = np.array([[[4, 0, 1, 8]]])
longueur = building[0][-1][0] + building[0][-1][2]
largeur = building[-1][-1][1] + building[0][-1][3]

design_building = np.zeros((largeur, longueur))

def placer_room(building, design_building, signe):
    for room_largeur in building:
        for room in room_largeur:
            for longueur in range(room[2]):
                design_building[room[1]][room[0]+longueur]=signe
                design_building[room[1]+room[3]-1][room[0]+longueur]=signe
                for largeur in range(room[3]):
                    design_building[room[1]+largeur][room[0]]=signe
                    design_building[room[1]+largeur][room[0]+room[2]-1]=signe


placer_room(building, design_building, 1)
placer_room(couloir, design_building, 2)


def placer_room_2(area, canvas, height):
    for floor in area.values():
        for room in floor:
            canvas.create_line(room.coordinate_x*20, height - room.coordinate_y*20, (room.coordinate_x)*20, height - (room.coordinate_y+room.height)*20, fill=room.color) #mur est
            canvas.create_line((room.coordinate_x+ room.width)*20, height - room.coordinate_y*20, (room.coordinate_x+ room.width)*20, height - (room.coordinate_y+room.height)*20, fill=room.color) #mur ouest
            canvas.create_line(room.coordinate_x*20, height - room.coordinate_y*20, (room.coordinate_x + room.width)*20, height - room.coordinate_y*20, fill=room.color) #mur nord
            canvas.create_line((room.coordinate_x)*20, height - (room.coordinate_y+room.height)*20, (room.coordinate_x+ room.width)*20, height - (room.coordinate_y+room.height)*20, fill=room.color) #mur sud
            canvas.create_text((room.coordinate_x*20+room.coordinate_x*20+room.width*20)/2, height -(room.coordinate_y + room.coordinate_y + room.height)*10, text=room.name, font="Arial 16 italic", fill="blue")
            
def placer_room_3(area, canvas, color_element, height, fenetre):
    for floor in area.values():
            for room in floor:
                canvas = Canvas(fenetre, width=room.width*20, height=room.height*20, background=room.color)
                canvas.place(x=room.coordinate_x*20, y=height - room.coordinate_y*20 - room.height*20)
                canvas.create_text(room.width*10, room.height*10, text=room.name, font="Arial 16 italic", fill="black")
                for element in room.elements:
                    canvas_element = Canvas(canvas, width=element.width*20, height=element.height*20, background=color_element)
                    canvas_element.place(x=element.coordinate_x*20, y=room.height *20 - element.coordinate_y*20 - element.height*20)
                        




