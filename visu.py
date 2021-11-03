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

print(design_building)



 

fenetre = Tk()

# canvas
width=longueur*20
height=largeur*20
canvas = Canvas(fenetre, width=width, height=height, background='white')


def placer_room_2(building, canvas, color_wall, name):
    for room_largeur in building:
        for room in room_largeur:
            canvas.create_line(room[0]*20, height - room[1]*20, (room[0])*20, height - (room[1]+room[3])*20, fill=color_wall) #mur est
            canvas.create_line((room[0]+room[2])*20, height - room[1]*20, (room[0]+room[2])*20, height - (room[1]+room[3])*20, fill=color_wall) #mur ouest
            canvas.create_line(room[0]*20, height - room[1]*20, (room[0]+room[2])*20, height - room[1]*20, fill=color_wall) #mur nord
            canvas.create_line((room[0])*20, height - (room[1]+room[3])*20, (room[0]+room[2])*20, height - (room[1]+room[3])*20, fill=color_wall) #mur sud
            canvas.create_text((room[0]*20+room[0]*20+room[2]*20)/2, height -(room[1] + room[1] + room[3])*10, text=name, font="Arial 16 italic", fill="blue")

def placer_room_3(building, canvas, color_room, name):
    for room_largeur in building:
        for room in room_largeur:
            canvas = Canvas(fenetre, width=room[2]*20, height=room[3]*20, background=color_room)
            canvas.place(x=room[0]*20,y=height - room[1]*20 - room[3]*20)
            canvas.create_text(room[2]*10, room[3]*10, text=name, font="Arial 16 italic", fill="black")
                        

placer_room_2(building, canvas, 'orange', "room")
placer_room_2(couloir, canvas, 'blue', "")
canvas.pack()
fenetre.mainloop()


