import numpy as np

class Building:
    def __init__(self, width, height, nbfloor):
        self.width = width
        self.height = height
        self.nbfloor = nbfloor
        self.areas = {}
        for i in range(nbfloor):
            self.areas[i]=[]

    def collision(self, new_area, floor):
        for area in self.areas[floor]:
            if (new_area.coordinate_x + new_area.width > area.coordinate_x) and (new_area.coordinate_x < area.coordinate_x + area.width):
                return True
            elif (new_area.coordinate_x < area.coordinate_x + area.width) and (new_area.coordinate_x + new_area.width > area.coordinate_x):
                return True
            elif (new_area.coordinate_y + new_area.height > area.coordinate_y) and (new_area.coordinate_y < area.coordinate_y + area.height):
                return True
            elif (new_area.coordinate_y < area.coordinate_y + area.height) and (new_area.coordinate_y + new_area.height > area.coordinate_y):
                return True
            return False

    def area_not_in_building(self, area):
        if area.coordinate_x + area.width > self.width:
            return True
        elif area.coordinate_y + area.height > self.height:
            return True
        return False

    def add_area(self, area, floor):
        if self.collision(area, floor):
            print("Error : there is already an area at this place")
        elif self.area_not_in_building(area):
            print("Error : The area is not in the building")
        else :
            self.areas[floor].append(area)

    def get_areas(self):
        return self.areas

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def delete_area(self, area, floor):
        if area in self.areas[floor]:
            self.areas[floor].remove(area)
        else:
            print("Error : the room doesn't exist")


class Area:
    def __init__(self, coordinate_x, coordinate_y, width, height):
        self.width = width
        self.height = height
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.elements = []
        self.walls = np.zeros((4,1))

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_coordinates(self):
        return np.array([self.coordinate_x, self.coordinate_y, self.width, self.height])

    def collision(self, new_element):
        for element in self.elements:
            if (new_element.coordinate_x + new_element.width > element.coordinate_x) and (new_element.coordinate_x < element.coordinate_x + element.width):
                return True
            elif (new_element.coordinate_x < element.coordinate_x + element.width) and (new_element.coordinate_x + new_element.width > element.coordinate_x):
                return True
            elif (new_element.coordinate_y + new_element.height > element.coordinate_y) and (new_element.coordinate_y < element.coordinate_y + element.height):
                return True
            elif (new_element.coordinate_y < element.coordinate_y + element.height) and (new_element.coordinate_y + new_element.height > element.coordinate_y):
                return True
            return False

    def area_not_in_building(self, element):
        if element.coordinate_x + element.width > self.width:
            return True
        elif element.coordinate_y + element.height > self.height:
            return True
        return False

    def add_element(self, element):
        if self.collision(element):
            print("Error : there is already an area at this place")
        elif self.area_not_in_building(element):
            print("Error : The area is not in the building")
        else :
            self.areas.append(element)

    def create_wall(self):
        room_coordinates = self.get_coordinates()
        room_coordinates_abs = room_coordinates[0]
        room_coordinates_ord = room_coordinates[1]
        room_coordinates_width = room_coordinates[2]
        room_coordinates_height = room_coordinates[3]
        self.walls[0] = Wall(room_coordinates_abs, room_coordinates_ord, room_coordinates_width, 0)
        self.walls[1] = Wall(room_coordinates_abs, room_coordinates_ord, 0, room_coordinates_height)
        self.walls[2] = Wall(room_coordinates_abs, room_coordinates_ord + room_coordinates_height, room_coordinates_width, 0)
        self.walls[3] = Wall(room_coordinates_abs + room_coordinates_width, room_coordinates_ord, 0, room_coordinates_height)


    
class Element():
    def __init__(self, coordinate_x, coordinate_y, width, height):
        self.width = width
        self.height = height
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_coordinate_x(self):
        return self.coordinate_x

    def get_coordinate_y(self):
        return self.coordinate_y


class Wall(Element):
    def __init__(self, coordinate_x, coordinate_y, width, height):
        self.width = width
        self.height = height
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y


building = Building(20, 20, 2)
room1 = Area(5,5, 5, 5)
building.add_area(room1, 1)

room2 = Area(5,5, 2, 2)
building.add_area(room2, 1)

room3 = Area(0,0, 5, 5)
building.add_area(room3, 1)

print(building.areas)

from tkinter import *

fenetre = Tk()

# canvas
width=building.width*20
height=building.height*20
canvas = Canvas(fenetre, width=width, height=height, background='white')

def placer_room_3(area, canvas, color_room, name):
    for floor in area.values():
            for room in floor:
                canvas = Canvas(fenetre, width=room.width*20, height=room.height*20, background=color_room)
                canvas.place(x=room.coordinate_x*20, y=height - room.coordinate_y*20 - room.height*20)
                canvas.create_text(room.width*10, room.height*10, text=name, font="Arial 16 italic", fill="black")
                        
print("okaaaay")
placer_room_3(building.areas, canvas, 'orange', "room")

canvas.pack()
fenetre.mainloop()






